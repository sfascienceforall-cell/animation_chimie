# -*- coding: utf-8 -*-
"""CH5 — Nommer et ecrire les composes inorganiques. 4 animations.

Figures au format 470 x 470 : dans une colonne de 502 px pour une zone utile de
542 px, un viewBox carre occupe 93 % de la hauteur disponible.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH5-04 : la table des douze ions polyatomiques ----------------
# Deux colonnes de six : les couples -ate / -ite sont alors cote a cote sur une
# meme ligne, ce qui rend la regle de nomenclature lisible sans commentaire.
IONS = [("nitrate", "NO₃⁻"), ("nitrite", "NO₂⁻"),
        ("sulfate", "SO₄²⁻"), ("sulfite", "SO₃²⁻"),
        ("carbonate", "CO₃²⁻"), ("hydrogénocarbonate", "HCO₃⁻"),
        ("phosphate", "PO₄³⁻"), ("hydroxyde", "OH⁻"),
        ("ammonium", "NH₄⁺"), ("hydronium", "H₃O⁺"),
        ("permanganate", "MnO₄⁻"), ("dichromate", "Cr₂O₇²⁻")]
NCOL, CW, CH_, X0, Y0 = 2, 231, 64, 4, 40
GAP = 8
TABLE = ""
for i, (nom, f) in enumerate(IONS):
    c, r = i % NCOL, i // NCOL
    x, y = X0 + c * CW, Y0 + r * CH_
    TABLE += ('<rect x="%d" y="%d" width="%d" height="%d" rx="9" fill="%s" stroke="%s" stroke-width="1.4"/>'
              % (x, y, CW - GAP, CH_ - GAP, TINT, GREY))
    TABLE += ('<text x="%d" y="%d" font-size="17" font-family="Be Vietnam Pro,Arial" fill="%s">%s</text>'
              % (x + 14, y + 25, INK2, nom))
    TABLE += ('<text x="%d" y="%d" font-size="24" font-family="Be Vietnam Pro,Arial" fill="%s" '
              'font-weight="700">%s</text>' % (x + 14, y + 51, DEEP, f))

# les deux couples -ate / -ite : lignes 0 et 1, soit les indices 0 a 3
PAIRES = ""
for i in range(4):
    c, r = i % NCOL, i // NCOL
    x, y = X0 + c * CW, Y0 + r * CH_
    PAIRES += ('<rect x="%d" y="%d" width="%d" height="%d" rx="9" fill="none" stroke="%s" stroke-width="3"/>'
               % (x, y, CW - GAP, CH_ - GAP, RED))
BAS_TABLE = Y0 + (len(IONS) // NCOL) * CH_          # 40 + 6*64 = 424
assert BAS_TABLE == 424, BAS_TABLE

SLIDES = """
  <!-- ==================== ANIM-CH5-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH5-01" data-title="Écrire une formule à partir des charges" data-sub="Le croisement des indices, en trois secondes" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <rect x="24" y="34" width="190" height="86" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <rect x="256" y="34" width="190" height="86" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="119" y="90" text-anchor="middle" font-size="44" @@FF@@ fill="@@DEEP@@" font-weight="700">Al³⁺</text>
            <text x="351" y="90" text-anchor="middle" font-size="44" @@FF@@ fill="@@DEEP@@" font-weight="700">SO₄²⁻</text>
          </g>
          <g class="step s2">
            <line x1="150" y1="132" x2="320" y2="212" stroke="@@SFA@@" stroke-width="3.4" marker-end="url(#v1)"/>
            <line x1="320" y1="132" x2="150" y2="212" stroke="@@SFA@@" stroke-width="3.4" marker-end="url(#v1)"/>
            <text x="235" y="248" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">la charge de l'un devient l'indice de l'autre</text>
          </g>
          <g class="step s3">
            <rect x="84" y="272" width="302" height="90" rx="16" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="235" y="332" text-anchor="middle" font-size="46" @@FF@@ fill="@@DEEP@@" font-weight="700">Al₂(SO₄)₃</text>
          </g>
          <g class="step s4">
            <rect x="60" y="392" width="350" height="54" rx="12" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.6"/>
            <text x="235" y="426" text-anchor="middle" font-size="22" @@FF@@ fill="@@SFA@@" font-weight="700">2 × (+3) + 3 × (−2) = 0 ✓</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un composé ionique est neutre</h3>
          <p style="font-size:17px">Les charges positives compensent <b>exactement</b> les négatives. Ce n'est pas une convention : c'est la seule façon pour le solide d'exister.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le croisement des indices</h3>
          <p style="font-size:17px">La charge du cation devient l'<b>indice</b> de l'anion, et réciproquement. Trois et deux se croisent : deux aluminiums, trois sulfates.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les parenthèses ne sont pas décoratives</h3>
          <p style="font-size:17px">Quand un ion <b>polyatomique</b> est pris plusieurs fois, on l'encadre. Al₂(SO₄)₃ contient 2 aluminiums, 3 soufres et <b>12 oxygènes</b> — sans parenthèses, la formule ne veut plus rien dire.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Simplifier, et contrôler</h3>
          <p style="font-size:17px"><b>On simplifie si possible :</b> Mg²⁺ et O²⁻ croisés donnent Mg₂O₂, qu'on réduit à <b>MgO</b>. Le croisement donne une formule juste, pas toujours la plus simple.<br><br><b>Le contrôle est gratuit :</b> on multiplie chaque charge par son indice et on additionne. Si la somme n'est pas nulle, la formule est fausse — et on le sait en trois secondes, sans rien relire.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux ions, et leurs charges — lues dans le tableau, jamais apprises.",
      "On les croise : la charge de l'un devient l'indice de l'autre.",
      "La formule s'écrit d'elle-même, parenthèses comprises.",
      "Et le contrôle tient en une addition : la somme des charges doit être nulle.",
      "<em>Dernier réflexe :</em> simplifier quand c'est possible, comme Mg₂O₂ qui devient MgO."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH5-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH5-02" data-title="Les quatre grandes fonctions inorganiques" data-sub="Oxyde, hydroxyde, acide, sel — et ce qui les relie" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <rect x="14" y="20" width="196" height="84" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="112" y="52" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">OXYDE de métal</text>
            <text x="112" y="84" text-anchor="middle" font-size="22" @@FF@@ fill="#3F3F46">Na₂O</text>
            <rect x="260" y="20" width="196" height="84" rx="12" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="358" y="52" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">OXYDE de non-métal</text>
            <text x="358" y="84" text-anchor="middle" font-size="22" @@FF@@ fill="#3F3F46">SO₃</text>
          </g>
          <g class="step s2">
            <line x1="112" y1="112" x2="112" y2="176" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v2)"/>
            <line x1="358" y1="112" x2="358" y2="176" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v2)"/>
            <text x="235" y="150" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">+ eau</text>
            <rect x="14" y="186" width="196" height="84" rx="12" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="112" y="218" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">HYDROXYDE</text>
            <text x="112" y="250" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">NaOH · une base</text>
            <rect x="260" y="186" width="196" height="84" rx="12" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="358" y="218" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">ACIDE</text>
            <text x="358" y="250" text-anchor="middle" font-size="22" @@FF@@ fill="#3F3F46">H₂SO₄</text>
          </g>
          <g class="step s3">
            <line x1="112" y1="278" x2="176" y2="330" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v2)"/>
            <line x1="358" y1="278" x2="294" y2="330" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v2)"/>
            <rect x="122" y="340" width="226" height="88" rx="14" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="235" y="374" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">SEL</text>
            <text x="235" y="408" text-anchor="middle" font-size="22" @@FF@@ fill="#3F3F46">Na₂SO₄ + eau</text>
            <text x="235" y="456" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">quatre étapes d'une même chaîne, pas quatre listes</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Tout part d'un oxyde</h3>
          <p style="font-size:17px">Un <b>oxyde</b> est la combinaison d'un élément avec l'oxygène. Et selon que cet élément est un métal ou un non-métal, la suite diverge.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'eau les transforme</h3>
          <p style="font-size:17px">Un oxyde de métal donne un <b>hydroxyde</b> — une base, reconnaissable à son groupement OH. Un oxyde de non-métal donne un <b>acide</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et leur rencontre donne un sel</h3>
          <p style="font-size:17px">Acide plus base donne un <b>sel</b> et de l'eau. Les quatre fonctions ne sont donc pas quatre listes à mémoriser : ce sont <b>quatre étapes d'une même chaîne</b>.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi cette chaîne vaut mieux qu'une liste</h3>
          <p style="font-size:17px">Une liste de quatre définitions se confond. Une chaîne se <b>reconstruit</b> : partant d'un élément, on sait ce que son oxyde donnera avec l'eau, puis ce que le produit donnera avec son opposé.<br><br>C'est aussi le fil qui mènera directement au chapitre CH7 : les acides et les bases y seront repris, avec leur définition exacte — <b>celui qui donne un proton</b>, et celui qui le prend.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux oxydes, l'un d'un métal, l'autre d'un non-métal.",
      "L'eau les transforme : le premier donne un hydroxyde, le second un acide.",
      "Et leur rencontre donne un <b>sel</b>, plus de l'eau.",
      "Les quatre fonctions ne sont pas quatre listes — c'est une seule chaîne.",
      "<em>Et elle se reconstruit</em>, là où une liste de définitions se confond."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH5-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH5-03" data-title="Oxyde acide ou oxyde basique" data-sub="Le métal d'un côté, le non-métal de l'autre" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <rect x="12" y="24" width="446" height="62" rx="12" fill="@@TINT2@@"/>
            <text x="123" y="63" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">MÉTAUX</text>
            <text x="347" y="63" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">NON-MÉTAUX</text>
            <line x1="235" y1="24" x2="235" y2="86" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="235" y="112" text-anchor="middle" font-size="17" @@FF@@ fill="@@GREY@@">le tableau périodique, coupé en deux</text>
            <line x1="235" y1="130" x2="235" y2="402" stroke="@@RULE@@" stroke-width="2"/>
          </g>
          <g class="step s2">
            <text x="123" y="182" text-anchor="middle" font-size="27" @@FF@@ fill="@@DEEP@@" font-weight="700">Na₂O + H₂O</text>
            <line x1="123" y1="204" x2="123" y2="266" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v3)"/>
            <text x="123" y="308" text-anchor="middle" font-size="29" @@FF@@ fill="@@DEEP@@" font-weight="700">2 NaOH</text>
            <rect x="24" y="336" width="198" height="50" rx="11" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="123" y="368" text-anchor="middle" font-size="20" @@FF@@ fill="@@SFA@@" font-weight="700">oxyde BASIQUE</text>
          </g>
          <g class="step s3">
            <text x="347" y="182" text-anchor="middle" font-size="27" @@FF@@ fill="@@DEEP@@" font-weight="700">SO₃ + H₂O</text>
            <line x1="347" y1="204" x2="347" y2="266" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v3)"/>
            <text x="347" y="308" text-anchor="middle" font-size="29" @@FF@@ fill="@@DEEP@@" font-weight="700">H₂SO₄</text>
            <rect x="248" y="336" width="198" height="50" rx="11" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.4"/>
            <text x="347" y="368" text-anchor="middle" font-size="20" @@FF@@ fill="@@RED@@" font-weight="700">oxyde ACIDE</text>
          </g>
          <g class="step s4">
            <rect x="12" y="414" width="446" height="46" rx="11" fill="@@TINT2@@"/>
            <text x="235" y="444" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">la position de l'élément donne le classement</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le critère est géographique</h3>
          <p style="font-size:17px">On regarde <b>de quel côté du tableau</b> se trouve l'élément. Métal à gauche, non-métal à droite : il n'y a rien d'autre à examiner.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Oxyde de métal → basique</h3>
          <p style="font-size:17px">Avec l'eau, il donne un <b>hydroxyde</b>. L'oxyde de sodium donne de la soude : c'est un oxyde basique.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Oxyde de non-métal → acide</h3>
          <p style="font-size:17px">Avec l'eau, il donne un <b>acide</b>. Le trioxyde de soufre donne l'acide sulfurique : c'est un oxyde acide.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Aucune de ces équations n'est à mémoriser</h3>
          <p style="font-size:17px">La <b>nature de l'élément</b> donne le produit, et le produit donne le classement. Le tableau périodique fait tout le travail.<br><br><b>Et le pont avec l'écologie :</b> les oxydes de soufre et d'azote rejetés par les industries et les moteurs sont des oxydes <b>acides</b>. Dissous dans l'eau des nuages, ils donnent des acides — ce sont les pluies acides. Le dire ici relie la chimie à la section D de biologie.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le tableau périodique se lit en deux blocs : métaux à gauche, non-métaux à droite.",
      "Un oxyde de métal plus de l'eau donne un hydroxyde : c'est un oxyde <b>basique</b>.",
      "Un oxyde de non-métal plus de l'eau donne un acide : c'est un oxyde <b>acide</b>.",
      "Le classement se lit donc dans la position de l'élément, et rien d'autre.",
      "<em>Et c'est le mécanisme des pluies acides :</em> des oxydes de non-métaux dissous dans les nuages."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH5-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH5-04" data-title="Les ions polyatomiques à connaître" data-sub="Douze ions, et toute la nomenclature suit" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <text x="235" y="26" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">les douze, et il n'y en a pas d'autres au programme</text>
            @@TABLE@@
          </g>
          <g class="step s2">@@PAIRES@@
            <text x="235" y="452" text-anchor="middle" font-size="20" @@FF@@ fill="@@RED@@" font-weight="700">-ate : plus d'oxygène &nbsp;·&nbsp; -ite : moins</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La seule mémorisation du chapitre</h3>
          <p style="font-size:17px">Les charges des ions <b>monoatomiques</b> se lisent dans le tableau. Celles des ions polyatomiques, non — il faut les connaître. Ils sont <b>douze</b>.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et ils sont structurés</h3>
          <p style="font-size:17px">La terminaison porte l'information : <b>-ate</b> pour le plus riche en oxygène, <b>-ite</b> pour le moins. Sulfate SO₄²⁻ et sulfite SO₃²⁻ · nitrate NO₃⁻ et nitrite NO₂⁻.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Douze, ce n'est pas douze</h3>
          <p style="font-size:17px">Quatre familles, deux terminaisons, et deux cations isolés. Une fois la règle -ate / -ite acquise, il n'en reste <b>que huit</b> à apprendre réellement.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Où chacun resservira</h3>
          <p style="font-size:17px">Le <b>permanganate</b> MnO₄⁻ et le <b>dichromate</b> Cr₂O₇²⁻ sont les deux oxydants du chapitre CH8 : ils reviendront dans toutes les demi-équations.<br><br>L'<b>hydronium</b> H₃O⁺ et l'<b>hydroxyde</b> OH⁻ sont les deux protagonistes du chapitre CH7. L'<b>hydrogénocarbonate</b> HCO₃⁻ y servira d'exemple d'espèce amphotère — et c'est lui qui régule le pH du sang.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Douze ions polyatomiques. C'est la seule mémorisation réelle du chapitre.",
      "Mais ils sont structurés : <b>-ate</b> pour le plus riche en oxygène, <b>-ite</b> pour le moins.",
      "Une fois la règle acquise, il n'en reste que huit à apprendre vraiment.",
      "Et aucun n'est là par hasard : chacun a un rendez-vous plus loin dans le programme.",
      "<em>Permanganate et dichromate</em> reviendront en CH8 ; hydronium et hydroxyde, en CH7."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "TABLE": TABLE, "PAIRES": PAIRES,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED, "RULE": "#E3E7EE",
})

print("table des ions : %d colonnes x %d lignes, bas = %d" % (NCOL, len(IONS) // NCOL, BAS_TABLE))
print("ok", make("CH5", "Capsule CH5 — Nommer et écrire les composés inorganiques · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH5.html")))
