# -*- coding: utf-8 -*-
"""Audit de l'occupation verticale reelle de la zone utile.

Pour chaque diapositive et chaque etape, on mesure la boite englobante du
contenu visible et on la compare a la zone .body :
  - haut   : espace inutilise au-dessus du contenu
  - bas    : depassement sous la zone (le contenu mord la ligne du pied)
Un espace mort en haut alors que le bas deborde signale un contenu centre
verticalement alors qu'il est trop haut : c'est le defaut a corriger.
"""
import sys, asyncio, pathlib, json

from playwright.async_api import async_playwright

JS = r"""() => {
  const out = [];
  const zone = document.querySelector('.body');
  for (const s of document.querySelectorAll('.slide')) {
    const etait = s.style.display;
    s.style.display = '';
    const T = +s.dataset.steps || 1;
    for (let k = 0; k < T; k++) {
      [...s.querySelectorAll('.step')].forEach(el => {
        let app = 1, hide = 99;
        (el.getAttribute('class')||'').split(/\s+/).forEach(c => {
          let a = /^s(\d+)$/.exec(c); if (a) app = +a[1];
          let h = /^h(\d+)$/.exec(c); if (h) hide = +h[1];
        });
        el.classList.toggle('on', k+1 >= app);
        el.classList.toggle('gone', k+1 >= hide);
      });
      const z = s.querySelector('.mid') || s;
      const zr = z.getBoundingClientRect();
      let hautMin = Infinity, basMax = -Infinity;
      const noeuds = z.querySelectorAll('.card, .expr, svg, table, .kv');
      for (const n of noeuds) {
        if (n.closest('.gone')) continue;
        const st = n.closest('.step');
        if (st && !st.classList.contains('on')) continue;
        const r = n.getBoundingClientRect();
        if (!r.height) continue;
        if (r.top < hautMin) hautMin = r.top;
        if (r.bottom > basMax) basMax = r.bottom;
      }
      if (!isFinite(hautMin)) continue;
      out.push({ref: s.dataset.ref, step: k + 1,
                haut: Math.round(hautMin - zr.top),
                bas: Math.round(basMax - zr.bottom),
                zone: Math.round(zr.height),
                pris: Math.round(basMax - hautMin)});
    }
    s.style.display = etait;
  }
  return out;
}"""


async def main(motif, seuil_haut, seuil_bas):
    files = sorted(pathlib.Path('.').glob(motif))
    tout = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        for f in files:
            await pg.goto("file://" + str(f.resolve()))
            await pg.wait_for_timeout(900)
            for r in await pg.evaluate(JS):
                r["file"] = f.name
                tout.append(r)
        await b.close()

    pathlib.Path("/tmp/audit_zone.json").write_text(json.dumps(tout))
    deborde = [r for r in tout if r["bas"] > seuil_bas]
    creux = [r for r in tout if r["haut"] > seuil_haut]
    print("fichiers analyses :", len(files), "· mesures :", len(tout))
    print("depassements sous la zone (> %d px) : %d" % (seuil_bas, len(deborde)))
    for r in sorted(deborde, key=lambda r: -r["bas"])[:20]:
        print("   %-16s %-13s etape %d  bas +%3d  haut %3d" % (r["file"], r["ref"], r["step"], r["bas"], r["haut"]))
    print("espace mort en haut (> %d px) : %d" % (seuil_haut, len(creux)))
    for r in sorted(creux, key=lambda r: -r["haut"])[:20]:
        print("   %-16s %-13s etape %d  haut %3d  pris %3d / %d"
              % (r["file"], r["ref"], r["step"], r["haut"], r["pris"], r["zone"]))


asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "anim_CH*.html",
                 int(sys.argv[2]) if len(sys.argv) > 2 else 40,
                 int(sys.argv[3]) if len(sys.argv) > 3 else 2))
