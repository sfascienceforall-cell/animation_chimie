# -*- coding: utf-8 -*-
"""CH8-B — Equilibrer et predire avec la table. 4 animations.

Figures au format 470 x 470, palette verte. L'echelle des potentiels est
calculee ; une assertion verifie que deux reperes ne peuvent pas se toucher.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH8-06 : la table des potentiels et le gamma ----------------
COUPLES = [("MnO₄⁻", "Mn²⁺", "1,51"), ("Fe³⁺", "Fe²⁺", "0,77"),
           ("H⁺", "H₂", "0,00"), ("Zn²⁺", "Zn", "−0,76")]
EXX, EXW = 6, 48                       # colonne des potentiels
OXX, OXW = 60, 166                     # colonne des oxydants
RDX, RDW = 258, 190                    # colonne des reducteurs
TY0, TH_, TPAS = 64, 46, 54
TABLE = ""
for i, (ox, red, e) in enumerate(COUPLES):
    y = TY0 + i * TPAS
    TABLE += ('<text x="%d" y="%d" text-anchor="middle" font-size="15" '
              'font-family="Be Vietnam Pro,Arial" fill="%s">%s</text>'
              % (EXX + EXW // 2, y + 29, GREY, e))
    for x, w, txt, fond in ((OXX, OXW, ox, TINT), (RDX, RDW, red, "#FFFFFF")):
        TABLE += ('<rect x="%d" y="%d" width="%d" height="%d" rx="9" fill="%s" stroke="%s" '
                  'stroke-width="1.6"/>' % (x, y, w, TH_, fond, GREY))
        TABLE += ('<text x="%d" y="%d" text-anchor="middle" font-size="21" '
                  'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
                  % (x + w // 2, y + 31, DEEP, txt))


def centre(i):
    return TY0 + i * TPAS + TH_ / 2


Y1, Y2 = centre(0), centre(1)
GAMMA = ('<path d="M %d,%.1f L 242,%.1f L 242,%.1f L %d,%.1f" fill="none" stroke="%s" '
         'stroke-width="4" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#v2)"/>'
         % (OXX + OXW, Y1, Y1, Y2, RDX - 4, Y2, SFA))
assert OXX + OXW < 242 < RDX, "le coude du gamma doit tomber entre les deux colonnes"
assert TY0 + 3 * TPAS + TH_ == 272

# ---------------- CH8-07 : l'echelle des potentiels ----------------
AXE_X, E_MIN, E_MAX, Y_BAS, Y_HAUT = 150, -1.0, 1.6, 380, 58
METAUX = [("MnO₄⁻ / Mn²⁺", 1.51, RED), ("Ag⁺ / Ag", 0.80, DEEP), ("Cu²⁺ / Cu", 0.34, DEEP),
          ("H⁺ / H₂", 0.00, SFA), ("Fe²⁺ / Fe", -0.44, DEEP), ("Zn²⁺ / Zn", -0.76, DEEP)]


def ye(e):
    return Y_BAS - (e - E_MIN) / (E_MAX - E_MIN) * (Y_BAS - Y_HAUT)


ECHELLE = ""
for nom, e, coul in METAUX:
    y = ye(e)
    ECHELLE += ('<circle cx="%d" cy="%.1f" r="8" fill="%s"/>' % (AXE_X, y, coul))
    ECHELLE += ('<text x="%d" y="%.1f" font-size="17" font-family="Be Vietnam Pro,Arial" fill="%s" '
                'font-weight="700">%s</text>' % (AXE_X + 18, y + 6, coul, nom))
    ECHELLE += ('<text x="%d" y="%.1f" text-anchor="end" font-size="15" '
                'font-family="Be Vietnam Pro,Arial" fill="%s">%s V</text>'
                % (AXE_X - 16, y + 5, INK2, ("%+.2f" % e).replace(".", ",").replace("+", "+ ")
                   .replace("-", "− ")))
_ys = sorted(ye(e) for _, e, _ in METAUX)
assert min(_ys[i + 1] - _ys[i] for i in range(len(_ys) - 1)) > 24, _ys
Y_REF = ye(0.0)

SLIDES = """
  <!-- ==================== ANIM-CH8-05 ==================== -->
  <section class="slide" data-ref="ANIM-CH8-05" data-title="Assembler deux demi-équations" data-sub="Le plus petit multiple commun des électrons" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <text x="16" y="38" font-size="16" @@FF@@ fill="@@GREY@@">réduction · 5 électrons captés</text>
            <text x="235" y="76" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">MnO₄⁻ + 8 H⁺ + 5 e⁻ → Mn²⁺ + 4 H₂O</text>
          </g>
          <g class="step s2">
            <text x="16" y="124" font-size="16" @@FF@@ fill="@@GREY@@">oxydation · 1 électron cédé</text>
            <text x="235" y="162" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">Fe²⁺ → Fe³⁺ + e⁻</text>
            <text x="235" y="206" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">ppcm(5 ; 1) = 5 → on multiplie la seconde par 5</text>
          </g>
          <g class="step s3">
            <line x1="34" y1="226" x2="436" y2="226" stroke="@@DEEP@@" stroke-width="2.4"/>
            <rect x="18" y="240" width="434" height="92" rx="14" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="235" y="280" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">MnO₄⁻ + 8 H⁺ + 5 Fe²⁺</text>
            <text x="235" y="316" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">→ Mn²⁺ + 4 H₂O + 5 Fe³⁺</text>
          </g>
          <g class="step s4">
            <rect x="10" y="348" width="450" height="110" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="235" y="380" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">aucun électron ne subsiste ✓</text>
            <text x="235" y="412" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">charges : + 17 à gauche · + 17 à droite ✓</text>
            <text x="235" y="442" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">atomes : Mn 1 · O 4 · H 8 · Fe 5 ✓</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le principe, et il est exact</h3>
          <p style="font-size:17px">Les électrons cédés par le réducteur sont <b>exactement</b> ceux que capte l'oxydant. Il n'en reste donc aucun dans l'équation finale.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La méthode</h3>
          <p style="font-size:17px">On cherche le <b>plus petit multiple commun</b> des nombres d'électrons, on multiplie chaque demi-équation pour l'atteindre, puis on additionne.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un détail de convention à ne pas oublier</h3>
          <p style="font-size:17px">Une demi-équation s'écrit toujours dans le sens de la <b>réduction</b>. Celle du réducteur doit donc être <b>inversée</b> avant l'addition.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le contrôle immédiat, et pourquoi il suffit</h3>
          <p style="font-size:17px">S'il reste des électrons dans l'équation finale, les coefficients sont faux — sans exception. C'est le contrôle le plus rapide du chapitre.<br><br>Et il se double du contrôle des charges : + 17 de chaque côté ici. Deux vérifications, dix secondes, et l'équation entière est validée.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "La demi-équation de réduction capte cinq électrons.",
      "Celle d'oxydation n'en cède qu'un : il faut les mettre au même nombre.",
      "Le plus petit multiple commun vaut 5 : on multiplie la seconde par cinq.",
      "On additionne, et <b>les électrons disparaissent</b>.",
      "<em>Et c'est le contrôle :</em> s'il en reste, les coefficients sont faux."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH8-06 ==================== -->
  <section class="slide" data-ref="ANIM-CH8-06" data-title="La règle du gamma, deuxième application" data-sub="Exactement la même figure qu'en CH7" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="30" y="44" text-anchor="middle" font-size="15" @@FF@@ fill="@@GREY@@">E° (V)</text>
            <text x="143" y="44" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">OXYDANTS</text>
            <text x="353" y="44" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">RÉDUCTEURS</text>
            @@TAB@@
            <line x1="459" y1="266" x2="459" y2="80" stroke="@@GREY@@" stroke-width="3" marker-end="url(#d2)"/>
          </g>
          <g class="step s2">@@GAM@@</g>
          <g class="step s3">
            <rect x="10" y="286" width="450" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="318" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">oxydant fort + réducteur fort → la réaction a lieu</text>
          </g>
          <g class="step s4">
            <rect x="10" y="348" width="450" height="52" rx="12" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="380" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">tracé inversé → pas de réaction</text>
            <rect x="10" y="410" width="450" height="48" rx="12" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.2"/>
            <text x="235" y="440" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">c'est la figure de CH7-B, sur une autre table</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Comment la table est rangée</h3>
          <p style="font-size:17px">Par <b>potentiel standard croissant</b> : les oxydants les plus forts en haut, leurs réducteurs conjugués — donc les plus faibles — en face.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La règle, mot pour mot celle de CH7</h3>
          <p style="font-size:17px">L'oxydant le plus fort réagit avec le réducteur le plus fort. Le tracé entre les deux dessine un <b>gamma</b>, et la réaction a lieu.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et le tracé inversé dit l'inverse</h3>
          <p style="font-size:17px">Si le tracé ne forme pas un gamma, la réaction <b>ne se produit pas spontanément</b>. Un seul coup d'œil suffit à trancher.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">À dire explicitement, et à ne surtout pas réexpliquer</h3>
          <p style="font-size:17px">Ce n'est pas une nouvelle méthode : c'est <b>la même figure</b> qu'en CH7-B, appliquée à une autre table. Le professeur le dit en une phrase et passe à la suite.<br><br>Réexpliquer la construction reviendrait à suggérer qu'il y a deux choses à apprendre. Il n'y en a qu'une, et elle sert deux fois.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "La table des potentiels : les oxydants les plus forts en haut.",
      "On relie l'oxydant qui réagit au réducteur qui réagit.",
      "Le tracé dessine un gamma : la réaction a lieu.",
      "Tracé inversé : elle ne se produit pas spontanément.",
      "<em>C'est la figure de CH7-B, à l'identique</em> — une construction, deux chapitres."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH8-07 ==================== -->
  <section class="slide" data-ref="ANIM-CH8-07" data-title="Prédire si une réaction a lieu" data-sub="Le couple H⁺/H₂ comme référence, et ce qu'il sépare" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <line x1="@@AX@@" y1="44" x2="@@AX@@" y2="392" stroke="@@GREY@@" stroke-width="2"/>
            <text x="26" y="42" font-size="16" @@FF@@ fill="@@GREY@@">E° croissant vers le haut</text>
            @@ECH@@
          </g>
          <g class="step s2">
            <line x1="26" y1="@@YREF@@" x2="66" y2="@@YREF@@" stroke="@@SFA@@" stroke-width="2.4" stroke-dasharray="7 5"/><line x1="262" y1="@@YREF@@" x2="454" y2="@@YREF@@" stroke="@@SFA@@" stroke-width="2.4" stroke-dasharray="7 5"/>
          </g>
          <g class="step s3">
            <text x="452" y="100" text-anchor="end" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">non attaqués par les acides</text>
            <text x="452" y="404" text-anchor="end" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">attaqués par les acides</text>
          </g>
          <g class="step s4">
            <rect x="10" y="420" width="450" height="44" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="449" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">potentiel plus grand = oxydant plus fort</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La règle chiffrée</h3>
          <p style="font-size:17px">Une réaction est spontanée si le potentiel de l'<b>oxydant</b> est <b>supérieur</b> à celui du réducteur mis en jeu. C'est la règle du gamma, exprimée en nombres.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une seule valeur à situer</h3>
          <p style="font-size:17px">Le couple <b>H⁺/H₂</b> sert de référence, à <b>0 V</b>. Au-dessus, les oxydants forts ; en dessous, les réducteurs forts. Les autres valeurs sont fournies.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'application classique</h3>
          <p style="font-size:17px">Un métal dont le potentiel est <b>inférieur</b> à celui de H⁺/H₂ est attaqué par les acides. C'est le cas du zinc et du fer — pas du cuivre, ni de l'argent.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi cette lecture vaut mieux qu'une liste</h3>
          <p style="font-size:17px">« Quels métaux sont attaqués par les acides ? » est une question qu'on peut apprendre par cœur — ou <b>lire sur la table</b> en trois secondes.<br><br>La table est fournie au concours. Ce qui est évalué n'est jamais de connaître les potentiels : c'est de savoir <b>où passe la ligne du zéro</b>, et de quel côté se trouve l'espèce qu'on vous donne.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Une échelle verticale de potentiels : les oxydants les plus forts en haut.",
      "Le couple H⁺/H₂ est à zéro — c'est la référence de toute l'échelle.",
      "Au-dessus de cette ligne, les métaux ne sont pas attaqués par les acides.",
      "En dessous, ils le sont : c'est le cas du fer et du zinc.",
      "<em>Rien de tout cela ne s'apprend :</em> la table est fournie, il faut savoir la lire."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH8-08 ==================== -->
  <section class="slide" data-ref="ANIM-CH8-08" data-title="Le contrôle final en trois vérifications" data-sub="Atomes, charges, électrons" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <rect x="12" y="26" width="446" height="96" rx="13" fill="@@TINT@@" stroke="@@GREY@@" stroke-width="1.6"/>
            <text x="235" y="62" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">1 · les atomes</text>
            <text x="235" y="98" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">Mn 1/1 · O 4/4 · H 8/8 · Fe 5/5 ✓</text>
          </g>
          <g class="step s2">
            <rect x="12" y="136" width="446" height="96" rx="13" fill="@@TINT@@" stroke="@@GREY@@" stroke-width="1.6"/>
            <text x="235" y="172" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">2 · les charges</text>
            <text x="235" y="208" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">(−1) + 8 + 10 = + 17 &nbsp;·&nbsp; (+2) + 15 = + 17 ✓</text>
          </g>
          <g class="step s3">
            <rect x="12" y="246" width="446" height="96" rx="13" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="2.2"/>
            <text x="235" y="282" text-anchor="middle" font-size="21" @@FF@@ fill="@@DEEP@@" font-weight="700">3 · les électrons</text>
            <text x="235" y="318" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">aucun ne subsiste dans l'équation finale ✓</text>
          </g>
          <g class="step s4">
            <rect x="10" y="368" width="450" height="90" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.6"/>
            <text x="235" y="402" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">quinze secondes de vérification</text>
            <text x="235" y="436" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">et toutes les erreurs de coefficient sont attrapées</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les atomes</h3>
          <p style="font-size:17px">Chaque élément doit apparaître en <b>nombre égal</b> des deux côtés. On les compte dans l'ordre de l'équation, sans en sauter un.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les charges</h3>
          <p style="font-size:17px">La <b>somme algébrique</b> des charges doit être la même de part et d'autre. Elle n'a pas à être nulle — seulement identique.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les électrons</h3>
          <p style="font-size:17px">Il ne doit plus en rester <b>aucun</b>. Un électron qui subsiste signale que les deux demi-équations n'ont pas été mises au même nombre.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi ces trois contrôles sont obligatoires, pas facultatifs</h3>
          <p style="font-size:17px">Une erreur de coefficient ne se voit pas à la relecture : l'équation reste plausible. Elle ne se voit qu'au <b>recomptage</b>.<br><br>Quinze secondes, et l'on récupère un point que la moitié de la salle perdra. Sur un concours à −1/3 par erreur, c'est le meilleur rapport entre le temps investi et les points gagnés de tout le programme de chimie.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Premier contrôle : chaque élément, en nombre égal des deux côtés.",
      "Deuxième : la somme des charges, identique de part et d'autre.",
      "Troisième : plus aucun électron dans l'équation finale.",
      "Quinze secondes, et toutes les erreurs de coefficient sont attrapées.",
      "<em>Ce n'est pas facultatif :</em> une erreur de coefficient ne se voit qu'au recomptage."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "TAB": TABLE, "GAM": GAMMA, "ECH": ECHELLE,
    "AX": str(AXE_X), "AXT": str(AXE_X - 16), "YREF": "%.1f" % Y_REF,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH8-B : gamma %.0f -> %.0f · reference 0 V a y = %.1f · ecart minimal des reperes %.1f px"
      % (Y1, Y2, Y_REF, min(_ys[i + 1] - _ys[i] for i in range(len(_ys) - 1))))
print("ok", make("CH8-B", "Capsule CH8-B — Équilibrer et prédire avec la table · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH8B.html")))
