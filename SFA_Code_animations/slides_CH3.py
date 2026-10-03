# -*- coding: utf-8 -*-
"""CH3 — Les liaisons et la cohesion de la matiere. 4 animations.

Figures au format 470 x 470. Le diagramme d'ebullition est redessine autour de
la ligne 0 °C : les barres pendent sous le zero pour les temperatures negatives
et montent au-dessus pour l'eau, ce qui rend l'ecart lisible — l'ancienne
version, calee sur -200 °C, ecrasait O2 et CH4 en deux traits de 10 px.
"""
import math
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH3-04 : temperatures d'ebullition, echelle calculee ----------------
Y_ZERO, K = 250.0, 0.75                   # 0 °C a y = 250 ; 0,75 px par degre
BARW = 84


def ybar(T):
    return Y_ZERO - T * K


SERIE = [("O₂", -183, 52), ("CH₄", -161, 193), ("H₂O", 100, 334)]
BARS = ""
for nom, T, x in SERIE:
    y = ybar(T)
    haut, bas = min(y, Y_ZERO), max(y, Y_ZERO)
    col = RED if T > 0 else SFA
    BARS += ('<rect x="%d" y="%.1f" width="%d" height="%.1f" rx="5" fill="%s" opacity="0.85"/>'
             % (x, haut, BARW, bas - haut, col))
    cx = x + BARW // 2
    # dans les deux cas le nom vient d'abord, la temperature ensuite, en
    # s'eloignant de la ligne du zero : la lecture est la meme des deux cotes.
    if T > 0:                              # barre montante : libelles au-dessus
        yn, yt = haut - 14, haut - 42
    else:                                  # barre descendante : libelles en dessous
        yn, yt = bas + 30, bas + 56
    BARS += ('<text x="%d" y="%.1f" text-anchor="middle" font-size="19" font-family="Be Vietnam Pro,Arial" '
             'fill="%s" font-weight="700">%+d °C</text>' % (cx, yt, DEEP, T))
    BARS += ('<text x="%d" y="%.1f" text-anchor="middle" font-size="22" font-family="Be Vietnam Pro,Arial" '
             'fill="%s" font-weight="700">%s</text>' % (cx, yn, DEEP, nom))
    assert 20 <= min(yt, yn) - 22 and max(yt, yn) <= 462, (nom, yt, yn)

# ---------------- CH3-02 : NH3, liaisons calculees bord a bord ----------------
NCX, NCY, NR = 235, 210, 34
HS = [(145, 296), (325, 296), (235, 336)]
HR = 24
LIAISONS = ""
for hx, hy in HS:
    dx, dy = hx - NCX, hy - NCY
    d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    LIAISONS += ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3.4" '
                 'stroke-linecap="round"/>'
                 % (NCX + NR * ux, NCY + NR * uy, hx - HR * ux, hy - HR * uy, DEEP))
HYDROS = ""
for hx, hy in HS:
    HYDROS += ('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" stroke-width="2.2"/>'
               % (hx, hy, HR, TINT2, DEEP))
    HYDROS += ('<text x="%d" y="%d" text-anchor="middle" font-size="21" font-family="Be Vietnam Pro,Arial" '
               'fill="%s" font-weight="700">H</text>' % (hx, hy + 8, DEEP))

