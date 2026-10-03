# -*- coding: utf-8 -*-
"""CH4-B — Solutions, concentrations et dissociation. 4 animations.

Figures au format 470 x 470. Les particules des bechers sont tirees dans un
rectangle interieur calcule, et une assertion verifie qu'aucune ne touche la
paroi.
"""
import sys, random
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

RP = 9                                    # rayon d'une particule de solute
MARGE = 20                                # distance minimale a la paroi


def becher(x, y, w, h):
    """Contour d'un becher : parois verticales, fond arrondi."""
    return ('<path d="M %d,%d L %d,%d Q %d,%d %d,%d L %d,%d Q %d,%d %d,%d L %d,%d" '
            'fill="none" stroke="%s" stroke-width="3.4" stroke-linecap="round"/>'
            % (x, y, x, y + h - 16, x, y + h, x + 16, y + h,
               x + w - 16, y + h, x + w, y + h, x + w, y + h - 16, x + w, y, DEEP))


def points(x, y, w, h, n, seed, col=None):
    """n particules tirees dans le rectangle interieur, paroi respectee."""
    rd = random.Random(seed)
    pts = [(x + rd.uniform(MARGE, w - MARGE), y + rd.uniform(MARGE, h - MARGE)) for _ in range(n)]
    for px, py in pts:
        assert x + 3 <= px - RP and px + RP <= x + w - 3, (px, x, w)
        assert y + 3 <= py - RP and py + RP <= y + h - 3, (py, y, h)
    return "".join('<circle cx="%.0f" cy="%.0f" r="%d" fill="%s"/>' % (px, py, RP, col or SFA)
                   for px, py in pts)


# CH4-06 : meme nombre de particules, deux volumes
N_SOL = 14
B1 = becher(40, 200, 142, 172) + points(40, 200, 142, 172, N_SOL, 11)
B2 = becher(248, 128, 196, 244) + points(248, 128, 196, 244, N_SOL, 11)

# CH4-07 : dissociation de CaCl2 — 1 Ca2+ pour 2 Cl-
N_UNITES = 3
CA = [(290 + 60 * i, 250) for i in range(N_UNITES)]
CL = [(270 + 34 * i, 306) for i in range(2 * N_UNITES)]
assert max(x for x, _ in CL) + 11 <= 462, CL[-1]
DISS = "".join('<circle cx="%d" cy="%d" r="14" fill="%s"/>' % (x, y, SFA) for x, y in CA)
DISS_CL = "".join('<circle cx="%d" cy="%d" r="11" fill="%s"/>' % (x, y, DEEP) for x, y in CL)

