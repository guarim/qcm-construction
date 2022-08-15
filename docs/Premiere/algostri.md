
{% set num = 9 %}
{% set titre = "Algorithmes de tri"%}
{% set theme = "algorithmique" %}
{% set niveau = "premiere"%} 


{{ titre_chapitre(num,titre,theme,niveau)}}
 
## Activités 

{{ titre_activite("Tri par sélection",[],0) }}

0. Commencer par télécharger une application Python :

    * {{telecharger("Tri par sélection","./files/C9/activite1.zip")}}
    * Copier ce fichier dans le répertoire de votre choix
    * Faire un clic droit sur le fichier compressé et choisir *Extraire ici*
    * Lancer le programme Python `activite1.py`, en tapant `python activite1.py` dans un terminal ou depuis Vs Code (en ayant ouvert le dossier contenant le fichier activite1.py)

1. Dans cette activité, on doit ranger des cartes par ordre croissant mais **sans les voir**, on dispose par contre de deux boutons :

    * Un bouton <span class=encadre>Trouver la plus petit carte depuis l'emplacement</span> qui permet de savoir quelle carte est la plus petite à partir de l'emplacement qu'on sélectionne dans le menu déroulant à côté.
    * Un bouton <span class=encadre>Echanger les cartes situés aux emplacements</span> qui permet d'échanger les cartes situés aux emplacements sélectionnés dans les menus déroulants.


    Voici une capture d'écran de l'application dans laquelle on vient de sélectionner la plus petite carte depuis l'emplacement 0, elle est alors indiquée par une flèche rouge au-dessus (emplacement 6) :
    ![capture](./images/C9/act1.png){: .centre}

2. Proposer un algorithme permettant à un ordinateur de ranger une suite de nombres par ordre croissant.

3. Implémentation en python

    1. Ecrire une fonction `echange(liste,i,j)` qui échange les éléments d'indice `i` et `j` de la liste `liste` par exemple si `liste=[12,17,10,11,32]` alors après `echange(liste,0,2)` le contenu de `liste` sera `[10,17,12,11,32]`.
    2. Ecrire une fonction `min_depuis(liste,i)` qui renvoie le minimum de la liste `liste` à partir de l'indice `i` par exemple `min_depuis([10,17,12,11,32],2)` renvoie `11`.
    3. En utilisant ces deux fonctions, proposer une implémentation en Python de l'algorithme du tri par sélection.

{{ titre_activite("Tri par insertion",[]) }}

1. De même que dans l'activité précédente, commencer par télécharger une application Python :

    * {{telecharger("Tri par insertion","./files/C9/activite2.zip")}}
    * Copier ce fichier dans le répertoire de votre choix
    * Faire un clic droit sur le fichier compressé et choisir *Extraire ici*
    * Lancer le programme Python `activite2.py`, en tapant `python activite2.py` dans un terminal ou depuis Vs Code (en ayant ouvert le dossier contenant le fichier activite2.py)

2. De même que dans l'activité précédente, il faut ranger les cartes dans l'ordre *sans les voir*, on dispose d'un unique bouton permettant d'échanger une carte dont on donne le numéro avec sa voisine *si elles ne sont pas dans le bon ordre*

3. Proposer un algorithme permettant de ranger une liste par ordre croissant en utilisant comme seul *"ingrédient"* l'échange de deux cartes dont on donne les emplacements.

    !!! aide
        Bien évidemment, des boucles et des tests seront aussi nécessaires


4. Proposer une implémentation en Python de cet algorithme 

    !!! aide
        On pourra utiliser la fonction `echange` définie dans l'activité précédente.

5. Tester cette fonction

## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Fonctionnement du tri par sélection",[],0) }}

1. Ecrire les étapes du tri par sélection pour la liste `[12,19,10,13,11,15,9,14]`
2. Même question pour la liste `["P","R","O","G","R","A","M","M","E"]

{{ exo("Fonctionnement du tri par insertion",[]) }}

1. Ecrire les étapes du tri par insertion pour la liste `[12,19,10,13,11,15,9,14]`
2. Même question pour la liste `["P","R","O","G","R","A","M","M","E"]

{{ exo("Tri par ordre décroissant",[])}}