SLIDES = """
  <!-- ==================== ANIM-CH3-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH3-01" data-title="Trois façons de satisfaire l'octet" data-sub="Ionique, covalente, métallique — une seule motivation" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <rect x="14" y="16" width="442" height="120" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="32" y="48" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">IONIQUE — l'un donne, l'autre prend</text>
            <circle cx="90" cy="98" r="21" fill="@@SFA@@"/><text x="90" y="105" text-anchor="middle" font-size="17" @@FF@@ fill="#FFFFFF" font-weight="700">Na</text>
            <line x1="118" y1="98" x2="212" y2="98" stroke="@@DEEP@@" stroke-width="2.6" marker-end="url(#d1)"/>
            <text x="165" y="86" text-anchor="middle" font-size="15" @@FF@@ fill="@@DEEP@@">1 e⁻</text>
            <circle cx="248" cy="98" r="21" fill="@@DEEP@@"/><text x="248" y="105" text-anchor="middle" font-size="17" @@FF@@ fill="#FFFFFF" font-weight="700">Cl</text>
            <text x="290" y="105" font-size="17" @@FF@@ fill="#3F3F46">métal + non-métal</text>
          </g>
          <g class="step s2">
            <rect x="14" y="150" width="442" height="120" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="32" y="182" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">COVALENTE — les deux partagent</text>
            <circle cx="110" cy="232" r="21" fill="@@SFA@@"/><text x="110" y="239" text-anchor="middle" font-size="17" @@FF@@ fill="#FFFFFF" font-weight="700">H</text>
            <circle cx="206" cy="232" r="21" fill="@@SFA@@"/><text x="206" y="239" text-anchor="middle" font-size="17" @@FF@@ fill="#FFFFFF" font-weight="700">H</text>
            <circle cx="150" cy="232" r="6" fill="@@DEEP@@"/><circle cx="166" cy="232" r="6" fill="@@DEEP@@"/>
            <text x="248" y="239" font-size="17" @@FF@@ fill="#3F3F46">deux non-métaux</text>
          </g>
          <g class="step s3">
            <rect x="14" y="284" width="442" height="120" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="32" y="316" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">MÉTALLIQUE — tous mettent en commun</text>
            <circle cx="90" cy="366" r="18" fill="@@SFA@@"/><circle cx="146" cy="366" r="18" fill="@@SFA@@"/><circle cx="202" cy="366" r="18" fill="@@SFA@@"/>
            <circle cx="118" cy="346" r="5" fill="@@DEEP@@"/><circle cx="174" cy="346" r="5" fill="@@DEEP@@"/>
            <circle cx="118" cy="386" r="5" fill="@@DEEP@@"/><circle cx="174" cy="386" r="5" fill="@@DEEP@@"/>
            <text x="244" y="373" font-size="17" @@FF@@ fill="#3F3F46">deux métaux</text>
          </g>
          <g class="step s4">
            <rect x="10" y="418" width="450" height="44" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="447" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">c'est la différence d'électronégativité qui tranche</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une seule motivation, trois moyens</h3>
          <p style="font-size:17px">Chaque atome cherche son <b>octet</b>. La liaison ionique est le transfert pur : un atome donne, l'autre prend, et les deux ions s'attirent.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Quand aucun ne peut arracher à l'autre</h3>
          <p style="font-size:17px">Ils <b>partagent</b> un doublet d'électrons : chacun le compte pour lui. C'est la liaison covalente, entre non-métaux.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et dans un métal</h3>
          <p style="font-size:17px">Les électrons de valence sont mis en commun dans tout le solide. C'est ce qui explique que les métaux <b>conduisent</b> et se <b>déforment</b> sans casser.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le critère de choix, et il est déjà connu</h3>
          <p style="font-size:17px">C'est la <b>différence d'électronégativité</b> — la flèche de la capsule CH2-B.<br><br><b>Grande différence</b> (un élément à gauche, un à droite du tableau) → l'un arrache à l'autre, c'est <b>ionique</b>. <b>Faible différence</b> (deux éléments voisins) → aucun ne l'emporte, c'est <b>covalent</b>.<br><br>Le type de liaison se lit donc dans le tableau, avant toute autre considération.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Premier moyen : un atome donne son électron, l'autre le prend. C'est la liaison <b>ionique</b>.",
      "Deuxième : aucun ne peut arracher à l'autre, alors ils <b>partagent</b>. C'est la covalente.",
      "Troisième : dans un métal, tous mettent leurs électrons en commun.",
      "Trois moyens, mais une seule motivation — satisfaire l'octet.",
      "<em>Et le choix se lit dans le tableau :</em> c'est la différence d'électronégativité qui tranche."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH3-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH3-02" data-title="Construire une structure de Lewis" data-sub="Cinq étapes, dans cet ordre, sans exception" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="235" y="44" text-anchor="middle" font-size="23" @@FF@@ fill="@@DEEP@@" font-weight="700">NH₃ &nbsp;·&nbsp; 5 + 3 × 1 = 8 électrons</text>
            <text x="235" y="76" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">soit 4 doublets à placer</text>
          </g>
          <g class="step s2">
            <circle cx="@@NCX@@" cy="@@NCY@@" r="@@NR@@" fill="@@SFA@@"/>
            <text x="@@NCX@@" y="@@NCT@@" text-anchor="middle" font-size="28" @@FF@@ fill="#FFFFFF" font-weight="700">N</text>
          </g>
          <g class="step s3">@@LIAISONS@@@@HYDROS@@</g>
          <g class="step s4">
            <circle cx="225" cy="146" r="8" fill="@@RED@@"/><circle cx="245" cy="146" r="8" fill="@@RED@@"/>
            <text x="266" y="136" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">doublet non liant</text>
            <text x="235" y="398" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">le moins électronégatif au centre, jamais l'hydrogène</text>
            <rect x="14" y="414" width="442" height="46" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="444" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">4 doublets comptés, 4 doublets placés ✓</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les cinq étapes, dans cet ordre</h3>
          <div class="expr" style="font-size:16px;text-align:left;line-height:1.45"><b>1.</b> compter les électrons de valence<br><b>2.</b> placer l'atome central<br><b>3.</b> relier par des liaisons simples<br><b>4.</b> compléter l'octet des périphériques<br><b>5.</b> former des liaisons multiples s'il manque</div></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'atome central</h3>
          <p style="font-size:17px">C'est le <b>moins électronégatif</b>, et ce n'est <b>jamais l'hydrogène</b> — il ne peut porter qu'une seule liaison.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le doublet qu'on oublie</h3>
          <p style="font-size:17px">Trois liaisons consomment 3 doublets ; il en reste <b>un</b>, qui se pose sur l'azote. Il ne relie rien, mais il <b>occupe de la place</b> — et c'est lui qui déformera la géométrie.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi l'ordre n'est pas négociable</h3>
          <p style="font-size:17px">Commencer par les liaisons multiples conduit presque toujours à une structure où il reste des électrons à placer et plus aucune position libre.<br><br>En suivant les cinq étapes, le compte <b>tombe juste par construction</b> : on a placé exactement le nombre d'électrons compté à l'étape 1, ni plus ni moins. C'est le contrôle final, et il est gratuit.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "On compte d'abord : cinq électrons pour l'azote, un par hydrogène. Huit en tout.",
      "L'azote va au centre — c'est le moins électronégatif, et l'hydrogène ne peut jamais y être.",
      "Trois liaisons simples relient les trois hydrogènes : trois doublets consommés.",
      "Il en reste <b>un</b>, qui se pose sur l'azote : c'est un <b>doublet non liant</b>.",
      "<em>Le compte tombe juste :</em> quatre doublets placés, quatre doublets comptés."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH3-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH3-03" data-title="De la géométrie à la polarité" data-sub="Les doublets se repoussent, la forme en découle" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <text x="118" y="34" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">CO₂ · linéaire</text>
            <circle cx="42" cy="110" r="24" fill="@@DEEP@@"/><text x="42" y="118" text-anchor="middle" font-size="18" @@FF@@ fill="#FFFFFF" font-weight="700">O</text>
            <circle cx="118" cy="110" r="24" fill="@@SFA@@"/><text x="118" y="118" text-anchor="middle" font-size="18" @@FF@@ fill="#FFFFFF" font-weight="700">C</text>
            <circle cx="194" cy="110" r="24" fill="@@DEEP@@"/><text x="194" y="118" text-anchor="middle" font-size="18" @@FF@@ fill="#FFFFFF" font-weight="700">O</text>
            <g stroke="@@GREY@@" stroke-width="2.6">
              <line x1="66" y1="105" x2="94" y2="105"/><line x1="66" y1="115" x2="94" y2="115"/>
              <line x1="142" y1="105" x2="170" y2="105"/><line x1="142" y1="115" x2="170" y2="115"/>
            </g>
          </g>
          <g class="step s2">
            <line x1="112" y1="178" x2="42" y2="178" stroke="@@RED@@" stroke-width="3.6" marker-end="url(#r3)"/>
            <line x1="124" y1="178" x2="194" y2="178" stroke="@@RED@@" stroke-width="3.6" marker-end="url(#r3)"/>
            <text x="118" y="216" text-anchor="middle" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">opposées</text>
            <text x="118" y="250" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">somme nulle</text>
            <text x="118" y="292" text-anchor="middle" font-size="27" @@FF@@ fill="@@SFA@@" font-weight="700">APOLAIRE</text>
          </g>
          <g class="step s3">
            <text x="352" y="34" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">H₂O · coudée</text>
            <circle cx="352" cy="86" r="24" fill="@@DEEP@@"/><text x="352" y="94" text-anchor="middle" font-size="18" @@FF@@ fill="#FFFFFF" font-weight="700">O</text>
            <circle cx="288" cy="166" r="21" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="2.2"/><text x="288" y="173" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">H</text>
            <circle cx="416" cy="166" r="21" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="2.2"/><text x="416" y="173" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">H</text>
            <g stroke="@@GREY@@" stroke-width="2.8">
              <line x1="336" y1="104" x2="302" y2="148"/><line x1="368" y1="104" x2="402" y2="148"/>
            </g>
          </g>
          <g class="step s4">
            <line x1="302" y1="148" x2="338" y2="102" stroke="@@RED@@" stroke-width="3.6" marker-end="url(#r3)"/>
            <line x1="402" y1="148" x2="366" y2="102" stroke="@@RED@@" stroke-width="3.6" marker-end="url(#r3)"/>
            <line x1="352" y1="232" x2="352" y2="122" stroke="@@SFA@@" stroke-width="4.4" marker-end="url(#v3)"/>
            <text x="352" y="262" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">somme non nulle</text>
            <text x="352" y="292" text-anchor="middle" font-size="27" @@FF@@ fill="@@RED@@" font-weight="700">POLAIRE</text>
            <rect x="14" y="330" width="442" height="128" rx="14" fill="@@TINT2@@"/>
            <text x="235" y="368" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">deux questions distinctes, dans cet ordre</text>
            <text x="235" y="406" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@">1 · les liaisons sont-elles polarisées ?</text>
            <text x="235" y="438" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@">2 · la forme les fait-elle s'annuler ?</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La géométrie se déduit, elle ne s'apprend pas</h3>
          <p style="font-size:17px">Les doublets autour de l'atome central se <b>repoussent</b> et s'écartent au maximum. Deux doublets → <b>linéaire</b> · trois → <b>trigonale plane</b> · quatre → <b>tétraédrique</b>.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Deux liaisons polarisées, et pourtant rien</h3>
          <p style="font-size:17px">CO₂ est <b>linéaire</b> : les deux effets sont exactement opposés et de même intensité. Ils s'annulent — la molécule est <b>apolaire</b>.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Mêmes liaisons, forme différente, résultat inverse</h3>
          <p style="font-size:17px">H₂O porte deux doublets non liants : la molécule est <b>coudée</b>. Les deux effets ne s'opposent plus, ils s'additionnent — la molécule est <b>polaire</b>.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Deux questions distinctes, dans cet ordre</h3>
          <p style="font-size:17px"><b>1.</b> Les liaisons sont-elles polarisées ? On compare les électronégativités.<br><b>2.</b> La molécule est-elle polaire ? On regarde la <b>forme</b>, et on fait la somme <b>vectorielle</b>.<br><br>Répondre à la première ne répond pas à la seconde : c'est tout l'enseignement de CO₂. Et cette somme vectorielle est celle de la capsule B2-A des mathématiques, appliquée à des molécules.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le dioxyde de carbone : deux doublets autour du carbone, donc une molécule linéaire.",
      "Ses deux liaisons sont polarisées, mais <b>exactement opposées</b> : la somme est nulle, elle est apolaire.",
      "L'eau, elle, porte deux doublets non liants : sa forme est <b>coudée</b>.",
      "Les deux effets ne s'opposent plus — ils s'additionnent. Elle est <b>polaire</b>.",
      "<em>Deux questions distinctes :</em> les liaisons d'abord, la forme ensuite."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH3-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH3-04" data-title="Pourquoi l'eau bout à 100 °C" data-sub="La liaison hydrogène, et l'anomalie qu'elle explique" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <line x1="26" y1="@@YZ@@" x2="444" y2="@@YZ@@" stroke="@@DEEP@@" stroke-width="2" stroke-dasharray="7 5"/>
            <text x="26" y="@@YZT@@" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">0 °C</text>
          </g>
          <g class="step s2">@@BARS@@</g>
          <g class="step s3">
            <rect x="10" y="20" width="450" height="44" rx="11" fill="@@TINT2@@"/>
            <text x="235" y="49" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">masses comparables, plus de 260 °C d'écart</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que bouillir veut dire</h3>
          <p style="font-size:17px">Faire bouillir un liquide, c'est vaincre les forces <b>entre</b> les molécules — pas casser les molécules elles-mêmes. Les liaisons covalentes restent intactes.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Trois molécules, trois régimes</h3>
          <p style="font-size:17px">O₂ et CH₄ sont <b>apolaires</b> : seules des forces très faibles les retiennent, elles bouillent bien en dessous de zéro. H₂O est polaire.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La liaison hydrogène</h3>
          <p style="font-size:17px">Elle apparaît quand un hydrogène est lié à un atome très électronégatif — <b>O, N ou F</b>. C'est la plus forte des forces intermoléculaires, et de loin.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'anomalie, et ce qu'elle rend possible</h3>
          <p style="font-size:17px">Au vu de sa masse, l'eau devrait bouillir vers <b>− 80 °C</b>. Elle bout à + 100 °C : ses liaisons hydrogène la retiennent.<br><br>Sans elles, il n'y aurait <b>aucune eau liquide</b> sur Terre — et donc aucune vie. C'est le pont direct avec la biologie, et il mérite d'être dit.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Une échelle de température, et le zéro tracé en pointillés.",
      "Trois molécules de masses comparables — et trois températures d'ébullition.",
      "O₂ et CH₄ bouillent très en dessous de zéro. L'eau, à cent degrés au-dessus.",
      "L'écart dépasse <b>260 degrés</b>, et une seule chose l'explique : la liaison hydrogène.",
      "<em>Sans elle</em>, il n'y aurait pas d'eau liquide sur Terre — donc pas de vie."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "BARS": BARS, "YZ": "%.1f" % Y_ZERO, "YZT": "%.1f" % (Y_ZERO - 10),
    "LIAISONS": LIAISONS, "HYDROS": HYDROS,
    "NCX": str(NCX), "NCY": str(NCY), "NCT": str(NCY + 10), "NR": str(NR),
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("ebullition : y(0) = %.1f · y(-183) = %.1f · y(-161) = %.1f · y(100) = %.1f"
      % (ybar(0), ybar(-183), ybar(-161), ybar(100)))
print("ok", make("CH3", "Capsule CH3 — Les liaisons et la cohésion de la matière · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH3.html")))
