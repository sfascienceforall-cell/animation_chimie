# -*- coding: utf-8 -*-
"""Audit des collisions : deux libelles ne doivent jamais se toucher.

Les deux audits precedents verifiaient le cadre (viewBox) et les aplats. Il
restait un angle mort : deux textes voisins qui se chevauchent, ou qui se
touchent au point de se lire comme un seul mot. On compare donc, a chaque
etape, les boites englobantes de tous les couples de textes visibles et on
exige un ecart horizontal minimal quand ils partagent la meme ligne.
"""
import sys, asyncio, pathlib, json

from playwright.async_api import async_playwright

ECART = 8          # ecart horizontal minimal entre deux textes d'une meme ligne

JS = r"""(ECART) => {
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
      // visible = ni masque (.gone), ni encore non revele (.step sans .on)
      const montre = el => {
        if (el.closest('.gone') || el.closest('defs')) return false;
        const st = el.closest('.step');
        return !st || st.classList.contains('on');
      };
      for (const svg of s.querySelectorAll('svg')) {
        const ts = [];
        for (const t of svg.querySelectorAll('text')) {
          if (!montre(t)) continue;
          let b; try { b = t.getBBox(); } catch (e) { continue; }
          if (!b.width || !b.height) continue;
          ts.push({b, txt: (t.textContent||'').trim()});
        }
        // un trait ne doit pas traverser un libelle
        for (const L of svg.querySelectorAll('line')) {
          if (!montre(L)) continue;
          const x1=+L.getAttribute('x1'), y1=+L.getAttribute('y1');
          const x2=+L.getAttribute('x2'), y2=+L.getAttribute('y2');
          if (Math.abs(y1-y2) > 1 && Math.abs(x1-x2) > 1) continue;   // seulement H et V
          for (const t of ts) {
            const b = t.b;
            const inX = Math.min(x1,x2) < b.x + b.width - 2 && Math.max(x1,x2) > b.x + 2;
            const inY = Math.min(y1,y2) < b.y + b.height - 2 && Math.max(y1,y2) > b.y + 2;
            if (inX && inY) {
              out.push({ref: s.dataset.ref, step: k, ecart: -99,
                        a: 'TRAIT', b: t.txt.slice(0, 26)});
            }
          }
        }
        for (let i = 0; i < ts.length; i++) {
          for (let j = i + 1; j < ts.length; j++) {
            const A = ts[i].b, B = ts[j].b;
            // recouvrement vertical : sont-ils sur la meme ligne ?
            const recouvY = Math.min(A.y+A.height, B.y+B.height) - Math.max(A.y, B.y);
            if (recouvY < Math.min(A.height, B.height) * 0.45) continue;
            const ecart = Math.max(A.x, B.x) - Math.min(A.x+A.width, B.x+B.width);
            if (ecart < ECART) {
              out.push({ref: s.dataset.ref, step: k, ecart: Math.round(ecart),
                        a: ts[i].txt.slice(0, 26), b: ts[j].txt.slice(0, 26)});
            }
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
            for r in await pg.evaluate(JS, ECART):
                r["file"] = f.name
                tout.append(r)
        await b.close()

    vus = {}
    for r in tout:
        cle = (r["file"], r["ref"], r["a"], r["b"])
        if cle not in vus or r["ecart"] < vus[cle]["ecart"]:
            vus[cle] = r
    pires = sorted(vus.values(), key=lambda r: r["ecart"])
    pathlib.Path("/tmp/audit_collision.json").write_text(json.dumps(pires))
    print("fichiers analyses :", len(files))
    print("couples de libelles trop proches (ecart < %d) : %d" % (ECART, len(pires)))
    for r in pires:
        print("   %-16s %-13s ecart %+4d   « %s »  /  « %s »"
              % (r["file"], r["ref"], r["ecart"], r["a"], r["b"]))


asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "anim_CH*.html"))
