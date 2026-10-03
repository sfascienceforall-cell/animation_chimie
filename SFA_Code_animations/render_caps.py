# -*- coding: utf-8 -*-
"""Rendu HTML des fiches bullet points — capsules maths SFA."""
import pathlib, importlib

CSS = """
@page{size:A4;margin:14mm 13mm 13mm 13mm}
:root{
  --ink:#0F1319;--ink2:#39404C;--muted:#6A7180;
  --rule:#DDE1E8;--rule2:#B7BDC9;
  --m:#1D4ED8;--m-t:#EEF2FE;--m-ink:#0A2A6E;--m-soft:#C9D6F5;
  --blue:#1D4ED8;--blue-t:#EEF2FE;
  --red:#C02A20;--red-t:#FCEFED;
  --green:#166B47;--green-t:#E8F4EE;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}

/* --- lecture a l'ecran : marges confortables, rien ne touche le bord --- */
@media screen{
  html{background:#E9ECF1}
  body{max-width:200mm;margin:0 auto;padding:22mm 18mm 26mm;background:#fff;
       box-shadow:0 1px 34px rgba(15,19,25,.14)}
}

body{font-family:"Carlito","DejaVu Sans",sans-serif;color:var(--ink);font-size:9.5pt;line-height:1.45;
     -webkit-print-color-adjust:exact;print-color-adjust:exact}
p{margin:.42em 0}

/* ---------------- couverture ---------------- */
.masthead{border-bottom:3pt solid var(--m-ink);padding-bottom:10pt;margin-bottom:12pt}
.org{font-family:"DejaVu Sans Mono",monospace;font-size:6.8pt;letter-spacing:.16em;text-transform:uppercase;
     color:var(--m);margin:0 0 6pt}
h1{font-size:25pt;line-height:1.03;letter-spacing:-.024em;margin:0;font-weight:700;color:var(--m-ink)}
h1 em{font-style:normal;color:var(--m)}
.lede{color:var(--ink2);margin:8pt 0 0;font-size:9.4pt;max-width:154mm}

.box{border:.7pt solid var(--rule2);border-radius:4pt;padding:9pt 11pt;margin:9pt 0;break-inside:avoid}
.box.key{border:none;border-left:4pt solid var(--m);background:var(--m-t)}
.box.warn{border:none;border-left:4pt solid var(--red);background:var(--red-t)}
.box p,.box li{font-size:8.8pt}
.lab{font-family:"DejaVu Sans Mono",monospace;font-size:6.6pt;letter-spacing:.12em;text-transform:uppercase;
     color:var(--muted);display:block;margin-bottom:4pt}
.box.key .lab{color:var(--m-ink)}
.box.warn .lab{color:var(--red)}

/* ---------------- chapitre ---------------- */
.chap{break-before:page}
.chap-title{display:flex;align-items:center;gap:10pt;background:var(--m-ink);color:#fff;
            border-radius:4pt;padding:8pt 12pt;margin-bottom:6pt}
.chap-title .cd{font-family:"DejaVu Sans Mono",monospace;font-size:11pt;font-weight:700;
                background:rgba(255,255,255,.17);padding:2.5pt 7pt;border-radius:3pt;flex:none}
.chap-title h2{margin:0;font-size:17pt;letter-spacing:-.022em;font-weight:700}
.chap-intro{color:var(--ink2);font-size:8.9pt;margin:0 0 4pt}

/* ---------------- capsule ---------------- */
.caps{margin-top:11pt}
.caps.brk{break-before:page;margin-top:0}
.caps-head{border:1pt solid var(--m);border-radius:4pt;overflow:hidden;margin-bottom:9pt;break-inside:avoid}
.caps-head .top{background:var(--m);color:#fff;padding:6pt 11pt;display:flex;align-items:center;gap:9pt}
.caps-head .top .cd{font-family:"DejaVu Sans Mono",monospace;font-size:8pt;font-weight:700;
                    background:rgba(255,255,255,.20);padding:2pt 6pt;border-radius:2.5pt;flex:none}
.caps-head .top h3{margin:0;font-size:13.5pt;letter-spacing:-.018em;font-weight:700}
.caps-head .top .rang{margin-left:auto;font-family:"DejaVu Sans Mono",monospace;font-size:6.9pt;
                      letter-spacing:.1em;background:rgba(255,255,255,.20);padding:2pt 6pt;border-radius:2.5pt;flex:none}
.caps-head .top .dur{font-family:"DejaVu Sans Mono",monospace;font-size:7.4pt;opacity:.92;flex:none}
.caps-head .sub{padding:6pt 11pt;background:var(--m-t);font-size:8.6pt;color:var(--ink2)}
.caps-head .sub b{color:var(--m-ink)}

/* ---------------- les trois temps ---------------- */
.temps{margin:10pt 0}
.temps-head{display:flex;align-items:center;gap:8pt;break-after:avoid;
            border-bottom:1.6pt solid var(--m-soft);padding-bottom:3.5pt;margin-bottom:6pt}
.temps-head .t{font-family:"DejaVu Sans Mono",monospace;font-size:6.6pt;letter-spacing:.12em;color:#fff;
               background:var(--m);padding:2.4pt 6pt;border-radius:2.5pt;flex:none}
.temps-head h4{margin:0;font-size:11.5pt;letter-spacing:-.012em;color:var(--m-ink)}
.temps-head .min{margin-left:auto;font-family:"DejaVu Sans Mono",monospace;font-size:7pt;color:var(--muted)}
h5{font-size:9.5pt;margin:8pt 0 2pt;letter-spacing:-.006em;break-after:avoid;color:var(--m-ink)}
h5 .tag{font-family:"DejaVu Sans Mono",monospace;font-size:6.5pt;font-weight:400;color:var(--muted);
        margin-left:5pt;letter-spacing:.05em}
ul{margin:.28em 0;padding-left:14pt}
li{margin:2.2pt 0;color:var(--ink2)}
li b{color:var(--ink)}
li.piege{color:var(--red)}
li.piege b{color:var(--red)}
.anim{display:inline-block;font-family:"DejaVu Sans Mono",monospace;font-size:6.7pt;font-weight:700;
      color:#fff;background:var(--blue);padding:1.8pt 5pt;border-radius:2.5pt;letter-spacing:.04em}
.animline{background:var(--blue-t);border-left:3pt solid var(--blue);border-radius:2.5pt;
          padding:5pt 9pt;margin:4.5pt 0 6pt;font-size:8.5pt;color:var(--ink2);break-inside:avoid}
.animline b{color:var(--ink)}

/* ---------------- exercices : panneaux prets a etre captures ---------------- */
.exwrap{margin:9pt 0 11pt;break-inside:avoid}
.ex{border:1.1pt solid var(--m);border-radius:4pt;overflow:hidden;background:#fff}
.ex .h{background:var(--m-ink);color:#fff;padding:5.5pt 10pt;display:flex;align-items:center;gap:8pt}
.ex .h .num{font-family:"DejaVu Sans Mono",monospace;font-size:6.9pt;font-weight:700;letter-spacing:.1em;
            background:rgba(255,255,255,.20);padding:2pt 6pt;border-radius:2.5pt;flex:none}
.ex .h b{font-size:10pt;letter-spacing:-.01em;font-weight:700}
.ex .h .cat{margin-left:auto;font-family:"DejaVu Sans Mono",monospace;font-size:6.5pt;letter-spacing:.09em;
            text-transform:uppercase;opacity:.82;flex:none}
.ex .en{padding:7pt 11pt 7.5pt;background:#FAFBFE;border-bottom:.8pt solid var(--m-soft)}
.ex .en .lab{color:var(--m);margin-bottom:3pt}
.ex .en .txt{font-family:"DejaVu Serif",Georgia,serif;font-size:10.4pt;line-height:1.5;color:var(--ink)}
.ex .cor{padding:8.5pt 11pt 8pt}
.ex .cor .lab{color:var(--m);margin-bottom:4pt}
.ex ol{margin:0;padding:0;list-style:none;counter-reset:st}
.ex ol li{position:relative;counter-increment:st;margin:0 0 4.5pt;padding:2.5pt 0 2.5pt 20pt;
          font-size:9.6pt;line-height:1.45;color:var(--ink2)}
.ex ol li::before{content:counter(st);position:absolute;left:0;top:2.2pt;
  width:13pt;height:13pt;border-radius:50%;background:var(--m-t);color:var(--m-ink);
  font-family:"DejaVu Sans Mono",monospace;font-size:7pt;font-weight:700;
  display:flex;align-items:center;justify-content:center}
.ex ol li b{color:var(--ink)}
.ex ol li.fin{background:var(--m-t);border-radius:3pt;padding:5pt 9pt 5pt 20pt;margin-bottom:0;color:var(--m-ink)}
.ex ol li.fin::before{background:var(--m);color:#fff;left:4pt;top:4.6pt}
.ex ol li.fin b{color:var(--m-ink)}
.cue{font-size:8.5pt;color:var(--ink2);margin:4.5pt 0 0;padding:4.5pt 9pt;border-radius:3pt;
     border-left:3pt solid var(--rule2);background:#F6F7F9}
.tagoff{font-family:"DejaVu Sans Mono",monospace;font-size:6.2pt;letter-spacing:.1em;
             text-transform:uppercase;color:var(--muted);border:.6pt solid var(--rule2);
             border-radius:2pt;padding:.8pt 4pt;margin-right:5pt;white-space:nowrap}
.cue.red{border-left-color:var(--red);background:var(--red-t);color:var(--red)}
.cue.green{border-left-color:var(--green);background:var(--green-t);color:var(--green)}
.cue b{color:inherit}

/* --- notation vectorielle : la fleche est dessinee, jamais un caractere de police --- */
.vec{position:relative;display:inline-block;white-space:nowrap;font-style:italic}
.vec::after{content:"→";position:absolute;left:0;right:0;top:-.60em;
  font-family:"DejaVu Sans","Carlito",sans-serif;font-style:normal;font-size:.64em;
  line-height:1;text-align:center;letter-spacing:0}
.ex .en .vec::after{top:-.54em;font-size:.58em}

table{width:100%;border-collapse:collapse;font-size:8.6pt;margin:7pt 0}
th{text-align:left;font-size:6.7pt;letter-spacing:.09em;text-transform:uppercase;color:var(--m);
   font-weight:700;border-bottom:1.2pt solid var(--m-soft);padding:3.5pt 7pt 3.5pt 0}
td{padding:3.6pt 7pt 3.6pt 0;border-bottom:.6pt solid var(--rule);vertical-align:top;color:var(--ink2)}
td.first{color:var(--m-ink);font-weight:700;white-space:nowrap;font-family:"DejaVu Sans Mono",monospace;font-size:7.6pt}
.foot{margin-top:13pt;padding-top:7pt;border-top:1.4pt solid var(--m-ink);
  font-family:"DejaVu Sans Mono",monospace;font-size:6.8pt;color:var(--muted)}
"""

