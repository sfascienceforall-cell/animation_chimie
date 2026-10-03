import sys, asyncio, pathlib, json
from playwright.async_api import async_playwright

async def main():
    files = sorted(pathlib.Path('.').glob('anim_CH*.html'))
    out = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        for f in files:
            await pg.goto("file://" + str(f.resolve()))
            await pg.wait_for_timeout(1100)
            res = await pg.evaluate("""() => {
              const zone = document.querySelector('.body');
              const zr = zone.getBoundingClientRect();
              const foot = document.querySelector('.foot').getBoundingClientRect();
              const head = document.querySelector('.head').getBoundingClientRect();
              const slides = [...document.querySelectorAll('.slide')];
              const bad = [];
              slides.forEach(s => {
                const T = +s.dataset.steps || 1;
                const cols = [...s.querySelectorAll('.col')].filter(c => c.querySelector('.card, .expr, .kv, table'));
                let zoom = cols.map(c => +(c.style.zoom || 1));
                let worst = 0, worstStep = 0;
                for (let k = 0; k < T; k++) {
                  [...s.querySelectorAll('.step')].forEach(el => {
                    let app = 1, hide = 99;
                    (el.getAttribute('class')||'').split(/\\s+/).forEach(c => {
                      let a = /^s(\\d+)$/.exec(c); if (a) app = +a[1];
                      let h = /^h(\\d+)$/.exec(c); if (h) hide = +h[1];
                    });
                    el.classList.toggle('on', k+1 >= app);
                    el.classList.toggle('gone', k+1 >= hide);
                  });
                  cols.forEach(c => {
                    const r = c.getBoundingClientRect();
                    const over = Math.max(r.bottom - foot.top, head.bottom - r.top, 0);
                    if (over > worst) { worst = over; worstStep = k; }
                  });
                }
                bad.push({ref: s.dataset.ref, over: Math.round(worst), step: worstStep,
                          zoom: zoom.map(z => +z.toFixed(3))});
              });
              return bad;
            }""")
            for r in res:
                r["file"] = f.name
                out.append(r)
        await b.close()
    pathlib.Path("/tmp/audit_ch.json").write_text(json.dumps(out))
    over = [r for r in out if r["over"] > 2]
    small = [r for r in out if min(r["zoom"] or [1]) < 0.88]
    print("animations :", len(out))
    print("debordements restants :", len(over))
    for r in over: print("   ", r["file"], r["ref"], "+%dpx" % r["over"], r["zoom"])
    print("colonnes reduites sous 0,88 :", len(small))
    for r in small: print("   ", r["file"], r["ref"], r["zoom"])
asyncio.run(main())
