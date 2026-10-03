# -*- coding: utf-8 -*-
"""CH1 — La mole, les masses et les unites. 4 animations.

Format des figures : 470 x 470. La colonne figure fait 502 px de large pour une
zone utile de 542 px de haut ; un viewBox carre occupe donc 93 % de la hauteur,
contre 59 % avec l'ancien format 470 x 300.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------- CH1-01 : une boite de six par deux, qui SE COMPTE d'un coup d'oeil ----------
BX, BY, BW, BH = 52, 90, 366, 180
COLS, ROWS, R = 6, 2, 28
dx = BW / COLS
dy = BH / ROWS
OEUFS = ""
for r in range(ROWS):
    for c in range(COLS):
        cx = BX + dx * (c + 0.5)
        cy = BY + dy * (r + 0.5)
        OEUFS += ('<ellipse cx="%.1f" cy="%.1f" rx="%d" ry="%d" fill="#F0D9A8" stroke="%s" stroke-width="2.4"/>'
                  % (cx, cy, R - 4, R, DEEP))
# alveoles de la boite : un trait vertical entre chaque colonne
ALV = "".join('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.6" opacity="0.5"/>'
              % (BX + dx * i, BY, BX + dx * i, BY + BH, DEEP) for i in range(1, COLS))
ALV += '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.6" opacity="0.5"/>' % (
    BX, BY + dy, BX + BW, BY + dy, DEEP)
N_OEUFS = COLS * ROWS

# ---------- CH1-04 : le cube decoupe ----------
CX, CY, CS, N = 40, 80, 250, 10
PAS = CS / N
GRILLE = ""
for i in range(1, N):
    x = CX + PAS * i
    GRILLE += ('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#FFFFFF" stroke-width="1.3" opacity="0.75"/>'
               % (x, CY, x, CY + CS))
    y = CY + PAS * i
    GRILLE += ('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#FFFFFF" stroke-width="1.3" opacity="0.75"/>'
               % (CX, y, CX + CS, y))

SLIDES = """
  <!-- ==================== ANIM-CH1-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH1-01" data-title="La mole est un paquet, rien d'autre" data-sub="Comme la douzaine, mais pour compter des atomes" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1 h3">
            <text x="235" y="58" text-anchor="middle" font-size="22" @@FF@@ fill="#3F3F46">une douzaine</text>
            <rect x="@@BX@@" y="@@BY@@" width="@@BW@@" height="@@BH@@" rx="16" fill="#FAF3E4" stroke="@@DEEP@@" stroke-width="3"/>
            @@ALV@@@@OEUFS@@
            <text x="235" y="326" text-anchor="middle" font-size="38" @@FF@@ fill="#111" font-weight="700">12 œufs</text>
            <text x="235" y="366" text-anchor="middle" font-size="19" @@FF@@ fill="@@GREY@@">six par deux — on les compte d'un coup d'œil</text>
          </g>
          <g class="step s3">
            <rect x="34" y="66" width="402" height="240" rx="22" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3.5"/>
            <text x="235" y="118" text-anchor="middle" font-size="23" @@FF@@ fill="#3F3F46">une mole</text>
            <text x="235" y="200" text-anchor="middle" font-size="52" @@FF@@ fill="@@DEEP@@" font-weight="700">6,02 × 10²³</text>
            <text x="235" y="256" text-anchor="middle" font-size="21" @@FF@@ fill="#3F3F46">entités, quelles qu'elles soient</text>
          </g>
          <g class="step s4">
            <line x1="140" y1="316" x2="140" y2="366" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d1)"/>
            <line x1="330" y1="316" x2="330" y2="366" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d1)"/>
            <text x="140" y="400" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">12 g de carbone</text>
            <text x="330" y="400" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">1 mol d'atomes</text>
            <rect x="34" y="424" width="402" height="40" rx="10" fill="@@TINT2@@"/>
            <text x="235" y="451" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">et c'est vrai pour tous les éléments</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2 h3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un mot qui ne désigne qu'un nombre</h3>
          <p style="font-size:17px">Une douzaine, c'est douze. Un millier, mille. <b>Une mole, c'est 6,02 × 10²³</b> — le nombre d'Avogadro. Rien de plus mystérieux.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi ce nombre-là</h3>
          <p style="font-size:17px">Il n'a pas été trouvé, il a été <b>choisi</b> : c'est le nombre d'atomes qu'il faut pour que 12 g de carbone en contiennent exactement une mole.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La conséquence, et c'est tout le chapitre</h3>
          <p style="font-size:17px">La masse d'une mole, en grammes, est <b>égale à la masse atomique lue dans le tableau</b>. Le carbone pèse 12, donc une mole pèse 12 g. Aucune conversion à retenir.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'ordre de grandeur, et le piège de vocabulaire</h3>
          <p style="font-size:17px">6,02 × 10²³ échappe à l'intuition : une mole de grains de riz recouvrirait la Terre sur plusieurs kilomètres d'épaisseur.<br><br><b>Le piège :</b> « une mole de dioxygène » désigne une mole de <b>molécules</b> O₂ — donc <b>deux</b> moles d'atomes d'oxygène. L'énoncé le précise toujours ; il faut le lire.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Une boîte de six par deux : douze œufs, et on les compte sans y penser.",
      "Un chimiste a le même besoin, mais à une tout autre échelle.",
      "Sa douzaine à lui s'appelle la <b>mole</b>, et elle vaut 6,02 × 10²³.",
      "Ce nombre a été choisi pour qu'une mole de carbone pèse exactement <b>12 grammes</b>.",
      "<em>D'où la règle :</em> la masse d'une mole, en grammes, est la masse atomique du tableau."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH1-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH1-02" data-title="Le triangle masse — mole — nombre de particules" data-sub="Trois grandeurs, deux passages, aucune formule à retenir" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <rect x="140" y="26" width="190" height="84" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="235" y="58" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">quantité de matière</text>
            <text x="235" y="92" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">n (mol)</text>
          </g>
          <g class="step s2">
            <rect x="10" y="330" width="190" height="84" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="105" y="362" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">masse</text>
            <text x="105" y="396" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">m (g)</text>
            <line x1="168" y1="114" x2="110" y2="322" stroke="@@SFA@@" stroke-width="3.4" marker-end="url(#v2)"/>
            <line x1="129" y1="327" x2="187" y2="119" stroke="@@SFA@@" stroke-width="3.4" marker-end="url(#v2)"/>
            <text x="94" y="204" text-anchor="end" font-size="22" @@FF@@ fill="@@SFA@@" font-weight="700">× M</text>
            <text x="214" y="278" text-anchor="end" font-size="22" @@FF@@ fill="@@SFA@@" font-weight="700">÷ M</text>
          </g>
          <g class="step s3">
            <rect x="270" y="330" width="190" height="84" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="365" y="362" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">nombre d'entités</text>
            <text x="365" y="396" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">N</text>
            <line x1="302" y1="114" x2="360" y2="322" stroke="@@SFA@@" stroke-width="3.4" marker-end="url(#v2)"/>
            <line x1="341" y1="327" x2="283" y2="119" stroke="@@SFA@@" stroke-width="3.4" marker-end="url(#v2)"/>
            <text x="376" y="204" font-size="22" @@FF@@ fill="@@SFA@@" font-weight="700">× N<tspan font-size="15" dy="6">A</tspan></text>
            <text x="256" y="278" font-size="22" @@FF@@ fill="@@SFA@@" font-weight="700">÷ N<tspan font-size="15" dy="6">A</tspan></text>
          </g>
          <g class="step s4">
            <rect x="10" y="426" width="450" height="40" rx="11" fill="@@TINT2@@"/>
            <text x="235" y="453" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">aucun passage direct : on passe par le centre</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">De la masse aux moles</h3>
          <div class="expr" style="font-size:24px;text-align:left;line-height:1.3">n = m / M</div>
          <p style="font-size:17px;margin-top:4px">M est la <b>masse molaire</b>, en g/mol : la somme des masses atomiques du tableau, avec les indices de la formule.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Des moles aux particules</h3>
          <div class="expr" style="font-size:24px;text-align:left;line-height:1.3">N = n × N<sub>A</sub></div>
          <p style="font-size:17px;margin-top:4px">Une mole contient N<sub>A</sub> entités. Deux moles en contiennent deux fois plus. Il n'y a rien d'autre dans cette relation.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La mole est toujours au centre</h3>
          <p style="font-size:17px">Il n'existe <b>aucun passage direct</b> de la masse au nombre de particules. Toute conversion transite par la quantité de matière.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Comment ne jamais se tromper de sens</h3>
          <p style="font-size:17px">On ne mémorise pas les flèches, on <b>regarde les unités</b>. Des grammes divisés par des grammes par mole donnent des moles : la division est forcée, il n'y a rien à choisir.<br><br>C'est l'analyse dimensionnelle, et elle décide à votre place dans tout le programme de chimie.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Au centre, la quantité de matière — la grandeur que le chimiste manipule.",
      "À gauche, ce que la balance mesure : une masse. On y passe par la <b>masse molaire</b>.",
      "À droite, ce qu'on compte vraiment : des particules. On y passe par le <b>nombre d'Avogadro</b>.",
      "Et il n'y a <b>aucun chemin direct</b> entre la masse et le nombre : on passe toujours par le centre.",
      "<em>Le sens de chaque flèche</em> se lit dans les unités, jamais dans la mémoire."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH1-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH1-03" data-title="Masse volumique et densité" data-sub="Deux mots qu'on confond, une seule différence" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <text x="235" y="44" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">même volume</text>
            <rect x="42" y="66" width="176" height="176" rx="10" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="3.4"/>
            <rect x="252" y="66" width="176" height="176" rx="10" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="3.4"/>
            <text x="130" y="274" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">1 litre de liège</text>
            <text x="340" y="274" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">1 litre de plomb</text>
          </g>
          <g class="step s2">
            <text x="130" y="168" text-anchor="middle" font-size="34" @@FF@@ fill="@@DEEP@@" font-weight="700">240 g</text>
            <text x="340" y="168" text-anchor="middle" font-size="34" @@FF@@ fill="@@DEEP@@" font-weight="700">11 340 g</text>
            <text x="235" y="310" text-anchor="middle" font-size="21" @@FF@@ fill="@@SFA@@" font-weight="700">masses très différentes</text>
          </g>
          <g class="step s3">
            <rect x="42" y="332" width="386" height="54" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="368" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">ρ = m / V &nbsp;·&nbsp; en g/cm³</text>
          </g>
          <g class="step s4">
            <rect x="42" y="398" width="386" height="54" rx="12" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="434" text-anchor="middle" font-size="26" @@FF@@ fill="@@RED@@" font-weight="700">d = ρ / ρ<tspan font-size="17" dy="6">eau</tspan><tspan dy="-6"> &nbsp;·&nbsp; sans unité</tspan></text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que la masse volumique mesure</h3>
          <p style="font-size:17px">Pas « le poids », mais la masse <b>par unité de volume</b>. C'est ce qui permet de comparer deux matières à volume égal.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une grandeur physique, avec son unité</h3>
          <p style="font-size:17px">Le liège : 0,24 g/cm³. Le plomb : 11,34 g/cm³. <b>L'unité fait partie de la réponse</b> — sans elle, le nombre ne veut rien dire.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La densité, elle, est un rapport</h3>
          <p style="font-size:17px">C'est la masse volumique <b>divisée par celle d'une référence</b> — l'eau pour les liquides et les solides, l'air pour les gaz. Deux grandeurs de même unité : <b>la densité n'en a donc aucune</b>.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi on les confond, et comment trancher</h3>
          <p style="font-size:17px">L'eau vaut 1,00 g/cm³. Diviser par 1 ne change pas le nombre : pour un liquide, masse volumique en g/cm³ et densité ont donc <b>la même valeur numérique</b>. C'est toute l'origine de la confusion.<br><br><b>Le test, en une seconde :</b> si la réponse porte une unité, c'est une masse volumique. Une densité n'en a jamais.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux cubes de même volume : un litre de liège, un litre de plomb.",
      "Les masses n'ont rien à voir — c'est exactement ce que la masse volumique mesure.",
      "Elle se calcule en divisant la masse par le volume, et elle <b>porte une unité</b>.",
      "La densité est autre chose : c'est ce rapport divisé par celui de l'eau.",
      "<em>Le test :</em> une unité dans la réponse ? C'est une masse volumique, pas une densité."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH1-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH1-04" data-title="Les conversions qui font perdre des points" data-sub="Le tableau des préfixes, et le piège du volume" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s2">
            <rect x="@@CX@@" y="@@CY@@" width="@@CS@@" height="@@CS@@" rx="6" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="3.4"/>
            <text x="165" y="62" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">1 m de côté</text>
          </g>
          <g class="step s3">@@GRILLE@@</g>
          <g class="step s4">
            <rect x="@@CX@@" y="@@CY@@" width="@@PAS@@" height="@@PAS@@" fill="@@SFA@@"/>
            <text x="76" y="352" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">1 cm</text>
            <text x="310" y="176" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">10 × 10 × 10</text>
            <text x="310" y="222" font-size="30" @@FF@@ fill="@@SFA@@" font-weight="700">= 10⁶ cm³</text>
            <text x="310" y="260" font-size="17" @@FF@@ fill="#3F3F46">et non 100</text>
            <rect x="30" y="384" width="410" height="72" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="414" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">longueur × k &nbsp;·&nbsp; aire × k² &nbsp;·&nbsp; volume × k³</text>
            <text x="235" y="442" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">une seule phrase couvre tous les cas</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1 h2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les préfixes, une fois pour toutes</h3>
          <div class="expr" style="font-size:19px;text-align:left;line-height:1.5">kilo 10³ · déci 10⁻¹ · centi 10⁻²<br>milli 10⁻³ · micro 10⁻⁶ · nano 10⁻⁹</div></div>
        <div class="card step s1 h2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les deux équivalences à savoir</h3>
          <div class="expr" style="font-size:21px;text-align:left;line-height:1.4">1 L = 1 dm³ = 10⁻³ m³<br>1 mL = 1 cm³</div></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège, et il est géométrique</h3>
          <p style="font-size:17px">Un mètre vaut cent centimètres. Mais un mètre <b>cube</b> ne vaut pas cent centimètres cubes : il en vaut <b>un million</b>.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La discipline qui évite l'erreur</h3>
          <p style="font-size:17px">Toutes les conversions se font sur la <b>première ligne</b> de la résolution, avant tout calcul. Convertir en cours de route est la façon la plus sûre de se perdre.<br><br>Et le contrôle est immédiat : un volume exprimé dans une unité plus petite donne toujours un <b>nombre plus grand</b>. Si ce n'est pas le cas, la conversion est inversée.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Les préfixes et les deux équivalences de volume : c'est le socle, on le pose une fois.",
      "Maintenant le piège. Voici un cube d'un mètre de côté.",
      "On découpe chaque arête en dix — pour qu'on y voie quelque chose ; en réalité, en cent.",
      "Le petit cube compte <b>dix fois dix fois dix</b> : un million de cm³ dans un m³, pas cent.",
      "<em>La règle :</em> longueur au facteur, aire au carré, <b>volume au cube</b>."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "OEUFS": OEUFS, "ALV": ALV, "GRILLE": GRILLE,
    "BX": str(BX), "BY": str(BY), "BW": str(BW), "BH": str(BH),
    "CX": str(CX), "CY": str(CY), "CS": str(CS), "PAS": "%.1f" % PAS,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("boite a oeufs : %d colonnes x %d rangees = %d oeufs" % (COLS, ROWS, N_OEUFS))
assert N_OEUFS == 12, N_OEUFS
print("ok", make("CH1", "Capsule CH1 — La mole, les masses et les unités · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH1.html")))