# ---------------------------------------------------------------- palettes
# Le document est monochrome : une seule teinte pilote bandeaux, pastilles,
# encarts et tableaux. On la change en un point, tout suit.
BLEU = {"m": "#1D4ED8", "m_t": "#EEF2FE", "m_ink": "#0A2A6E", "m_soft": "#C9D6F5"}
VERT = {"m": "#0F7A4F", "m_t": "#E9F4EE", "m_ink": "#08402A", "m_soft": "#A9D4BE"}


def css(p=None):
    """CSS du document dans la teinte demandee (bleu SFA par defaut)."""
    if p is None or p is BLEU:
        return CSS
    return (CSS.replace("--m:#1D4ED8", "--m:" + p["m"])
               .replace("--m-t:#EEF2FE", "--m-t:" + p["m_t"])
               .replace("--m-ink:#0A2A6E", "--m-ink:" + p["m_ink"])
               .replace("--m-soft:#C9D6F5", "--m-soft:" + p["m_soft"])
               .replace("--blue:#1D4ED8", "--blue:" + p["m"])
               .replace("--blue-t:#EEF2FE", "--blue-t:" + p["m_t"]))


def render_t2(items):
    out, inul = [], False
    for it in items:
        kind = it[0]
        if kind in ("h", "anim") and inul:
            out.append("</ul>"); inul = False
        if kind == "h":
            tag = f'<span class="tag">{it[2]}</span>' if len(it) > 2 else ""
            out.append(f"<h5>{it[1]}{tag}</h5>")
        elif kind == "anim":
            out.append(f'<div class="animline"><span class="anim">{it[1]}</span> &nbsp;<b>{it[2]}</b> — {it[3]}</div>')
        else:
            if not inul:
                out.append("<ul>"); inul = True
            cls = ' class="piege"' if kind == "p" else ""
            out.append(f"<li{cls}>{it[1]}</li>")
    if inul:
        out.append("</ul>")
    return "\n".join(out)

