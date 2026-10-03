# -*- coding: utf-8 -*-
"""CH7-A — Couples acide-base et equilibrage. 4 animations.

Figures au format 470 x 470, palette verte.
"""
import sys
import os
_ICI = os.path.dirname(os.path.abspath(__file__))   # le dossier du script
sys.path.insert(0, _ICI)
from chem import defs, finish, make, SFA, DEEP, TINT, TINT2, GREY, INK2, RED

# ---------------- CH7-04 : l'echelle des pKa ----------------
PKA_X0, PKA_X1, PKA_Y = 34, 436, 336
ACIDES = [("A", 3.8, SFA), ("B", 4.8, DEEP), ("C", 9.2, RED)]
PMIN, PMAX = 0.0, 14.0


def xpka(p):
    return PKA_X0 + (p - PMIN) / (PMAX - PMIN) * (PKA_X1 - PKA_X0)


REPERES = ""
for nom, p, coul in ACIDES:
    x = xpka(p)
    REPERES += ('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="3"/>'
                % (x, PKA_Y - 14, x, PKA_Y + 14, coul))
    REPERES += ('<text x="%.1f" y="%d" text-anchor="middle" font-size="20" '
                'font-family="Be Vietnam Pro,Arial" fill="%s" font-weight="700">%s</text>'
                % (x, PKA_Y - 24, coul, nom))
# les valeurs, alternees en hauteur pour ne jamais se toucher
VALEURS = ""
for i, (nom, p, coul) in enumerate(ACIDES):
    VALEURS += ('<text x="%.1f" y="%d" text-anchor="middle" font-size="17" '
                'font-family="Be Vietnam Pro,Arial" fill="%s">%s</text>'
                % (xpka(p), PKA_Y + 36 + (i % 2) * 24, INK2, ("%.1f" % p).replace(".", ",")))
_ecarts = [xpka(ACIDES[i + 1][1]) - xpka(ACIDES[i][1]) for i in range(len(ACIDES) - 1)]
assert min(_ecarts) > 24, _ecarts

