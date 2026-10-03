import pathlib

SHELL = (pathlib.Path(__file__).with_name("shell_anim.html")
         .read_text())        # le gabarit est a cote de ce fichier

# Une seule teinte pilote tout le fichier d'animation : bandeaux, cartes,
# pastilles, courbes. On la change en un point, tout suit.
BLEU = {"sfa": "#1D4ED8", "deep": "#0A2A6E", "tint": "#E9EEFC",
        "tint2": "#D3DEFA", "surface": "#F4F6FA"}
VERT = {"sfa": "#0F7A4F", "deep": "#08402A", "tint": "#E4F2EA",
        "tint2": "#C2E0D0", "surface": "#F2F7F4"}


def shell(p=None):
    if p is None or p is BLEU:
        return SHELL
    return (SHELL.replace("--sfa:#1D4ED8", "--sfa:" + p["sfa"])
                 .replace("--deep:#0A2A6E", "--deep:" + p["deep"])
                 .replace("--tint:#E9EEFC", "--tint:" + p["tint"])
                 .replace("--tint2:#D3DEFA", "--tint2:" + p["tint2"])
                 .replace("--surface:#F4F6FA", "--surface:" + p["surface"]))


def build(code, toc, slides_html, out, palette=None):
    h = (shell(palette).replace("@@CODE@@", code)
                       .replace("@@TOC@@", toc)
                       .replace("@@SLIDES@@", slides_html))
    pathlib.Path(out).write_text(h)
    return out
