# -*- coding: utf-8 -*-
"""Trames de tournage — physique. Même rendu que le dossier de mathématiques."""
import pathlib
import render_caps as R
import data_CH1, data_CH2, data_CH3

CHS = (data_CH1.CHAPITRES + data_CH2.CHAPITRES
       + data_CH3.CHAPITRES)

# rang de tournage (sur les 17 capsules du programme de chimie)
_r = 0
for _ch in CHS:
    for _c in _ch["caps"]:
        _r += 1
        _c["rang"] = _r
        _c["total"] = 17

# tableau annexe des animations, construit à partir des pastilles réellement posées
for _ch in CHS:
    _t, _lettre = [], "ABCDEFGH"
    for _c in _ch["caps"]:
        _bloc = -1
        for _it in _c["t2"]:
            if _it[0] == "h":
                _bloc += 1
            elif _it[0] == "anim":
                _t.append((_it[1], _it[2], f'{_c["code"]} · bloc {_lettre[_bloc]}'))
    _ch["anims"] = _t

N_CAPS = sum(len(c["caps"]) for c in CHS)
N_ANIM = sum(len(c["anims"]) for c in CHS)
N_EXOS = sum(len(cap["t3"]) for c in CHS for cap in c["caps"])

COVER = f"""
<header class="masthead">
  <p class="org">SFA · Science For All — Prépa médecine · Bullet points de tournage · Chimie</p>
  <h1>Les dix-sept capsules de chimie,<br><em>point par point.</em></h1>
  <p class="lede">La trame de tournage de l'intégralité de la chimie, alignée sur le <b>programme ARES
  version 10</b> — les dix chapitres, des cinq sections A à E. Ces bullet points ne sont pas un texte à
  lire : ce sont les points essentiels à la compréhension de l'étudiant, dans l'ordre où il faut les dire.
  Le professeur parle avec ses mots, mais ne saute rien et ne change pas l'ordre.</p>
</header>

<div class="box key">
  <span class="lab">Mode d'emploi</span>
  <p>Chaque capsule suit les <b>trois temps</b> du protocole : introduction du concept, explication avec
  schéma animé, correction d'exercices déjà écrits. Les minutages sont des repères ; la seule contrainte
  est la fourchette <b>15 à 35 minutes</b>.</p>
  <p>Les pastilles <span class="anim">ANIM-CH0-00</span> marquent le moment exact où l'animation SFA doit
  apparaître. Les lignes <span style="color:#C02A20"><b>en rouge</b></span> sont les <b>pièges du
  concours</b> : ce sont elles qui font gagner des points, elles ne se sautent jamais.</p>
</div>

<div class="box key">
  <span class="lab">Les exercices sont prêts à être projetés</span>
  <p>Chaque capsule se termine par <b>trois exercices, énoncé et correction complète déjà rédigés</b> —
  <b>cinquante et un au total</b>. Le cadre vert est la <b>zone à capturer</b> : le professeur en fait une
  capture d'écran, la projette pendant le tournage et la commente au pointeur laser, étape par étape. Il
  n'écrit rien en direct.</p>
  <p>La dernière étape de chaque correction est <b>surlignée</b> : c'est la conclusion, celle sur laquelle
  on s'arrête et qu'on entoure au pointeur. La ligne grise
  <span class="tagoff" style="display:inline-block">hors capture</span> sous le cadre n'est <b>pas</b>
  destinée à l'écran : c'est le commentaire pédagogique que le professeur dit à voix haute.</p>
  <p><b>Toutes les valeurs numériques des cinquante et une corrections ont été recalculées</b> et vérifiées
  une à une, masses molaires comprises.</p>
</div>

<div class="box warn">
  <span class="lab">La chimie est la seule matière en version 10</span>
  <p>Les mathématiques, la physique et la biologie sont alignées sur le programme <b>ARES v8</b> ; la
  chimie est la seule à être régie par la <b>v10</b>. C'est cette version qui fonde chacune des clauses
  citées ici, et c'est elle qu'il faudra surveiller en cas de mise à jour.</p>
</div>

<div class="box key">
  <span class="lab">Deux chapitres jumeaux : CH7 et CH8</span>
  <p>L'acido-basicité et l'oxydoréduction ont <b>exactement la même structure</b> : un transfert, des
  couples conjugués, des demi-équations, une table à lire et la même règle du gamma. Seul l'objet transféré
  change — un <b>proton</b> dans un cas, un <b>électron</b> dans l'autre.</p>
  <p>Cette symétrie n'est pas une coïncidence pédagogique, elle est réelle — et elle se dit à l'écran. Le
  professeur annonce en ouverture de CH8 que qui a compris CH7 possède déjà la moitié du chapitre. La
  règle du gamma, posée une fois en CH7-B, n'est <b>pas réexpliquée</b> en CH8-B : elle est rappelée.</p>
</div>

<div class="box warn">
  <span class="lab">CH3 est entièrement de soutien, et c'est dit à l'écran</span>
  <p>Le texte v10 ne nomme <b>ni</b> les structures de Lewis, <b>ni</b> la géométrie moléculaire, <b>ni</b>
  les forces intermoléculaires. Aucune des quatre notions de CH3 n'est exigée en tant que telle.</p>
  <p>Le chapitre est maintenu parce que le programme exige <b>la règle de l'octet</b> et <b>les propriétés
  des solides, des liquides et des gaz</b> — qui ne s'expliquent pas sans lui. Le professeur l'assume
  explicitement au premier temps de la capsule : c'est un choix pédagogique, il est identifiable, il est
  donc révisable.</p>
</div>

<div class="box warn">
  <span class="lab">Quatre points retirés du référentiel</span>
  <p>Quatre sujets que le référentiel SFA contenait ne sont pas nommés par le texte officiel et ont été
  retirés : la <b>pile électrochimique</b> (le programme demande de prédire avec une table, pas de monter
  un dispositif), la <b>cinétique</b> (vitesse de réaction, catalyseur), la <b>radioactivité</b>, et les
  <b>mécanismes réactionnels organiques</b> — combustion, addition, estérification. Pour ce dernier point,
  le texte demande la dénomination et les propriétés des fonctions, pas les mécanismes.</p>
</div>

<div class="box key">
  <span class="lab">Ce que la chimie doit aux mathématiques</span>
  <p>La chimie est bien moins contrainte que la physique : ses dépendances portent presque toutes sur le
  <b>calcul élémentaire</b>, posé dès la première capsule de mathématiques. Les puissances de dix (A1) sont
  employées dès CH1, la proportionnalité dans tout CH4, les systèmes linéaires (A2-B) pour pondérer en CH9.</p>
  <p>Une seule dépendance est tardive : le <b>logarithme décimal</b> de la capsule D2-A, sans lequel le pH
  ne peut pas être défini. <b>CH7-B ne peut donc pas être filmée avant la douzième capsule de
  mathématiques.</b> C'est la seule contrainte de calendrier réelle de toute la chimie.</p>
</div>

<table>
  <tr><th>Rang</th><th>Chap.</th><th>Capsules</th></tr>
  <tr><td class="first">1</td><td class="first">CH1</td><td>La mole, les masses et les unités</td></tr>
  <tr><td class="first">2-3</td><td class="first">CH2</td><td>L'atome, l'ion, et la couche de valence · Le tableau périodique et ce qu'il prédit</td></tr>
  <tr><td class="first">4</td><td class="first">CH3</td><td>Les liaisons et la cohésion de la matière</td></tr>
  <tr><td class="first">5-6</td><td class="first">CH4</td><td>États de la matière et lois des gaz · Solutions, concentrations et dissociation</td></tr>
  <tr><td class="first">7</td><td class="first">CH5</td><td>Nommer et écrire les composés inorganiques</td></tr>
  <tr><td class="first">8-9</td><td class="first">CH6</td><td>Le carbone et les groupes fonctionnels · Nommer, et l'isomérie</td></tr>
  <tr><td class="first">10-11</td><td class="first">CH7</td><td>Couples acide-base et équilibrage · Lire la table, prédire, calculer le pH</td></tr>
  <tr><td class="first">12-13</td><td class="first">CH8</td><td>Oxydant, réducteur, nombre d'oxydation · Équilibrer et prédire avec la table</td></tr>
  <tr><td class="first">14-16</td><td class="first">CH9</td><td>Pondérer et faire un bilan · Réactif limitant, gravimétrie, volumétrie · Rendement et calcul mental</td></tr>
  <tr><td class="first">17</td><td class="first">CH10</td><td>L'équilibre chimique et Le Chatelier</td></tr>
</table>
"""


def build(out):
    body = "\n".join(R.render_chapter(ch) for ch in CHS)
    foot = (f'<p class="foot">SFA · Science For All — bullet points de tournage, chimie · '
            f'{N_CAPS} capsules, {N_ANIM} animations, '
            f'{N_EXOS} exercices corrigés · programme ARES version 10 · '
            f'conforme au protocole de création des capsules vidéo.</p>')
    html = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8">'
            f'<title>SFA — Trames des capsules de chimie</title>'
            f'<style>{R.css(R.VERT)}</style></head><body>{COVER}{body}{foot}</body></html>')
    pathlib.Path(out).write_text(html)
    return N_CAPS, N_ANIM, N_EXOS


if __name__ == "__main__":
    print(build(str(pathlib.Path(__file__).with_name("trames_chimie.html"))))
