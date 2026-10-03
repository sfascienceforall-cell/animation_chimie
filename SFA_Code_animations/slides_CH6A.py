# -*- coding: utf-8 -*-
"""CH6-A — Le carbone et les groupes fonctionnels. 4 animations.

Figures au format 470 x 470. Le tableau des sept fonctions est en une colonne :
les deux groupes sans C=O sont alors contigus, et l'encadrement des deux
familles se lit sans commentaire.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH6-02 : la table des sept fonctions, en une colonne ----------------
# Ordre choisi : d'abord les deux fonctions SANS C=O, puis les cinq qui en portent un.
FONC = [("alcool", "— OH"), ("amine", "— NH₂"),
        ("aldéhyde", "— CHO"), ("cétone", "— CO —"),
        ("acide carboxylique", "— COOH"), ("ester", "— COO —"),
        ("amide", "— CONH₂")]
SANS_CO = 2                                  # les deux premieres lignes
X0, Y0, TW, RH, GAP = 14, 46, 442, 50, 6
TAB = ""
for i, (nom, f) in enumerate(FONC):
    y = Y0 + i * RH
    TAB += ('<rect x="%d" y="%d" width="%d" height="%d" rx="9" fill="%s" stroke="%s" stroke-width="1.4"/>'
            % (X0, y, TW, RH - GAP, TINT, GREY))
    TAB += ('<text x="%d" y="%d" font-size="20" font-family="Be Vietnam Pro,Arial" fill="%s">%s</text>'
            % (X0 + 18, y + 30, INK2, nom))
    TAB += ('<text x="%d" y="%d" text-anchor="end" font-size="21" font-family="Be Vietnam Pro,Arial" '
            'fill="%s" font-weight="700">%s</text>' % (X0 + TW - 18, y + 30, DEEP, f))

def _cadre(i0, n, coul):
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="11" fill="none" stroke="%s" stroke-width="3"/>'
            % (X0 - 4, Y0 + i0 * RH - 4, TW + 8, n * RH - GAP + 8, coul))

CADRE_SANS = _cadre(0, SANS_CO, RED)
CADRE_AVEC = _cadre(SANS_CO, len(FONC) - SANS_CO, SFA)
Y_BAS = Y0 + len(FONC) * RH - GAP            # 46 + 350 - 6 = 390
assert Y_BAS == 390, Y_BAS

# ---------------- CH6-01 : la chaine carbonee ----------------
NC, XA, XB, YHAUT, YBAS = 7, 46, 424, 322, 368
PASC = (XB - XA) / (NC - 1)
_pts = [(XA + PASC * i, YBAS if i % 2 == 0 else YHAUT) for i in range(NC)]
CHAINE = "".join('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d"/>'
                 % (_pts[i][0], _pts[i][1], _pts[i + 1][0], _pts[i + 1][1]) for i in range(NC - 1))
ATOMES = "".join('<circle cx="%.1f" cy="%d" r="15"/>' % p for p in _pts)

SLIDES = """
  <!-- ==================== ANIM-CH6-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH6-01" data-title="Pourquoi le carbone fait quatre liaisons" data-sub="Et pourquoi lui seul construit des chaînes" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <circle cx="235" cy="104" r="40" fill="@@SFA@@"/>
            <text x="235" y="118" text-anchor="middle" font-size="36" @@FF@@ fill="#FFFFFF" font-weight="700">C</text>
            <text x="235" y="216" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">4 électrons de valence</text>
            <text x="235" y="244" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">il lui en faut 4 de plus</text>
          </g>
          <g class="step s2">
            <g stroke="@@DEEP@@" stroke-width="3.4" stroke-linecap="round">
              <line x1="235" y1="62" x2="235" y2="26"/>
              <line x1="235" y1="146" x2="235" y2="182"/>
              <line x1="193" y1="104" x2="122" y2="104"/>
              <line x1="277" y1="104" x2="348" y2="104"/>
            </g>
            <text x="235" y="282" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">4 liaisons, toujours</text>
          </g>
          <g class="step s3">
            <g stroke="@@DEEP@@" stroke-width="3.4" stroke-linecap="round">@@CHAINE@@</g>
            <g fill="@@SFA@@">@@ATOMES@@</g>
            <rect x="14" y="400" width="442" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="433" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">et il se lie à lui-même, indéfiniment</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Quatre électrons de valence</h3>
          <p style="font-size:17px">Le carbone est en colonne 14 : il en a quatre, il lui en faut quatre de plus pour atteindre l'octet. C'est la configuration de <b>CH2-A</b>, rien de neuf.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Donc quatre liaisons covalentes</h3>
          <p style="font-size:17px">Toujours quatre, sans exception. <b>C'est le contrôle de toute formule développée :</b> un carbone à trois ou cinq liaisons signale une erreur d'écriture.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et il se lie à lui-même</h3>
          <p style="font-size:17px">C'est le <b>seul</b> élément qui forme durablement de longues chaînes avec ses semblables. D'où les millions de composés organiques connus, contre quelques centaines de milliers d'inorganiques.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Trois formes de chaîne, trois types de liaison</h3>
          <p style="font-size:17px">Les chaînes peuvent être <b>linéaires</b>, <b>ramifiées</b> ou <b>cycliques</b> ; les liaisons entre carbones peuvent être <b>simples</b>, <b>doubles</b> ou <b>triples</b>.<br><br>Ces deux libertés combinées suffisent à expliquer l'immense diversité du vivant — et c'est pourquoi la chimie du carbone porte le nom de chimie <b>organique</b>.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le carbone a quatre électrons de valence. Il lui en faut quatre de plus.",
      "Il forme donc <b>quatre liaisons</b> covalentes, toujours — c'est le contrôle de toute formule.",
      "Et surtout : il se lie à lui-même, en chaînes aussi longues qu'on veut.",
      "Aucun autre élément ne fait cela durablement.",
      "<em>D'où le nom :</em> la chimie du carbone est la chimie du vivant."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH6-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH6-02" data-title="Les sept groupes fonctionnels" data-sub="Le tableau qui tient sur une page" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="235" y="28" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">les sept du programme, et pas un de plus</text>
            @@TAB@@
          </g>
          <g class="step s2">@@CADRE_SANS@@
            <text x="235" y="424" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">les deux sans C=O</text>
          </g>
          <g class="step s3">@@CADRE_AVEC@@
            <text x="235" y="452" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">les cinq avec un C=O, seul ou combiné</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Sept groupes, et c'est tout le programme</h3>
          <p style="font-size:17px">Le texte ARES en nomme sept : alcool, aldéhyde, cétone, acide carboxylique, ester, amine, amide. <b>Aucun autre n'est exigible.</b></p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une structure, pas une liste</h3>
          <p style="font-size:17px">Deux groupes n'ont <b>pas</b> de C=O : l'alcool et l'amine. Tous les autres en portent un, seul ou combiné à un O ou un N.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et cette structure guide la reconnaissance</h3>
          <p style="font-size:17px">Chercher d'abord le <b>C=O</b>, puis regarder ce qui l'entoure : c'est l'arbre de décision de la dernière animation, et il découle directement de ce classement.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi on classe ainsi, et pas par taille</h3>
          <p style="font-size:17px">Parce que <b>les propriétés suivent la fonction</b>, pas le nombre de carbones. Un alcool à deux carbones et un alcool à dix se comportent qualitativement pareil ; un alcool et une cétone de même taille, non.<br><br>C'est ce qui rend le classement utile : connaître la fonction, c'est connaître la polarité, la solubilité et le comportement de la molécule — sans rien savoir d'autre d'elle.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Sept groupes fonctionnels. Le programme n'en nomme pas un de plus.",
      "Deux n'ont pas de C=O : l'alcool et l'amine.",
      "Les cinq autres en portent un, seul ou combiné à un oxygène ou un azote.",
      "Ce classement n'est pas décoratif : c'est lui qui guidera la reconnaissance.",
      "<em>Et il vaut mieux qu'un classement par taille :</em> les propriétés suivent la fonction."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH6-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH6-03" data-title="Aldéhyde ou cétone : la position décide" data-sub="Le carbonyle en bout de chaîne, ou au milieu" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <text x="235" y="32" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">le même groupe C=O dans les deux cas</text>
            <line x1="14" y1="248" x2="456" y2="248" stroke="@@RULE@@" stroke-width="2"/>
          </g>
          <g class="step s2">
            <rect x="14" y="60" width="442" height="34" rx="9" fill="@@TINT@@"/>
            <text x="235" y="84" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">ALDÉHYDE · le C=O est en bout de chaîne</text>
            <g stroke="@@DEEP@@" stroke-width="3.4" stroke-linecap="round">
              <line x1="118" y1="150" x2="150" y2="150"/><line x1="218" y1="150" x2="252" y2="150"/>
            </g>
            <text x="80" y="158" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₃</text>
            <text x="184" y="158" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₂</text>
            <text x="270" y="158" text-anchor="middle" font-size="26" @@FF@@ fill="@@SFA@@" font-weight="700">C</text>
            <g stroke="@@SFA@@" stroke-width="3.4" stroke-linecap="round">
              <line x1="290" y1="143" x2="338" y2="143"/><line x1="290" y1="157" x2="338" y2="157"/>
            </g>
            <text x="360" y="158" text-anchor="middle" font-size="26" @@FF@@ fill="@@SFA@@" font-weight="700">O</text>
            <line x1="270" y1="170" x2="270" y2="190" stroke="@@DEEP@@" stroke-width="3.4" stroke-linecap="round"/>
            <text x="270" y="216" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">H</text>
          </g>
          <g class="step s3">
            <rect x="14" y="274" width="442" height="34" rx="9" fill="@@TINT@@"/>
            <text x="235" y="298" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">CÉTONE · le C=O est entre deux carbones</text>
            <text x="235" y="352" text-anchor="middle" font-size="26" @@FF@@ fill="@@SFA@@" font-weight="700">O</text>
            <g stroke="@@SFA@@" stroke-width="3.4" stroke-linecap="round">
              <line x1="229" y1="364" x2="229" y2="392"/><line x1="241" y1="364" x2="241" y2="392"/>
            </g>
            <g stroke="@@DEEP@@" stroke-width="3.4" stroke-linecap="round">
              <line x1="148" y1="410" x2="212" y2="410"/><line x1="258" y1="410" x2="322" y2="410"/>
            </g>
            <text x="110" y="418" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₃</text>
            <text x="235" y="418" text-anchor="middle" font-size="26" @@FF@@ fill="@@SFA@@" font-weight="700">C</text>
            <text x="360" y="418" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₃</text>
            <text x="235" y="458" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">une cétone demande donc au moins trois carbones</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'aldéhyde : le carbonyle est au bout</h3>
          <p style="font-size:17px">Son carbone porte donc encore un <b>hydrogène</b> — d'où l'écriture <b>CHO</b>, qui suffit à le reconnaître.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La cétone : il est entouré de carbones</h3>
          <p style="font-size:17px">Le carbonyle est <b>à l'intérieur</b> de la chaîne, entre deux carbones. Aucun hydrogène ne lui est lié.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une conséquence à connaître</h3>
          <p style="font-size:17px">Une cétone demande <b>au moins trois carbones</b>. Avec deux seulement, le carbonyle serait forcément en bout de chaîne — donc un aldéhyde. C'est un contrôle utile quand on cherche des isomères.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Même formule brute, deux molécules différentes</h3>
          <p style="font-size:17px">Le propanal et la propanone ont <b>tous deux</b> la formule C₃H₆O. Même nombre d'atomes, même masse molaire — et pourtant deux fonctions distinctes, donc deux comportements différents.<br><br>C'est une <b>isomérie de fonction</b>, et c'est la plus profonde des trois : ce n'est pas la forme du squelette qui change, c'est la nature chimique de la molécule.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le même groupe C=O — le carbonyle — dans les deux cas.",
      "S'il est en <b>bout</b> de chaîne, son carbone porte encore un hydrogène : c'est un <b>aldéhyde</b>.",
      "S'il est <b>entre deux carbones</b>, c'est une <b>cétone</b>.",
      "D'où une conséquence : une cétone demande au moins trois carbones.",
      "<em>Et les deux peuvent avoir la même formule brute :</em> c'est l'isomérie de fonction."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH6-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH6-04" data-title="Reconnaître une fonction sur une formule" data-sub="L'arbre de décision, en quatre questions" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <rect x="12" y="18" width="252" height="54" rx="12" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="138" y="52" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">1 · y a-t-il un azote ?</text>
            <line x1="138" y1="74" x2="138" y2="98" stroke="@@GREY@@" stroke-width="2.6"/>
            <line x1="268" y1="45" x2="288" y2="45" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="294" y="51" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">amine / amide</text>
          </g>
          <g class="step s2">
            <rect x="12" y="100" width="252" height="54" rx="12" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="138" y="134" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">2 · y a-t-il un C=O ?</text>
            <line x1="138" y1="156" x2="138" y2="180" stroke="@@GREY@@" stroke-width="2.6"/>
            <line x1="268" y1="127" x2="288" y2="127" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="294" y="121" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">non, mais un OH :</text>
            <text x="294" y="143" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">alcool</text>
          </g>
          <g class="step s3">
            <rect x="12" y="182" width="252" height="54" rx="12" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="138" y="216" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">3 · que porte le C=O ?</text>
            <line x1="138" y1="238" x2="138" y2="262" stroke="@@GREY@@" stroke-width="2.6"/>
            <line x1="268" y1="209" x2="288" y2="209" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="294" y="203" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">OH → acide</text>
            <text x="294" y="225" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">O—C → ester</text>
          </g>
          <g class="step s4">
            <rect x="12" y="264" width="252" height="54" rx="12" fill="@@SFA@@"/>
            <text x="138" y="298" text-anchor="middle" font-size="19" @@FF@@ fill="#FFFFFF" font-weight="700">4 · en bout ou au milieu ?</text>
            <line x1="268" y1="291" x2="288" y2="291" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="294" y="285" font-size="16" @@FF@@ fill="@@DEEP@@" font-weight="700">aldéhyde</text>
            <text x="294" y="307" font-size="16" @@FF@@ fill="@@DEEP@@" font-weight="700">ou cétone</text>
            <rect x="12" y="352" width="446" height="104" rx="14" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="386" text-anchor="middle" font-size="20" @@FF@@ fill="@@RED@@" font-weight="700">et on parcourt TOUTE la formule</text>
            <text x="235" y="420" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₃—CH(OH)—COOH</text>
            <text x="235" y="444" text-anchor="middle" font-size="16" @@FF@@ fill="#3F3F46">un alcool et un acide dans la même molécule</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Toujours dans cet ordre</h3>
          <p style="font-size:17px">L'azote d'abord, parce qu'il ne concerne que deux fonctions et les élimine immédiatement. Le C=O ensuite, parce qu'il partage le reste en deux.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Puis ce qui entoure le carbonyle</h3>
          <p style="font-size:17px">Un <b>OH</b> accroché au C=O → acide carboxylique. Un <b>O relié à un autre carbone</b> → ester. Sinon, il reste les deux derniers cas.</p></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et la position tranche</h3>
          <p style="font-size:17px">En bout de chaîne → <b>aldéhyde</b>. Entre deux carbones → <b>cétone</b>. Quatre questions, sept fonctions, aucune hésitation possible.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège : s'arrêter à la première</h3>
          <p style="font-size:17px">Une molécule peut porter <b>plusieurs</b> fonctions. L'acide lactique, CH₃—CH(OH)—COOH, en porte deux : un alcool sur le carbone central, un acide carboxylique au bout.<br><br>On parcourt donc <b>toute</b> la formule, jamais seulement son début — et le contrôle des quatre liaisons par carbone valide au passage l'écriture entière.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Première question : y a-t-il un azote ? Si oui, il ne reste que deux possibilités.",
      "Deuxième : y a-t-il un C=O ? Si non et qu'il y a un OH, c'est un alcool.",
      "Troisième : que porte ce C=O ? Un OH donne un acide, un O—C donne un ester.",
      "Quatrième : est-il en bout de chaîne, ou au milieu ? Aldéhyde, ou cétone.",
      "<em>Et le piège :</em> une molécule peut porter plusieurs fonctions. On lit tout."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "TAB": TAB, "CADRE_SANS": CADRE_SANS, "CADRE_AVEC": CADRE_AVEC,
    "CHAINE": CHAINE, "ATOMES": ATOMES,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED, "RULE": "#E3E7EE",
})

print("table des fonctions : %d lignes, bas = %d · chaine : %d carbones" % (len(FONC), Y_BAS, NC))
print("ok", make("CH6-A", "Capsule CH6-A — Le carbone et les groupes fonctionnels · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH6A.html")))
