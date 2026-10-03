# -*- coding: utf-8 -*-
"""Audit des bandeaux : un texte pose sur un aplat doit tenir DANS cet aplat.

L'audit geometrique precedent ne comparait qu'au viewBox. Un libelle plus large
que le rectangle colore place derriere lui passait donc inapercu — c'est le
defaut signale sur CH1-02 et CH2-02. Ici, pour chaque texte, on cherche le
rectangle qui lui sert de fond (celui qui l'englobe verticalement et le
chevauche horizontalement) et on exige une marge laterale minimale.
"""
import sys, asyncio, pathlib, json

from playwright.async_api import async_playwright

PAD = 10                      # marge laterale minimale exigee, en unites de viewBox

JS = r"""(PAD) => {
  const out = [];
  for (const s of document.querySelectorAll('.slide')) {
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
        const vis = el => !el.closest('.gone') && !el.closest('defs');
        const rects = [...svg.querySelectorAll('rect')].filter(vis).map(r => {
          let b; try { b = r.getBBox(); } catch (e) { return null; }
          const f = (r.getAttribute('fill')||'').trim().toLowerCase();
          if (!f || f === 'none') return null;          // un simple contour n'est pas un fond
          return {x: b.x, y: b.y, w: b.width, h: b.height};
        }).filter(Boolean);
        for (const t of svg.querySelectorAll('text')) {
          if (!vis(t)) continue;
          let b; try { b = t.getBBox(); } catch (e) { continue; }
          if (!b.width) continue;
          const cy = b.y + b.height / 2, cx = b.x + b.width / 2;
          // le fond = le plus petit rectangle qui contient le centre du texte
          let fond = null;
          for (const r of rects) {
            if (cx < r.x || cx > r.x + r.w || cy < r.y || cy > r.y + r.h) continue;
            if (!fond || r.w * r.h < fond.w * fond.h) fond = r;
          }
          if (!fond) continue;
          const marge = Math.min(b.x - fond.x, (fond.x + fond.w) - (b.x + b.width));
          if (marge < PAD) {
            out.push({ref: s.dataset.ref, step: k,
                      txt: (t.textContent||'').trim().slice(0, 46),
                      marge: Math.round(marge),
                      tw: Math.round(b.width), rw: Math.round(fond.w)});
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
            await pg.wait_for_timeout(900)
            for r in await pg.evaluate(JS, PAD):
                r["file"] = f.name
                tout.append(r)
        await b.close()

    vus = {}
    for r in tout:
        cle = (r["file"], r["ref"], r["txt"])
        if cle not in vus or r["marge"] < vus[cle]["marge"]:
            vus[cle] = r
    pires = sorted(vus.values(), key=lambda r: r["marge"])
    pathlib.Path("/tmp/audit_band.json").write_text(json.dumps(pires))
    print("fichiers analyses :", len(files))
    print("libelles trop larges pour leur aplat (marge < %d) : %d" % (PAD, len(pires)))
    for r in pires:
        print("   %-16s %-13s marge %+4d  (texte %3d / aplat %3d)  %s"
              % (r["file"], r["ref"], r["marge"], r["tw"], r["rw"], r["txt"]))


asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "anim_CH*.html"))
