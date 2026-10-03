# -*- coding: utf-8 -*-
"""CH9-B — Reactif limitant, gravimetrie et volumetrie. 4 animations.

Figures au format 470 x 470, palette verte. Les longueurs de barre du reactif
en exces sont calculees a partir des quantites, jamais estimees.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH9-06 : la chaine de la gravimetrie ----------------
LIGNES = [("1", "n = 50 ÷ 100 = 0,50 mol", "masse → mole, avec M(CaCO₃) = 100 g/mol"),
          ("2", "coefficients 1 et 1 → 0,50 mol", "mole → mole, par le rapport des coefficients"),
          ("3", "m = 0,50 × 56", "mole → masse, avec M(CaO) = 56 g/mol"),
          ("4", "m = 28 g", "et le bilan massique le confirme")]
LY0, LPAS, LXC, LXT = 70, 82, 32, 62


def ligne(i):
    n, eq, com = LIGNES[i]
    y = LY0 + i * LPAS
    fin = (i == len(LIGNES) - 1)
    coul = SFA if fin else DEEP
    o = ('<circle cx="%d" cy="%d" r="15" fill="%s"/>'
         '<text x="%d" y="%d" text-anchor="middle" font-size="16" '
         'font-family="Be Vietnam Pro,Arial" fill="#FFFFFF" font-weight="700">%s</text>'
         % (LXC, y - 7, coul, LXC, y - 1, n))
    o += ('<text x="%d" y="%d" font-size="%d" font-family="Be Vietnam Pro,Arial" fill="%s" '
          'font-weight="700">%s</text>' % (LXT, y, 30 if fin else 22, coul, eq))
    o += ('<text x="%d" y="%d" font-size="15" font-family="Be Vietnam Pro,Arial" '
          'fill="#3F3F46">%s</text>' % (LXT, y + 24, com))
    return o


ETAPE = [ligne(i) for i in range(4)]

# ---------------- CH9-08 : le reactif en exces, barre calculee ----------------
N_INIT, N_CONSO = 3.0, 2.0                 # moles de O2 : disponibles, consommees
BX, BW, BY, BH = 26, 418, 168, 68
X_COUPE = BX + BW * N_CONSO / N_INIT
assert abs(X_COUPE - 304.667) < 0.01, X_COUPE
BARRE = ('<rect x="%d" y="%d" width="%.1f" height="%d" rx="10" fill="%s" opacity="0.85"/>'
         '<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="10" fill="%s" opacity="0.30"/>'
         '<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="none" stroke="%s" stroke-width="2.4"/>'
         % (BX, BY, X_COUPE - BX, BH, SFA,
            X_COUPE, BY, BX + BW - X_COUPE, BH, RED,
            BX, BY, BW, BH, DEEP))
CX_CONSO = (BX + X_COUPE) / 2
CX_RESTE = (X_COUPE + BX + BW) / 2

SLIDES = """
  <!-- ==================== ANIM-CH9-05 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-05" data-title="Trouver le réactif limitant" data-sub="On compare des rapports, pas des quantités" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <text x="235" y="34" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">2 H₂ + O₂ → 2 H₂O</text>
            <rect x="14" y="54" width="200" height="94" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="114" y="88" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">dihydrogène</text>
            <text x="114" y="126" text-anchor="middle" font-size="28" @@FF@@ fill="@@DEEP@@" font-weight="700">4,0 mol</text>
            <rect x="256" y="54" width="200" height="94" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="356" y="88" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">dioxygène</text>
            <text x="356" y="126" text-anchor="middle" font-size="28" @@FF@@ fill="@@DEEP@@" font-weight="700">3,0 mol</text>
          </g>
          <g class="step s2">
            <line x1="114" y1="160" x2="114" y2="188" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d1)"/>
            <line x1="356" y1="160" x2="356" y2="188" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d1)"/>
            <text x="114" y="220" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">4,0 ÷ 2 = 2,0</text>
            <text x="356" y="220" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">3,0 ÷ 1 = 3,0</text>
            <text x="235" y="256" text-anchor="middle" font-size="17" @@FF@@ fill="@@GREY@@">on divise chaque quantité par son coefficient</text>
          </g>
          <g class="step s3">
            <rect x="14" y="278" width="200" height="66" rx="13" fill="@@TINT2@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="114" y="320" text-anchor="middle" font-size="24" @@FF@@ fill="@@SFA@@" font-weight="700">limitant</text>
            <rect x="256" y="278" width="200" height="66" rx="13" fill="#FFFFFF" stroke="@@GREY@@" stroke-width="2"/>
            <text x="356" y="320" text-anchor="middle" font-size="24" @@FF@@ fill="@@GREY@@">en excès</text>
          </g>
          <g class="step s4">
            <rect x="10" y="366" width="450" height="92" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="400" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">on en avait pourtant davantage</text>
            <text x="235" y="434" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">on compare des rapports, jamais des quantités</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qu'est le réactif limitant</h3>
          <p style="font-size:17px">Celui qui <b>s'épuise en premier</b>. C'est lui, et lui seul, qui fixe la quantité de produit formée — l'autre attendra.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La méthode, en une opération</h3>
          <p style="font-size:17px">On divise la quantité disponible de chaque réactif par son <b>coefficient</b>. Le plus <b>petit</b> rapport désigne le limitant.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège, et il est construit exprès</h3>
          <p style="font-size:17px">Ici on a <b>plus</b> de dihydrogène que de dioxygène, et c'est pourtant lui le limitant — parce que l'équation en demande <b>deux fois plus</b>.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi la comparaison brute ne marche jamais</h3>
          <p style="font-size:17px">Comparer 4,0 et 3,0 revient à comparer des choses que l'équation ne consomme pas au même rythme. C'est comme comparer des roues et des châssis pour savoir combien de voitures on peut monter : il en faut <b>quatre pour un</b>.<br><br>Le rapport quantité ÷ coefficient ramène tout à la même unité : « combien de fois la réaction peut se produire ». Ces nombres-là sont comparables, et le plus petit gagne.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux réactifs, en quantités quelconques : quatre moles et trois moles.",
      "On divise chacune par son coefficient dans l'équation.",
      "Deux contre trois : c'est le <b>dihydrogène</b> qui s'épuisera le premier.",
      "Et pourtant on en avait davantage — c'est exactement le piège du concours.",
      "<em>On compare des rapports</em>, jamais des quantités brutes."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-06 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-06" data-title="La chaîne de la gravimétrie" data-sub="Masse → mole → mole → masse, toujours" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="16" y="34" font-size="17" @@FF@@ fill="@@GREY@@">50 g de CaCO₃ → CaO + CO₂</text>
            @@L0@@
          </g>
          <g class="step s2">@@L1@@</g>
          <g class="step s3">@@L2@@</g>
          <g class="step s4">@@L3@@
            <rect x="10" y="386" width="450" height="72" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="416" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">la chaîne se pose avant de lire les nombres</text>
            <text x="235" y="444" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">puis on remplit case par case</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Étape 1 — masse vers mole</h3>
          <p style="font-size:17px">n = m / M. La masse molaire de CaCO₃ vaut 40 + 12 + 48 = <b>100 g/mol</b>, ce qui rend la division immédiate.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Étape 2 — le rapport des coefficients</h3>
          <p style="font-size:17px">C'est la <b>seule</b> étape où l'équation intervient. Ici les coefficients valent 1 et 1 : la quantité ne change pas.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Étape 3 — mole vers masse</h3>
          <p style="font-size:17px">m = n × M, avec cette fois la masse molaire du <b>produit</b> : CaO vaut 40 + 16 = 56 g/mol.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que le contrôle apporte, en une ligne</h3>
          <p style="font-size:17px">Le bilan massique valide tout : 28 g de CaO plus 22 g de CO₂ font bien les <b>50 g</b> de départ ✓<br><br>Et la discipline qui fait gagner du temps : <b>poser les quatre étapes avant de lire les nombres</b>. L'exercice devient alors un remplissage, sans décision à prendre en cours de route — donc sans endroit où se tromper.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Cinquante grammes de calcaire, et la question : combien de chaux obtient-on ?",
      "Première étape, toujours la même : la masse devient des moles.",
      "Deuxième : les coefficients de l'équation donnent les moles du produit.",
      "Troisième : on repasse en masse, avec la masse molaire du produit.",
      "<em>Vingt-huit grammes</em> — et le bilan massique le confirme sans calcul."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-07 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-07" data-title="La volumétrie et le gaz" data-sub="Le volume molaire remplace la masse molaire" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <rect x="110" y="24" width="250" height="64" rx="13" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.6"/>
            <text x="235" y="65" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">0,50 mol de CO₂</text>
            <line x1="120" y1="94" x2="120" y2="126" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d3)"/>
            <line x1="350" y1="94" x2="350" y2="126" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d3)"/>
          </g>
          <g class="step s2">
            <rect x="14" y="132" width="212" height="150" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="120" y="166" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">solide ou liquide</text>
            <text x="120" y="212" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">m = n × M</text>
            <text x="120" y="256" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">en grammes</text>
          </g>
          <g class="step s3">
            <rect x="244" y="132" width="212" height="150" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="350" y="166" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">gaz</text>
            <text x="350" y="212" text-anchor="middle" font-size="26" @@FF@@ fill="@@SFA@@" font-weight="700">V = n × V<tspan font-size="17" dy="6">m</tspan></text>
            <text x="350" y="256" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">en litres</text>
            <rect x="60" y="308" width="350" height="76" rx="14" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="235" y="357" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">0,50 × 22,4 = 11,2 L</text>
          </g>
          <g class="step s4">
            <rect x="10" y="400" width="450" height="58" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="435" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">22,4 L/mol : seulement aux conditions normales</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une seule case change</h3>
          <p style="font-size:17px">Pour un gaz, on passe du volume aux moles par le <b>volume molaire</b> : n = V / V<sub>m</sub>. Tout le reste de la chaîne est identique.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et pour une solution</h3>
          <p style="font-size:17px">C'est la <b>concentration</b> qui joue ce rôle : n = c × V. C'est ce qui relie ce chapitre directement à CH4-B.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Trois situations, une seule méthode</h3>
          <p style="font-size:17px">Solide ou liquide → la <b>masse molaire</b>. Gaz → le <b>volume molaire</b>. Solution → la <b>concentration</b>. La chaîne, elle, ne bouge jamais.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège, et il est récurrent</h3>
          <p style="font-size:17px">Utiliser 22,4 L/mol sans vérifier les conditions. Cette valeur n'est valable qu'à <b>0 °C et 1 atm</b> — l'énoncé le précise, ou donne une autre valeur.<br><br>À 25 °C, le volume molaire vaut environ 24,5 L/mol, soit <b>9 % d'écart</b>. Assez pour tomber sur une mauvaise proposition du QCM, jamais assez pour que le résultat paraisse absurde.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "On repart du même nombre de moles : un demi-mole de dioxyde de carbone.",
      "Pour un solide ou un liquide, on passerait par la masse molaire.",
      "Pour un gaz, c'est le <b>volume molaire</b> qui prend sa place.",
      "Onze virgule deux litres — et la chaîne était rigoureusement la même.",
      "<em>Mais 22,4 n'est vrai qu'aux conditions normales</em> : on vérifie toujours."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-08 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-08" data-title="Le réactif en excès, et ce qu'il en reste" data-sub="La question posée juste après" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <text x="235" y="40" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">dioxygène disponible</text>
            <text x="235" y="110" text-anchor="middle" font-size="46" @@FF@@ fill="@@DEEP@@" font-weight="700">3,0 mol</text>
            @@BARRE@@
          </g>
          <g class="step s2">
            <text x="@@CXC@@" y="212" text-anchor="middle" font-size="20" @@FF@@ fill="#FFFFFF" font-weight="700">consommé</text>
            <text x="@@CXC@@" y="266" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">2,0 mol</text>
            <text x="@@CXR@@" y="212" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">reste</text>
            <text x="@@CXR@@" y="266" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">1,0 mol</text>
          </g>
          <g class="step s3">
            <rect x="10" y="292" width="450" height="76" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="322" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">le consommé se calcule à partir du limitant</text>
            <text x="235" y="352" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">4,0 ÷ 2 = 2,0 mol de O₂ consommées</text>
          </g>
          <g class="step s4">
            <rect x="10" y="384" width="450" height="74" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="416" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">un reste négatif est impossible</text>
            <text x="235" y="446" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">cela signifie qu'on s'est trompé de limitant</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La question qui suit toujours</h3>
          <p style="font-size:17px">Une fois le limitant identifié, l'énoncé demande presque systématiquement <b>ce qu'il reste</b> de l'autre réactif.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La méthode</h3>
          <p style="font-size:17px">On calcule combien du réactif en excès a été <b>consommé</b> par le limitant, et on le soustrait de la quantité initiale.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et toujours à partir du limitant</h3>
          <p style="font-size:17px">La consommation se calcule <b>à partir du limitant</b>, jamais à partir de la quantité initiale de l'autre. C'est le limitant qui décide de tout.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le contrôle, et ce qu'il révèle</h3>
          <p style="font-size:17px">Le reste doit être <b>positif</b>. Un résultat négatif n'est pas une petite erreur de calcul : il signifie qu'on a désigné le <b>mauvais réactif</b> comme limitant.<br><br>C'est donc un contrôle qui ne dit pas seulement « c'est faux », mais <b>où</b> c'est faux — et il suffit de reprendre à la comparaison des rapports.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Trois moles de dioxygène au départ, et le dihydrogène est limitant.",
      "Il en consomme deux — et c'est le limitant qui fixe ce nombre.",
      "Il en reste donc <b>une mole</b>, qui ne réagira pas.",
      "On calcule toujours le consommé à partir du limitant, jamais de l'autre.",
      "<em>Et si le reste est négatif</em>, ce n'est pas un calcul faux : c'est le mauvais limitant."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "L0": ETAPE[0], "L1": ETAPE[1], "L2": ETAPE[2], "L3": ETAPE[3],
    "BARRE": BARRE, "CXC": "%.1f" % CX_CONSO, "CXR": "%.1f" % CX_RESTE,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH9-B : coupe de la barre a x = %.1f (%.0f %% de %.1f mol)"
      % (X_COUPE, 100 * N_CONSO / N_INIT, N_INIT))
print("ok", make("CH9-B", "Capsule CH9-B — Réactif limitant, gravimétrie et volumétrie · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH9B.html")))
