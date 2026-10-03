# Animations SFA — code source complet (chimie)

Tout ce qui construit les **17 capsules et 68 animations** de chimie. Rien n'est
écrit à la main en HTML : chaque fichier livré est **généré** par un script, et
cinq audits automatiques vérifient le résultat avant livraison.

---

## 1 · Démarrer

Tous les fichiers sont **à plat dans un seul dossier**, et aucun ne contient de
chemin absolu : le dossier fonctionne tel quel, où qu'on le dépose.

```bash
pip install playwright --break-system-packages
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers   # Chromium déjà présent chez SFA

for f in slides_CH*.py; do python3 "$f"; done      # construit les 17 capsules
python3 pack_anims_ch.py                           # sommaire + ZIP livrable
```

Seuls les audits ont besoin de Playwright. Construire les animations ne demande
que Python : aucune dépendance.

**Ce dossier a été vérifié depuis zéro** — copié ailleurs, vidé de ses
`anim_*.html`, puis reconstruit : 17 capsules, 68 animations, les cinq audits à
zéro, et le ZIP livrable régénéré.

Chaque `slides_*.py` écrit **un** fichier `anim_*.html` autonome : aucune
dépendance, aucun serveur, il s'ouvre dans n'importe quel navigateur.

---

## 2 · Architecture

```
shell_anim.html          le gabarit : mise en page, moteur d'étapes, autofit
   │
build_anim.py            injecte le contenu dans le gabarit, applique la palette
   │
chem.py                  outils communs aux figures de chimie (couleurs,
   │                     flèches, courbes, macro de police)
   │
slides_CH*.py  × 17      une capsule = un script = 4 animations
   │
   └──→  anim_CH*.html   le livrable
```

### Le gabarit — `shell_anim.html`

Trois jetons y sont remplacés : `@@CODE@@`, `@@TOC@@`, `@@SLIDES@@`.

La zone utile d'une diapositive fait **542 px de haut** pour une colonne de
figure de **502 px de large** — d'où le format de figure retenu, `viewBox
470 × 470`, qui occupe **93 %** de la hauteur disponible.

Deux mécanismes méritent qu'on les connaisse avant de toucher au gabarit :

- **`applySteps(s, st)`** pilote l'apparition. Une classe `sN` fait apparaître
  l'élément à l'étape N, `hN` le fait disparaître à partir de l'étape N.
- **`autofit()`** réduit une colonne de texte trop haute. Il mesure
  `scrollHeight` — la hauteur du **contenu** — et non `getBoundingClientRect`,
  qui ne donne que la boîte attribuée par le flex et peut être **plus petite que
  le contenu**. C'est le bug qui faisait passer les cartes sous le filet du pied.
  Les colonnes sont étirées (`align-items:stretch`) et non centrées : le contenu
  part du haut, et les cartes ne remontent plus à chaque apparition — ce qui
  compte pour le tournage.

### La boîte à outils — `chem.py`

```python
defs(n)          # marqueurs de flèches, ids v<n> / d<n> / r<n>
curve(f, …)      # trace y = f(x), points calculés et non estimés
finish(s, subs)  # remplace les macros @@XXX@@
make(…)          # construit le fichier, palette verte
```

Une précaution à ne pas défaire : le jeton de police est **`@@FF@@`**, pas `FF`.
Une macro de deux lettres frapperait aussi les couleurs hexadécimales
(`#FFFFFF` devenait illisible, et les encadrés blancs sortaient noirs).

### Une capsule — `slides_CH*.py`

Chaque script suit la même forme :

1. les **géométries calculées en Python** (positions, échelles, grilles), avec
   des `assert` qui refusent de générer le fichier si une figure sort de son
   cadre ;
2. la chaîne `SLIDES` — quatre `<section class="slide">`, chacune avec sa
   figure SVG à gauche, ses cartes à droite, et ses cinq légendes de bas d'écran ;
3. l'appel à `finish()` puis `make()`.

**La règle qui a coûté le plus cher à apprendre : aucune coordonnée de figure
n'est estimée.** Un point qui doit tomber sur une courbe est calculé par la même
fonction qui trace la courbe. Les premières versions plaçaient les points « à
l'œil » et la droite ne passait pas par le point.

