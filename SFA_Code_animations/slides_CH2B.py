# -*- coding: utf-8 -*-
"""CH2-B — Le tableau periodique et ce qu'il predit. 4 animations.

Figures au format 470 x 470. Le tableau simplifie passe de cases de 46 x 40 a
des cases de 52 x 52, et tous les libelles qui debordaient a droite sont
descendus sous le tableau, ou la largeur utile est celle du viewBox entier.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- tableau periodique simplifie : 4 periodes x 8 colonnes ----------------
CW, CH_, X0, Y0 = 52, 52, 32, 90
COLS, ROWS = 8, 4
ELEM = {  # (colonne 1..8, periode 1..4) -> symbole
    (1, 1): "H", (8, 1): "He",
    (1, 2): "Li", (2, 2): "Be", (3, 2): "B", (4, 2): "C", (5, 2): "N", (6, 2): "O", (7, 2): "F", (8, 2): "Ne",
    (1, 3): "Na", (2, 3): "Mg", (3, 3): "Al", (4, 3): "Si", (5, 3): "P", (6, 3): "S", (7, 3): "Cl", (8, 3): "Ar",
    (1, 4): "K", (2, 4): "Ca",
}
IW = CW - 3                                  # largeur interieure d'une case


def cell(c, r):
    return X0 + (c - 1) * CW, Y0 + (r - 1) * CH_


def centre(c, r):
    x, y = cell(c, r)
    return x + IW / 2, y + IW / 2


def grille(fill=None):
    o = []
    for (c, r), s in sorted(ELEM.items()):
        x, y = cell(c, r)
        bg = (fill or {}).get(c, "#FFFFFF")
        o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="4" fill="%s" stroke="%s" stroke-width="1.4"/>'
                 % (x, y, IW, IW, bg, GREY))
        o.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="20" %s fill="%s" '
                 'font-weight="600">%s</text>'
                 % (x + IW / 2, y + IW / 2 + 7, 'font-family="Be Vietnam Pro,Arial"', DEEP, s))
    return "".join(o)


BASE = grille()
FAM = grille(fill={1: "#CBE7D8", 2: "#E4F2EA", 7: "#E4F2EA", 8: "#CBE7D8"})

# reperes de lignes et de colonnes
REPS = []
for r in range(1, ROWS + 1):
    x, y = cell(1, r)
    REPS.append('<text x="%d" y="%.1f" text-anchor="end" font-size="15" font-family="Be Vietnam Pro,Arial" '
                'fill="%s">%d</text>' % (x - 9, y + IW / 2 + 5, GREY, r))
for c in range(1, COLS + 1):
    x, y = cell(c, 1)
    REPS.append('<text x="%.1f" y="%d" text-anchor="middle" font-size="15" font-family="Be Vietnam Pro,Arial" '
                'fill="%s">%d</text>' % (x + IW / 2, y - 10, GREY, c))
REPS = "".join(REPS)

XL, XR = X0, X0 + COLS * CW - 3               # 32 .. 448
YT, YB = Y0, Y0 + ROWS * CH_ - 3              # 90 .. 297
assert XR <= 462 and YB <= 310, (XR, YB)

# encadrements
_x3, _y3 = cell(1, 3)
PERIODE3 = ('<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="none" stroke="%s" stroke-width="3.5"/>'
            % (XL - 5, _y3 - 5, (XR - XL) + 10, IW + 10, SFA))
COLONNE1 = ('<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="none" stroke="%s" stroke-width="3.5"/>'
            % (XL - 5, YT - 5, IW + 10, (YB - YT) + 10, RED))

# repere du fluor, centre calcule et non estime
FX, FY = centre(7, 2)

# centres de colonne, pour les libelles de familles
C1X, C2X = centre(1, 1)[0], centre(2, 1)[0]
C7X, C8X = centre(7, 1)[0], centre(8, 1)[0]


# ---------------- CH2-06 : legende des quatre familles ----------------
# Deux lignes de deux cellules : chaque fond reprend la teinte de sa colonne
# dans le tableau, ce qui suffit a faire le lien sans fleche ni renvoi.
TEINTE = {1: "#CBE7D8", 2: "#E4F2EA", 7: "#E4F2EA", 8: "#CBE7D8"}
FAMILLES = [(1, "alcalins", "colonne 1 · ion 1+", SFA),
            (2, "alcalino-terreux", "colonne 2 · ion 2+", SFA),
            (7, "halogènes", "colonne 7 · ion 1−", SFA),
            (8, "gaz nobles", "colonne 8 · aucun ion", RED)]
LW, LH, LX, LY, LGAP = 222, 56, 10, 306, 6


def _cellule(i):
    col, nom, detail, coul = FAMILLES[i]
    x = LX + (i % 2) * (LW + LGAP)
    y = LY + (i // 2) * (LH + LGAP)
    cx = x + LW / 2
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="11" fill="%s" stroke="%s" stroke-width="1.6"/>'
            '<text x="%.1f" y="%d" text-anchor="middle" font-size="18" font-family="Be Vietnam Pro,Arial" '
            'fill="%s" font-weight="700">%s</text>'
            '<text x="%.1f" y="%d" text-anchor="middle" font-size="16" font-family="Be Vietnam Pro,Arial" '
            'fill="%s" font-weight="700">%s</text>'
            % (x, y, LW, LH, TEINTE[col], GREY, cx, y + 26, DEEP, nom, cx, y + 47, coul, detail))


LEG_GAUCHE = _cellule(0) + _cellule(1)
LEG_DROITE = _cellule(2) + _cellule(3)
assert LY + 2 * LH + LGAP == 424, LY + 2 * LH + LGAP

SLIDES = """
  <!-- ==================== ANIM-CH2-05 ==================== -->
  <section class="slide" data-ref="ANIM-CH2-05" data-title="Lire le tableau : périodes et familles" data-sub="Une ligne, une couche ; une colonne, une valence" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <text x="235" y="46" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">les vingt premiers éléments : tout le programme</text>
            @@BASE@@@@REPS@@
          </g>
          <g class="step s2">@@PERIODE3@@
            <text x="235" y="346" text-anchor="middle" font-size="21" @@FF@@ fill="@@SFA@@" font-weight="700">3ᵉ période → 3 couches électroniques</text>
          </g>
          <g class="step s3">@@COLONNE1@@
            <text x="235" y="386" text-anchor="middle" font-size="21" @@FF@@ fill="@@RED@@" font-weight="700">colonne 1 → 1 électron de valence</text>
          </g>
          <g class="step s4">
            <rect x="24" y="406" width="422" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="439" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">ligne 3, colonne 1 → 2, 8, 1</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une ligne, c'est une période</h3>
          <p style="font-size:17px">Son numéro donne le <b>nombre de couches</b> électroniques occupées. Le sodium est en 3ᵉ ligne : il a trois couches.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une colonne, c'est une famille</h3>
          <p style="font-size:17px">Tous ses éléments ont le <b>même nombre d'électrons de valence</b> — et c'est exactement pour cela qu'ils ont les mêmes propriétés chimiques.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que Mendeleïev a vraiment fait</h3>
          <p style="font-size:17px">Il n'a pas rangé les éléments par masse. Il les a rangés pour que <b>ceux qui se ressemblent tombent dans la même colonne</b> — quitte à laisser des cases vides pour des éléments non encore découverts.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La conséquence, et elle est énorme</h3>
          <p style="font-size:17px">Connaître la <b>position</b> d'un élément, c'est connaître sa configuration de valence <b>sans la calculer</b>. Ligne 3, colonne 1 : trois couches, un électron sur la dernière. Donc 2, 8, 1.<br><br>Le tableau est fourni au concours. Ce qui est évalué n'est jamais de le connaître — c'est de savoir le lire.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le tableau, réduit à ce qui tombe au concours : les vingt premiers éléments.",
      "Une <b>ligne</b> est une période : son numéro donne le nombre de couches.",
      "Une <b>colonne</b> est une famille : même nombre d'électrons de valence.",
      "C'est ce classement par colonne qui fait tout l'intérêt du tableau.",
      "<em>Position lue, configuration connue :</em> ligne 3 colonne 1 donne 2, 8, 1."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH2-06 ==================== -->
  <section class="slide" data-ref="ANIM-CH2-06" data-title="Les quatre familles à connaître" data-sub="Alcalins, alcalino-terreux, halogènes, gaz nobles" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="235" y="46" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">quatre colonnes portent un nom, et ce sont celles-là</text>
            @@FAM@@@@REPS@@
          </g>
          <g class="step s2">@@LEGG@@</g>
          <g class="step s3">@@LEGD@@</g>
          <g class="step s4">
            <rect x="10" y="432" width="450" height="36" rx="10" fill="@@TINT2@@"/>
            <text x="235" y="457" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">même colonne, même réaction chimique</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">À gauche, ceux qui perdent</h3>
          <p style="font-size:17px"><b>Alcalins</b> (colonne 1) : un électron de valence, très réactifs, ion <b>1+</b>. <b>Alcalino-terreux</b> (colonne 2) : deux électrons, ion <b>2+</b>.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">À droite, ceux qui gagnent — et ceux qui ne font rien</h3>
          <p style="font-size:17px"><b>Halogènes</b> : sept électrons de valence, très réactifs, ion <b>1−</b>. <b>Gaz nobles</b> : couche complète, <b>inertes</b>.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'analogie chimique, et ce qu'elle fait gagner</h3>
          <p style="font-size:17px">Le sodium et le potassium réagissent de la même façon parce qu'ils ont le même unique électron de valence. <b>Une question sur l'un se répond avec ce qu'on sait de l'autre.</b></p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi ce sont les extrêmes qui réagissent</h3>
          <p style="font-size:17px">Un alcalin n'a qu'<b>un</b> électron à perdre pour atteindre l'octet ; un halogène n'en a qu'<b>un</b> à gagner. Dans les deux cas, le chemin est le plus court possible — d'où leur réactivité extrême.<br><br>Les éléments du milieu du tableau, eux, devraient en échanger trois ou quatre : c'est trop coûteux, ils préfèrent <b>partager</b>. C'est la liaison covalente, et c'est tout le chapitre suivant.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Quatre colonnes portent un nom, et ce sont celles qui tombent au concours.",
      "À gauche, les <b>alcalins</b> et les <b>alcalino-terreux</b> : ils perdent un ou deux électrons.",
      "À droite, les <b>halogènes</b> en gagnent un — et les <b>gaz nobles</b> ne font rien.",
      "Deux éléments d'une même colonne réagissent pareil : c'est l'analogie chimique.",
      "<em>Et les plus réactifs sont les extrêmes :</em> ce sont eux qui ont le chemin le plus court."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH2-07 ==================== -->
  <section class="slide" data-ref="ANIM-CH2-07" data-title="Les trois flèches du tableau" data-sub="Rayon, ionisation, électronégativité : deux sens à retenir" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">@@BASE@@</g>
          <g class="step s2">
            <line x1="410" y1="326" x2="72" y2="326" stroke="@@SFA@@" stroke-width="4" marker-end="url(#v3)"/>
            <line x1="16" y1="104" x2="16" y2="288" stroke="@@SFA@@" stroke-width="4" marker-end="url(#v3)"/>
            <text x="235" y="356" text-anchor="middle" font-size="20" @@FF@@ fill="@@SFA@@" font-weight="700">le rayon atomique augmente</text>
          </g>
          <g class="step s3">
            <line x1="72" y1="62" x2="410" y2="62" stroke="@@RED@@" stroke-width="4" marker-end="url(#r3)"/>
            <line x1="462" y1="288" x2="462" y2="104" stroke="@@RED@@" stroke-width="4" marker-end="url(#r3)"/>
            <text x="235" y="36" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">ionisation et électronégativité augmentent</text>
          </g>
          <g class="step s4">
            <circle cx="@@FX@@" cy="@@FY@@" r="27" fill="none" stroke="@@RED@@" stroke-width="3.4"/>
            <text x="235" y="396" text-anchor="middle" font-size="20" @@FF@@ fill="@@RED@@" font-weight="700">F : le plus électronégatif de tous</text>
            <rect x="24" y="414" width="422" height="46" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="444" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">un petit atome retient mieux, donc attire mieux</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le rayon atomique</h3>
          <p style="font-size:17px">Il augmente vers le <b>bas</b> — on ajoute des couches — et vers la <b>gauche</b> : moins de protons pour retenir la même couche.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les deux autres vont à l'inverse</h3>
          <p style="font-size:17px">L'<b>énergie d'ionisation</b> — l'énergie pour arracher un électron — et l'<b>électronégativité</b> augmentent toutes deux vers le haut et vers la droite.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Deux règles, pas six</h3>
          <p style="font-size:17px">Le rayon dans un sens, les deux autres dans l'autre. Et le <b>fluor</b> est le plus électronégatif de tous : c'est le repère qui oriente la figure.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'explication qui les unifie</h3>
          <p style="font-size:17px">Tout découle du <b>rayon</b>. Plus l'atome est petit, plus son noyau est proche des électrons de valence — donc plus il les retient, et plus il en attire.<br><br>Il n'y a donc qu'une seule idée à comprendre : les deux autres flèches en sont la conséquence mécanique. C'est pour cela qu'elles pointent dans le sens opposé.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Trois propriétés varient régulièrement dans le tableau. Trois flèches suffisent.",
      "Le <b>rayon atomique</b> augmente vers le bas et vers la gauche.",
      "L'<b>ionisation</b> et l'<b>électronégativité</b> augmentent exactement à l'inverse.",
      "Le fluor, en haut à droite, est donc le plus électronégatif de tous.",
      "<em>Une seule idée les unifie :</em> un petit atome retient mieux, donc attire mieux."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH2-08 ==================== -->
  <section class="slide" data-ref="ANIM-CH2-08" data-title="Prédire une formule sans rien apprendre" data-sub="La place dans le tableau donne la formule du composé" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <rect x="20" y="24" width="206" height="98" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="123" y="58" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">calcium · colonne 2</text>
            <text x="123" y="100" text-anchor="middle" font-size="34" @@FF@@ fill="@@DEEP@@" font-weight="700">Ca²⁺</text>
            <rect x="244" y="24" width="206" height="98" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="347" y="58" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">chlore · halogène</text>
            <text x="347" y="100" text-anchor="middle" font-size="34" @@FF@@ fill="@@DEEP@@" font-weight="700">Cl⁻</text>
          </g>
          <g class="step s2">
            <text x="235" y="172" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">il faut équilibrer les charges</text>
            <text x="235" y="212" text-anchor="middle" font-size="25" @@FF@@ fill="@@SFA@@" font-weight="700">un Ca²⁺ pour deux Cl⁻</text>
          </g>
          <g class="step s3">
            <line x1="235" y1="230" x2="235" y2="262" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d4)"/>
            <rect x="108" y="272" width="254" height="92" rx="16" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="235" y="334" text-anchor="middle" font-size="46" @@FF@@ fill="@@DEEP@@" font-weight="700">CaCl₂</text>
          </g>
          <g class="step s4">
            <rect x="48" y="398" width="374" height="54" rx="12" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.6"/>
            <text x="235" y="432" text-anchor="middle" font-size="21" @@FF@@ fill="@@SFA@@" font-weight="700">(+2) + 2 × (−1) = 0 ✓</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">On part des colonnes, jamais d'une liste</h3>
          <p style="font-size:17px">Colonne 2 → deux électrons de valence → ion <b>2+</b>. Halogène → sept électrons → ion <b>1−</b>. Les deux charges se lisent, elles ne se retiennent pas.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un composé ionique est neutre</h3>
          <p style="font-size:17px">Les charges positives doivent compenser exactement les négatives. Une charge 2+ demande donc <b>deux</b> charges 1−.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et le contrôle est gratuit</h3>
          <p style="font-size:17px">On multiplie chaque charge par son indice et on additionne. Si la somme n'est pas nulle, la formule est fausse — en trois secondes, sans rien vérifier d'autre.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Quand les charges ne tombent pas juste</h3>
          <p style="font-size:17px">Pour Al³⁺ et O²⁻, on cherche le <b>plus petit multiple commun</b> de 3 et 2, soit 6 : il faut deux aluminiums et trois oxygènes, donc <b>Al₂O₃</b>.<br><br>Contrôle : 2 × (+3) + 3 × (−2) = 0 ✓ La méthode ne change jamais, quels que soient les nombres — et elle sera systématisée en CH5 sous le nom de <b>croisement des indices</b>.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux éléments, deux colonnes — et donc deux charges, lues et non apprises.",
      "Le composé doit être neutre : il faut deux chlorures pour un calcium.",
      "La formule s'écrit d'elle-même : <b>CaCl₂</b>.",
      "Et le contrôle tient en une addition : la somme des charges doit être nulle.",
      "<em>Quand les charges ne tombent pas juste</em>, on prend leur plus petit multiple commun."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "BASE": BASE, "FAM": FAM, "REPS": REPS,
    "PERIODE3": PERIODE3, "COLONNE1": COLONNE1,
    "FX": "%.1f" % FX, "FY": "%.1f" % FY,
    "LEGG": LEG_GAUCHE, "LEGD": LEG_DROITE,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("tableau : x %d..%d  y %d..%d · fluor centre (%.1f ; %.1f)" % (XL, XR, YT, YB, FX, FY))
print("ok", make("CH2-B", "Capsule CH2-B — Le tableau périodique et ce qu'il prédit · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH2B.html")))
