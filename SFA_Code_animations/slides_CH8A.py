# -*- coding: utf-8 -*-
"""CH8-A — Oxydant, reducteur, et le nombre d'oxydation. 4 animations.

Figures au format 470 x 470, palette verte.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH8-01 : la correspondance terme a terme avec CH7 ----------------
PAIRES = [("acide", "oxydant"), ("base", "réducteur"),
          ("proton H⁺", "électron e⁻"), ("échelle de pKa", "échelle de E°")]
PX1, PX2, PW, PH_, PY0, PPAS = 14, 256, 200, 52, 64, 60
CORR = ""
for i, (g, d) in enumerate(PAIRES):
    y = PY0 + i * PPAS
    CORR += ('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="#FFFFFF" stroke="%s" '
             'stroke-width="1.8"/>'
             '<text x="%d" y="%d" text-anchor="middle" font-size="19" '
             'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
             % (PX1, y, PW, PH_, GREY, PX1 + PW // 2, y + 33, INK2, g))
    CORR += ('<rect x="%d" y="%d" width="%d" height="%d" rx="10" fill="%s" stroke="%s" '
             'stroke-width="1.8"/>'
             '<text x="%d" y="%d" text-anchor="middle" font-size="19" '
             'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
             % (PX2, y, PW, PH_, TINT, SFA, PX2 + PW // 2, y + 33, DEEP, d))
    CORR += ('<text x="235" y="%d" text-anchor="middle" font-size="22" '
             'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">↔</text>'
             % (y + 34, GREY))
BAS_CORR = PY0 + (len(PAIRES) - 1) * PPAS + PH_
assert BAS_CORR == 296, BAS_CORR

# ---------------- CH8-04 : la demi-equation, ligne a ligne ----------------
LIGNES = [("1", "MnO₄⁻ → Mn²⁺", "l'élément qui change"),
          ("2", "MnO₄⁻ → Mn²⁺ + 4 H₂O", "les oxygènes, avec de l'eau"),
          ("3", "MnO₄⁻ + 8 H⁺ → Mn²⁺ + 4 H₂O", "les hydrogènes, avec des H⁺"),
          ("4", "MnO₄⁻ + 8 H⁺ + 5 e⁻ → Mn²⁺ + 4 H₂O", "les charges, avec des électrons")]
LY0, LPAS, LXC, LXT = 62, 76, 32, 62


def ligne(i, final=False):
    n, eq, com = LIGNES[i]
    y = LY0 + i * LPAS
    coul = SFA if final else DEEP
    o = ('<circle cx="%d" cy="%d" r="15" fill="%s"/>'
         '<text x="%d" y="%d" text-anchor="middle" font-size="16" '
         'font-family="Be Vietnam Pro,Arial" fill="#FFFFFF" font-weight="700">%s</text>'
         % (LXC, y - 7, coul, LXC, y - 1, n))
    o += ('<text x="%d" y="%d" font-size="20" font-family="Be Vietnam Pro,Arial" fill="%s" '
          'font-weight="700">%s</text>' % (LXT, y, coul, eq))
    o += ('<text x="%d" y="%d" font-size="15" font-family="Be Vietnam Pro,Arial" '
          'fill="#3F3F46">%s</text>' % (LXT, y + 24, com))
    return o


ETAPE = [ligne(i, final=(i == 3)) for i in range(4)]
assert LY0 + 3 * LPAS + 24 == 314

SLIDES = """
  <!-- ==================== ANIM-CH8-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH8-01" data-title="Le même schéma qu'en acido-basicité" data-sub="On transfère des électrons au lieu de protons" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <text x="114" y="44" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">CH7 · acido-basicité</text>
            <text x="356" y="44" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">CH8 · oxydo-réduction</text>
            @@CORR@@
          </g>
          <g class="step s2">
            <rect x="10" y="312" width="450" height="50" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="343" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">un seul mot change : proton → électron</text>
          </g>
          <g class="step s3">
            <rect x="60" y="380" width="350" height="78" rx="14" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="3"/>
            <text x="235" y="429" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">Ox + n e⁻ ⇌ Red</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Deux verbes, comme au chapitre précédent</h3>
          <p style="font-size:17px">Un <b>oxydant</b> capte des électrons. Un <b>réducteur</b> en cède. C'est exactement la structure d'acide et base, avec un autre objet transféré.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le couple, la demi-équation, la table</h3>
          <p style="font-size:17px">Tout est identique : le couple s'écrit <b>oxydant/réducteur</b>, la demi-équation dans le sens de la réduction, et une table classe les couples par force.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une réaction met en jeu deux couples</h3>
          <p style="font-size:17px">L'oxydant de l'un prend les électrons du réducteur de l'autre. Là encore, jamais un couple seul : il faut quelqu'un pour donner.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi il faut annoncer cette correspondance d'emblée</h3>
          <p style="font-size:17px">L'étudiant qui a compris CH7 possède déjà <b>la moitié</b> de ce chapitre. Le lui dire au début change complètement sa façon de l'aborder : il cherche les analogies au lieu de tout réapprendre.<br><br>Ce qui reste réellement nouveau tient en deux points : le <b>nombre d'oxydation</b>, et l'équilibrage en milieu acide. Le reste est du déjà-vu.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le chapitre précédent, colonne de gauche. Celui-ci, colonne de droite.",
      "Acide devient oxydant, base devient réducteur.",
      "Le proton devient un électron, et l'échelle de pKa une échelle de potentiels.",
      "<b>Un seul mot change</b> — tout le reste de la méthode est identique.",
      "<em>Ce qui est vraiment nouveau :</em> le nombre d'oxydation, et l'équilibrage en milieu acide."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH8-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH8-02" data-title="Oxydant et réducteur : qui fait quoi" data-sub="Le moyen mnémotechnique qui ne trompe pas" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <rect x="14" y="24" width="200" height="140" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="114" y="60" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">OXYDANT</text>
            <text x="114" y="96" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">il capte les électrons</text>
            <text x="114" y="136" text-anchor="middle" font-size="20" @@FF@@ fill="@@SFA@@" font-weight="700">il est RÉDUIT</text>
            <rect x="256" y="24" width="200" height="140" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="356" y="60" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">RÉDUCTEUR</text>
            <text x="356" y="96" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">il cède les électrons</text>
            <text x="356" y="136" text-anchor="middle" font-size="20" @@FF@@ fill="@@SFA@@" font-weight="700">il est OXYDÉ</text>
          </g>
          <g class="step s2">
            <line x1="350" y1="208" x2="261" y2="208" stroke="@@SFA@@" stroke-width="4"/><line x1="209" y1="208" x2="120" y2="208" stroke="@@SFA@@" stroke-width="4" marker-end="url(#v2)"/>
            <circle cx="235" cy="208" r="22" fill="@@SFA@@"/>
            <text x="235" y="215" text-anchor="middle" font-size="17" @@FF@@ fill="#FFFFFF" font-weight="700">e⁻</text>
            <text x="235" y="256" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">les électrons vont du réducteur vers l'oxydant</text>
          </g>
          <g class="step s3">
            <rect x="10" y="278" width="450" height="76" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="310" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">oxydation = perte d'électrons</text>
            <text x="235" y="340" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">réduction = gain d'électrons</text>
          </g>
          <g class="step s4">
            <rect x="10" y="368" width="450" height="90" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="402" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">« l'oxydant est oxydé » est faux</text>
            <text x="235" y="436" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">il oxyde l'autre, et se trouve lui-même réduit</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les deux définitions</h3>
          <p style="font-size:17px"><b>Oxydation</b> = perte d'électrons. <b>Réduction</b> = gain d'électrons. Deux lignes, et elles ne se déduisent pas du sens courant des mots.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le moyen de ne jamais confondre</h3>
          <p style="font-size:17px">L'espèce qui est <b>oxydée</b> est le <b>réducteur</b> — c'est elle qui a réduit l'autre. Et inversement. Les deux mots désignent le <b>rôle</b>, pas ce qui arrive.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une formulation qui aide vraiment</h3>
          <p style="font-size:17px">« Réduction » se lit sur la <b>charge</b>, qui diminue quand on gagne des électrons négatifs. Réduire, c'est faire <b>baisser</b> — et c'est la charge qui baisse.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège de vocabulaire, et il revient à chaque contrôle</h3>
          <p style="font-size:17px">« Cu²⁺ est l'oxydant, donc il est oxydé » — l'enchaînement paraît logique, il est faux.<br><br>L'oxydant <b>fait</b> l'oxydation de l'autre, et subit donc lui-même la <b>réduction</b>. Le mot décrit ce que l'espèce provoque, jamais ce qu'elle subit. Un QCM sur ce point départage à lui seul une promotion.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux rôles : l'oxydant capte les électrons, le réducteur les cède.",
      "Et ce qui circule, ce sont les électrons — du réducteur vers l'oxydant.",
      "Oxydation, c'est perdre des électrons. Réduction, c'est en gagner.",
      "Donc l'espèce oxydée est le <b>réducteur</b>, et l'espèce réduite est l'<b>oxydant</b>.",
      "<em>Le piège :</em> l'oxydant n'est pas oxydé. Il oxyde l'autre, et se trouve réduit."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH8-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH8-03" data-title="Calculer un nombre d'oxydation" data-sub="Quatre règles, appliquées dans l'ordre" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <text x="235" y="72" text-anchor="middle" font-size="46" @@FF@@ fill="@@DEEP@@" font-weight="700">MnO₄⁻</text>
            <text x="235" y="110" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">que vaut le nombre d'oxydation du manganèse ?</text>
          </g>
          <g class="step s2">
            <text x="235" y="168" text-anchor="middle" font-size="28" @@FF@@ fill="@@DEEP@@" font-weight="700">Mn + 4 × (−2) = −1</text>
            <text x="235" y="200" text-anchor="middle" font-size="16" @@FF@@ fill="#3F3F46">l'oxygène vaut −2, et la somme vaut la charge</text>
          </g>
          <g class="step s3">
            <text x="235" y="248" text-anchor="middle" font-size="28" @@FF@@ fill="@@DEEP@@" font-weight="700">Mn − 8 = −1</text>
          </g>
          <g class="step s4">
            <rect x="130" y="272" width="210" height="80" rx="14" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="235" y="326" text-anchor="middle" font-size="42" @@FF@@ fill="@@DEEP@@" font-weight="700">Mn = +7</text>
            <rect x="10" y="378" width="450" height="80" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="235" y="410" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">+7 est proche du maximum du manganèse</text>
            <text x="235" y="440" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">il ne peut plus que capter : oxydant puissant</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les quatre règles, dans l'ordre</h3>
          <div class="expr" style="font-size:16px;text-align:left;line-height:1.45"><b>1.</b> un corps simple vaut 0 : Fe, O₂, Cl₂<br><b>2.</b> l'oxygène vaut −2, l'hydrogène +1<br><b>3.</b> un ion monoatomique vaut sa charge<br><b>4.</b> la somme vaut la charge globale</div></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La méthode qui en découle</h3>
          <p style="font-size:17px">On applique les règles 1 à 3 pour tout ce qu'on connaît, et la règle 4 donne l'inconnue par une <b>simple équation du premier degré</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les deux exceptions à connaître</h3>
          <p style="font-size:17px">L'oxygène vaut −1 dans les <b>peroxydes</b>, et l'hydrogène −1 dans les <b>hydrures métalliques</b>. Elles sont rares, et l'énoncé les signale toujours.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">À quoi sert réellement ce nombre</h3>
          <p style="font-size:17px">Il ne sert pas à décorer une formule : il <b>prédit le rôle</b> de l'espèce.<br><br>Un élément à nombre d'oxydation élevé a déjà cédé presque tout ce qu'il pouvait : il ne peut plus que <b>capter</b>. C'est pourquoi le permanganate (Mn à +7) et le dichromate (Cr à +6) sont les deux grands oxydants du programme — leur formule le dit avant tout tableau.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "L'ion permanganate, et la question : combien vaut le manganèse ?",
      "L'oxygène vaut −2, il y en a quatre, et la somme doit valoir la charge : −1.",
      "L'équation se résout en une ligne.",
      "Le manganèse est à <b>+7</b>.",
      "<em>Et ce nombre prédit son rôle :</em> à +7, il ne peut plus que capter. C'est un oxydant."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH8-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH8-04" data-title="Écrire une demi-équation" data-sub="Cinq étapes, et le contrôle des charges" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <text x="16" y="30" font-size="17" @@FF@@ fill="@@GREY@@">réduction du permanganate en milieu acide</text>
            @@L0@@
          </g>
          <g class="step s2">@@L1@@</g>
          <g class="step s3">@@L2@@</g>
          <g class="step s4">@@L3@@
            <rect x="10" y="352" width="450" height="106" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="386" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">5 · on vérifie, et c'est obligatoire</text>
            <text x="235" y="418" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">charges : (−1) + 8 − 5 = +2 des deux côtés ✓</text>
            <text x="235" y="446" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">atomes : Mn 1 · O 4 · H 8 ✓</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les cinq étapes, et leur ordre</h3>
          <div class="expr" style="font-size:16px;text-align:left;line-height:1.45"><b>1.</b> l'élément qui change<br><b>2.</b> les oxygènes, avec H₂O<br><b>3.</b> les hydrogènes, avec H⁺<br><b>4.</b> les charges, avec des e⁻<br><b>5.</b> on vérifie atomes et charges</div></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'ordre n'est pas modifiable</h3>
          <p style="font-size:17px">Équilibrer les charges <b>avant</b> les atomes conduit systématiquement à une impasse. Oxygènes, puis hydrogènes, puis charges — toujours dans ce sens.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les électrons ne se devinent pas</h3>
          <p style="font-size:17px">Ils <b>tombent du calcul des charges</b>. Ici : +7 à gauche, +2 à droite, donc cinq électrons à gauche. Il n'y a rien à chercher.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le contrôle refait le calcul dans l'autre sens</h3>
          <p style="font-size:17px">On recompte les charges sur l'équation terminée : (−1) + 8 − 5 = +2 à gauche, +2 à droite ✓<br><br>C'est le calcul de l'étape 4 relu à l'envers — trois secondes, et toute la demi-équation est validée. Or une demi-équation fausse sera multipliée par un coefficient en CH8-B.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "On part de l'élément qui change : le manganèse, déjà équilibré.",
      "Quatre oxygènes à gauche : on ajoute quatre molécules d'eau à droite.",
      "Huit hydrogènes sont apparus : on ajoute huit H⁺ à gauche.",
      "Les charges donnent le nombre d'électrons : <b>cinq</b>, et on ne les devine pas.",
      "<em>Le contrôle refait ce calcul à l'envers</em> — trois secondes, et tout est validé."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "CORR": CORR,
    "L0": ETAPE[0], "L1": ETAPE[1], "L2": ETAPE[2], "L3": ETAPE[3],
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH8-A : %d correspondances, %d etapes de demi-equation" % (len(PAIRES), len(LIGNES)))
print("ok", make("CH8-A", "Capsule CH8-A — Oxydant, réducteur, et le nombre d'oxydation · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH8A.html")))