def render_ex(ex, n):
    steps = ex["steps"]
    lis = []
    for i, s in enumerate(steps):
        cls = ' class="fin"' if i == len(steps) - 1 else ""
        lis.append(f"<li{cls}>{s}</li>")
    cue = ""
    if ex.get("note"):
        col, txt = ex["note"]
        cue = (f'<p class="cue {col}"><span class="tagoff">hors capture</span>'
               f'<b>\u00c0 dire au pointeur :</b> {txt}</p>')
    return (f'<div class="exwrap"><div class="ex">'
            f'<div class="h"><span class="num">EXERCICE {n}</span><b>{ex["titre"]}</b>'
            f'<span class="cat">{ex["cat"]}</span></div>'
            f'<div class="en"><span class="lab">\u00c9nonc\u00e9</span>'
            f'<div class="txt">{ex["enonce"]}</div></div>'
            f'<div class="cor"><ol>{"".join(lis)}</ol></div>'
            f'</div>{cue}</div>')

def render_caps(c, first):
    brk = "" if first else " brk"
    t2 = render_t2(c["t2"])
    t1 = "".join(f"<li>{b}</li>" for b in c["t1"])
    t3 = "\n".join(render_ex(e, i + 1) for i, e in enumerate(c["t3"]))
    return f"""
<section class="caps{brk}">
<div class="caps-head">
  <div class="top"><span class="cd">{c['code']}</span><h3>{c['titre']}</h3><span class="rang">TOURNAGE {c.get("rang","-")}/{c.get("total",20)}</span><span class="dur">{c['duree']}</span></div>
  <div class="sub"><b>Couvre :</b> {c['couvre']}</div>
</div>
<div class="temps">
  <div class="temps-head"><span class="t">TEMPS 1</span><h4>Introduction du concept</h4><span class="min">&asymp; 3 min</span></div>
  <ul>{t1}</ul>
</div>
<div class="temps">
  <div class="temps-head"><span class="t">TEMPS 2</span><h4>Explication avec schéma animé</h4><span class="min">{c['t2min']}</span></div>
  {t2}
</div>
<div class="temps">
  <div class="temps-head"><span class="t">TEMPS 3</span><h4>Correction des exercices</h4><span class="min">{c['t3min']}</span></div>
  {t3}
</div>
</section>"""

