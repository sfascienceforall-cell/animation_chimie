# -*- coding: utf-8 -*-
"""Boite a outils commune aux animations de chimie (palette verte)."""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from build_anim import build, VERT

F = 'font-family="Be Vietnam Pro,Arial"'
SFA, DEEP, TINT, TINT2 = "#0F7A4F", "#08402A", "#E4F2EA", "#C2E0D0"
GREY, INK, INK2, RULE = "#8A8F98", "#111111", "#3F3F46", "#E3E7EE"
RED = "#C02A20"

_M = ('<marker id="%s{n}" markerWidth="15" markerHeight="15" refX="13.5" refY="7.5" '
      'orient="auto" markerUnits="userSpaceOnUse">'
      '<path d="M0,0 L15,7.5 L0,15 z" fill="%s"/></marker>')


def defs(n):
    """Fleches de taille fixe, independantes de l'epaisseur du trait."""
    return ("<defs>" + (_M % ("v", SFA)).replace("{n}", str(n))
            + (_M % ("d", DEEP)).replace("{n}", str(n))
            + (_M % ("r", RED)).replace("{n}", str(n)) + "</defs>")


def curve(f, x0, x1, ox, oy, ux, uy, n=240):
    return "M " + " L ".join("%.1f,%.1f" % (ox + ux * (x0 + (x1 - x0) * i / n),
                                            oy - uy * f(x0 + (x1 - x0) * i / n))
                             for i in range(n + 1))


def finish(slides, subs):
    """Substitue les fragments calcules, puis la macro de police.

    Le jeton est @@FF@@ et non FF : une macro de deux lettres frapperait
    aussi les couleurs hexadecimales (#FFFFFF).
    """
    for k, v in subs.items():
        slides = slides.replace("@@%s@@" % k, v)
    return slides.replace("@@FF@@", F)


def make(code, toc, slides, out):
    return build(code, toc, slides, out, palette=VERT)
