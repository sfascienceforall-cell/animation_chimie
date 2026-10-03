import sys, asyncio
from playwright.async_api import async_playwright

async def main(src, out_prefix, shots):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width":1600,"height":900})
        await pg.goto("file://"+src)
        await pg.wait_for_timeout(500)
        prev = 0
        for i,(slide,step) in enumerate(shots):
            await pg.keyboard.press("Home")
            await pg.wait_for_timeout(120)
            for _ in range(slide):
                await pg.keyboard.press("ArrowDown"); await pg.wait_for_timeout(60)
            for _ in range(step):
                await pg.keyboard.press("ArrowRight"); await pg.wait_for_timeout(80)
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"{out_prefix}{i}.png")
        await b.close()

src, pref = sys.argv[1], sys.argv[2]
shots = [tuple(int(x) for x in a.split(",")) for a in sys.argv[3:]]
asyncio.run(main(src, pref, shots))
