# -*- coding: utf-8 -*-
"""CH7-B — Lire la table, predire, calculer le pH. 4 animations.

Figures au format 470 x 470, palette verte. La courbe de titrage et l'echelle
de pH sont calculees, jamais estimees.
"""
import math
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, curve, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH7-05 : la table des couples et le gamma ----------------
COUPLES = [("H₃O⁺", "H₂O"), ("CH₃COOH", "CH₃COO⁻"), ("NH₄⁺", "NH₃"), ("H₂O", "OH⁻")]
GX, GW, GH, GY0, GPAS = 24, 196, 46, 64, 54
GX2 = 252
TABLE = ""
for i, (ac, ba) in enumerate(COUPLES):
    y = GY0 + i * GPAS
    for x, txt in ((GX, ac), (GX2, ba)):
        TABLE += ('<rect x="%d" y="%d" width="%d" height="%d" rx="9" fill="%s" stroke="%s" '
                  'stroke-width="1.6"/>' % (x, y, GW, GH, TINT, GREY))
        TABLE += ('<text x="%d" y="%d" text-anchor="middle" font-size="21" '
                  'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
                  % (x + GW // 2, y + 31, DEEP, txt))


def centre_ligne(i):
    return GY0 + i * GPAS + GH / 2


# le gamma : de l'acide de la ligne 2 vers la base de la ligne 3
YA, YB = centre_ligne(1), centre_ligne(2)
GAMMA = ('<path d="M %d,%.1f L 236,%.1f L 236,%.1f L %d,%.1f" fill="none" stroke="%s" '
         'stroke-width="4" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#v1)"/>'
         % (GX + GW, YA, YA, YB, GX2 - 4, YB, SFA))
BAS_TABLE = GY0 + (len(COUPLES) - 1) * GPAS + GH
assert BAS_TABLE == 272, BAS_TABLE

# ---------------- CH7-06 : l'echelle de pH ----------------
PHX0, PHU, PHY = 30, 30, 200          # x(pH) = 30 + 30 pH  ->  pH 14 en x = 450


def xph(p):
    return PHX0 + PHU * p


GRAD = ""
for p in range(0, 15, 2):
    x = xph(p)
    GRAD += ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.8"/>'
             % (x, PHY, x, PHY + 10, GREY))
    GRAD += ('<text x="%d" y="%d" text-anchor="middle" font-size="15" '
             'font-family="Be Vietnam Pro,Arial" fill="%s">%d</text>' % (x, PHY + 30, INK2, p))
assert xph(14) == 450

MARQUES = ""
for p, lib in ((3, "10⁻³"), (5, "10⁻⁵")):
    x = xph(p)
    MARQUES += ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3"/>'
                % (x, PHY - 44, x, PHY - 28, DEEP))
    MARQUES += ('<text x="%d" y="%d" text-anchor="middle" font-size="20" '
                'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
                % (x, PHY - 52, DEEP, lib))
assert xph(5) - xph(3) > 44                 # les deux libelles ne peuvent pas se toucher

# ---------------- CH7-08 : la courbe de titrage ----------------
TOX, TOY, TUX, TUY = 44, 360, 16.0, 23.0    # origine et echelles
VEQ, PHEQ = 16.0, 7.0


def ph_titrage(V):
    return 7.0 + 5.2 * math.tanh((V - VEQ) / 1.2)


TITRAGE = curve(ph_titrage, 0.0, 25.0, TOX, TOY, TUX, TUY, n=300)
XEQ, YEQ = TOX + TUX * VEQ, TOY - TUY * PHEQ
assert abs(XEQ - 300.0) < 0.5 and abs(YEQ - 199.0) < 0.5, (XEQ, YEQ)
assert TOY - TUY * ph_titrage(25.0) > 30, "la courbe sort du cadre en haut"

