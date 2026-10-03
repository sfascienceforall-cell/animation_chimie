# -*- coding: utf-8 -*-
"""Construit le dossier telechargeable des 17 capsules d'animations de chimie.

Meme principe que pour les mathematiques : un sommaire HTML en tete, les
fichiers numerotes dans l'ordre de tournage, le tout dans un ZIP. Les
animations listees sont celles REELLEMENT presentes dans les fichiers — elles
sont relues depuis le HTML construit, jamais recopiees a la main.
"""
import pathlib, shutil, unicodedata, re, zipfile, html

import render_trames_ch as RT

ICI = pathlib.Path(__file__).resolve().parent
OUT = ICI / "pack_ch"
DEST = OUT / "SFA_Animations_Chimie"
if OUT.exists():
    shutil.rmtree(OUT)
DEST.mkdir(parents=True)

_RX = re.compile(r'data-ref="(ANIM-[A-Z0-9-]+)"\s+data-title="([^"]*)"\s+data-sub="([^"]*)"')


def detag(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def slug(s):
    s = unicodedata.normalize("NFKD", detag(s)).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")


def fichier(code):
    """CH4-A -> anim_CH4A.html · CH10 -> anim_CH10.html"""
    return pathlib.Path("anim_%s.html" % code.replace("-", ""))


lignes, rang = [], 0
for ch in RT.CHS:
    for cap in ch["caps"]:
        rang += 1
        src = fichier(cap["code"])
        if not src.exists():
            raise SystemExit("fichier manquant : %s (capsule %s)" % (src, cap["code"]))
        anims = _RX.findall(src.read_text())
        if not anims:
            raise SystemExit("aucune animation lue dans %s" % src)
        nom = "%02d_%s_%s.html" % (rang, cap["code"], slug(cap["titre"]))
        shutil.copy(src, DEST / nom)
        lignes.append((rang, cap["code"], detag(cap["titre"]), detag(ch["titre"]),
                       cap["duree"], nom, anims))

N_CAPS = len(lignes)
N_ANIM = sum(len(l[6]) for l in lignes)


def carte(l):
    rang, code, titre, chap, duree, nom, anims = l
    li = "".join('<li><span class="ref">%s</span> <span class="t">%s</span>'
                 '<span class="s">%s</span></li>' % (r, t, s) for r, t, s in anims)
    return ('<article class="c"><a class="hd" href="%s">'
            '<span class="n">%02d</span>'
            '<span class="tt"><b>%s</b><em>%s &middot; %s</em></span>'
            '<span class="meta"><span class="d">%s</span><span class="go">ouvrir &rarr;</span></span>'
            '</a><ol class="an">%s</ol></article>' % (nom, rang, titre, code, chap, duree, li))


INDEX = """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SFA &mdash; Animations de chimie</title>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--sfa:#0F7A4F;--deep:#08402A;--ink:#111;--g:#3F3F46;--l:#8A8F98;--line:#E3E7EE;--bg:#F3F7F4}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Be Vietnam Pro",system-ui,Arial,sans-serif;color:var(--ink);background:var(--bg);
     line-height:1.5;padding:40px 20px 70px}
.w{max-width:1080px;margin:0 auto}
header{border-bottom:3px solid var(--deep);padding-bottom:20px;margin-bottom:8px;
       display:flex;align-items:flex-end;gap:24px;flex-wrap:wrap}
header>div:first-child{flex:1 1 420px;min-width:0}
.org{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--sfa);font-weight:600;margin-bottom:8px}
h1{font-size:34px;letter-spacing:-.025em;color:var(--deep);line-height:1.1}
h1 em{font-style:normal;color:var(--sfa)}
.stats{margin-left:auto;display:flex;gap:26px;text-align:right}
.stats div b{display:block;font-size:26px;color:var(--deep);letter-spacing:-.02em}
.stats div span{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--l)}
.note{background:#fff;border-left:4px solid var(--sfa);border-radius:8px;padding:16px 20px;margin:22px 0 26px;
      font-size:15px;color:var(--g);box-shadow:0 1px 3px rgba(15,19,25,.05)}
.note b{color:var(--ink)}
.note p+p{margin-top:8px}
.note kbd{font-family:ui-monospace,Menlo,monospace;font-size:12.5px;background:#E4F2EA;color:var(--deep);
          border:1px solid #A9D4BE;border-radius:4px;padding:1px 6px;font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(400px,1fr));gap:16px}
.c{background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden;
   box-shadow:0 1px 3px rgba(15,19,25,.05);transition:box-shadow .15s,transform .15s}
.c:hover{box-shadow:0 6px 22px rgba(15,19,25,.12);transform:translateY(-2px)}
.hd{display:grid;grid-template-columns:auto 1fr;grid-template-areas:"n tt" "meta meta";
    gap:11px 12px;padding:14px 16px;text-decoration:none;background:var(--deep);color:#fff}
.hd .n{grid-area:n;font-family:ui-monospace,Menlo,monospace;font-size:13px;font-weight:700;
       background:rgba(255,255,255,.18);padding:5px 9px;border-radius:5px;align-self:start}
.hd .tt{grid-area:tt;min-width:0}
.hd .tt b{display:block;font-size:16px;letter-spacing:-.014em;line-height:1.24;font-weight:700}
.hd .tt em{display:block;font-style:normal;font-size:11.5px;opacity:.74;letter-spacing:.02em;margin-top:3px}
.hd .meta{grid-area:meta;display:flex;align-items:center;gap:10px;
          border-top:1px solid rgba(255,255,255,.16);padding-top:10px}
.hd .d{font-family:ui-monospace,Menlo,monospace;font-size:10.5px;opacity:.8}
.hd .go{margin-left:auto;font-size:11px;font-weight:600;letter-spacing:.04em;background:var(--sfa);
        padding:5px 10px;border-radius:5px}
.an{list-style:none;padding:8px 16px 14px}
.an li{padding:7px 0;border-bottom:1px solid #F0F2F6;font-size:13.5px}
.an li:last-child{border-bottom:none}
.an .ref{font-family:ui-monospace,Menlo,monospace;font-size:9.5px;font-weight:700;color:#fff;background:var(--sfa);
         padding:2px 5px;border-radius:3px;letter-spacing:.02em;position:relative;top:-1px}
.an .t{color:var(--ink);font-weight:600}
.an .s{display:block;color:var(--l);font-size:12.5px;line-height:1.4;margin-top:2px}
footer{margin-top:34px;padding-top:14px;border-top:2px solid var(--deep);font-size:12px;color:var(--l)}
@media(max-width:640px){h1{font-size:26px}.stats{margin-left:0}}
</style></head><body><div class="w">
<header><div><p class="org">SFA &middot; Science For All &mdash; Pr&eacute;pa m&eacute;decine</p>
<h1>Animations de chimie,<br><em>dans l'ordre de tournage.</em></h1></div>
<div class="stats"><div><b>@@NC@@</b><span>capsules</span></div><div><b>@@NA@@</b><span>animations</span></div></div></header>
<div class="note"><p><b>Un fichier = une capsule.</b> On l'ouvre dans n'importe quel navigateur, on passe en plein &eacute;cran, et on avance avec les fl&egrave;ches : <kbd>&rarr;</kbd> &eacute;tape suivante, <kbd>&larr;</kbd> &eacute;tape pr&eacute;c&eacute;dente, <kbd>&darr;</kbd> animation suivante, <kbd>S</kbd> sommaire de la capsule, <kbd>G</kbd> rep&egrave;res.</p>
<p><b>L'ordre des fichiers est l'ordre de tournage</b>, et pour la chimie il suit le programme ARES version 10 : chaque chapitre s'appuie sur le pr&eacute;c&eacute;dent. Une seule contrainte vient d'une autre mati&egrave;re &mdash; <b>CH7-B a besoin du logarithme</b>, donc de la capsule <b>D2-A</b> des math&eacute;matiques, qui doit &ecirc;tre tourn&eacute;e avant.</p>
<p>Deux figures reviennent &agrave; l'identique dans deux capsules diff&eacute;rentes : la <b>r&egrave;gle du gamma</b> en CH7-B puis en CH8-B. C'est voulu &mdash; le professeur le dit explicitement et ne la r&eacute;explique pas.</p></div>
<div class="grid">@@CARTES@@</div>
<footer>SFA &middot; Science For All &mdash; @@NC@@ capsules, @@NA@@ animations &middot; programme ARES version 10 &middot; charte graphique SFA &middot; logo &agrave; substituer avant diffusion.</footer>
</div></body></html>"""

(DEST / "00_SOMMAIRE.html").write_text(
    INDEX.replace("@@CARTES@@", "".join(carte(l) for l in lignes))
         .replace("@@NA@@", str(N_ANIM)).replace("@@NC@@", str(N_CAPS)))

zpath = ICI / "SFA_Animations_Chimie_17_capsules.zip"
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for f in sorted(DEST.iterdir()):
        z.write(f, "SFA_Animations_Chimie/" + f.name)
print(zpath, "%.1f Mo" % (zpath.stat().st_size / 1e6), "|", N_CAPS, "capsules,", N_ANIM, "animations")
for l in lignes:
    print("  %02d  %-6s %-52s %d animations" % (l[0], l[1], l[2][:52], len(l[6])))
