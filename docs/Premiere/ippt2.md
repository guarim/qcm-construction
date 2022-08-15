
{% set num = 5 %}
{% set titre = "Initiation à Python avec Turtle"%}
{% set theme = "python"%}
{% set niveau = "premiere"%} 

{{ titre_chapitre(num,titre,theme,niveau)}}
 
## Activités 

{{ titre_activite("Retour sur le jeu du pendu",["rappel"],0) }}

#### Rappels
1. Télécharger ci-dessous le programme déjà entamé sur le jeu du pendu :
{{ telecharger("Debut du jeu du pendu","./files/C5/debut-pendu.py")}}
2. Ouvrir ce fichier dans VS Code, que nous utiliserons à présent comme éditeur
3. Relire ce fichier

#### Interaction avec le joueur

Pour demander une lettre  on utilise `feuille.textinput(titre, question)` qui crée une fenêtre dans laquelle l'utilisateur peut taper sa réponse. Les paramètres `titre` et `question` permettent de spécifier le titre de cette fenêtre et d'écrire le texte de la question.
Par exemple :

```python
lettre = feuille.textinput("Proposer une lettre", "Quelle lettre proposez-vous ?")
```
 affichera :
![textinput](./images/C5/textinput.png){: .imgcentre}

1. Tester cette instruction en l'intégrant dans le programme.
2. Cette instruction n'accepte-t-elle qu'une lettre comme voulu dans le programme ?
3. Pour vérifier que le joueur propose bien une unique lettre, on écrit une fonction qui renverra la saisie de l'utilisateur seulement si elle est valide. On introduit donc ici l'instruction `return` (**renvoyer** en français), qui permet à une fonction de transmettre un résultat au reste du programme :

```python linenums="1"
def demander_lettre():
    lettre = feuille.textinput("Proposer une lettre", "Quelle lettre proposez-vous ?")
    # On ajoutera ici la validation de la saisie
    return lettre
```

Il nous reste à valider la saisie avant de renvoyer la lettre via l'utilisation d'une **instruction conditionnelle**.

#### Instruction conditionnelle

L'instruction conditionnelle permet de traduire en python le traitement suivant :

> **si** la saisie est une lettre de l'alphabet <br>
**alors** afficher le message "lettre acceptée" et renvoyer cette lettre<br>
**sinon** afficher un avertissement et renvoyer une chaîne de caractères vide

```python linenums="1"
def get_lettre():
    lettre = feuille.textinput("Proposer une lettre", "Quelle lettre proposez-vous ?")
    if len(lettre) == 1 and lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        efface_message()
        affiche_message("Lettre acceptée")
        return lettre
    else:
        efface_message()
        affiche_message("Il faut saisir une lettre majuscule")
        return ""
```

Les fonctions `affiche_message` et `efface_message` vous sont données :

!!! note "Afficher et effacer des messages"

    ```python
    def affiche_message(message):
        crayon.penup()
        crayon.goto(0,300)
        crayon.pendown()
        crayon.write(message, font=("Arial",24,"bold"),align="center")

    def efface_message():
        crayon.penup()
        crayon.goto(0,300)
        crayon.pendown()
        crayon.color("beige")
        crayon.write(chr(0x2588)*40, font=("Arial",24,"bold"),align="center")
        crayon.color("black")
    ```

!!! exercice "A faire vous-même"

    1. Copier-coller les trois nouvelles fonctions
    2. Écrire une boucle `for` dans votre programme permettant d'appeler `get_lettre` à cinq reprises pour tester cette fonction.


#### Boucle non bornée

La boucle `for`, déjà rencontrée permet de répéter des instructions un nombre **déterminé** de fois, on parle dans ce cas, de **boucles bornées**. La situation ici est différente, on ne connaît pas le nombre d'erreurs que va commettre le joueur avant de découvrir le mot. On utilise une **boucle non bornée** en spécifiant sa condition d'arrêt, en français cela donne : *tant que* le nombre d'erreurs possibles (limité à 6), n'est pas atteint répéter la demande d'une lettre. Ou encore en Python:

```python
nb_erreurs = 0
while nb_erreurs<7:
    lettre=get_lettre()
```

!!! exercice "A faire vous-même"

    Dans votre programme, remplacer la boucle `for` que vous aviez mise précédemment par les lignes ci-dessus et constater que la boucle est pour le moment infinie puisque la variable `nb_erreurs` reste à 0. 

#### Encore des instructions conditionnelles ...

Il faut donc mettre à jour l'affichage du jeu en fonction de la réponse du joueur :

* si la lettre fait  partie du mot, alors on écrit cette lettre dans la case ou les cases correspondantes ; cette tâche est réalisée par la fonction `ecrit_lettre` dont la définition vous est donnée :

```python
def ecrit_lettre(mot, lettre):
    x = -50*len(mot)//2
    for l in mot:
        if l == lettre:
            crayon.penup()
            crayon.goto(x+20,-250)
            crayon.pendown()
            crayon.write(lettre,font=("Arial",24,"bold"),align="center")
        x+=50
```

* sinon on incrémente le nombre d'erreurs :

```python
nb_erreurs = 0
while nb_erreurs < 7:
    lettre = get_lettre()
    # On teste si une lettre a bien été proposée (sinon c'est la chaine vide qui est renvoyée)
    if lettre != "":
        if lettre in MOT:
            ecrit_lettre(MOT, lettre)
        else:
            nb_erreurs+=1
```

!!! exercice "A faire vous-même"

    Dans votre programme, remplacer la boucle précédente par celle-ci, et vérifier qu'à présent la boucle se termine après 7 erreurs.

#### Dessin du pendu correspondant au nombre d'erreurs