1. On donne ci-dessous l'implémentation du tri par sélection vu en cours :
```python
def tri_selection(liste):
    longueur = len(liste)
    for ind in range(longueur):
        ind_min = min_liste(liste,ind)
        echange(liste,ind,ind_min)
```
Modifier cette fonction afin d'effectuer un tri dans l'ordre décroissant.

2. Même question pour l'algorithme du tri par insertion ci-dessous :
```python
def tri_insertion(liste):
    for ind in range(1,len(liste)-1):
        j = ind
        while liste[j+1]<liste[j] and j>=0:
            echange(liste,j,j+1)
            j=j-1
```

{{ exo("Tri dans une nouvelle liste",[])}}

Les algorithmes vus en cours modifient la liste donnée en paramètre, on dit qu'on effectue un *tri en place* c'est à dire directement dans la liste.

1. Modifier la fonction de tri par sélection vu en classe afin d'effectuer le tri en créant une nouvelle liste (et donc sans modifier la liste de départ)
2. Même question pour le tri par insertion

!!! aide
        Comme une *nouvelle liste* est crée, on utilisera l'instruction `return` pour la renvoyer vers le programme principal. 

{{ exo("Comparaison de temps d'exécution",[])}}

1. Ecrire une fonction `hasard(n,mini,maxi)` qui renvoie une liste de `n` nombres entiers tirés au sort entre `mini` et `maxi`.
    
    !!! aide
        Utiliser la fonction `randint` du module random
    
2. En utilisant le module `time` de Python, donner une estimation du temps d'exécution de l'algorithme du tri par sélection vu en cours lorsque la taille de la liste augmente. On pourra utiliser un tableau comme :

    |Taille de la liste | Temps d'exécution|
    |-------------------|------------------|
    | $20\,000$ | ...... |
    | $40\,000$ | ...... |
    | $100\,000$ | ...... |
    | .... | ...... |

3. En utilisant un tableur, tracer la courbe d'évolution du temps d'exécution en fonction de la taille de la liste. Le résultat était-il prévisible ? Justifier en citant un résultat du cours.

4. La méthode `sort` des listes de Python permet de trier une liste de Python, par exemple si `liste=[5,19,11,13]`, après l'exécution de `liste.sort()`, le contenu de liste devient : `liste = [5,11,13,19]`. Faire un tableau de mesures de temps d'exécution de `sort` en faisant varier la longueur de la liste comme ci-dessus.

5. Avec le tableur, représenter sur le même graphique les mesures de temps d'exécution pour l'algorithme du tri par sélection et pour la méthode `sort`. Que remarquez-vous ?


{{ exo("Compléxité",[])}}

1. Ecrire une fonction `cherche_min` qui prend en argument une liste et renvoie son minimum.

2. Pour une liste de $n$ éléments, quel sera le nombre maximal de comparaisons effectué par votre fonction `cherche_min`. En déduire sa complexité.

3. Mesurer le temps d'exécution de votre fonction pour une liste de $500\,000$ éléments, prédire le temps pour une liste de $1\,500\,000$.

2. Jérémy a mesuré que son implémentation du tri par insertion permet de trier une liste de $10\,000$ éléments en environ 0.3 secondes.

    a. Estimer le temps nécessaire pour trier une liste de $200\,000$ éléments

    b. Même question pour une liste de $500\,000$ éléments.
    
    c. Peut-on utiliser ce programme pour trier une liste de un milliard d'éléments ? Justifier

{{ exo("Tri à bulles",[])}}

1. En effectuant vos propres recherches sur le *web*, expliquer le principe du **tri à bulles**.
2. Détailler le fonctionnement de cet algorithme de tri sur la liste suivante : `[12,9,17,11,3]`
3. Programmer cet algorithme en python

    !!! aide
        On pourra utiliser la fonction `echange(liste,i,j)` déjà programmée en cours. 


{{ exo("Liste triée",[])}}

1. Ecrire une fonction `est_triee` qui prend en argument une `liste` et qui renvoie `True` si `liste` est triée par ordre croissant et `False` dans le cas contraire.

    !!! Attention
        On ne doit pas trier la liste, simplement vérifier si elle l'est déjà ou pas.

2. Ajouter un paramètre  `reverse` à cette fonction de façon à vérifier si la liste est trié par ordre croissant (`reverse=False`) ou décroissant (`reverse=True`).