SLIDES = """
  <!-- ==================== ANIM-CH4-05 ==================== -->
  <section class="slide" data-ref="ANIM-CH4-05" data-title="Les quatre façons d'exprimer une concentration" data-sub="Et comment passer de l'une à l'autre" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <rect x="16" y="34" width="214" height="152" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="123" y="70" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">molarité</text>
            <text x="123" y="122" text-anchor="middle" font-size="30" @@FF@@ fill="@@SFA@@" font-weight="700">c = n / V</text>
            <text x="123" y="160" text-anchor="middle" font-size="16" @@FF@@ fill="#3F3F46">mol/L · celle qui sert</text>
          </g>
          <g class="step s2">
            <rect x="240" y="34" width="214" height="152" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="347" y="70" text-anchor="middle" font-size="16" @@FF@@ fill="@@DEEP@@" font-weight="700">concentration massique</text>
            <text x="347" y="122" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">m / V</text>
            <text x="347" y="160" text-anchor="middle" font-size="16" @@FF@@ fill="#3F3F46">g/L · on passe par M</text>
          </g>
          <g class="step s3">
            <rect x="16" y="202" width="214" height="152" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="123" y="238" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">pourcentage massique</text>
            <text x="123" y="290" text-anchor="middle" font-size="27" @@FF@@ fill="@@DEEP@@" font-weight="700">m / m<tspan font-size="17">totale</tspan></text>
            <text x="123" y="328" text-anchor="middle" font-size="16" @@FF@@ fill="@@RED@@" font-weight="700">rapporté au TOTAL</text>
            <rect x="240" y="202" width="214" height="152" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="347" y="238" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">fraction molaire</text>
            <text x="347" y="290" text-anchor="middle" font-size="27" @@FF@@ fill="@@DEEP@@" font-weight="700">n / n<tspan font-size="17">totale</tspan></text>
            <text x="347" y="328" text-anchor="middle" font-size="16" @@FF@@ fill="@@RED@@" font-weight="700">sans unité · somme = 1</text>
          </g>
          <g class="step s4">
            <rect x="10" y="392" width="450" height="62" rx="14" fill="@@TINT2@@"/>
            <text x="235" y="430" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">le dénominateur change tout : volume, ou total ?</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La molarité, et elle seule, sert aux réactions</h3>
          <p style="font-size:17px">c = n / V, en mol/L. C'est la seule qui donne directement un nombre de moles — donc la seule utilisable avec les coefficients d'une équation.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Passer de l'une à l'autre</h3>
          <p style="font-size:17px">De la concentration massique à la molarité, on <b>divise par la masse molaire</b>. C'est encore le triangle de CH1, appliqué à un litre de solution.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Les deux grandeurs sans unité</h3>
          <p style="font-size:17px">Le <b>pourcentage massique</b> et la <b>fraction molaire</b> se rapportent au total. La somme de toutes les fractions molaires d'un mélange vaut exactement <b>1</b> — un contrôle gratuit.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le dénominateur, et c'est là que tout se joue</h3>
          <p style="font-size:17px">La molarité rapporte au <b>volume de solution</b> — jamais au volume de solvant ajouté. Les pourcentages et fractions rapportent au <b>total</b>, soluté compris.<br><br>Confondre les deux revient à oublier le soluté au dénominateur : l'erreur est faible en solution diluée, et devient énorme en solution concentrée. C'est ce que le concours teste.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "La molarité : des moles par litre. C'est celle qui servira dans toutes les réactions.",
      "La concentration massique dit la même chose en grammes — on passe de l'une à l'autre par M.",
      "Les deux dernières se rapportent au <b>total</b>, et n'ont pas d'unité.",
      "Toute la difficulté est au dénominateur : un volume, ou un total ?",
      "<em>Et la molarité rapporte au volume de solution</em>, jamais au solvant ajouté."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH4-06 ==================== -->
  <section class="slide" data-ref="ANIM-CH4-06" data-title="La dilution : ce qui change et ce qui ne change pas" data-sub="La quantité de soluté est conservée" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">@@B1@@
            <text x="111" y="186" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">avant</text>
            <text x="111" y="400" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">petit volume</text>
          </g>
          <g class="step s2">
            <line x1="196" y1="286" x2="240" y2="286" stroke="@@SFA@@" stroke-width="3.6" marker-end="url(#v2)"/>
            <text x="218" y="268" text-anchor="middle" font-size="17" @@FF@@ fill="@@SFA@@" font-weight="700">+ eau</text>
          </g>
          <g class="step s3">@@B2@@
            <text x="346" y="114" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">après</text>
            <text x="346" y="400" text-anchor="middle" font-size="18" @@FF@@ fill="#3F3F46">grand volume</text>
          </g>
          <g class="step s4">
            <text x="111" y="152" text-anchor="middle" font-size="21" @@FF@@ fill="@@SFA@@" font-weight="700">@@N@@ particules</text>
            <text x="346" y="80" text-anchor="middle" font-size="21" @@FF@@ fill="@@SFA@@" font-weight="700">@@N@@ particules</text>
            <rect x="16" y="418" width="438" height="44" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="447" text-anchor="middle" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">le soluté se conserve : c₁V₁ = c₂V₂</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Diluer, c'est ajouter du solvant</h3>
          <p style="font-size:17px">On ne touche <b>pas</b> au soluté. On ne lui en ajoute pas, on ne lui en retire pas : on lui donne seulement plus de place.</p></div>
        <div class="card acc step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qui se conserve</h3>
          <p style="font-size:17px">Le <b>nombre de moles de soluté</b>. C'est exactement ce que dit la relation de dilution, et elle ne dit rien d'autre.</p>
          <div class="expr" style="font-size:24px;text-align:left;line-height:1.25;margin-top:6px">c₁ V₁ = c₂ V₂</div></div>
        <div class="card step s4" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Trois choses à dire, dans cet ordre</h3>
          <p style="font-size:17px">Le <b>volume augmente</b> · la <b>concentration diminue</b> · la <b>quantité de matière ne bouge pas</b>. C'est la troisième qu'on oublie, et c'est la seule qui fonde la formule.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le contrôle mental, avant tout calcul</h3>
          <p style="font-size:17px">Le <b>facteur de dilution</b> est le rapport des volumes. Passer de 25 à 200 mL, c'est diluer <b>huit fois</b> : la concentration doit donc être divisée par 8, exactement.<br><br>On connaît le résultat <b>avant</b> d'écrire la relation. Si le calcul ne le confirme pas, l'erreur est trouvée sans avoir à le relire.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Un bécher, et un certain nombre de particules de soluté.",
      "On ajoute de l'eau — rien d'autre.",
      "Le volume a augmenté, mais il y a toujours <b>exactement le même nombre</b> de particules.",
      "C'est tout ce que dit c₁V₁ = c₂V₂ : le soluté se conserve.",
      "<em>Le contrôle :</em> volume multiplié par huit, concentration divisée par huit."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH4-07 ==================== -->
  <section class="slide" data-ref="ANIM-CH4-07" data-title="La dissociation d'un électrolyte" data-sub="Une mole de sel, combien de moles d'ions ?" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <text x="106" y="106" text-anchor="middle" font-size="40" @@FF@@ fill="@@DEEP@@" font-weight="700">CaCl₂</text>
            <text x="106" y="142" text-anchor="middle" font-size="17" @@FF@@ fill="#3F3F46">solide, avant dissolution</text>
          </g>
          <g class="step s2">
            <line x1="188" y1="96" x2="240" y2="96" stroke="@@SFA@@" stroke-width="3.6" marker-end="url(#v3)"/>
            <text x="214" y="78" text-anchor="middle" font-size="17" @@FF@@ fill="@@SFA@@" font-weight="700">eau</text>
            <text x="352" y="106" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">Ca²⁺ + 2 Cl⁻</text>
          </g>
          <g class="step s3">
            <line x1="16" y1="186" x2="454" y2="186" stroke="@@RULE@@" stroke-width="2"/>
            <text x="106" y="246" text-anchor="middle" font-size="26" @@FF@@ fill="@@SFA@@" font-weight="700">3 unités</text>
            <text x="106" y="280" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">de formule</text>
            <line x1="196" y1="266" x2="248" y2="266" stroke="@@GREY@@" stroke-width="2.6" marker-end="url(#d3)"/>
            @@DISS@@@@DISSCL@@
            <text x="352" y="352" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">3 Ca²⁺ &nbsp;et&nbsp; 6 Cl⁻</text>
          </g>
          <g class="step s4">
            <rect x="16" y="402" width="438" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="435" text-anchor="middle" font-size="21" @@FF@@ fill="@@RED@@" font-weight="700">[Cl⁻] est le DOUBLE de [CaCl₂]</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce qu'est un électrolyte</h3>
          <p style="font-size:17px">Une espèce qui se <b>dissocie en ions</b> lorsqu'elle est dissoute. La solution devient alors conductrice — c'est même ainsi qu'on le met en évidence.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'équation porte les coefficients</h3>
          <p style="font-size:17px">NaCl donne <b>un</b> Na⁺ et <b>un</b> Cl⁻. Mais CaCl₂ donne un Ca²⁺ et <b>deux</b> Cl⁻ : les indices de la formule deviennent les coefficients de la dissociation.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Et donc les concentrations diffèrent</h3>
          <p style="font-size:17px">Une solution de CaCl₂ à 0,1 mol/L contient 0,1 mol/L d'ions calcium mais <b>0,2 mol/L</b> d'ions chlorure. Ce ne sont pas les mêmes nombres.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le piège, et le contrôle qui l'attrape</h3>
          <p style="font-size:17px"><b>Le piège :</b> donner la concentration du sel comme concentration de chaque ion. Il faut relire les coefficients de l'équation de dissociation, à chaque fois.<br><br><b>Le contrôle :</b> la solution reste électriquement <b>neutre</b>. Ici (+2) × 0,1 + (−1) × 0,2 = 0 ✓ Si la somme n'est pas nulle, un coefficient a été oublié.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Du chlorure de calcium solide, avant d'être mis dans l'eau.",
      "Il se dissocie — et l'équation dit en quoi : un Ca²⁺, et <b>deux</b> Cl⁻.",
      "Pour trois unités de formule, on obtient trois calcium mais <b>six</b> chlorures.",
      "La concentration en chlorure est donc le <b>double</b> de celle du sel.",
      "<em>Le contrôle :</em> la solution reste neutre — la somme des charges doit être nulle."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH4-08 ==================== -->
  <section class="slide" data-ref="ANIM-CH4-08" data-title="Fort ou faible : une question de degré" data-sub="La double flèche qui change tout" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <rect x="16" y="34" width="438" height="156" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="38" y="76" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">ÉLECTROLYTE FORT</text>
            <text x="100" y="142" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">AB</text>
            <line x1="140" y1="134" x2="208" y2="134" stroke="@@SFA@@" stroke-width="3.6" marker-end="url(#v4)"/>
            <text x="292" y="142" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">A⁺ + B⁻</text>
            <text x="408" y="142" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">totale</text>
          </g>
          <g class="step s2">
            <rect x="16" y="214" width="438" height="156" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="38" y="256" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">ÉLECTROLYTE FAIBLE</text>
            <text x="100" y="322" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">AB</text>
            <line x1="140" y1="306" x2="208" y2="306" stroke="@@RED@@" stroke-width="3.2" marker-end="url(#r4)"/>
            <line x1="208" y1="324" x2="140" y2="324" stroke="@@RED@@" stroke-width="3.2" marker-end="url(#r4)"/>
            <text x="292" y="322" text-anchor="middle" font-size="30" @@FF@@ fill="@@DEEP@@" font-weight="700">A⁺ + B⁻</text>
            <text x="408" y="322" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">partielle</text>
          </g>
          <g class="step s3">
            <rect x="16" y="402" width="438" height="52" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="435" text-anchor="middle" font-size="20" @@FF@@ fill="@@DEEP@@" font-weight="700">la double flèche signale un équilibre</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Fort : la dissociation est totale</h3>
          <p style="font-size:17px">Il ne reste <b>plus rien</b> de l'espèce de départ en solution. On écrit une <b>flèche simple</b>, et le calcul est direct.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Faible : elle est partielle</h3>
          <p style="font-size:17px">Une partie seulement se dissocie, et un <b>équilibre</b> s'établit entre les deux formes. On écrit une <b>double flèche</b>.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La notation porte l'information</h3>
          <p style="font-size:17px">Voir une double flèche dans un énoncé, c'est savoir <b>immédiatement</b> qu'on a affaire à une espèce faible — et que la constante d'équilibre de CH10 s'appliquera.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Une distinction qu'on retrouvera deux fois</h3>
          <p style="font-size:17px">Cette opposition fort / faible est <b>exactement</b> celle qui reviendra en CH7 pour les acides et les bases. Ce n'est pas une notion voisine : c'est la même, appliquée à un autre transfert.<br><br>Et le chapitre CH10 en donnera enfin la théorie complète, sous le nom de <b>constante d'équilibre</b>. Trois rencontres, un seul concept — le dire ici économise deux apprentissages.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Un électrolyte fort se dissocie <b>totalement</b> : flèche simple, il ne reste rien du départ.",
      "Un électrolyte faible ne se dissocie qu'en partie : <b>double flèche</b>, un équilibre s'installe.",
      "La notation suffit donc à savoir à quoi on a affaire, avant tout calcul.",
      "C'est la même opposition qui reviendra pour les acides et les bases, en CH7.",
      "<em>Et sa théorie complète</em> viendra au dernier chapitre : la constante d'équilibre."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "B1": B1, "B2": B2, "DISS": DISS, "DISSCL": DISS_CL, "N": str(N_SOL),
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED, "RULE": "#E3E7EE",
})

print("bechers : %d particules chacun, paroi respectee · dissociation : %d Ca / %d Cl"
      % (N_SOL, len(CA), len(CL)))
print("ok", make("CH4-B", "Capsule CH4-B — Solutions, concentrations et dissociation · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH4B.html")))
