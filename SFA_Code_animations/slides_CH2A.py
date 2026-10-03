# -*- coding: utf-8 -*-
"""CH2-A — L'atome, l'ion, et la couche de valence. 4 animations.

Figures au format 470 x 470 : les couches electroniques, qui etaient
contraintes par une hauteur de 330, occupent maintenant toute la colonne.
"""
import sys, math
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED


# ---------- CH2-01 : noyau (8 p + 8 n) et 2 couches ----------
def noyau(cx, cy, np_, nn, rp=10):
    """Nucleons ranges en spirale serree, sans recouvrement."""
    out, k = [], 0
    for i in range(np_ + nn):
        ring = 0 if i == 0 else (1 if i < 7 else 2)
        r = [0, 19, 35][ring]
        n_in = [1, 6, 12][ring]
        idx = i - [0, 1, 7][ring]
        a = 2 * math.pi * idx / n_in
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        c = SFA if k < np_ else "#B7BDC9"
        out.append('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (x, y, rp, c))
        k += 1
    return "".join(out)


def couche(cx, cy, r, n, re=8, start=-90):
    o = ['<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="1.8" stroke-dasharray="5 5"/>'
         % (cx, cy, r, GREY)]
    for i in range(n):
        a = math.radians(start + 360 * i / n)
        o.append('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>'
                 % (cx + r * math.cos(a), cy + r * math.sin(a), re, DEEP))
    return "".join(o)


OX1, OY1 = 170, 190
NOY = noyau(OX1, OY1, 8, 8)
C1 = couche(OX1, OY1, 74, 2)
C2 = couche(OX1, OY1, 126, 6)
assert OX1 - 126 - 8 >= 4 and OY1 + 126 + 8 <= 330, "couches hors cadre"

# ---------- CH2-03 : remplissage des couches du sodium ----------
NX, NY = 235, 200
RK, RL, RM = 60, 108, 156
SOD_K = couche(NX, NY, RK, 2)
SOD_L = couche(NX, NY, RL, 8)
SOD_M = couche(NX, NY, RM, 1)
VX, VY = NX, NY - RM                       # position de l'electron de valence
assert VY - 18 >= 4, VY

SLIDES = """
  <!-- ==================== ANIM-CH2-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH2-01" data-title="Z et A, et ce qu'ils comptent vraiment" data-sub="Deux nombres, trois particules" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">@@NOY@@
            <text x="@@OX1@@" y="352" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">le noyau</text>
            <circle cx="336" cy="152" r="10" fill="@@SFA@@"/><text x="358" y="159" font-size="18" @@FF@@ fill="#3F3F46">8 protons</text>
            <circle cx="336" cy="196" r="10" fill="#B7BDC9"/><text x="358" y="203" font-size="18" @@FF@@ fill="#3F3F46">8 neutrons</text>
          </g>
          <g class="step s2">@@C1@@@@C2@@
            <circle cx="336" cy="240" r="8" fill="@@DEEP@@"/><text x="358" y="247" font-size="18" @@FF@@ fill="#3F3F46">8 électrons</text>
          </g>
          <g class="step s3">
            <rect x="20" y="376" width="430" height="84" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.6"/>
            <text x="146" y="410" text-anchor="end" font-size="26" @@FF@@ fill="@@SFA@@" font-weight="700">16</text>
            <text x="146" y="446" text-anchor="end" font-size="26" @@FF@@ fill="@@SFA@@" font-weight="700">8</text>
            <text x="156" y="432" font-size="50" @@FF@@ fill="@@DEEP@@" font-weight="700">O</text>
            <text x="228" y="410" font-size="19" @@FF@@ fill="@@GREY@@">A = nucléons = 16</text>
            <text x="228" y="442" font-size="19" @@FF@@ fill="@@GREY@@">Z = protons = 8</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le numéro atomique Z</h3>
          <p style="font-size:17px">C'est le nombre de <b>protons</b>. Et c'est lui, et lui seul, qui définit l'élément : changer Z, c'est changer d'élément.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le nombre de masse A</h3>
          <p style="font-size:17px">C'est le nombre de <b>nucléons</b> — protons plus neutrons. Le nombre de neutrons vaut donc <b>A − Z</b>, et jamais A.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un atome est neutre</h3>
          <p style="font-size:17px">Autant d'électrons que de protons, donc <b>Z électrons</b>. C'est ce qui rend l'atome électriquement neutre, et c'est ce qu'un ion cesse d'être.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qui change quand on forme un ion</h3>
          <p style="font-size:17px">Un ion a gagné ou perdu des <b>électrons</b>. Le noyau n'est <b>jamais</b> touché : Z et A ne bougent pas.<br><br><b>Le piège :</b> croire qu'un cation a perdu un proton. S'il en perdait un, ce ne serait plus le même élément. Il a perdu un électron — c'est pour cela qu'il devient positif, et qu'il reste le même élément.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Au centre, le noyau : des protons et des neutrons, serrés ensemble.",
      "Autour, les électrons, répartis sur des couches — autant que de protons.",
      "Deux nombres résument tout : <b>Z</b> compte les protons, <b>A</b> compte les nucléons.",
      "Le nombre de neutrons ne se lit nulle part : il se calcule, <b>A − Z</b>.",
      "<em>Et pour un ion :</em> seuls les électrons changent. Le noyau, donc Z et A, reste intact."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH2-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH2-02" data-title="Les isotopes, et d'où vient la masse décimale" data-sub="Pourquoi le chlore pèse 35,5" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <rect x="22" y="26" width="206" height="164" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="125" y="84" text-anchor="middle" font-size="40" @@FF@@ fill="@@DEEP@@" font-weight="700">³⁵Cl</text>
            <text x="125" y="122" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">17 protons · 18 neutrons</text>
            <text x="125" y="166" text-anchor="middle" font-size="30" @@FF@@ fill="@@SFA@@" font-weight="700">75 %</text>
            <rect x="242" y="26" width="206" height="164" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="345" y="84" text-anchor="middle" font-size="40" @@FF@@ fill="@@DEEP@@" font-weight="700">³⁷Cl</text>
            <text x="345" y="122" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">17 protons · 20 neutrons</text>
            <text x="345" y="166" text-anchor="middle" font-size="30" @@FF@@ fill="@@SFA@@" font-weight="700">25 %</text>
          </g>
          <g class="step s2">
            <text x="235" y="232" text-anchor="middle" font-size="21" @@FF@@ fill="@@RED@@" font-weight="700">même Z, donc exactement la même chimie</text>
          </g>
          <g class="step s3">
            <rect x="26" y="262" width="309" height="62" rx="4" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="1.8"/>
            <rect x="335" y="262" width="103" height="62" rx="4" fill="@@SFA@@" opacity="0.45" stroke="@@DEEP@@" stroke-width="1.8"/>
            <text x="180" y="300" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">0,75 × 35</text>
            <text x="386" y="300" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">0,25 × 37</text>
          </g>
          <g class="step s4">
            <text x="235" y="384" text-anchor="middle" font-size="34" @@FF@@ fill="@@DEEP@@" font-weight="700">26,25 + 9,25 = 35,5</text>
            <rect x="10" y="410" width="450" height="48" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="441" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">aucun atome ne pèse 35,5 : c'est une moyenne</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Deux isotopes du même élément</h3>
          <p style="font-size:17px">Même Z, des A différents : le nombre de <b>neutrons</b> change, rien d'autre. Ce sont deux variétés du même élément.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et pourtant, la même chimie</h3>
          <p style="font-size:17px">Les propriétés chimiques ne dépendent que des <b>électrons</b>. Le nombre d'électrons n'a pas changé : les deux isotopes réagissent exactement pareil.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La masse du tableau est une moyenne</h3>
          <p style="font-size:17px">Pondérée par l'abondance naturelle de chaque isotope. C'est pour cela qu'elle n'est presque jamais un nombre entier.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que le 35,5 signifie vraiment</h3>
          <p style="font-size:17px"><b>Aucun atome de chlore ne pèse 35,5.</b> Il en existe à 35 et à 37, jamais entre les deux. La valeur du tableau est une moyenne statistique — elle décrit un échantillon, pas un atome.<br><br>C'est pourtant elle qu'on utilise dans tous les calculs de mole, parce qu'on manipule toujours des milliards d'atomes à la fois.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le chlore existe sous deux formes : l'une à 35 nucléons, l'autre à 37.",
      "Même nombre de protons, donc même nombre d'électrons — donc <b>exactement la même chimie</b>.",
      "Mais pas dans les mêmes proportions : trois quarts, un quart.",
      "La masse du tableau est la moyenne pondérée : <b>35,5</b>.",
      "<em>À retenir :</em> aucun atome ne pèse 35,5. C'est une moyenne, pas une mesure."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH2-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH2-03" data-title="Remplir les couches électroniques" data-sub="L'ordre de remplissage, et la couche qui compte" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <circle class="step s1" cx="@@NX@@" cy="@@NY@@" r="27" fill="@@SFA@@"/>
          <text class="step s1" x="@@NX@@" y="@@NYT@@" text-anchor="middle" font-size="22" @@FF@@ fill="#FFFFFF" font-weight="700">Na</text>
          <g class="step s1">@@SODK@@</g>
          <g class="step s2">@@SODL@@</g>
          <g class="step s3">@@SODM@@
            <circle cx="@@VX@@" cy="@@VY@@" r="19" fill="none" stroke="@@RED@@" stroke-width="3.2"/>
            <line x1="256" y1="@@VY@@" x2="316" y2="@@VY@@" stroke="@@RED@@" stroke-width="2.4"/>
            <text x="324" y="38" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">couche de</text>
            <text x="324" y="60" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">valence</text>
          </g>
          <g class="step s4">
            <text x="235" y="408" text-anchor="middle" font-size="32" @@FF@@ fill="@@DEEP@@" font-weight="700">Na (Z = 11) : 2, 8, 1</text>
            <rect x="10" y="422" width="450" height="44" rx="11" fill="@@TINT2@@"/>
            <text x="235" y="451" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">un seul chiffre, et toute la chimie du sodium suit</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Des couches de capacité fixe</h3>
          <p style="font-size:17px"><b>2, puis 8, puis 8</b> pour les vingt premiers éléments — les seuls qui tombent au concours. On ne va pas plus loin.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">On remplit dans l'ordre, sans sauter</h3>
          <p style="font-size:17px">La couche suivante ne commence que lorsque la précédente est <b>pleine</b>. Il n'y a aucun choix à faire, aucune exception à connaître.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La dernière couche décide de tout</h3>
          <p style="font-size:17px">C'est la <b>couche de valence</b>. Les couches internes n'interviennent jamais dans une réaction : toute la chimie de l'élément tient dans ce dernier étage.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que cette seule information permet de prédire</h3>
          <p style="font-size:17px">Le sodium a <b>un</b> électron de valence. Cela suffit à savoir qu'il le perdra, qu'il donnera un ion <b>Na⁺</b>, qu'il est très réactif, et qu'il ressemble au lithium et au potassium.<br><br>Quatre prédictions à partir d'un seul chiffre — c'est ce qui rend le tableau périodique utilisable.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le sodium, onze électrons à placer. La première couche en accueille deux.",
      "Elle est pleine : les suivants vont sur la deuxième, qui en accueille huit.",
      "Reste un électron, tout seul sur la troisième couche : c'est la <b>couche de valence</b>.",
      "La configuration s'écrit <b>2, 8, 1</b>. Le total redonne bien onze.",
      "<em>Et ce dernier chiffre suffit à prédire toute la chimie du sodium.</em>"
    ]</script>
  </section>

  <!-- ==================== ANIM-CH2-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH2-04" data-title="La règle de l'octet gouverne les ions" data-sub="La charge d'un ion se lit dans le tableau" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <rect x="20" y="26" width="206" height="136" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="123" y="66" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">Na : 2, 8, 1</text>
            <text x="123" y="104" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">1 électron de valence</text>
            <text x="123" y="140" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">il en perd 1</text>
            <rect x="244" y="26" width="206" height="136" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="347" y="66" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">Cl : 2, 8, 7</text>
            <text x="347" y="104" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">7 électrons de valence</text>
            <text x="347" y="140" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">il en gagne 1</text>
          </g>
          <g class="step s2">
            <line x1="123" y1="174" x2="123" y2="216" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v4)"/>
            <line x1="347" y1="174" x2="347" y2="216" stroke="@@SFA@@" stroke-width="3.2" marker-end="url(#v4)"/>
            <text x="123" y="278" text-anchor="middle" font-size="46" @@FF@@ fill="@@DEEP@@" font-weight="700">Na⁺</text>
            <text x="347" y="278" text-anchor="middle" font-size="46" @@FF@@ fill="@@DEEP@@" font-weight="700">Cl⁻</text>
          </g>
          <g class="step s3">
            <rect x="20" y="310" width="430" height="92" rx="14" fill="@@TINT2@@"/>
            <text x="235" y="348" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">tous deux ont désormais 2, 8, 8</text>
            <text x="235" y="382" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">la structure de l'argon, le gaz noble voisin</text>
          </g>
          <g class="step s4">
            <text x="235" y="444" text-anchor="middle" font-size="20" @@FF@@ fill="@@RED@@" font-weight="700">aucune charge n'est à mémoriser</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La règle de l'octet</h3>
          <p style="font-size:17px">Un atome tend à obtenir <b>huit électrons</b> sur sa couche de valence — deux seulement pour les tout premiers, qui visent l'hélium.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le chemin le plus court décide</h3>
          <p style="font-size:17px"><b>1, 2 ou 3</b> électrons de valence → l'atome en perd, il devient un <b>cation</b>. <b>5, 6 ou 7</b> → il en gagne, il devient un <b>anion</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et la charge se déduit du compte</h3>
          <p style="font-size:17px">Le sodium perd un électron : il lui reste une charge positive de trop, donc <b>Na⁺</b>. Le chlore en gagne un : <b>Cl⁻</b>. Aucune charge n'est à mémoriser.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi les gaz nobles ne réagissent pas</h3>
          <p style="font-size:17px">Ils ont <b>déjà</b> huit électrons de valence. Ils n'ont donc rien à gagner ni à perdre : ils ne forment pas d'ions et ne réagissent pratiquement pas.<br><br>C'est ce qui en fait la <b>référence</b> de toute la chimie : chaque atome cherche à leur ressembler, et c'est cette course qui produit toutes les réactions du programme.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le sodium a un électron de valence, le chlore en a sept. Chacun vise huit.",
      "Le plus court chemin : le sodium en perd un, le chlore en gagne un.",
      "Le premier devient <b>Na⁺</b>, le second <b>Cl⁻</b> — et la charge se lit dans le compte.",
      "Tous deux ont maintenant la configuration de l'argon.",
      "<em>Voilà pourquoi les gaz nobles ne réagissent pas :</em> ils y sont déjà."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "NOY": NOY, "C1": C1, "C2": C2, "OX1": str(OX1),
    "SODK": SOD_K, "SODL": SOD_L, "SODM": SOD_M,
    "NX": str(NX), "NY": str(NY), "NYT": str(NY + 8),
    "VX": str(VX), "VY": str(VY),
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("sodium : couches r = %d / %d / %d · valence en (%d ; %d)" % (RK, RL, RM, VX, VY))
print("ok", make("CH2-A", "Capsule CH2-A — L'atome, l'ion, et la couche de valence · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH2A.html")))
