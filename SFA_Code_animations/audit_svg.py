# -*- coding: utf-8 -*-
"""Audit geometrique des figures : rien ne doit sortir de son cadre.

Pour chaque animation, a chaque etape, on mesure la boite englobante reelle de
chaque element SVG (getBBox) et on la compare au viewBox. Un texte trop long,
une particule hors de sa boite ou un rectangle trop large sont donc detectes
automatiquement — ce que l'audit vertical seul ne voyait pas.
"""
import sys, asyncio, pathlib, json
from playwright.async_api import async_playwright

JS = r"""() => {
  const out = [];
  const slides = [...document.querySelectorAll('.slide')];
  for (const s of slides) {
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
      for (const svg of s.querySelectorAll('svg')) {
        const vb = svg.viewBox.baseVal;
        if (!vb || !vb.width) continue;
        for (const el of svg.querySelectorAll('text,rect,circle,line,path,polygon')) {
          if (el.closest('.gone')) continue;
          if (el.closest('defs')) continue;
          let b; try { b = el.getBBox(); } catch (e) { continue; }
          if (!b.width && !b.height) continue;
          const over = Math.max(
            vb.x - b.x, vb.y - b.y,
            (b.x + b.width) - (vb.x + vb.width),
            (b.y + b.height) - (vb.y + vb.height));
          if (over > 1.5) {
            out.push({ref: s.dataset.ref, step: k, tag: el.tagName,
                      txt: (el.textContent||'').trim().slice(0, 44),
                      over: Math.round(over)});
          }
        }
      }
    }
  }
  return out;
}"""


async def main(motif):
    files = sorted(pathlib.Path('.').glob(motif))
    tout = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        for f in files:
            await pg.goto("file://" + str(f.resolve()))
            await pg.wait_for_timeout(1000)
            for r in await pg.evaluate(JS):
                r["file"] = f.name
                tout.append(r)
        await b.close()

    # on ne garde qu'une ligne par element fautif (le pire depassement)
    vus = {}
    for r in tout:
        cle = (r["file"], r["ref"], r["tag"], r["txt"])
        if cle not in vus or r["over"] > vus[cle]["over"]:
            vus[cle] = r
    pires = sorted(vus.values(), key=lambda r: -r["over"])
    pathlib.Path("/tmp/audit_svg.json").write_text(json.dumps(pires))
    print("fichiers analyses :", len(files))
    print("elements hors cadre :", len(pires))
    for r in pires:
        print("   %-16s %-13s %-7s +%3dpx  %s" % (r["file"], r["ref"], r["tag"], r["over"], r["txt"]))


asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "anim_CH*.html"))
