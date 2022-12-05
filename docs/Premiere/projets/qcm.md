# QCM


Le but du projet est de programmer un jeu de type {{sc("qcm")}} à la façon du célèbre jeu télévisé [qui veut gagner des millions](https://fr.wikipedia.org/wiki/Qui_veut_gagner_des_millions_%3F){target=_blank}. Une interface graphique est nécessaire et pourra être réalisé au choix de l'élève à l'aide de `turtle`, `pyxel` ou d'outils plus élaborés. Les questions devront être stockés dans un fichier externe au format `csv`.

## Etape 1 :  Faire l'interface graphique

On suppose dans un premier temps que les questions proposent à chaque fois quatre choix et qu'un seul est correct. On devra donc proposer une interface graphique permettant d'afficher :

* l'enoncé de la question
* les quatres choix possibles

on pourra s'inspirer de celle du jeu *qui veut gagner des millions* ?

## Etape 2 : Ecriture des questions

Créer un fichier `csv` contenant les énoncés des questions ainsi que la bonne réponse et les trois mauvaises.
Le thème des questions est laissé libre (et on peut même créer plusieurs fichiers), cependant un questionnaire sur Python permettrait de réviser le cours tout en faisant son projet !

## Etape 3 : Interaction avec le joueur

Afficher une question dans l'interface et récupérer la réponse du joueur (à l'aide d'un `textinput` de `turtle` par exemple)

## Etape 4 : Partie complète

Proposer de jouer une partie complète (déroulé de toutes les questions du fichier `csv`) puis afficher le score du joeur.

## Etape 5 : Aller plus loin

Améliorer le jeu par exemple en proposant :  
    * un indicateur de difficulté à chaque question (et donc un score différent)
    * de jouer à la souris
    * de proposer au joueur de créer ses propres questions
    * gérer le cas ou certaines questions acceptent plusieurs réponses possibles
    * ...
