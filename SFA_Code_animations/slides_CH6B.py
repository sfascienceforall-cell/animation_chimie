# -*- coding: utf-8 -*-
"""CH6-B — Nommer, et l'isomerie. 4 animations.

Figures au format 470 x 470, palette verte.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH6-05 : les quatre etapes ----------------
ETAPES = [("1 · la chaîne principale", "la plus longue qui contient la fonction"),
          ("2 · la numérotation", "du côté qui donne le plus petit indice"),
          ("3 · les substituants", "nommés avec leur position : méthyl, éthyl"),
          ("4 · le suffixe", "-ol · -al · -one · -oïque")]
EX, EW, EH, EY0, EGAP = 12, 446, 58, 152, 62


def etape(i):
    t1, t2 = ETAPES[i]
    y = EY0 + i * EGAP
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="11" fill="%s" stroke="%s" stroke-width="1.6"/>'
            '<text x="%d" y="%d" font-size="18" font-family="Be Vietnam Pro,Arial" fill="%s" '
            'font-weight="700">%s</text>'
            '<text x="%d" y="%d" font-size="15" font-family="Be Vietnam Pro,Arial" fill="#3F3F46">%s</text>'
            % (EX, y, EW, EH, TINT, GREY, EX + 18, y + 24, DEEP, t1, EX + 18, y + 46, t2))


ETAPE = [etape(i) for i in range(4)]
assert EY0 + 3 * EGAP + EH == 396

# ---------------- CH6-06 : la chaine numerotee dans les deux sens ----------------
CXS = [70, 175, 280, 385]
CY, CR = 130, 26
CHAINE = "".join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="3.4"/>'
                 % (CXS[i] + CR, CY, CXS[i + 1] - CR, CY, DEEP) for i in range(3))
CARBONES = "".join('<circle cx="%d" cy="%d" r="%d" fill="%s"/>'
                   '<text x="%d" y="%d" text-anchor="middle" font-size="20" '
                   'font-family="Be Vietnam Pro,Arial" fill="#FFFFFF" font-weight="700">C</text>'
                   % (x, CY, CR, SFA, x, CY + 7) for x in CXS)
NUM_HAUT = "".join('<text x="%d" y="72" text-anchor="middle" font-size="22" '
                   'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%d</text>'
                   % (x, SFA, i + 1) for i, x in enumerate(CXS))
NUM_BAS = "".join('<text x="%d" y="286" text-anchor="middle" font-size="22" '
                  'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%d</text>'
                  % (x, RED, 4 - i) for i, x in enumerate(CXS))

# ---------------- CH6-07 : solubilite et longueur de chaine ----------------
ALCOOLS = [("éthanol · 2 carbones", 2, "totalement miscible à l'eau", SFA),
           ("butan-1-ol · 4 carbones", 4, "partiellement soluble", DEEP),
           ("décan-1-ol · 10 carbones", 10, "pratiquement insoluble", RED)]
TX0, TU, TH = 86, 27, 26                  # origine de la queue, pas par carbone, epaisseur
BARRES = ""
for i, (nom, n, verdict, coul) in enumerate(ALCOOLS):
    y = 96 + i * 92
    lg = n * TU
    assert TX0 + lg <= 456, (nom, TX0 + lg)
    BARRES += ('<text x="16" y="%d" font-size="17" font-family="Be Vietnam Pro,Arial" fill="%s" '
               'font-weight="700">%s</text>' % (y - 18, DEEP, nom))
    BARRES += ('<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="#C8CDD6"/>'
               % (TX0, y - TH // 2, lg, TH, TH // 2))
    BARRES += ('<circle cx="46" cy="%d" r="22" fill="%s"/>'
               '<text x="46" y="%d" text-anchor="middle" font-size="15" '
               'font-family="Be Vietnam Pro,Arial" fill="#FFFFFF" font-weight="700">OH</text>'
               % (y, SFA, y + 6))
    BARRES += ('<text x="16" y="%d" font-size="16" font-family="Be Vietnam Pro,Arial" fill="%s" '
               'font-weight="700">%s</text>' % (y + 36, coul, verdict))

# ---------------- CH6-08 : les deux isomeres de C4H10 ----------------
def zigzag(xs, ys):
    seg = "".join('<line x1="%d" y1="%d" x2="%d" y2="%d"/>' % (xs[i], ys[i], xs[i + 1], ys[i + 1])
                  for i in range(len(xs) - 1))
    bil = "".join('<circle cx="%d" cy="%d" r="13"/>' % (x, y) for x, y in zip(xs, ys))
    return ('<g stroke="%s" stroke-width="3.4" stroke-linecap="round">%s</g><g fill="%s">%s</g>'
            % (DEEP, seg, SFA, bil))


LINEAIRE = zigzag([110, 180, 250, 320], [128, 96, 128, 96])
RAMIFIE = zigzag([130, 200, 270], [276, 244, 276]) + zigzag([200, 200], [244, 186])

SLIDES = """
  <!-- ==================== ANIM-CH6-05 ==================== -->
  <section class="slide" data-ref="ANIM-CH6-05" data-title="Nommer en quatre étapes" data-sub="Chaîne principale, numérotation, substituants, suffixe" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <g stroke="@@DEEP@@" stroke-width="3.4" stroke-linecap="round">
              <line x1="96" y1="62" x2="136" y2="62"/><line x1="186" y1="62" x2="224" y2="62"/>
              <line x1="296" y1="62" x2="336" y2="62"/>
            </g>
            <text x="62" y="70" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₃</text>
            <text x="162" y="70" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">CH</text>
            <text x="262" y="70" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₂</text>
            <text x="372" y="70" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₃</text>
            <line x1="162" y1="80" x2="162" y2="102" stroke="@@SFA@@" stroke-width="3.4" stroke-linecap="round"/>
            <text x="162" y="130" text-anchor="middle" font-size="24" @@FF@@ fill="@@SFA@@" font-weight="700">OH</text>
          </g>
          <g class="step s1">@@E0@@</g>
          <g class="step s2">@@E1@@</g>
          <g class="step s3">@@E2@@</g>
          <g class="step s4">@@E3@@
            <rect x="12" y="406" width="446" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="440" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">butan-2-ol</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Nommer n'est pas mémoriser</h3>
          <p style="font-size:17px">C'est un <b>algorithme</b> en quatre étapes, toujours les mêmes, toujours dans cet ordre. Aucune exception n'est au programme.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le radical vient du compte de carbones</h3>
          <p style="font-size:17px">méth (1) · éth (2) · prop (3) · but (4) · pent (5) · hex (6). C'est la seule liste à connaître de tout le chapitre.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège de la chaîne principale</h3>
          <p style="font-size:17px">Ce n'est pas la plus longue <b>en apparence</b> : c'est la plus longue qui <b>contient la fonction</b>. Une chaîne plus longue qui ne la contient pas n'est pas la principale.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que le concours teste réellement</h3>
          <p style="font-size:17px">Le squelette proposé est presque toujours simple — quatre ou cinq carbones. Ce qui départage les réponses, c'est le <b>sens de numérotation</b>.<br><br>C'est donc là qu'il faut ralentir, et nulle part ailleurs. Les trois autres étapes se font en lisant.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Une molécule à nommer, et quatre étapes pour y arriver.",
      "D'abord la chaîne principale : la plus longue <b>qui contient la fonction</b>.",
      "Puis la numérotation, puis les substituants s'il y en a.",
      "Enfin le suffixe, qui dit la fonction : <b>-ol</b> pour un alcool.",
      "<em>Et le nom tombe :</em> butan-2-ol, sans avoir rien mémorisé."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH6-06 ==================== -->
  <section class="slide" data-ref="ANIM-CH6-06" data-title="La numérotation qui décide du nom" data-sub="On numérote toujours du côté qui donne le plus petit indice" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">@@CHAINE@@@@CARBONES@@
            <line x1="175" y1="156" x2="175" y2="186" stroke="@@SFA@@" stroke-width="3.4" stroke-linecap="round"/>
            <text x="175" y="214" text-anchor="middle" font-size="24" @@FF@@ fill="@@SFA@@" font-weight="700">OH</text>
          </g>
          <g class="step s2">@@NH@@
            <text x="235" y="42" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">de gauche à droite : le OH est en 2</text>
          </g>
          <g class="step s3">@@NB@@
            <text x="235" y="322" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">de droite à gauche : le OH serait en 3</text>
          </g>
          <g class="step s4">
            <rect x="12" y="348" width="446" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="382" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">butan-2-ol</text>
            <text x="235" y="430" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">on essaie les deux sens, on garde le plus petit</text>
            <text x="235" y="456" text-anchor="middle" font-size="16" @@FF@@ fill="@@RED@@" font-weight="700">le QCM propose toujours l'autre comme leurre</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La fonction est prioritaire</h3>
          <p style="font-size:17px">C'est elle, et pas un substituant, qui doit recevoir le <b>plus petit indice possible</b>. Cette priorité règle à elle seule la majorité des exercices.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">S'il n'y a pas de fonction</h3>
          <p style="font-size:17px">Pour un simple alcane ramifié, c'est le <b>substituant</b> qui prend le plus petit indice. Et en cas d'égalité, on compare les indices suivants un à un.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La vérification à imposer</h3>
          <p style="font-size:17px">On numérote dans les <b>deux</b> sens, on compare, on garde le plus petit. Dix secondes de travail, et l'erreur devient impossible.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi cette étape mérite qu'on s'y arrête</h3>
          <p style="font-size:17px">Un QCM propose presque toujours les <b>deux</b> numérotations parmi ses réponses. Le candidat qui n'en essaie qu'une a donc une chance sur deux de tomber sur le leurre.<br><br>C'est la seule étape du chapitre où une seconde d'inattention coûte un point entier — et un tiers de point de pénalité en plus.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "La même molécule, et la question du sens de numérotation.",
      "De gauche à droite, le groupe OH porte l'indice <b>2</b>.",
      "De droite à gauche, il porterait l'indice <b>3</b>.",
      "On garde le plus petit : la molécule s'appelle <b>butan-2-ol</b>.",
      "<em>Et c'est bien le leurre du QCM :</em> « butan-3-ol » y figure presque toujours."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH6-07 ==================== -->
  <section class="slide" data-ref="ANIM-CH6-07" data-title="Les propriétés se lisent dans la fonction" data-sub="Polarité, solubilité, point d'ébullition" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <text x="16" y="34" font-size="18" @@FF@@ fill="@@GREY@@">la même fonction, des chaînes de plus en plus longues</text>
            @@BARRES@@
          </g>
          <g class="step s2">
            <rect x="12" y="356" width="446" height="46" rx="11" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.2"/>
            <text x="235" y="385" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">tête polaire, queue apolaire : tout est dans le rapport</text>
          </g>
          <g class="step s3">
            <rect x="12" y="412" width="446" height="46" rx="11" fill="@@TINT2@@"/>
            <text x="235" y="441" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">liaison hydrogène possible → ébullition plus haute</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Deux parties, deux comportements</h3>
          <p style="font-size:17px">La <b>chaîne carbonée</b> est apolaire : elle fuit l'eau. Le <b>groupe fonctionnel</b> contenant O ou N est polaire : il l'attire.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La solubilité est un rapport de forces</h3>
          <p style="font-size:17px">L'éthanol, deux carbones, est <b>totalement miscible</b> à l'eau. Un alcool à dix carbones ne l'est plus du tout : la queue apolaire l'emporte.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et l'ébullition suit la même logique</h3>
          <p style="font-size:17px">Alcool, acide carboxylique et amine peuvent former des <b>liaisons hydrogène</b> : leurs points d'ébullition sont nettement plus élevés. C'est le mécanisme de CH3, appliqué.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que ce raisonnement permet de ne plus apprendre</h3>
          <p style="font-size:17px">Aucune de ces propriétés n'est une donnée à retenir : elles se <b>déduisent</b> toutes de la fonction et de la longueur de chaîne.<br><br>Et un acide carboxylique porte, comme son nom l'indique, un caractère <b>acide</b> : il cède l'hydrogène de son COOH. C'est le pont direct avec le chapitre CH7, qui commence là.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Trois alcools : même fonction, des chaînes de deux à dix carbones.",
      "La tête OH attire l'eau ; la queue carbonée la fuit.",
      "Deux carbones : la tête l'emporte, c'est miscible. Dix : la queue l'emporte.",
      "Et les fonctions à liaison hydrogène bouillent nettement plus haut.",
      "<em>Rien de tout cela ne s'apprend :</em> tout se déduit de la fonction."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH6-08 ==================== -->
  <section class="slide" data-ref="ANIM-CH6-08" data-title="Même formule brute, molécules différentes" data-sub="L'isomérie de constitution, en trois familles" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <text x="235" y="38" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">C₄H₁₀</text>
            @@LIN@@
            <text x="235" y="176" text-anchor="middle" font-size="21" @@FF@@ fill="@@SFA@@" font-weight="700">butane</text>
          </g>
          <g class="step s2">@@RAM@@
            <text x="235" y="322" text-anchor="middle" font-size="21" @@FF@@ fill="@@SFA@@" font-weight="700">2-méthylpropane</text>
          </g>
          <g class="step s3">
            <rect x="12" y="344" width="446" height="114" rx="13" fill="@@TINT@@" stroke="@@GREY@@" stroke-width="1.6"/>
            <text x="30" y="376" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">de chaîne — le squelette se ramifie</text>
            <text x="30" y="408" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">de position — la fonction se déplace</text>
            <text x="30" y="440" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">de fonction — la fonction elle-même change</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Des isomères, c'est quoi exactement</h3>
          <p style="font-size:17px">Même <b>formule brute</b>, structures différentes — donc propriétés différentes. Le compte d'atomes ne suffit jamais à identifier une molécule.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">C₄H₁₀ n'en admet que deux</h3>
          <p style="font-size:17px">La chaîne linéaire donne le <b>butane</b>. Une chaîne de trois carbones avec un méthyl donne le <b>2-méthylpropane</b>. Une chaîne de deux est impossible.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Trois familles, et une seule est profonde</h3>
          <p style="font-size:17px">Chaîne et position ne changent que la forme. L'isomérie de <b>fonction</b>, elle, change la nature chimique — c'est le propanal et la propanone de CH6-A.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La méthode de dénombrement, pour n'en oublier aucun</h3>
          <p style="font-size:17px">On part de la <b>chaîne la plus longue</b>, on la raccourcit d'un carbone, on place la ramification de toutes les façons possibles, et on s'arrête quand la chaîne devient trop courte pour porter le reste.<br><br>Procéder ainsi est ce qui distingue un dénombrement complet d'une énumération au hasard — et le QCM compte toujours sur la seconde.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Une formule brute, C₄H₁₀, et la question : combien de molécules différentes ?",
      "La chaîne linéaire donne le <b>butane</b>.",
      "En raccourcissant d'un carbone et en le mettant en ramification : le <b>2-méthylpropane</b>.",
      "Il n'y en a que deux — et c'est une isomérie <b>de chaîne</b>.",
      "<em>Trois familles existent</em>, et celle de fonction est la plus profonde des trois."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "E0": ETAPE[0], "E1": ETAPE[1], "E2": ETAPE[2], "E3": ETAPE[3],
    "CHAINE": CHAINE, "CARBONES": CARBONES, "NH": NUM_HAUT, "NB": NUM_BAS,
    "BARRES": BARRES, "LIN": LINEAIRE, "RAM": RAMIFIE,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH6-B : 4 etapes, chaine de %d carbones, %d alcools, 2 isomeres"
      % (len(CXS), len(ALCOOLS)))
print("ok", make("CH6-B", "Capsule CH6-B — Nommer, et l'isomérie · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH6B.html")))
