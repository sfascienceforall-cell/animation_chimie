# -*- coding: utf-8 -*-
"""CH10 — L'equilibre chimique et Le Chatelier. 4 animations.

Derniere capsule du programme de chimie. Figures au format 470 x 470,
palette verte.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH10-04 : les trois leviers ----------------
LEVIERS = [("la concentration", "ajouter un réactif pousse vers les produits", SFA, False),
           ("la pression", "elle pousse vers le côté qui compte le moins de gaz", SFA, False),
           ("la température", "elle favorise le sens endothermique — et change K", RED, True)]
LY0, LH, LPAS = 34, 104, 116
LEV = ""
for i, (titre, regle, coul, change_k) in enumerate(LEVIERS):
    y = LY0 + i * LPAS
    fond = TINT2 if change_k else TINT
    bord = DEEP if change_k else GREY
    LEV += ('<rect x="12" y="%d" width="446" height="%d" rx="13" fill="%s" stroke="%s" '
            'stroke-width="%s"/>' % (y, LH, fond, bord, "2.6" if change_k else "1.6"))
    LEV += ('<text x="235" y="%d" text-anchor="middle" font-size="22" '
            'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
            % (y + 40, DEEP, titre))
    LEV += ('<text x="235" y="%d" text-anchor="middle" font-size="17" '
            'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
            % (y + 74, coul, regle))
assert LY0 + 2 * LPAS + LH == 370

SLIDES = """
  <!-- ==================== ANIM-CH10-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH10-01" data-title="L'équilibre est dynamique, pas immobile" data-sub="Deux réactions à la même vitesse, en sens opposés" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <rect x="14" y="70" width="186" height="110" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="107" y="134" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">réactifs</text>
            <rect x="270" y="70" width="186" height="110" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="363" y="134" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">produits</text>
          </g>
          <g class="step s2">
            <line x1="212" y1="112" x2="258" y2="112" stroke="@@SFA@@" stroke-width="4" marker-end="url(#v1)"/>
            <line x1="258" y1="140" x2="212" y2="140" stroke="@@SFA@@" stroke-width="4" marker-end="url(#v1)"/>
            <text x="235" y="212" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">les deux sens se produisent en même temps</text>
          </g>
          <g class="step s3">
            <rect x="10" y="238" width="450" height="78" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="270" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">équilibre = les deux vitesses sont égales</text>
            <text x="235" y="300" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">les concentrations cessent alors de varier</text>
          </g>
          <g class="step s4">
            <rect x="10" y="332" width="450" height="60" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="235" y="369" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">mais rien ne s'est arrêté</text>
            <rect x="10" y="404" width="450" height="54" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="438" text-anchor="middle" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">les vitesses sont égales, pas les quantités</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une réaction réversible</h3>
          <p style="font-size:17px">Elle se produit dans les <b>deux sens simultanément</b>. C'est ce que la double flèche signifie — celle déjà rencontrée en CH4-B et en CH7-A.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Quand l'équilibre est atteint</h3>
          <p style="font-size:17px">Lorsque les <b>deux vitesses deviennent égales</b>. Les concentrations cessent alors de varier, et le système paraît figé.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Mais rien ne s'est arrêté</h3>
          <p style="font-size:17px">Il se forme autant de produit qu'il s'en détruit <b>à chaque instant</b>. C'est un équilibre <b>dynamique</b> — un régime permanent, pas un arrêt.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège, et il est très répandu</h3>
          <p style="font-size:17px">Croire qu'à l'équilibre il y a <b>autant de réactifs que de produits</b>. C'est faux, et rien ne l'impose.<br><br>Les <b>concentrations</b> n'ont aucune raison d'être égales : ce sont les <b>vitesses</b> qui le sont. Un équilibre peut très bien être atteint avec 99 % de produits et 1 % de réactifs — c'est justement ce que la constante K va mesurer.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Jusqu'ici les réactions étaient totales. Celle-ci se produit dans les deux sens.",
      "Au début, le sens direct l'emporte. Puis le sens inverse s'accélère.",
      "L'équilibre est atteint quand les <b>deux vitesses</b> deviennent égales.",
      "Les concentrations cessent de varier — mais rien ne s'est arrêté.",
      "<em>Le piège :</em> ce sont les vitesses qui sont égales, jamais les quantités."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH10-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH10-02" data-title="La constante d'équilibre" data-sub="Ce qu'elle contient, et ce qu'elle laisse dehors" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="235" y="52" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">a A + b B ⇌ c C + d D</text>
          </g>
          <g class="step s2">
            <text x="86" y="158" text-anchor="middle" font-size="34" @@FF@@ fill="@@DEEP@@" font-weight="700">K =</text>
            <text x="286" y="136" text-anchor="middle" font-size="30" @@FF@@ fill="@@SFA@@" font-weight="700">[C]<tspan font-size="20" dy="-10">c</tspan><tspan dy="10"> </tspan>[D]<tspan font-size="20" dy="-10">d</tspan></text>
            <line x1="140" y1="152" x2="432" y2="152" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="286" y="192" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">[A]<tspan font-size="20" dy="-10">a</tspan><tspan dy="10"> </tspan>[B]<tspan font-size="20" dy="-10">b</tspan></text>
            <text x="286" y="100" text-anchor="middle" font-size="17" @@FF@@ fill="@@SFA@@" font-weight="700">les produits au numérateur</text>
            <text x="286" y="224" text-anchor="middle" font-size="17" @@FF@@ fill="@@GREY@@">les réactifs au dénominateur</text>
          </g>
          <g class="step s3">
            <rect x="10" y="254" width="450" height="52" rx="12" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="286" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">les coefficients sont des EXPOSANTS</text>
          </g>
          <g class="step s4">
            <rect x="10" y="318" width="450" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="350" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">ni les solides ni le solvant n'y figurent</text>
            <rect x="10" y="382" width="450" height="76" rx="13" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="2.2"/>
            <text x="235" y="412" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">K très grand → réaction presque totale</text>
            <text x="235" y="442" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">K très petit → elle se produit à peine</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'écriture, et son ordre</h3>
          <p style="font-size:17px">Les <b>produits au numérateur</b>, les <b>réactifs au dénominateur</b>, chaque concentration élevée à la puissance de son coefficient. L'inverser donne 1/K.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Exposants, jamais facteurs</h3>
          <p style="font-size:17px">Les coefficients deviennent des <b>exposants</b>. Écrire 2 × [C] au lieu de [C]² est l'erreur d'écriture la plus fréquente du chapitre.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qui n'y figure pas</h3>
          <p style="font-size:17px">Les <b>solides</b> et le <b>solvant</b> : leur concentration ne varie pas. Une équation avec un solide donne une constante où il n'apparaît pas du tout.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Comment lire la valeur de K</h3>
          <p style="font-size:17px">K <b>très grand</b> : le numérateur domine, il y a beaucoup de produits — la réaction est presque totale. K <b>très petit</b> : elle se produit à peine.<br><br>C'est la réponse théorique à ce qui était affirmé sans preuve en CH4-B et CH7-A : un électrolyte fort, un acide fort, sont simplement des espèces dont la constante est très grande. Le programme se referme ici.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Une réaction réversible quelconque, avec ses quatre coefficients.",
      "K est le rapport des produits sur les réactifs — dans cet ordre, jamais l'inverse.",
      "Et les coefficients deviennent des <b>exposants</b>, jamais des facteurs.",
      "Les solides et le solvant n'y figurent pas : leur concentration ne varie pas.",
      "<em>K très grand :</em> la réaction est presque totale. Très petit : elle a à peine lieu."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH10-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH10-03" data-title="Le Chatelier : le système résiste" data-sub="Une phrase, trois perturbations" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <circle cx="235" cy="150" r="88" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="3"/>
            <text x="235" y="142" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">système</text>
            <text x="235" y="172" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">à l'équilibre</text>
          </g>
          <g class="step s2">
            <line x1="26" y1="130" x2="132" y2="130" stroke="@@RED@@" stroke-width="4.5" marker-end="url(#r3)"/>
            <text x="26" y="112" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">contrainte</text>
          </g>
          <g class="step s3">
            <line x1="338" y1="176" x2="444" y2="176" stroke="@@SFA@@" stroke-width="4.5" marker-end="url(#v3)"/>
            <text x="444" y="212" text-anchor="end" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">il s'y oppose</text>
          </g>
          <g class="step s4">
            <rect x="10" y="258" width="450" height="86" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="290" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">le système se déplace dans le sens</text>
            <text x="235" y="322" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">qui s'oppose à la contrainte imposée</text>
            <rect x="10" y="360" width="450" height="98" rx="13" fill="#FFFFFF" stroke="@@SFA@@" stroke-width="2.4"/>
            <text x="235" y="392" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">la méthode, et jamais l'inverse</text>
            <text x="235" y="424" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">on identifie la contrainte, on cherche</text>
            <text x="235" y="448" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">ce qui la réduirait, on en déduit le sens</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'énoncé, en une phrase</h3>
          <p style="font-size:17px">Lorsqu'on impose une contrainte à un système à l'équilibre, celui-ci se déplace dans le sens qui <b>s'oppose</b> à cette contrainte.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">C'est du bon sens avant d'être une loi</h3>
          <p style="font-size:17px">Le système fait ce qu'il faut pour <b>annuler en partie</b> ce qu'on lui fait subir. Il ne l'annule jamais complètement — il atténue.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La méthode d'application</h3>
          <p style="font-size:17px">On identifie la <b>contrainte</b>, on se demande <b>ce qui la réduirait</b>, et on en déduit le sens du déplacement. Jamais dans l'autre ordre.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi cette idée ferme bien le programme</h3>
          <p style="font-size:17px">C'est la seule loi de tout le cours de chimie qui ne se calcule pas : elle se <b>raisonne</b>. Aucune formule n'est nécessaire, aucune donnée numérique non plus.<br><br>Et elle se retrouvera telle quelle en biologie, dans tous les mécanismes de régulation — le pH du sang, la glycémie, la thermorégulation. Un système vivant fait exactement cela : il s'oppose à ce qui le sort de son équilibre.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Un système à l'équilibre, qu'on va perturber.",
      "On lui impose une contrainte — n'importe laquelle.",
      "Il se déplace dans le sens qui <b>s'oppose</b> à cette contrainte.",
      "C'est du bon sens avant d'être une loi : il atténue ce qu'on lui fait subir.",
      "<em>Et c'est exactement ce que fait un système vivant</em> pour se réguler."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH10-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH10-04" data-title="Les trois leviers, un par un" data-sub="Concentration, pression, température — et celui qui change K" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">@@LEV@@</g>
          <g class="step s2">
            <rect x="10" y="386" width="450" height="72" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="416" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">seule la température change la valeur de K</text>
            <text x="235" y="444" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">les deux autres déplacent l'équilibre sans y toucher</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La concentration</h3>
          <p style="font-size:17px">Ajouter un réactif déplace l'équilibre <b>vers les produits</b>, pour le consommer. Retirer un produit a exactement le même effet.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La pression, et seulement pour les gaz</h3>
          <p style="font-size:17px">Augmenter la pression déplace l'équilibre vers le côté qui compte le <b>moins de moles de gaz</b> — c'est ce qui réduit la pression.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La température</h3>
          <p style="font-size:17px">Augmenter la température favorise le sens <b>endothermique</b>, celui qui <b>absorbe</b> de la chaleur — et qui s'oppose donc à l'échauffement.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La distinction essentielle, et c'est la question du concours</h3>
          <p style="font-size:17px">Concentration et pression <b>déplacent</b> l'équilibre <b>sans changer K</b> : le système se réarrange pour retrouver le même rapport.<br><br>Seule la <b>température</b> modifie la valeur de K elle-même. C'est la seule difficulté réelle du chapitre, et c'est précisément ce que le QCM demande.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Trois leviers, et un seul est différent des deux autres.",
      "La <b>concentration</b> : ajouter un réactif pousse vers les produits.",
      "La <b>pression</b> : elle pousse vers le côté qui compte le moins de gaz.",
      "La <b>température</b> : elle favorise le sens qui absorbe la chaleur.",
      "<em>Et elle seule change la valeur de K</em> — c'est la question du concours."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4), "LEV": LEV,
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH10 : %d leviers, bas du dernier encadre = %d" % (len(LEVIERS), LY0 + 2 * LPAS + LH))
print("ok", make("CH10", "Capsule CH10 — L'équilibre chimique et Le Chatelier · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH10.html")))