SLIDES = """
  <!-- ==================== ANIM-CH7-05 ==================== -->
  <section class="slide" data-ref="ANIM-CH7-05" data-title="La règle du gamma" data-sub="Le sens de la réaction se lit sur la table, sans calcul" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <text x="122" y="44" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">ACIDES</text>
            <text x="350" y="44" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">BASES</text>
            @@TAB@@
            <line x1="11" y1="70" x2="11" y2="256" stroke="@@GREY@@" stroke-width="3" marker-end="url(#d1)"/>
            <line x1="459" y1="266" x2="459" y2="80" stroke="@@GREY@@" stroke-width="3" marker-end="url(#d1)"/>
          </g>
          <g class="step s2">@@GAM@@</g>
          <g class="step s3">
            <rect x="10" y="286" width="450" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="318" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">le tracé forme un gamma → la réaction a lieu</text>
          </g>
          <g class="step s4">
            <rect x="10" y="348" width="450" height="52" rx="12" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="380" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">tracé inversé → elle n'a pas lieu</text>
            <rect x="10" y="410" width="450" height="48" rx="12" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.2"/>
            <text x="235" y="440" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">aucun calcul : on lit la table</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Comment la table est rangée</h3>
          <p style="font-size:17px">Les couples sont classés par force : les acides les plus forts <b>en haut</b> à gauche, et leurs bases conjuguées — donc les plus faibles — en face.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La règle, en une phrase</h3>
          <p style="font-size:17px">L'acide le plus fort réagit avec la base la plus forte. On relie les deux espèces, et le tracé dessine un <b>gamma</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et le sens du tracé donne la réponse</h3>
          <p style="font-size:17px">Gamma à l'endroit — l'acide au-dessus, la base en dessous — la réaction <b>a lieu</b>. Tracé inversé : elle <b>n'a pas lieu</b>.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi cette figure mérite d'être apprise une fois pour toutes</h3>
          <p style="font-size:17px">Le programme ARES dit « <b>utilisation des tables</b> ». Ce qui est évalué n'est donc pas de retenir des pKa : c'est de <b>lire</b> une table fournie et d'en tirer une conclusion.<br><br>Et cette même figure reviendra <b>à l'identique</b> au chapitre CH8, sur la table des potentiels. Une construction, deux chapitres.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "La table des couples, classés par force : les acides forts en haut.",
      "On relie l'acide qui réagit à la base qui réagit — et le tracé dessine un <b>gamma</b>.",
      "Gamma à l'endroit : la réaction a lieu.",
      "Tracé inversé : elle n'a pas lieu. C'est tout.",
      "<em>Aucun calcul n'est nécessaire</em> — et c'est exactement ce que le programme demande."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH7-06 ==================== -->
  <section class="slide" data-ref="ANIM-CH7-06" data-title="Le pH est un logarithme" data-sub="L'échelle de la capsule D2-A des maths, en chimie" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="235" y="44" text-anchor="middle" font-size="28" @@FF@@ fill="@@DEEP@@" font-weight="700">pH = − log [H₃O⁺]</text>
          </g>
          <g class="step s2">
            <rect x="30" y="172" width="210" height="28" fill="@@RED@@" opacity="0.22"/>
            <rect x="240" y="172" width="210" height="28" fill="@@SFA@@" opacity="0.22"/>
            <text x="42" y="192" font-size="16" @@FF@@ fill="@@RED@@" font-weight="700">acide</text>
            <text x="438" y="192" text-anchor="end" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">basique</text>
            <line x1="26" y1="200" x2="454" y2="200" stroke="@@GREY@@" stroke-width="2"/>
            @@GRAD@@
          </g>
          <g class="step s3">@@MARQ@@</g>
          <g class="step s4">
            <rect x="10" y="262" width="450" height="68" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="292" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">une unité de pH = un facteur dix</text>
            <text x="235" y="318" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">de pH 3 à pH 5, la concentration est divisée par cent</text>
            <rect x="10" y="342" width="450" height="116" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="235" y="380" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">[H₃O⁺] = 10⁻ᵖᴴ</text>
            <text x="235" y="416" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">[H₃O⁺] × [OH⁻] = 10⁻¹⁴</text>
            <text x="235" y="446" text-anchor="middle" font-size="20" @@FF@@ fill="@@SFA@@" font-weight="700">donc pH + pOH = 14</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La définition, et elle suffit</h3>
          <p style="font-size:17px">pH = − log [H₃O⁺], la concentration étant exprimée en mol/L. C'est le logarithme décimal de la capsule <b>D2-A</b> des mathématiques, appliqué tel quel.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que l'échelle logarithmique change</h3>
          <p style="font-size:17px">Une unité de pH correspond à un facteur <b>dix</b> sur la concentration. Deux unités, un facteur cent. L'écart paraît petit, il ne l'est pas.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et la relation inverse</h3>
          <p style="font-size:17px">[H₃O⁺] = 10<sup>−pH</sup>. Pour un pH entier, <b>aucune calculatrice n'est nécessaire</b> — ce qui tombe bien, puisqu'elle est interdite.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'exemple qui fait comprendre l'échelle</h3>
          <p style="font-size:17px">Le suc gastrique est à pH 2, le sang à pH 7,4. Sur l'échelle, l'écart semble modeste : cinq unités et demie.<br><br>Sur les concentrations, il vaut 10<sup>5,4</sup> — le suc gastrique est <b>environ 250 000 fois plus acide</b> que le sang. Aucune définition ne fait comprendre le logarithme aussi bien que ce calcul.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le pH n'est pas une grandeur nouvelle : c'est un logarithme décimal.",
      "L'échelle va de 0 à 14, acide à gauche, basique à droite.",
      "Deux points : pH 3 et pH 5 — soit 10⁻³ et 10⁻⁵ mol/L.",
      "Deux unités d'écart, et la concentration est divisée par <b>cent</b>.",
      "<em>Et la relation inverse</em> se lit sans calculatrice pour tout pH entier."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH7-07 ==================== -->
  <section class="slide" data-ref="ANIM-CH7-07" data-title="Calculer le pH d'un acide fort" data-sub="Trois lignes, et le piège de la dilution extrême" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <rect x="56" y="22" width="358" height="66" rx="13" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="235" y="64" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">HCl à 1,0 × 10⁻² mol/L</text>
          </g>
          <g class="step s2">
            <line x1="235" y1="94" x2="235" y2="124" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d3)"/>
            <text x="235" y="152" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">acide fort → totalement dissocié</text>
            <text x="235" y="198" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">[H₃O⁺] = c = 10⁻² mol/L</text>
          </g>
          <g class="step s3">
            <rect x="40" y="222" width="390" height="76" rx="14" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="235" y="272" text-anchor="middle" font-size="32" @@FF@@ fill="@@DEEP@@" font-weight="700">pH = − log(10⁻²) = 2,0</text>
            <rect x="10" y="312" width="450" height="46" rx="12" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.2"/>
            <text x="235" y="341" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">base forte : pOH = − log c, puis pH = 14 − pOH</text>
          </g>
          <g class="step s4">
            <rect x="10" y="374" width="450" height="84" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="406" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">c = 10⁻⁸ ? la formule donnerait pH = 8</text>
            <text x="235" y="438" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">sous 10⁻⁶, l'eau domine et le pH tend vers 7</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi le calcul est immédiat</h3>
          <p style="font-size:17px">Un acide fort est <b>totalement dissocié</b>. La concentration en H₃O⁺ est donc <b>égale</b> à celle de l'acide introduit — il n'y a rien à calculer avant.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une seule ligne</h3>
          <p style="font-size:17px">pH = − log c. Pour c = 10⁻² mol/L, le pH vaut <b>2,0</b>. Aucune calculatrice, aucune approximation.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pour une base forte, un détour d'une ligne</h3>
          <p style="font-size:17px">On calcule d'abord le <b>pOH</b> = − log c, puis on passe au pH par <b>pH = 14 − pOH</b>. Calculer directement le pH d'une base est l'erreur d'étourderie classique.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège de la dilution extrême</h3>
          <p style="font-size:17px">Pour c = 10⁻⁸ mol/L, la formule donnerait pH = 8 — un acide qui rendrait la solution <b>basique</b>. C'est absurde.<br><br>En dessous de 10⁻⁶ mol/L, l'eau elle-même fournit plus d'ions que l'acide, et le pH tend vers 7. Le signaler suffit : le calcul complet n'est pas au programme, mais l'absurdité, elle, peut tomber en QCM.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Une solution d'acide chlorhydrique à un centième de mole par litre.",
      "Acide fort : il est totalement dissocié, donc [H₃O⁺] vaut exactement c.",
      "Le pH suit en une ligne : <b>2,0</b>.",
      "Pour une base forte, on passe d'abord par le pOH, puis par pH = 14 − pOH.",
      "<em>Et le piège :</em> sous 10⁻⁶ mol/L, la formule devient absurde — le pH tend vers 7."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH7-08 ==================== -->
  <section class="slide" data-ref="ANIM-CH7-08" data-title="Le titrage et son point d'équivalence" data-sub="Ce qu'on cherche, et comment on le repère" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <line x1="30" y1="360" x2="458" y2="360" stroke="@@GREY@@" stroke-width="1.8"/>
            <line x1="44" y1="30" x2="44" y2="376" stroke="@@GREY@@" stroke-width="1.8"/>
            <text x="56" y="44" font-size="17" @@FF@@ fill="@@GREY@@">pH</text>
            <text x="456" y="386" text-anchor="end" font-size="17" @@FF@@ fill="@@GREY@@">volume versé</text>
          </g>
          <g class="step s2">
            <path d="@@COURBE@@" fill="none" stroke="@@SFA@@" stroke-width="4.5" stroke-linecap="round"/>
            <text x="318" y="150" font-size="17" @@FF@@ fill="@@SFA@@" font-weight="700">saut brutal de pH</text>
          </g>
          <g class="step s3">
            <line x1="@@XEQ@@" y1="360" x2="@@XEQ@@" y2="@@YEQ@@" stroke="@@DEEP@@" stroke-width="2" stroke-dasharray="6 5"/>
            <line x1="44" y1="@@YEQ@@" x2="@@XEQ@@" y2="@@YEQ@@" stroke="@@DEEP@@" stroke-width="2" stroke-dasharray="6 5"/>
            <circle cx="@@XEQ@@" cy="@@YEQ@@" r="9" fill="@@RED@@"/>
            <text x="54" y="@@YTXT@@" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">pH = 7</text>
            <text x="@@XEQ@@" y="404" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">V à l'équivalence</text>
          </g>
          <g class="step s4">
            <rect x="10" y="420" width="450" height="46" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="450" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">à l'équivalence : c(A) × V(A) = c(B) × V(B)</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qu'on cherche</h3>
          <p style="font-size:17px">Titrer, c'est déterminer une <b>concentration inconnue</b> en la faisant réagir avec une solution de concentration connue.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le point d'équivalence</h3>
          <p style="font-size:17px">Il est atteint lorsque les réactifs ont été mélangés dans les <b>proportions exactes</b> de l'équation. Ni l'un ni l'autre n'est alors en excès.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Comment on le repère</h3>
          <p style="font-size:17px">Par un <b>saut brutal de pH</b> — la courbe devient presque verticale — ou par le virage d'un indicateur coloré choisi pour changer à ce pH-là.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La relation à l'équivalence, et un détail qui fait gagner du temps</h3>
          <p style="font-size:17px">Pour une réaction <b>un pour un</b> : c<sub>A</sub>V<sub>A</sub> = c<sub>B</sub>V<sub>B</sub>. Avec d'autres coefficients, on les fait intervenir.<br><br>Les volumes apparaissent <b>en rapport</b> : ils peuvent donc rester en millilitres des deux côtés. C'est l'un des rares cas du programme où la conversion en litres est inutile — le vérifier une fois évite de la refaire à chaque exercice.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux axes : le volume de solution titrante versé, et le pH du mélange.",
      "Au début, le pH bouge à peine. Puis il <b>saute</b>.",
      "Le milieu de ce saut est le <b>point d'équivalence</b> : les proportions y sont exactes.",
      "On lit alors le volume versé, et la concentration inconnue s'en déduit.",
      "<em>Et les volumes restent en millilitres :</em> ils apparaissent en rapport."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "TAB": TABLE, "GAM": GAMMA, "GRAD": GRAD, "MARQ": MARQUES,
    "COURBE": TITRAGE, "XEQ": "%.1f" % XEQ, "YEQ": "%.1f" % YEQ,
    "YTXT": "%.1f" % (YEQ - 8),
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH7-B : gamma ligne %.0f -> %.0f · equivalence (%.0f ; %.0f) · pH(0) = %.2f · pH(25) = %.2f"
      % (YA, YB, XEQ, YEQ, ph_titrage(0), ph_titrage(25)))
print("ok", make("CH7-B", "Capsule CH7-B — Lire la table, prédire, calculer le pH · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH7B.html")))