Après la mise à jour de `nb_erreurs`, on voudrait modifier en conséquence le dessin du pendu. On doit donc écrire une fonction `tracer_pendu` qui prend en paramètre le nombre d'erreurs commises par le joueur et trace le dessin correspondant. 

!!! exercice "A faire vous-même"

    Compléter la définition de cette fonction :

    ```python
    def tracer_pendu(nb):
        if nb == 1:
            pendu_1()
        elif nb == 2:
            pendu_2()
        elif nb == ...:
            pendu_....
        ......
    ```

    Remarquer l'instruction `elif` contraction de `else if`.


#### Appel de cette fonction dans la boucle

!!! exercice "A faire vous-même"

    Compléter la boucle `while` en y incluant l'appel à cette fonction lorsque le nombre d'erreurs augmente.

#### Victoire du joueur

Ajouter les instructions permettant  la prise en compte de la victoire du joueur et l'arrêt du jeu dans ce cas.

{{ titre_activite("Les listes de Python",[]) }}

{{ telecharger("Jupyter Notebook","./notebook/6.Liste-1.ipynb") }}

{{ titre_activite("Parcours d'une liste",[]) }}

{{ telecharger("Jupyter Notebook","./notebook/6.Liste-2.ipynb") }}

## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}} 

## Exercices

{{ exo("Lignes",[],0)}}

1. En utilisant une boucle `for` contenant une instruction conditionnelle, écrire un programme Python permettant de tracer la figure suivante :
![Lignes](./images/C5/ex1.png){: .imgcentre}
La ligne centrale est tracé avec un crayon d'épaisseur 4 et en couleur *darkred*, toutes les autres lignes sont d'épaisseur 2 et en couleur *navy*.

2. Modifier l'instruction conditionnelle contenue dans le boucle `for` de façon à ce que les lignes au dessus de la ligne centrale soient tracées en couleur *green*.

{{ exo("Suite de carrés",[])}}

Ecrire un programme python permettant de dessiner la figure ci-dessous :
![Carrés](./images/C5/ex2.png){: .imgcentre}
Votre programme devra contenir :

* la définition d'une fonction `carre` et des appels à cette fonction,
* une boucle,
* une instruction conditionnelle.

{{ exo("Génération de listes en Python",[])}}

1. On considère le programme suivant :
```python
liste1 = [0]*100
liste2 = [0 for k in range(100)]
liste3 = []
for k in range(100):
    liste3.append(0)
```

    1. Quel est le contenu de chacune des listes ?
    2. Indiquer par quel procédé chacune de ces listes a été crée.

2. Ecrire un programme python permettant de créer les listes suivantes :
    1. Une liste contenant 12 fois le chiffre 7.
    2. La liste des nombres entiers de 1 à 100.
    3. Une liste contenant 1000 nombres tirés au sort entre 1 et 6.

        !!! Aide 
            On rappelle que la fonction `randint` peut être importer depuis le module `random`, elle permet de tirer un nombre en deux valeurs `a` et `b` données en paramètres.

    4. La liste des cubes des entiers de 1 à 10.


{{ exo("Parcours de listes en Python",[])}}

On suppose qu'on dispose d'une liste de notes, on veut écrire une fonction qui renvoie le nombres de notes qui sont en dessous de la moyenne. 

1. On considère une première version de cette fonction :
```python
def inferieur_moyenne(liste_notes):
	nb = 0
	for note in liste_notes:
	    if .....:
	    	nb = .......
	return ...
```
    1. Recopier et compléter cette fonction
    2. Tester cette fonction 

2. Voici une deuxième version de cette fonction :
```python
def inferieur_moyenne(liste_notes):
	nb = 0
	for indice in ........:
	    if ........... : 
	    	nb = .......
	return ...
```
    1. Recopier et compléter cette fonction
    2. Tester cette fonction

3. Quelle est la différence principale entre ces deux versions de la même fonction ?
4. Ecrire les fonctions suivantes :
    
    1. `max_liste` qui prend comme argument une liste non vide de nombres et renvoie le plus grand de ces nombres.
    2. `somme_liste` qui prend comme argument une liste non vide de nombres et renvoie la somme de ces nombres.
    3. `moyenne_liste` qui prend comme argument une liste non vide de nombres et renvoie la moyenne de ces nombres.


{{ exo("Recherche d'occurences",[])}}

1. Ecrire une fonction `present(elt,liste)` qui renvoie `True` si `elt` se trouve dans la liste `liste` et `False` sinon. Par exemple `present(3,[1,4,5]` renvoie `False`, par contre `present(4,[1,4,5]` renvoie `True`.
2. Tester cette fonction
3.  Ecrire une fonction `occurence(elt,liste)` qui renvoie le nombre de fois où `elt` apparaît dans `liste`.


{{ exo("Chaines de caractères",[]) }}

1. Ecrire une fonction `compte_caractere(s,c)` qui prendre en argument une chaîne de caractère `s` et un caractère `c` et retourne le nombre de fois où `c` apparait dans `s`. Par exemple `compte_caractere("informatique","i"")` renvoie 2 puisqu'il y a deux `i` dans le mot `informatique`
2. Ecrire une fonction `inverse` qui prend en argument une chaîne de caractère et retourne cette chaîne écrite à l'envers. Par exemple, `inverse("Python")` donnera `"nohtyP"`.
3. Ecrire une fonction `compare` qui prend en argument deux chaînes de caractères et renvoie le nombre de fois où ces deux chaines on la même lettre au même emplacement. Par exemple, `compare("Python","Poterie")` retourne 2 car le "P" et le "t" sont situés aux mêmes emplacements dans les deux mots.