def render_chapter(ch):
    caps = "\n".join(render_caps(c, i == 0) for i, c in enumerate(ch["caps"]))
    rows = "".join(f'<tr><td class="first">{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>' for r in ch["anims"])
    annexe = f"""
<div class="temps" style="break-inside:avoid">
  <div class="temps-head"><span class="t">ANNEXE</span><h4>Les animations du chapitre {ch['code']}</h4>
    <span class="min">{len(ch['anims'])} animations</span></div>
  <table><tr><th>Réf.</th><th>Animation</th><th>Capsule &amp; moment</th></tr>{rows}</table>
</div>"""
    return f"""
<section class="chap">
  <div class="chap-title"><span class="cd">{ch['code']}</span><h2>{ch['titre']}</h2></div>
  <p class="chap-intro">{ch['intro']}</p>
</section>
{caps}
{annexe}"""

COVER = """
<header class="masthead">
  <p class="org">SFA · Science For All — Prépa médecine · Bullet points de tournage · Mathématiques</p>
  <h1>M2 à M8 —<br><em>les quatorze capsules, point par point.</em></h1>
  <p class="lede">La trame de tournage des capsules de mathématiques, du chapitre M2 au chapitre M8. Ces bullet points ne sont pas un texte à lire : ce sont les points essentiels à la compréhension de l'étudiant, dans l'ordre où il faut les dire. Le professeur parle avec ses mots, mais ne saute rien et ne change pas l'ordre.</p>
</header>

<div class="box key">
  <span class="lab">Mode d'emploi</span>
  <p>Chaque capsule suit les <b>trois temps</b> du protocole : introduction du concept, explication avec schéma animé, correction d'exercices déjà écrits. Les minutages sont des repères ; la seule contrainte est la fourchette <b>15 à 35 minutes</b>.</p>
  <p>Les pastilles <span class="anim">ANIM-M0-00</span> marquent le moment exact où l'animation SFA doit apparaître. Les lignes <span style="color:#C02A20"><b>en rouge</b></span> sont les <b>pièges du concours</b> : ce sont elles qui font gagner des points, elles ne se sautent jamais.</p>
  <p>Les <b>exercices s'écrivent — énoncé et correction complète — dans la présentation avant le tournage</b>. Pendant la capsule, le professeur commente au pointeur, il n'écrit rien en direct.</p>
</div>

<div class="box warn">
  <span class="lab">Le découpage, et pourquoi il n'est pas mécanique</span>
  <p>Les deux capsules d'un chapitre ne coupent pas le référentiel en deux moitiés arbitraires : elles regroupent les notions <b>par famille logique</b>, pour que chaque capsule raconte une seule chose. M1 sépare « calculer » et « résoudre » ; M2 sépare « lire une fonction » et « la parabole et les opérations sur les fonctions » ; et ainsi de suite.</p>
  <p><b>Deux notions apparaissent volontairement dans deux chapitres, et ce n'est pas une répétition :</b> le <b>calcul avec les radicaux</b> (&radic;(ab), rationaliser, exposants fractionnaires) est en M1, tandis que la <b>fonction</b> &radic;x — domaine, courbe, transformations — est en M2. Idem pour la valeur absolue : la distance en M1, la fonction |x| en M2. Le professeur ne retraite pas la partie déjà couverte : il y renvoie en une phrase.</p>
  <p><b>Les matrices et les déterminants ne sont pas au programme ARES</b> : les systèmes linéaires à deux ou trois inconnues se résolvent par substitution et combinaison, un point c'est tout.</p>
</div>

<table>
  <tr><th>Chap.</th><th>Capsule A</th><th>Capsule B</th></tr>
  <tr><td class="first">M2</td><td>Le langage des fonctions</td><td>La parabole, la composée, la réciproque</td></tr>
  <tr><td class="first">M3</td><td>L'exponentielle</td><td>Le logarithme et ses applications</td></tr>
  <tr><td class="first">M4</td><td>Le cercle trigonométrique</td><td>Formules, équations et triangles</td></tr>
  <tr><td class="first">M5</td><td>Géométrie classique et mesures</td><td>Vecteurs et géométrie analytique</td></tr>
  <tr><td class="first">M6</td><td>Limites, continuité, asymptotes</td><td>La dérivée et l'étude de fonction</td></tr>
  <tr><td class="first">M7</td><td>Primitives</td><td>L'intégrale définie et les aires</td></tr>
  <tr><td class="first">M8</td><td>Décrire une série statistique</td><td>Probabilités et lecture critique</td></tr>
</table>
"""

def build(chapters, out):
    body = "\n".join(render_chapter(ch) for ch in chapters)
    n_anim = sum(len(ch["anims"]) for ch in chapters)
    foot = (f'<p class="foot">SFA · Science For All — bullet points de tournage, chapitres M2 à M8 · '
            f'14 capsules, {n_anim} animations · version 1 · conforme au protocole de création des capsules vidéo du 21/09/2026.</p>')
    html = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
            f'<title>SFA — Bullet points capsules M2-M8</title><style>{CSS}</style></head><body>'
            f'{COVER}{body}{foot}</body></html>')
    pathlib.Path(out).write_text(html)
    return n_anim

if __name__ == "__main__":
    import caps_data_1, caps_data_2
    chs = caps_data_1.CHAPTERS + caps_data_2.CHAPTERS
    n = build(chs, str(pathlib.Path(__file__).with_name("m2m8.html")))
    print(f"{len(chs)} chapitres, {sum(len(c['caps']) for c in chs)} capsules, {n} animations")