---

## 3 · Les cinq audits

Chacun a été écrit **après** un défaut réel signalé en relecture. Ils tournent
sur les fichiers construits, dans un navigateur sans interface, à **chaque
étape de chaque animation**.

| Script | Ce qu'il contrôle | Le défaut qui l'a fait naître |
|---|---|---|
| `audit_ch.py` | débordement vertical d'une colonne, facteur de réduction | cartes sous le filet du pied |
| `audit_zone.py` | espace mort en haut, débordement sous la zone utile | contenu nivelé vers le bas |
| `audit_svg.py` | élément SVG hors cadre (`getBBox` contre `viewBox`) | textes coupés à droite |
| `audit_band.py` | libellé plus large que l'aplat coloré derrière lui | texte débordant de sa pastille verte |
| `audit_collision.py` | deux libellés qui se touchent · un trait qui traverse un libellé | « ÷ M÷ N<sub>A</sub> » illisible |

```bash
python3 audit_svg.py       "anim_CH*.html"
python3 audit_band.py      "anim_CH*.html"
python3 audit_collision.py "anim_CH*.html"
python3 audit_zone.py      "anim_CH*.html" 60 2
python3 audit_ch.py
```

État au moment de la livraison : **zéro sur les cinq**, 68 animations.

`audit_collision.py` ne compare que les éléments **réellement visibles** à
l'étape examinée : un élément `.step` sans la classe `.on` n'est pas encore
apparu et ne doit pas compter.

---

## 4 · Le livrable — `pack_anims_ch.py`

Construit `SFA_Animations_Chimie_17_capsules.zip` : les 17 fichiers numérotés
dans l'ordre de tournage, précédés d'un `00_SOMMAIRE.html`.

Le sommaire **relit les fichiers HTML construits** et en extrait les `data-ref`,
`data-title` et `data-sub`. Il ne peut donc ni citer une animation qui n'existe
pas, ni en oublier une. Les titres de capsules et de chapitres viennent de
`render_trames_ch.py`, de sorte que le sommaire et le dossier de trames ne
peuvent pas diverger.

---

## 5 · La charte

```python
# chimie — vert
SFA, DEEP, TINT, TINT2 = "#0F7A4F", "#08402A", "#E4F2EA", "#C2E0D0"
# mathématiques et physique — bleu
SFA, DEEP, TINT, TINT2 = "#1D4ED8", "#0A2A6E", "#E9EEFC", "#D3DEFA"
```

Tous les contrastes ont été vérifiés : AA ou mieux.

`build_anim.py` applique la palette par substitution dans le gabarit, qui reste
donc unique pour toutes les matières.

---

## 6 · Ce qui reste à faire

- **Le logo.** Il est encore un placeholder typographique dans les 17 fichiers,
  marqué `/* REMPLACER PAR LE VRAI LOGO */`. Le remplacement tient en une ligne
  dans `shell_anim.html` :
  `<img src="logo-sfa.svg" style="height:44px">`. Le fichier vectoriel n'a
  jamais été fourni.
- **La physique.** Architecture et trames prêtes — 20 capsules, 80 animations.
  Les `slides_PH*.py` restent à écrire, en bleu, sur le gabarit corrigé.
- **La biologie.** Rien n'est commencé : 10 chapitres, 19 capsules, couleur à
  choisir.

---

## 7 · Ajouter une capsule

1. Copier le `slides_CH*.py` le plus proche structurellement.
2. Calculer les géométries en Python, avec les `assert` qui vont avec.
3. Construire : `python3 slides_XX.py`.
4. Passer les cinq audits sur le seul fichier neuf.
5. Le déclarer dans `data_CH*.py` (bloc `anim`) pour qu'il entre au sommaire.
6. Reconstruire le dossier : `python3 pack_anims_ch.py`.

L'étape 4 n'est pas facultative : sur 68 animations, les audits ont attrapé
**21 défauts** qu'une relecture à l'œil avait laissés passer.
