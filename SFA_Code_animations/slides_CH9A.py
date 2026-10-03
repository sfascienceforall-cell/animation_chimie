# -*- coding: utf-8 -*-
"""CH9-A — Ponderer et faire un bilan. 4 animations.

Figures au format 470 x 470, palette verte.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH9-01 : la ponderation, element par element ----------------
LIGNES = [("1", "C₃H₈ + O₂ → CO₂ + H₂O", "l'équation de départ, non pondérée"),
          ("2", "C₃H₈ + O₂ → 3 CO₂ + H₂O", "le carbone : 3 à gauche, donc 3 CO₂"),
          ("3", "C₃H₈ + O₂ → 3 CO₂ + 4 H₂O", "l'hydrogène : 8 à gauche, donc 4 H₂O"),
          ("4", "C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O", "l'oxygène en dernier : 10 atomes à droite")]
LY0, LPAS, LXC, LXT = 66, 78, 32, 62


def ligne(i):
    n, eq, com = LIGNES[i]
    y = LY0 + i * LPAS
    fin = (i == len(LIGNES) - 1)
    coul = SFA if fin else DEEP
    o = ('<circle cx="%d" cy="%d" r="15" fill="%s"/>'
         '<text x="%d" y="%d" text-anchor="middle" font-size="16" '
         'font-family="Be Vietnam Pro,Arial" fill="#FFFFFF" font-weight="700">%s</text>'
         % (LXC, y - 7, coul, LXC, y - 1, n))
    o += ('<text x="%d" y="%d" font-size="22" font-family="Be Vietnam Pro,Arial" fill="%s" '
          'font-weight="700">%s</text>' % (LXT, y, coul, eq))
    o += ('<text x="%d" y="%d" font-size="15" font-family="Be Vietnam Pro,Arial" '
          'fill="#3F3F46">%s</text>' % (LXT, y + 24, com))
    return o


ETAPE = [ligne(i) for i in range(4)]
assert LY0 + 3 * LPAS + 24 == 324

# ---------------- CH9-03 : le tableau d'avancement ----------------
COLS = ["état", "H₂", "O₂", "H₂O"]
RANGS = [("initial", "4,0", "3,0", "0"),
         ("en cours", "4,0 − 2x", "3,0 − x", "2x"),
         ("final", "0", "1,0", "4,0")]
TW, TX0, TY0, TRH = 110, 12, 62, 48
TAB = ""
for c, nom in enumerate(COLS):
    x = TX0 + c * TW
    TAB += ('<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="1.4"/>'
            % (x, TY0, TW - 4, TRH - 4, TINT2, GREY))
    TAB += ('<text x="%d" y="%d" text-anchor="middle" font-size="18" '
            'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
            % (x + (TW - 4) // 2, TY0 + 29, DEEP, nom))
for r, rang in enumerate(RANGS):
    y = TY0 + (r + 1) * TRH
    for c, val in enumerate(rang):
        x = TX0 + c * TW
        gras = "700" if c == 0 else "500"
        coul = DEEP if c == 0 else INK2
        TAB += ('<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="#FFFFFF" stroke="%s" '
                'stroke-width="1.4"/>' % (x, y, TW - 4, TRH - 4, GREY))
        TAB += ('<text x="%d" y="%d" text-anchor="middle" font-size="17" '
                'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="%s">%s</text>'
                % (x + (TW - 4) // 2, y + 29, coul, gras, val))
BAS_TAB = TY0 + len(RANGS) * TRH + TRH - 4
assert BAS_TAB == 250, BAS_TAB
assert TX0 + len(COLS) * TW - 4 == 448

SLIDES = """
  <!-- ==================== ANIM-CH9-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-01" data-title="Pondérer sans tâtonner" data-sub="L'ordre dans lequel on équilibre les éléments" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <text x="16" y="32" font-size="17" @@FF@@ fill="@@GREY@@">combustion complète du propane</text>
            @@L0@@
          </g>
          <g class="step s2">@@L1@@</g>
          <g class="step s3">@@L2@@</g>
          <g class="step s4">@@L3@@
            <rect x="10" y="356" width="450" height="102" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="390" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">l'oxygène figure dans les deux produits</text>
            <text x="235" y="420" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">l'ajuster en premier oblige à tout reprendre</text>
            <text x="235" y="448" text-anchor="middle" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">on ne touche jamais aux indices</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le principe, et il est physique</h3>
          <p style="font-size:17px">Une réaction <b>conserve les atomes</b>. Aucun n'apparaît, aucun ne disparaît : ils se réorganisent. Pondérer, c'est simplement écrire cela.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'ordre à respecter</h3>
          <p style="font-size:17px">D'abord les éléments qui n'apparaissent que dans <b>une</b> espèce de chaque côté : le carbone, puis l'hydrogène. L'<b>oxygène en dernier</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi l'oxygène en dernier</h3>
          <p style="font-size:17px">Parce qu'il figure presque toujours dans <b>plusieurs produits</b>. L'ajuster en premier oblige à le reprendre après chaque autre élément.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La règle qu'on ne transgresse jamais</h3>
          <p style="font-size:17px">On modifie les <b>coefficients</b> devant les formules, <b>jamais les indices</b> à l'intérieur.<br><br>Changer H₂O en H₂O₂ ne rééquilibre pas une équation : cela remplace l'eau par de l'eau oxygénée. C'est une autre substance, et l'équation ne décrit plus la même réaction.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "La combustion du propane, telle qu'elle s'écrit avant d'être pondérée.",
      "Le <b>carbone</b> d'abord : trois à gauche, donc trois dioxydes de carbone.",
      "L'<b>hydrogène</b> ensuite : huit à gauche, donc quatre molécules d'eau.",
      "L'<b>oxygène en dernier</b> : dix atomes à droite, donc cinq dioxygènes.",
      "<em>Et jamais les indices :</em> on ne change que les coefficients devant les formules."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-02" data-title="Les coefficients sont des rapports de moles" data-sub="Jamais de masses, et c'est toute la difficulté" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <rect x="60" y="24" width="280" height="58" rx="12" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="200" y="61" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">masse donnée (g)</text>
            <line x1="200" y1="88" x2="200" y2="112" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d2)"/>
            <text x="352" y="106" font-size="17" @@FF@@ fill="@@SFA@@" font-weight="700">÷ M</text>
            <rect x="60" y="118" width="280" height="58" rx="12" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.6"/>
            <text x="200" y="155" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">moles du réactif</text>
          </g>
          <g class="step s2">
            <line x1="200" y1="182" x2="200" y2="206" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v2)"/>
            <text x="352" y="200" font-size="17" @@FF@@ fill="@@SFA@@" font-weight="700">coefficients</text>
            <rect x="60" y="212" width="280" height="58" rx="12" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.6"/>
            <text x="200" y="249" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">moles du produit</text>
          </g>
          <g class="step s3">
            <line x1="200" y1="276" x2="200" y2="300" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d2)"/>
            <text x="352" y="294" font-size="17" @@FF@@ fill="@@SFA@@" font-weight="700">× M</text>
            <rect x="60" y="306" width="280" height="58" rx="12" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="200" y="343" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">masse cherchée (g)</text>
          </g>
          <g class="step s4">
            <rect x="10" y="384" width="450" height="76" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="414" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">appliquer un coefficient à des grammes</text>
            <text x="235" y="444" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">c'est l'erreur qui coûte le plus au concours</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qu'une équation pondérée dit réellement</h3>
          <p style="font-size:17px">« Une mole de propane réagit avec <b>cinq moles</b> de dioxygène ». Elle ne dit <b>rien</b> sur les masses — pas un mot.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La conséquence pratique</h3>
          <p style="font-size:17px">Toute donnée en grammes doit être convertie en moles <b>avant</b> d'utiliser les coefficients, et reconvertie après. Il n'y a pas de raccourci.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La chaîne universelle du chapitre</h3>
          <p style="font-size:17px"><b>masse → mole → coefficients → mole → masse.</b> Elle ne change jamais, quel que soit l'exercice. On la pose avant même de lire les nombres.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">LE piège du chapitre, et de tout le programme</h3>
          <p style="font-size:17px">Appliquer un rapport de coefficients <b>directement à des grammes</b>. C'est l'erreur qui fait perdre le plus de points au concours de médecine, toutes matières confondues.<br><br>Elle se prévient par une <b>seule discipline</b> : convertir d'abord, toujours. Un coefficient ne multiplie jamais une masse.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "On part d'une masse, et on la convertit en moles. C'est n = m / M.",
      "C'est <b>là seulement</b> que les coefficients de l'équation interviennent.",
      "Puis on reconvertit en masse, si l'énoncé la demande.",
      "Cette chaîne ne change jamais : masse, mole, coefficients, mole, masse.",
      "<em>Et le piège :</em> un coefficient ne multiplie jamais une masse. Jamais."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-03" data-title="Le tableau d'avancement" data-sub="Trois lignes qui règlent tous les exercices" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <text x="235" y="36" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">2 H₂ + O₂ → 2 H₂O</text>
            @@TAB@@
          </g>
          <g class="step s2">
            <rect x="10" y="276" width="450" height="76" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="306" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">un réactif diminue de son coefficient fois x</text>
            <text x="235" y="336" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">un produit augmente de son coefficient fois x</text>
          </g>
          <g class="step s3">
            <rect x="10" y="368" width="450" height="90" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="235" y="400" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">x maximal quand le premier réactif s'épuise</text>
            <text x="235" y="434" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">c'est le réactif limitant — capsule suivante</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Trois lignes, une colonne par espèce</h3>
          <p style="font-size:17px">État <b>initial</b>, état <b>en cours</b>, état <b>final</b>. La structure est toujours la même, quelle que soit la réaction.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que l'avancement x représente</h3>
          <p style="font-size:17px">Le nombre de fois où la réaction s'est produite <b>telle qu'elle est écrite</b>. Chaque quantité s'exprime ensuite en fonction de lui.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Toute la mécanique tient en une ligne</h3>
          <p style="font-size:17px">Un réactif <b>diminue</b> de son coefficient fois x. Un produit <b>augmente</b> de son coefficient fois x. Il n'y a rien d'autre à savoir.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi ce tableau vaut la peine d'être posé</h3>
          <p style="font-size:17px">Il transforme un problème de raisonnement en un problème d'<b>écriture</b>. Une fois les trois lignes remplies, toutes les questions de l'énoncé se lisent dedans : quantité formée, quantité restante, réactif limitant.<br><br>Sur un QCM chronométré, poser le tableau coûte trente secondes et supprime toute hésitation pour les cinq questions qui suivent.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Trois lignes, une colonne par espèce. La structure ne change jamais.",
      "L'<b>avancement x</b> compte combien de fois la réaction s'est produite.",
      "Un réactif diminue de son coefficient fois x, un produit augmente d'autant.",
      "Le tableau se remplit donc sans réfléchir, ligne après ligne.",
      "<em>Et il s'arrête</em> quand le premier réactif s'épuise : c'est le limitant."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-04" data-title="Le bilan massique se conserve toujours" data-sub="Le contrôle qui ne coûte rien" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <text x="235" y="34" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O</text>
            <line x1="60" y1="118" x2="410" y2="118" stroke="@@DEEP@@" stroke-width="4" stroke-linecap="round"/>
            <path d="M235,118 L212,178 L258,178 Z" fill="@@DEEP@@"/>
            <line x1="130" y1="118" x2="130" y2="188" stroke="@@GREY@@" stroke-width="2.4"/>
            <line x1="340" y1="118" x2="340" y2="188" stroke="@@GREY@@" stroke-width="2.4"/>
            <rect x="56" y="188" width="148" height="92" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.4"/>
            <rect x="266" y="188" width="148" height="92" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="118" y="162" text-anchor="end" font-size="16" @@FF@@ fill="@@GREY@@">réactifs</text>
            <text x="352" y="162" font-size="16" @@FF@@ fill="@@GREY@@">produits</text>
          </g>
          <g class="step s2">
            <text x="130" y="222" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">1 × 44 + 5 × 32</text>
            <text x="130" y="258" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">204 g</text>
            <text x="340" y="222" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">3 × 44 + 4 × 18</text>
            <text x="340" y="258" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">204 g</text>
          </g>
          <g class="step s3">
            <rect x="10" y="304" width="450" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="336" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">la masse se conserve toujours ✓</text>
          </g>
          <g class="step s4">
            <rect x="10" y="372" width="450" height="86" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="404" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">mais pas le nombre de moles</text>
            <text x="235" y="438" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">6 moles de réactifs → 7 moles de produits</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La masse totale se conserve</h3>
          <p style="font-size:17px">La somme des masses des réactifs consommés égale <b>exactement</b> celle des produits formés. Ce n'est pas une approximation.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un contrôle gratuit</h3>
          <p style="font-size:17px">Il attrape <b>presque toutes</b> les erreurs de coefficient. On le fait systématiquement, même quand l'énoncé ne le demande pas.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qui ne se conserve pas</h3>
          <p style="font-size:17px">Le <b>nombre de moles</b>. Ici, six moles de réactifs donnent sept moles de produits. Confondre les deux mène à des raisonnements faux sur les gaz.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi la masse se conserve et pas les moles</h3>
          <p style="font-size:17px">Parce que la réaction <b>réorganise</b> les atomes sans en créer ni en détruire : leur nombre et leur masse totale sont intacts.<br><br>Mais rien n'impose que ces atomes se regroupent en autant de molécules qu'avant. Une molécule de propane et cinq de dioxygène — six objets — se redistribuent en trois dioxydes de carbone et quatre eaux : <b>sept</b> objets. Les atomes n'ont pas bougé en nombre ; leur emballage, si.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Une balance : les réactifs d'un côté, les produits de l'autre.",
      "On calcule les masses avec les masses molaires : 204 grammes de chaque côté.",
      "La masse se conserve — toujours, et c'est un contrôle gratuit.",
      "Mais le nombre de moles, lui, ne se conserve pas : six deviennent sept.",
      "<em>Ce sont les atomes qui se conservent</em>, pas la façon dont ils sont emballés."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "L0": ETAPE[0], "L1": ETAPE[1], "L2": ETAPE[2], "L3": ETAPE[3], "TAB": TAB,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH9-A : %d etapes de ponderation · tableau %d colonnes x %d lignes, bas = %d"
      % (len(LIGNES), len(COLS), len(RANGS) + 1, BAS_TAB))
print("ok", make("CH9-A", "Capsule CH9-A — Pondérer et faire un bilan · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH9A.html")))
