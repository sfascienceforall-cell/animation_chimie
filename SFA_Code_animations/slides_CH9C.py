# -*- coding: utf-8 -*-
"""CH9-C — Taux de conversion, rendement, et calcul sans calculatrice. 4 animations.

Figures au format 470 x 470, palette verte.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH9-10 : l'echelle des rendements ----------------
RX0, RX1, RY, RMAX = 26, 444, 190, 125.0        # l'echelle va de 0 a 125 %


def xr(p):
    return RX0 + p / RMAX * (RX1 - RX0)


X_CENT = xr(100.0)
assert abs(X_CENT - 360.4) < 0.5, X_CENT
JAUGE = ('<rect x="%d" y="%d" width="%.1f" height="56" rx="10" fill="%s" opacity="0.85"/>'
         '<rect x="%.1f" y="%d" width="%.1f" height="56" rx="10" fill="%s" opacity="0.28"/>'
         '<rect x="%d" y="%d" width="%d" height="56" rx="10" fill="none" stroke="%s" stroke-width="2.4"/>'
         % (RX0, RY, X_CENT - RX0, SFA,
            X_CENT, RY, RX1 - X_CENT, RED,
            RX0, RY, RX1 - RX0, DEEP))
GRAD = ""
for p in (0, 25, 50, 75, 100):
    x = xr(p)
    GRAD += ('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.8"/>'
             % (x, RY + 56, x, RY + 66, GREY))
    GRAD += ('<text x="%.1f" y="%d" text-anchor="middle" font-size="15" '
             'font-family="Be Vietnam Pro,Arial" fill="%s">%d %%</text>' % (x, RY + 88, INK2, p))

# ---------------- CH9-11 : les masses molaires arrondies ----------------
MASSES = [("H", "1"), ("C", "12"), ("N", "14"), ("O", "16"),
          ("Na", "23"), ("S", "32"), ("Cl", "35,5"), ("Ca", "40")]
PW, PH_, PX0, PY0, PGAP = 54, 76, 12, 76, 56
PUCES = ""
for i, (sym, m) in enumerate(MASSES):
    x = PX0 + i * PGAP
    PUCES += ('<rect x="%d" y="%d" width="%d" height="%d" rx="11" fill="%s" stroke="%s" '
              'stroke-width="1.6"/>' % (x, PY0, PW, PH_, TINT, GREY))
    PUCES += ('<text x="%d" y="%d" text-anchor="middle" font-size="21" '
              'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
              % (x + PW // 2, PY0 + 32, DEEP, sym))
    PUCES += ('<text x="%d" y="%d" text-anchor="middle" font-size="%d" '
              'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
              % (x + PW // 2, PY0 + 62, 17 if len(m) > 2 else 20, SFA, m))
assert PX0 + (len(MASSES) - 1) * PGAP + PW == 458

# ---------------- CH9-12 : les trois ordres de grandeur ----------------
REPERES = [("1 mole de gaz", "une vingtaine de litres"),
           ("une masse molaire usuelle", "entre 1 et 300 g/mol"),
           ("une concentration courante", "entre 10⁻³ et 10 mol/L")]
OY0, OH, OPAS = 56, 84, 96
ORDRES = ""
for i, (quoi, combien) in enumerate(REPERES):
    y = OY0 + i * OPAS
    ORDRES += ('<rect x="12" y="%d" width="446" height="%d" rx="13" fill="%s" stroke="%s" '
               'stroke-width="1.6"/>' % (y, OH, TINT, GREY))
    ORDRES += ('<text x="235" y="%d" text-anchor="middle" font-size="19" '
               'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
               % (y + 33, DEEP, quoi))
    ORDRES += ('<text x="235" y="%d" text-anchor="middle" font-size="19" '
               'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
               % (y + 64, SFA, combien))
assert OY0 + 2 * OPAS + OH == 332

SLIDES = """
  <!-- ==================== ANIM-CH9-09 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-09" data-title="Taux de conversion et rendement" data-sub="Deux rapports qu'on confond systématiquement" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <rect x="14" y="24" width="200" height="180" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="114" y="58" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">TAUX</text>
            <text x="114" y="84" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">DE CONVERSION</text>
            <text x="114" y="124" text-anchor="middle" font-size="16" @@FF@@ fill="@@SFA@@" font-weight="700">porte sur un RÉACTIF</text>
            <text x="114" y="160" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">la fraction qui</text>
            <text x="114" y="184" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">a réagi</text>
          </g>
          <g class="step s2">
            <rect x="256" y="24" width="200" height="180" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="356" y="58" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">RENDEMENT</text>
            <text x="356" y="124" text-anchor="middle" font-size="16" @@FF@@ fill="@@RED@@" font-weight="700">porte sur un PRODUIT</text>
            <text x="356" y="160" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">obtenu divisé par</text>
            <text x="356" y="184" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">théorique</text>
          </g>
          <g class="step s3">
            <rect x="10" y="228" width="450" height="64" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="256" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">tous deux en pourcentage</text>
            <text x="235" y="282" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">et souvent du même nombre — d'où la confusion</text>
          </g>
          <g class="step s4">
            <rect x="10" y="316" width="450" height="142" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.6"/>
            <text x="235" y="352" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">le repère de lecture</text>
            <text x="235" y="392" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">ce qui a DISPARU → taux de conversion</text>
            <text x="235" y="430" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">ce qui a été OBTENU → rendement</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le taux de conversion</h3>
          <p style="font-size:17px">Il porte sur un <b>réactif</b> : c'est la fraction du réactif qui a effectivement réagi. Il regarde <b>en arrière</b>, vers ce qui est parti.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le rendement</h3>
          <p style="font-size:17px">Il porte sur un <b>produit</b> : c'est la quantité réellement obtenue divisée par la quantité théoriquement attendue. Il regarde <b>en avant</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi on les confond</h3>
          <p style="font-size:17px">Les deux s'expriment en <b>pourcentage</b> et valent souvent le même nombre. Mais ils ne mesurent pas la même chose, et l'énoncé n'en demande qu'un.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le repère qui tranche en une seconde</h3>
          <p style="font-size:17px">On lit l'énoncé et on cherche <b>de quoi il parle</b>.<br><br>S'il parle de ce qui a <b>disparu</b> — « quelle fraction du réactif a réagi ? » — c'est un <b>taux de conversion</b>. S'il parle de ce qui a été <b>obtenu</b> — « on récupère 18 g au lieu des 22 g attendus » — c'est un <b>rendement</b>.<br><br>Un seul mot de l'énoncé suffit, et il est toujours là.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le taux de conversion porte sur un <b>réactif</b> : ce qui a réagi.",
      "Le rendement porte sur un <b>produit</b> : ce qu'on a obtenu.",
      "Tous deux en pourcentage, souvent du même nombre — d'où la confusion.",
      "Mais ils ne répondent pas à la même question.",
      "<em>Le repère :</em> ce qui a disparu, ou ce qui a été obtenu."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-10 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-10" data-title="Un rendement dépasse-t-il jamais 100 %" data-sub="La réponse, et ce qu'elle révèle sur un calcul" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="235" y="48" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">rendement d'une réaction</text>
            <text x="235" y="86" text-anchor="middle" font-size="18" @@FF@@ fill="@@GREY@@">obtenu ÷ théorique, en pourcentage</text>
            @@JAUGE@@@@GRAD@@
          </g>
          <g class="step s2">
            <line x1="@@XC@@" y1="164" x2="@@XC@@" y2="@@RY@@" stroke="@@RED@@" stroke-width="3"/>
            <text x="@@XC@@" y="154" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">jamais au-delà</text>
            <text x="180" y="224" text-anchor="middle" font-size="21" @@FF@@ fill="#FFFFFF" font-weight="700">possible</text>
            <text x="402" y="306" text-anchor="middle" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">impossible</text>
          </g>
          <g class="step s3">
            <rect x="10" y="324" width="450" height="74" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="354" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">un rendement supérieur à 100 % = une erreur</text>
            <text x="235" y="384" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">limitant, coefficient, ou conversion</text>
          </g>
          <g class="step s4">
            <rect x="10" y="406" width="450" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="438" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">contrôle instantané, et il ne coûte rien</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La réponse est non</h3>
          <p style="font-size:17px">Jamais. On ne peut pas obtenir <b>plus</b> que ce que la matière disponible permet — c'est la conservation de la masse qui l'interdit.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qu'un dépassement révèle</h3>
          <p style="font-size:17px">Une erreur, et presque toujours l'une de ces trois : <b>réactif limitant</b> mal identifié, <b>coefficient</b> oublié, ou <b>conversion</b> ratée.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Un contrôle instantané</h3>
          <p style="font-size:17px">On le fait <b>avant</b> même de relire le calcul. Un regard sur le résultat suffit à savoir s'il faut tout reprendre.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et pourquoi un rendement est presque toujours inférieur à 100 %</h3>
          <p style="font-size:17px">Trois causes, à citer sans les développer : la réaction peut être <b>incomplète</b>, il y a des <b>pertes à la manipulation</b>, et des <b>réactions parasites</b> consomment une part des réactifs.<br><br>Un rendement de 100 % exact est donc lui aussi suspect : dans la réalité d'un laboratoire, il n'arrive pratiquement jamais.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Le rendement se lit sur une échelle de zéro à cent pour cent.",
      "Et il ne franchit <b>jamais</b> la barre des cent.",
      "On ne peut pas obtenir plus que ce que la matière disponible permet.",
      "Un résultat au-delà signale donc une erreur, et on sait laquelle chercher.",
      "<em>Un contrôle qui ne coûte rien</em> — on le fait avant de relire le calcul."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-11 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-11" data-title="Arrondir juste ce qu'il faut" data-sub="Les masses molaires au gramme près, et pas au-delà" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <text x="235" y="42" text-anchor="middle" font-size="19" @@FF@@ fill="@@GREY@@">les seules masses molaires à connaître</text>
            @@PUCES@@
          </g>
          <g class="step s2">
            <rect x="10" y="184" width="450" height="64" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="212" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">aucune décimale au-delà</text>
            <text x="235" y="238" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">2 % de précision suffisent pour trancher un QCM</text>
          </g>
          <g class="step s3">
            <rect x="10" y="264" width="450" height="106" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="235" y="296" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">on cherche la simplification avant de diviser</text>
            <text x="235" y="332" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">50 ÷ 100 se voit &nbsp;·&nbsp; 44 ÷ 22 aussi</text>
            <text x="235" y="360" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">poser la division est le dernier recours</text>
          </g>
          <g class="step s4">
            <rect x="10" y="386" width="450" height="72" rx="13" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.2"/>
            <text x="235" y="416" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">les puissances de dix se traitent à part</text>
            <text x="235" y="444" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">séparées des mantisses, du début à la fin</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi cette capsule existe</h3>
          <p style="font-size:17px">Parce que le concours <b>interdit la calculatrice</b>. Un exercice parfaitement compris mais mal calculé rapporte zéro — et coûte un tiers de point.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les propositions du QCM sont écartées</h3>
          <p style="font-size:17px">Assez pour qu'une précision de <b>2 %</b> suffise à trancher. Chercher trois décimales fait perdre du temps sans jamais changer la réponse cochée.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La technique du calcul en fractions</h3>
          <p style="font-size:17px">50 ÷ 100 se voit, 44 ÷ 22 aussi. On cherche les <b>simplifications</b> avant de poser la division — qui devient alors rarement nécessaire.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les puissances de dix, traitées séparément</h3>
          <p style="font-size:17px">On sépare la <b>mantisse</b> de la <b>puissance de dix</b> dès la première ligne, et on ne les remélange qu'à la fin.<br><br>C'est exactement la méthode de la capsule <b>A1</b> des mathématiques, mise en situation ici. Et c'est ce qui évite l'erreur d'un facteur mille, qui est la plus fréquente de tout le chapitre.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Huit masses molaires, arrondies. Il n'y en a pas d'autres à connaître.",
      "Aucune décimale au-delà : deux pour cent de précision suffisent.",
      "Et avant de poser une division, on cherche la simplification.",
      "Cinquante sur cent se voit. Quarante-quatre sur vingt-deux aussi.",
      "<em>Et les puissances de dix se traitent à part</em> — c'est la méthode de A1."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH9-12 ==================== -->
  <section class="slide" data-ref="ANIM-CH9-12" data-title="L'ordre de grandeur comme contrôle" data-sub="Repérer une réponse absurde en trois secondes" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <text x="235" y="36" text-anchor="middle" font-size="19" @@FF@@ fill="@@GREY@@">les trois repères à avoir en tête</text>
            @@ORD@@
          </g>
          <g class="step s2">
            <rect x="10" y="352" width="450" height="46" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="382" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">une réponse hors de ces bornes est fausse</text>
          </g>
          <g class="step s3">
            <rect x="10" y="408" width="450" height="50" rx="12" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="439" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">presque toujours un facteur mille</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le contrôle de plausibilité</h3>
          <p style="font-size:17px">Avant de cocher, on se demande si le nombre est <b>possible</b>. Une masse de produit ne peut pas dépasser la masse totale des réactifs.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Trois repères suffisent</h3>
          <p style="font-size:17px">Une mole de gaz occupe une <b>vingtaine de litres</b>. Une masse molaire usuelle est entre <b>1 et 300 g/mol</b>. Une concentration courante, entre <b>10⁻³ et 10 mol/L</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qu'un écart signifie</h3>
          <p style="font-size:17px">Une réponse hors de ces bornes est presque toujours une erreur de conversion d'un <b>facteur mille</b> — un millilitre pris pour un litre, un gramme pour un kilogramme.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi ce contrôle vaut mieux que de refaire le calcul</h3>
          <p style="font-size:17px">Refaire un calcul prend une minute et reproduit souvent la même erreur, parce qu'on refait le même geste.<br><br>Le contrôle d'ordre de grandeur prend <b>trois secondes</b> et attaque le problème par un autre bout : il ne demande pas « ai-je bien calculé ? » mais « ce nombre a-t-il un sens ? ». Sur un QCM chronométré à −1/3 par erreur, c'est le meilleur réflexe qu'un étudiant puisse prendre.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Trois repères, et ils suffisent à repérer une réponse absurde.",
      "Une mole de gaz occupe une vingtaine de litres, jamais des milliers.",
      "Une masse molaire usuelle tient entre un et trois cents grammes par mole.",
      "Une concentration courante, entre un millième et dix moles par litre.",
      "<em>Hors de ces bornes</em>, c'est presque toujours un facteur mille."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "JAUGE": JAUGE, "GRAD": GRAD, "XC": "%.1f" % X_CENT, "RY": str(RY),
    "PUCES": PUCES, "ORD": ORDRES,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH9-C : 100 %% a x = %.1f · %d masses molaires · %d reperes"
      % (X_CENT, len(MASSES), len(REPERES)))
print("ok", make("CH9-C", "Capsule CH9-C — Taux de conversion, rendement, et calcul sans calculatrice · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH9C.html")))