SLIDES = """
  <!-- ==================== ANIM-CH7-01 ==================== -->
  <section class="slide" data-ref="ANIM-CH7-01" data-title="Un acide donne, une base prend" data-sub="Brønsted en une phrase, et le couple qui en découle" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D1@@
          <g class="step s1">
            <rect x="14" y="26" width="200" height="118" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="114" y="62" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">ACIDE</text>
            <text x="114" y="96" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">il donne</text>
            <text x="114" y="126" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">un proton H⁺</text>
            <rect x="256" y="26" width="200" height="118" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="356" y="62" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">BASE</text>
            <text x="356" y="96" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">elle prend</text>
            <text x="356" y="126" text-anchor="middle" font-size="19" @@FF@@ fill="#3F3F46">un proton H⁺</text>
          </g>
          <g class="step s2">
            <line x1="120" y1="188" x2="209" y2="188" stroke="@@SFA@@" stroke-width="4"/><line x1="261" y1="188" x2="350" y2="188" stroke="@@SFA@@" stroke-width="4" marker-end="url(#v1)"/>
            <circle cx="235" cy="188" r="22" fill="@@SFA@@"/>
            <text x="235" y="196" text-anchor="middle" font-size="18" @@FF@@ fill="#FFFFFF" font-weight="700">H⁺</text>
            <text x="235" y="240" text-anchor="middle" font-size="19" @@FF@@ fill="@@GREY@@">un seul objet change de mains</text>
          </g>
          <g class="step s3">
            <rect x="60" y="264" width="350" height="72" rx="14" fill="@@TINT2@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="235" y="312" text-anchor="middle" font-size="34" @@FF@@ fill="@@DEEP@@" font-weight="700">HCl / Cl⁻</text>
            <text x="235" y="364" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">acide ⇌ base + H⁺</text>
          </g>
          <g class="step s4">
            <rect x="10" y="390" width="450" height="68" rx="13" fill="#FFFFFF" stroke="@@RED@@" stroke-width="2.6"/>
            <text x="235" y="420" text-anchor="middle" font-size="17" @@FF@@ fill="@@RED@@" font-weight="700">un H⁺ seul n'existe pas en solution</text>
            <text x="235" y="446" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@" font-weight="700">l'eau le capte aussitôt : H₃O⁺</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La définition de Brønsted, en deux verbes</h3>
          <p style="font-size:17px">Un <b>acide</b> cède un proton H⁺. Une <b>base</b> en capte un. Il n'y a rien d'autre dans ce chapitre — tout le reste en découle.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le couple conjugué</h3>
          <p style="font-size:17px">Un acide qui a cédé son proton <b>devient</b> une base : sa base conjuguée. On note le couple acide/base, par exemple HCl/Cl⁻.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La demi-équation a toujours le même sens</h3>
          <p style="font-size:17px">On l'écrit <b>acide ⇌ base + H⁺</b>, par convention. Celle de la base s'obtient en la lisant à l'envers, jamais en la réécrivant.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le contrôle universel d'un couple</h3>
          <p style="font-size:17px">Les deux membres d'un couple diffèrent d'exactement <b>un H</b>, et d'exactement <b>une unité de charge</b>.<br><br>Si les deux formules diffèrent de deux hydrogènes, ou si les charges ne diffèrent pas d'une unité, le couple est faux. Ce contrôle prend deux secondes et attrape la totalité des erreurs de conjugué.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Deux rôles, et deux verbes : l'acide <b>donne</b>, la base <b>prend</b>.",
      "Ce qui change de mains, c'est un proton — un seul objet.",
      "L'acide qui a cédé devient une base : c'est le <b>couple conjugué</b>.",
      "Et la demi-équation s'écrit toujours dans le même sens : acide ⇌ base + H⁺.",
      "<em>Un détail qui compte :</em> H⁺ seul n'existe pas, l'eau le capte pour donner H₃O⁺."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH7-02 ==================== -->
  <section class="slide" data-ref="ANIM-CH7-02" data-title="Écrire une réaction acide-base" data-sub="Deux couples, un transfert, une équation" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D2@@
          <g class="step s1">
            <text x="16" y="38" font-size="16" @@FF@@ fill="@@GREY@@">l'acide cède</text>
            <text x="235" y="76" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₃COOH → CH₃COO⁻ + H⁺</text>
          </g>
          <g class="step s2">
            <text x="16" y="130" font-size="16" @@FF@@ fill="@@GREY@@">la base capte</text>
            <text x="235" y="168" text-anchor="middle" font-size="24" @@FF@@ fill="@@DEEP@@" font-weight="700">NH₃ + H⁺ → NH₄⁺</text>
          </g>
          <g class="step s3">
            <line x1="34" y1="204" x2="436" y2="204" stroke="@@DEEP@@" stroke-width="2.4"/>
            <text x="16" y="242" font-size="16" @@FF@@ fill="@@GREY@@">on additionne</text>
            <text x="235" y="286" text-anchor="middle" font-size="22" @@FF@@ fill="@@DEEP@@" font-weight="700">CH₃COOH + NH₃ → CH₃COO⁻ + NH₄⁺</text>
            <text x="235" y="326" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">H⁺ s'élimine : il figurait des deux côtés</text>
          </g>
          <g class="step s4">
            <rect x="10" y="352" width="450" height="106" rx="13" fill="@@TINT2@@"/>
            <text x="235" y="386" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">deux contrôles, et l'équation est validée</text>
            <text x="235" y="418" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">H⁺ ne figure plus dans l'équation finale ✓</text>
            <text x="235" y="446" text-anchor="middle" font-size="17" @@FF@@ fill="@@DEEP@@">charges : 0 à gauche · (−1) + (+1) = 0 à droite ✓</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Toute réaction met en jeu deux couples</h3>
          <p style="font-size:17px">L'acide de l'un cède son proton à la base de l'autre. Jamais un couple seul : il faut quelqu'un pour prendre.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">La méthode tient en trois lignes</h3>
          <p style="font-size:17px">On écrit la demi-équation de l'acide dans le sens qui <b>cède</b>, celle de la base dans le sens qui <b>capte</b>, puis on additionne membre à membre.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le proton disparaît, et c'est le contrôle</h3>
          <p style="font-size:17px">H⁺ apparaît à droite dans la première et à gauche dans la seconde : il <b>s'élimine</b>. S'il figure encore dans l'équation finale, l'addition est incomplète.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi cette méthode plutôt que d'écrire directement</h3>
          <p style="font-size:17px">Écrire l'équation globale d'un seul jet oblige à deviner <b>qui cède et qui prend</b>, et c'est là que l'erreur se produit.<br><br>Les deux demi-équations, elles, s'écrivent sans réfléchir : chaque couple n'a qu'un sens possible. L'addition fait le reste — et le contrôle des charges valide l'ensemble en deux secondes.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Premier couple : l'acide éthanoïque cède son proton.",
      "Second couple : l'ammoniac le capte.",
      "On additionne les deux demi-équations membre à membre — et H⁺ s'élimine.",
      "L'équation finale ne contient plus aucun proton libre.",
      "<em>Et le contrôle des charges</em> valide l'écriture en deux secondes."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH7-03 ==================== -->
  <section class="slide" data-ref="ANIM-CH7-03" data-title="Les espèces amphotères" data-sub="L'eau, qui joue les deux rôles" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D3@@
          <g class="step s1">
            <rect x="140" y="160" width="190" height="80" rx="14" fill="@@SFA@@"/>
            <text x="235" y="212" text-anchor="middle" font-size="34" @@FF@@ fill="#FFFFFF" font-weight="700">H₂O</text>
          </g>
          <g class="step s2">
            <rect x="140" y="30" width="190" height="80" rx="14" fill="@@TINT@@" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="235" y="82" text-anchor="middle" font-size="32" @@FF@@ fill="@@DEEP@@" font-weight="700">H₃O⁺</text>
            <line x1="235" y1="152" x2="235" y2="120" stroke="@@SFA@@" stroke-width="3.4" marker-end="url(#v3)"/>
            <text x="252" y="142" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">elle capte un H⁺</text>
            <text x="235" y="398" text-anchor="middle" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">couple H₃O⁺/H₂O — l'eau y est la base</text>
          </g>
          <g class="step s3">
            <rect x="140" y="290" width="190" height="80" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="235" y="342" text-anchor="middle" font-size="32" @@FF@@ fill="@@DEEP@@" font-weight="700">OH⁻</text>
            <line x1="235" y1="248" x2="235" y2="280" stroke="@@RED@@" stroke-width="3.4" marker-end="url(#r3)"/>
            <text x="252" y="278" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">elle cède un H⁺</text>
            <text x="235" y="426" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">couple H₂O/OH⁻ — l'eau y est l'acide</text>
          </g>
          <g class="step s4">
            <text x="235" y="458" text-anchor="middle" font-size="18" @@FF@@ fill="@@DEEP@@" font-weight="700">amphotère : le rôle dépend du partenaire</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Ce que veut dire amphotère</h3>
          <p style="font-size:17px">Une espèce qui peut se comporter <b>en acide ou en base</b>, selon ce qu'elle rencontre. Son rôle n'est pas une propriété fixe.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'eau est le cas type</h3>
          <p style="font-size:17px">Elle appartient au couple <b>H₃O⁺/H₂O</b>, où elle est la base, et au couple <b>H₂O/OH⁻</b>, où elle est l'acide. Les deux sont vrais simultanément.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le second exemple à citer</h3>
          <p style="font-size:17px">L'ion <b>hydrogénocarbonate HCO₃⁻</b>. Il peut céder son H ou capter un proton — et c'est lui qui régule le pH du sang.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Le pont avec la biologie, et il vaut la peine d'être dit</h3>
          <p style="font-size:17px">Le pH du sang tient entre <b>7,35 et 7,45</b>. En dehors de cet intervalle d'un dixième d'unité, les protéines se dénaturent.<br><br>C'est le couple HCO₃⁻/H₂CO₃ qui maintient cet équilibre : il absorbe les protons quand il y en a trop, en libère quand il en manque. Un amphotère n'est donc pas une curiosité de cours — c'est ce qui rend la vie possible.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "L'eau, au centre. Et deux chemins possibles.",
      "Elle peut <b>capter</b> un proton : elle devient H₃O⁺, et elle joue la base.",
      "Elle peut aussi en <b>céder</b> un : elle devient OH⁻, et elle joue l'acide.",
      "Une espèce qui fait les deux est dite <b>amphotère</b>.",
      "<em>Le second exemple :</em> l'hydrogénocarbonate, qui régule le pH du sang."
    ]</script>
  </section>

  <!-- ==================== ANIM-CH7-04 ==================== -->
  <section class="slide" data-ref="ANIM-CH7-04" data-title="Fort ou faible : ce que Ka mesure" data-sub="Et pourquoi on préfère le pKa" data-steps="5">
    <div class="mid"><div class="split">
      <div class="col" style="flex:0 0 502px;display:flex;justify-content:center">
        <svg viewBox="0 0 470 470" width="470" height="470">
          @@D4@@
          <g class="step s1">
            <rect x="12" y="20" width="446" height="104" rx="14" fill="@@TINT@@" stroke="@@SFA@@" stroke-width="3"/>
            <text x="32" y="54" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">ACIDE FORT — dissociation totale</text>
            <text x="96" y="100" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">HA</text>
            <line x1="132" y1="92" x2="196" y2="92" stroke="@@SFA@@" stroke-width="3.6" marker-end="url(#v4)"/>
            <text x="278" y="100" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">H⁺ + A⁻</text>
            <text x="404" y="100" text-anchor="middle" font-size="19" @@FF@@ fill="@@SFA@@" font-weight="700">Ka grand</text>
          </g>
          <g class="step s2">
            <rect x="12" y="140" width="446" height="104" rx="14" fill="#FFFFFF" stroke="@@DEEP@@" stroke-width="2.6"/>
            <text x="32" y="174" font-size="19" @@FF@@ fill="@@DEEP@@" font-weight="700">ACIDE FAIBLE — équilibre</text>
            <text x="96" y="220" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">HA</text>
            <line x1="132" y1="204" x2="196" y2="204" stroke="@@RED@@" stroke-width="3.2" marker-end="url(#r4)"/>
            <line x1="196" y1="222" x2="132" y2="222" stroke="@@RED@@" stroke-width="3.2" marker-end="url(#r4)"/>
            <text x="278" y="220" text-anchor="middle" font-size="26" @@FF@@ fill="@@DEEP@@" font-weight="700">H⁺ + A⁻</text>
            <text x="404" y="220" text-anchor="middle" font-size="19" @@FF@@ fill="@@RED@@" font-weight="700">Ka petit</text>
          </g>
          <g class="step s3">
            <line x1="@@PX0@@" y1="@@PY@@" x2="@@PX1@@" y2="@@PY@@" stroke="@@GREY@@" stroke-width="2.4"/>
            <text x="@@PX1@@" y="@@PYL@@" text-anchor="end" font-size="17" @@FF@@ fill="@@GREY@@">pKa</text>
            @@REP@@@@VAL@@
            <text x="34" y="296" font-size="18" @@FF@@ fill="@@SFA@@" font-weight="700">acide fort</text>
            <text x="436" y="296" text-anchor="end" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">acide faible</text>
          </g>
          <g class="step s4">
            <rect x="10" y="412" width="450" height="46" rx="12" fill="@@TINT2@@"/>
            <text x="235" y="441" text-anchor="middle" font-size="18" @@FF@@ fill="@@RED@@" font-weight="700">pKa = − log Ka : le signe moins inverse le sens</text>
          </g>
        </svg>
      </div>
      <div class="col" style="flex:1;display:flex;flex-direction:column;gap:11px">
        <div class="card step s1" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Fort : la dissociation est totale</h3>
          <p style="font-size:17px">L'acide cède <b>tout</b> son proton. La réaction est complète, et on écrit une <b>flèche simple</b>. C'est exactement l'électrolyte fort de CH4-B.</p></div>
        <div class="card acc step s2" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Faible : elle est partielle</h3>
          <p style="font-size:17px">Une partie seulement se dissocie, un <b>équilibre</b> s'installe, et on écrit une <b>double flèche</b>. La constante Ka mesure jusqu'où va cet équilibre.</p></div>
        <div class="card step s3" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">Pourquoi on passe au pKa</h3>
          <p style="font-size:17px">Les Ka s'étendent sur des <b>dizaines de puissances de dix</b> : impossible de les comparer de tête. Le logarithme ramène tout sur une échelle de 0 à 14.</p></div>
        <div class="card deep step s5 rise" style="padding:14px 22px"><h3 style="margin-bottom:6px;font-size:18px">L'erreur la plus fréquente du chapitre</h3>
          <p style="font-size:17px">« Plus le pKa est grand, plus l'acide est fort » — c'est faux, et c'est le réflexe que produit le Ka.<br><br>Le pKa est un <b>moins</b> logarithme : il <b>inverse</b> le sens. Ka grand = acide fort = pKa <b>petit</b>. Et le classement des bases conjuguées est exactement l'inverse de celui des acides.</p></div>
      </div>
    </div></div>
    <script type="application/json" class="caps">[
      "Un acide fort cède tout : flèche simple, dissociation totale.",
      "Un acide faible n'en cède qu'une partie : double flèche, et un équilibre.",
      "La constante <b>Ka</b> mesure jusqu'où va cet équilibre — grand pour un acide fort.",
      "Mais les Ka couvrent des dizaines de puissances de dix : on passe au <b>pKa</b>.",
      "<em>Et le signe moins inverse tout :</em> plus le pKa est petit, plus l'acide est fort."
    ]</script>
  </section>
"""

SLIDES = finish(SLIDES, {
    "D1": defs(1), "D2": defs(2), "D3": defs(3), "D4": defs(4),
    "REP": REPERES, "VAL": VALEURS,
    "PX0": str(PKA_X0), "PX1": str(PKA_X1), "PY": str(PKA_Y), "PYL": str(PKA_Y - 14),
    "SFA": SFA, "DEEP": DEEP, "TINT": TINT, "TINT2": TINT2,
    "GREY": GREY, "INK2": INK2, "RED": RED,
})

print("CH7-A : echelle pKa %d..%d px · reperes %s"
      % (PKA_X0, PKA_X1, ["%.0f" % xpka(p) for _, p, _ in ACIDES]))
print("ok", make("CH7-A", "Capsule CH7-A — Couples acide-base et équilibrage · 4 animations",
                 SLIDES, os.path.join(_ICI, "anim_CH7A.html")))
