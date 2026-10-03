# -*- coding: utf-8 -*-
"""CH4-A — Etats de la matiere et lois des gaz. 4 animations.

Figures au format 470 x 470. Toutes les particules sont placees par le code et
leur boite englobante est verifiee par assertion : aucune ne peut deborder de
son cadre.
"""
import sys, random
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, curve, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ================= CH4-02 : les trois etats =================
BW, BH, BY = 142, 180, 46          # boite d'un etat
BXS = (12, 164, 316)               # abscisses des trois boites
R = 10                             # rayon d'une particule
PAD = 18                           # marge interieure minimale


def _cercles(pts):
    return "".join('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (x, y, R, SFA) for x, y in pts)


def _verif(pts, bx):
    """Aucune particule ne sort de sa boite."""
    for x, y in pts:
        assert bx + 2 <= x - R and x + R <= bx + BW - 2, (x, bx)
        assert BY + 2 <= y - R and y + R <= BY + BH - 2, (y,)
    return pts


def solide(bx, n=4, pas=30):
    span = pas * (n - 1)
    x0 = bx + PAD + (BW - 2 * PAD - span) / 2
    y0 = BY + PAD + (BH - 2 * PAD - span) / 2
    return _verif([(x0 + pas * i, y0 + pas * j) for i in range(n) for j in range(n)], bx)


def liquide(bx, n=4, pas=30, seed=7, jx=6.0, jy=5.0):
    r = random.Random(seed)
    span = pas * (n - 1)
    x0 = bx + PAD + (BW - 2 * PAD - span) / 2
    y0 = BY + PAD + (BH - 2 * PAD - span) / 2
    return _verif([(x0 + pas * i + r.uniform(-jx, jx), y0 + pas * j + r.uniform(-jy, jy))
                   for i in range(n) for j in range(n)], bx)


def gaz(bx, n=6, seed=3):
    r = random.Random(seed)
    x1, x2 = bx + PAD, bx + BW - PAD
    y1, y2 = BY + PAD, BY + BH - PAD
    return _verif([(r.uniform(x1, x2), r.uniform(y1, y2)) for _ in range(n)], bx)


SOL = _cercles(solide(BXS[0]))
LIQ = _cercles(liquide(BXS[1]))
GAZ = _cercles(gaz(BXS[2]))

# ================= CH4-03 : isotherme de Boyle, P = 300/V =================
OX, OY, UX, UY = 64, 360, 62, 0.96
BOYLE = curve(lambda V: 300.0 / V, 1, 6, OX, OY, UX, UY)
P1 = (OX + UX * 1, OY - UY * 300)          # V = 1 · P = 300
P2 = (OX + UX * 2, OY - UY * 150)          # V = 2 · P = 150
assert 40 < P1[1] < OY and 40 < P2[1] < OY, (P1, P2)
assert OX < P2[0] < 452

SLIDES = """
  <!-- ==================== ANIM-CH4-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH4-01" data-title="Corps pur, mélange, phase" data-sub="Trois mots, et le test qui les distingue" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <text x="83" y="32" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">corps pur</text>
            <rect x="12" y="48" width="142" height="212" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <circle cx="50" cy="104" r="13" fill="@@SFA@@"/><circle cx="116" cy="104" r="13" fill="@@SFA@@"/>
            <circle cx="83" cy="154" r="13" fill="@@SFA@@"/>
            <circle cx="50" cy="204" r="13" fill="@@SFA@@"/><circle cx="116" cy="204" r="13" fill="@@SFA@@"/>
            <text x="83" y="292" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">une seule espèce</text>
          </g>
          <g class="step s2">
            <text x="235" y="32" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">homogène</text>
            <rect x="164" y="48" width="142" height="212" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <circle cx="202" cy="104" r="13" fill="@@SFA@@"/><circle cx="268" cy="104" r="13" fill="@@DEEP@@"/>
            <circle cx="235" cy="154" r="13" fill="@@DEEP@@"/>
            <circle cx="202" cy="204" r="13" fill="@@DEEP@@"/><circle cx="268" cy="204" r="13" fill="@@SFA@@"/>
            <text x="235" y="292" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">une seule phase</text>
          </g>
          <g class="step s3">
            <text x="387" y="32" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">hétérogène</text>
            <rect x="316" y="48" width="142" height="212" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <path d="M318 154 L318 248 Q318 260 330 260 L444 260 Q456 260 456 248 L456 154 Z" fill="@@TINT2@@"/>
            <circle cx="354" cy="98" r="13" fill="@@SFA@@"/><circle cx="420" cy="98" r="13" fill="@@SFA@@"/>
            <circle cx="387" cy="126" r="13" fill="@@SFA@@"/>
            <circle cx="354" cy="196" r="13" fill="@@DEEP@@"/><circle cx="420" cy="196" r="13" fill="@@DEEP@@"/>
            <circle cx="387" cy="226" r="13" fill="@@DEEP@@"/>
            <line x1="318" y1="154" x2="456" y2="154" stroke="@@RED@@" stroke-width="3"/>
            <text x="387" y="292" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">deux phases</text>
          </g>
          <g class="step s4">
            <rect x="12" y="330" width="446" height="104" rx="14" fill="@@TINT2@@"/>
            <text x="235" y="372" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">on distingue les constituants ?</text>
            <text x="235" y="408" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">alors c'est hétérogène</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un corps pur</h3>
          <p style="font-size:17px">Il ne contient qu'<b>une seule espèce chimique</b>. L'eau distillée est un corps pur ; l'eau du robinet ne l'est pas.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une phase</h3>
          <p style="font-size:17px">C'est une région d'aspect et de composition <b>uniformes</b>. Un mélange homogène n'en présente qu'une ; un mélange hétérogène en présente plusieurs.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le test, et il est visuel</h3>
          <p style="font-size:17px">Si on <b>distingue</b> les constituants — à l'œil ou au microscope — le mélange est hétérogène. Sinon il est homogène.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège de vocabulaire</h3>
          <p style="font-size:17px"><b>« Homogène » ne veut pas dire « pur ».</b> L'eau salée est parfaitement homogène — une seule phase, aucune séparation visible — et ce n'est pourtant pas un corps pur : elle contient deux espèces.<br><br>Les deux mots répondent à deux questions différentes : <b>combien d'espèces</b>, et <b>combien de phases</b>.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Un corps pur : une seule espèce chimique, rien d'autre.",
      "Un mélange homogène : plusieurs espèces, mais une seule phase — on ne les distingue pas.",
      "Un mélange hétérogène : on voit la séparation, il y a deux phases.",
      "Le test tient en une question : distingue-t-on les constituants ?",
      "<em>Et le piège :</em> homogène ne veut pas dire pur. L'eau salée en est la preuve."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH4-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH4-02" data-title="Les trois états, vus par les liaisons" data-sub="Ce que CH3 vient d'expliquer, appliqué" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="83" y="32" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">SOLIDE</text>
            <rect x="12" y="46" width="142" height="180" rx="12" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            @@SOL@@
            <text x="83" y="262" text-anchor="middle" font-size="15" @@FF@@ fill="#3F3F46">forces dominantes</text>
            <text x="83" y="288" text-anchor="middle" font-size="15" @@FF@@ fill="#3F3F46">ordonné, figé</text>
            <text x="83" y="330" text-anchor="middle" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">forme et volume</text>
            <text x="83" y="352" text-anchor="middle" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">propres</text>
          </g>
          <g class="step s2">
            <text x="235" y="32" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">LIQUIDE</text>
            <rect x="164" y="46" width="142" height="180" rx="12" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            @@LIQ@@
            <text x="235" y="262" text-anchor="middle" font-size="15" @@FF@@ fill="#3F3F46">forces présentes</text>
            <text x="235" y="288" text-anchor="middle" font-size="15" @@FF@@ fill="#3F3F46">mobile mais serré</text>
            <text x="235" y="330" text-anchor="middle" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">volume propre</text>
            <text x="235" y="352" text-anchor="middle" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">seulement</text>
          </g>
          <g class="step s3">
            <text x="387" y="32" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">GAZ</text>
            <rect x="316" y="46" width="142" height="180" rx="12" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            @@GAZ@@
            <text x="387" y="262" text-anchor="middle" font-size="15" @@FF@@ fill="#3F3F46">forces faibles</text>
            <text x="387" y="288" text-anchor="middle" font-size="15" @@FF@@ fill="#3F3F46">libre et espacé</text>
            <text x="387" y="330" text-anchor="middle" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">ni forme</text>
            <text x="387" y="352" text-anchor="middle" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">ni volume</text>
          </g>
          <g class="step s4">
            <rect x="12" y="382" width="446" height="76" rx="14" fill="@@TINT2@@"/>
            <text x="235" y="412" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">solide et liquide : incompressibles</text>
            <text x="235" y="440" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">gaz : surtout du vide, donc compressible</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une seule grandeur explique les trois</h3>
          <p style="font-size:17px">C'est le rapport entre les <b>forces intermoléculaires</b> — vues en CH3 — et l'<b>agitation thermique</b>. Chauffer, c'est augmenter la seconde.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que « volume propre » signifie</h3>
          <p style="font-size:17px">Dans un solide et un liquide, les particules se <b>touchent déjà</b> : on ne peut plus les rapprocher. C'est pourquoi ils sont pratiquement <b>incompressibles</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un gaz est surtout du vide</h3>
          <p style="font-size:17px">Ses particules sont très éloignées les unes des autres. Il est donc <b>fortement compressible</b>, et occupe tout le volume qu'on lui offre.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que ce tableau permet de prédire</h3>
          <p style="font-size:17px">Une substance à fortes liaisons intermoléculaires — l'eau, avec ses liaisons hydrogène — sera <b>liquide</b> là où une substance apolaire de masse comparable sera <b>gazeuse</b>.<br><br>L'état d'un corps à température ambiante n'est donc pas une donnée à apprendre : il se <b>déduit</b> de la nature de ses liaisons. C'est le lien direct avec la capsule précédente.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Dans un solide, les forces l'emportent : les particules sont ordonnées et fixes.",
      "Dans un liquide, elles se touchent encore mais peuvent glisser les unes sur les autres.",
      "Dans un gaz, elles sont libres et très espacées — le gaz est surtout du vide.",
      "D'où l'incompressibilité des deux premiers, et la compressibilité du troisième.",
      "<em>Et l'état se déduit :</em> fortes liaisons intermoléculaires, donc liquide plutôt que gaz."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH4-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH4-03" data-title="PV = nRT, et les trois lois qu'elle contient" data-sub="Boyle, Charles, Gay-Lussac en une seule équation" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <line x1="46" y1="360" x2="458" y2="360" stroke="@@GREY@@" stroke-width="1.8"/>
            <line x1="64" y1="36" x2="64" y2="378" stroke="@@GREY@@" stroke-width="1.8"/>
            <text x="456" y="384" text-anchor="end" font-size="16" @@FF@@ fill="@@GREY@@">volume V</text>
            <text x="76" y="50" font-size="16" @@FF@@ fill="@@GREY@@">pression P</text>
          </g>
          <g class="step s2">
            <path d="@@BOYLE@@" fill="none" stroke="@@SFA@@" stroke-width="4.5" stroke-linecap="round"/>
            <text x="248" y="148" font-size="20" @@FF@@ fill="@@SFA@@" font-weight="700">P × V = constante</text>
            <text x="248" y="176" font-size="16" @@FF@@ fill="#3F3F46">à température constante</text>
          </g>
          <g class="step s3">
            <circle cx="@@X1@@" cy="@@Y1@@" r="9" fill="@@DEEP@@"/>
            <circle cx="@@X2@@" cy="@@Y2@@" r="9" fill="@@DEEP@@"/>
            <line x1="@@X1@@" y1="@@Y1@@" x2="@@X2@@" y2="@@Y2@@" stroke="@@DEEP@@" stroke-width="2.2" stroke-dasharray="6 5"/>
            <text x="206" y="304" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">V doublé → P divisée par 2</text>
          </g>
          <g class="step s4">
            <rect x="44" y="402" width="382" height="58" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="426" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">T toujours en kelvins</text>
            <text x="235" y="450" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">T(K) = θ(°C) + 273</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une seule équation</h3>
          <div class="expr" style="font-size:26px;text-align:left;line-height:1.25">P V = n R T</div>
          <p style="font-size:17px;margin-top:4px">Elle relie les quatre grandeurs d'un gaz. Les trois lois historiques n'en sont que des cas particuliers.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">À température constante : Boyle</h3>
          <p style="font-size:17px">P × V reste constant. Comprimer, c'est faire monter la pression <b>en proportion inverse</b> — d'où cette courbe, qui est une hyperbole.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">À pression constante : Charles</h3>
          <p style="font-size:17px">V / T reste constant : le volume est <b>proportionnel à la température absolue</b>. Et c'est là que le piège se referme.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La méthode la plus rapide, et le piège à éviter</h3>
          <p style="font-size:17px">Quand on <b>compare deux états</b>, on n'utilise jamais PV = nRT directement. On écrit <b>P₁V₁ / T₁ = P₂V₂ / T₂</b> et on simplifie ce qui ne change pas : ni R ni n n'apparaissent.<br><br><b>Le piège :</b> travailler en degrés Celsius. Passer de 20 à 40 °C ne double pas le volume — en kelvins, on passe de 293 à 313, soit <b>7 % de plus</b> seulement.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux axes : le volume d'un gaz, et sa pression.",
      "À température constante, leur produit reste constant — c'est la loi de Boyle.",
      "Doubler le volume divise donc la pression par deux, exactement.",
      "Et la température, elle, entre toujours en <b>kelvins</b>. Jamais en degrés Celsius.",
      "<em>Pour comparer deux états :</em> P₁V₁/T₁ = P₂V₂/T₂, et on simplifie."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH4-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH4-04" data-title="Le volume molaire, et les conditions qui le fixent" data-sub="22,4 L, mais à quelles conditions" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <text x="88" y="34" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">H₂</text>
            <text x="235" y="34" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">O₂</text>
            <text x="382" y="34" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">CO₂</text>
            <rect x="26" y="52" width="124" height="230" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <rect x="173" y="52" width="124" height="230" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <rect x="320" y="52" width="124" height="230" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="88" y="176" text-anchor="middle" font-size="21" @@FF@@ fill="#3F3F46">1 mol</text>
            <text x="235" y="176" text-anchor="middle" font-size="21" @@FF@@ fill="#3F3F46">1 mol</text>
            <text x="382" y="176" text-anchor="middle" font-size="21" @@FF@@ fill="#3F3F46">1 mol</text>
          </g>
          <g class="step s2">
            <line x1="88" y1="294" x2="88" y2="322" stroke="@@GREY@@" stroke-width="2.4" marker-end="url(#d4)"/>
            <line x1="235" y1="294" x2="235" y2="322" stroke="@@GREY@@" stroke-width="2.4" marker-end="url(#d4)"/>
            <line x1="382" y1="294" x2="382" y2="322" stroke="@@GREY@@" stroke-width="2.4" marker-end="url(#d4)"/>
            <text x="235" y="374" text-anchor="middle" font-size="40" @@FF@@ fill="@@SFA@@" font-weight="700">22,4 L chacun</text>
          </g>
          <g class="step s3">
            <rect x="46" y="400" width="378" height="56" rx="12" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="435" text-anchor="middle" font-size="21" @@FF@@ fill="@@RED@@" font-weight="700">à 0 °C et 1 atm — et seulement là</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La nature du gaz n'intervient pas</h3>
          <p style="font-size:17px">Dans PV = nRT, <b>aucun terme ne dépend du gaz</b>. Une mole de dihydrogène et une mole de dioxyde de carbone occupent donc le même volume.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Mais la valeur dépend des conditions</h3>
          <p style="font-size:17px">22,4 L/mol vaut aux <b>conditions normales</b> : 0 °C et 1 atm. À 25 °C, le volume molaire vaut environ <b>24,5 L/mol</b>.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Citer 22,4 sans vérifier est une faute</h3>
          <p style="font-size:17px">L'énoncé précise toujours les conditions, ou donne directement la valeur à utiliser. <b>On la lit, on ne la suppose pas.</b></p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que cela change pour tout le chapitre CH9</h3>
          <p style="font-size:17px">Pour un solide ou un liquide, on passe de la masse aux moles par la <b>masse molaire</b>. Pour un gaz, on passe du volume aux moles par le <b>volume molaire</b>.<br><br>C'est le <b>seul</b> changement entre un problème de gravimétrie et un problème de volumétrie. La chaîne de conversion, elle, ne bouge pas : on remplace une case, pas la méthode.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Trois gaz différents, une mole de chacun.",
      "Ils occupent <b>exactement le même volume</b> : 22,4 litres.",
      "Mais seulement à 0 °C et 1 atm — à 25 °C, ce serait 24,5 litres.",
      "La valeur n'est donc pas une constante universelle : elle dépend des conditions.",
      "<em>Et c'est le seul changement</em> entre gravimétrie et volumétrie, au chapitre CH9."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "SOL": SOL, "LIQ": LIQ, "GAZ": GAZ, "BOYLE": BOYLE,
    "X1": "%.1f" % P1[0], "Y1": "%.1f" % P1[1],
    "X2": "%.1f" % P2[0], "Y2": "%.1f" % P2[1],
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("particules confinees : solide %d · liquide %d · gaz %d"
      % (len(solide(BXS[0])), len(liquide(BXS[1])), len(gaz(BXS[2]))))
print("Boyle : V=1 -> (%.1f ; %.1f)  V=2 -> (%.1f ; %.1f)" % (P1[0], P1[1], P2[0], P2[1]))
print("ok", make("CH4-A", "Capsule CH4-A — États de la matière et lois des gaz · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH4A.html")))
