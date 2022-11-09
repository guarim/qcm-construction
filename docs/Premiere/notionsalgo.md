
{% set num = 6 %}
{% set titre = "Recherche dans une liste"%}
{% set theme = "algorithmique"%}
{% set niveau = "premiere"%} 


{{ titre_chapitre(num,titre,theme,niveau)}}
 
## Activités 

{{ titre_activite("Rechercher dans une liste",[],0) }}

On souhaite écrire une fonction `recherche(element,liste)` en Python qui renvoie `True` ou `False` suivant que `element` se trouve ou non dans `liste`. On donne ci-dessous la réponse d'un élève :

```python linenums="1"
def recherche(element,liste):
    ''' Renvoie True si element est dans liste, False sinon '''
    for x in liste:
        # Si x est bien égal à élément renvoyer True sinon renvoyer False
        if x=element: 
            return True
        else:
            return False
```

1. Recopier ce code puis corriger l'erreur commise sur le test d'égalité à la ligne 5.
2. Vérifier que les tests `recherche(3,[3,10,7])` et `recherche(4,[3,10,7])` renvoient les valeurs attendues.
3. En faisant un test adapté, montrer que cette fonction n'est pas correcte.
4. Doit-on renvoyer `False` si le *premier* élément testé est différent de celui recherché comme indiqué dans le commentaire ligne 4 ?
5. Corriger cette fonction.


{{ titre_activite("Recherche dichotomique",[]) }}
1. Télécharger et exécuter le programme du [jeu du nombre mystère](./files/C6/mystere.py)
    1. Faire quelques parties, expliquer la stratégie de l'ordinateur pour trouver le nombre mystère.
    2. Lorsque le nombre est compris entre 1 et 100, en combien d'essais au maximum l'ordinateur trouve-t-il la solution ?
    3. Et si le nombre mystère est compris entre 1 et 200 ?
2. En s'inspirant de cette stratégie de recherche appelée **dichotomie** (*couper en deux*), on cherche un algorithme pour déterminer si un élément se trouve ou non dans une liste. Par exemple, si on recherche $\textcolor{red}{28}$ dans $[14, 15, 17, 22, 23, 25, 29, 34, 38]$, le tableau ci-dessous représente les étapes de la méthode :

    |Etape | Liste | Milieu|Comparaison |
    |------|-------|--------------|------------|
    |:one:|$\underbrace{[\overset{\textcolor{red}{_\wedge^{0}}}{14}, 15, 17, 22,}_{ } \underset{_4^\uparrow}{\textcolor{darkblue}{23}} , \overbrace{25, 29, 34, \underset{\textcolor{red}{_8^{\vee}}}{38}]}_{ }$| $(0+8)//2 = 4$ |$\textcolor{darkblue}{23} <\textcolor{red}{28}$ |
    |:two:|$[\colorbox{lightgray}{14, 15, 17, 22,23} , \underbrace{\overset{\textcolor{red}{_\wedge^{5}}}{25}} \underset{_6^\uparrow}{\textcolor{darkblue}{29}}, \overbrace{34, \underset{\textcolor{red}{_8^{\vee}}}{38}]}_{ }$ | $(5+8)//2=6$|$\textcolor{darkblue}{29} \geq \textcolor{red}{28}$.|
    |:three:|$[\colorbox{lightgray}{14, 15, 17, 22,23} , \underset{_5^\uparrow}{\overset{\textcolor{red}{_\wedge^{5}}}{25}}, \underset{\textcolor{red}{_6^{\vee}}}{29} \colorbox{lightgray}{34,38}]$ | $(5+6)//2=5$ |$\textcolor{darkblue}{25} < \textcolor{red}{28}$.|
    |:four:|$[\colorbox{lightgray}{14, 15, 17, 22,23,25} \underset{\textcolor{red}{_6^{\vee}}}{\overset{\textcolor{red}{_\wedge^6}}{29}} \colorbox{lightgray}{34,38}]$ | - | - |

    Arrêt de l'algorithme, $28$ n'est pas dans la liste.

    1. Dès l'étape 2, on a grisé les éléments situés avant 23 pour indiquer que 28 ne s'y trouve pas. Quelle propriété de la liste le permet ?
    2. Que représente les nombres situés en rouge au-dessus (ou au-dessous) des éléments de la liste ?
    3. Quelle est la condition d'arrêt de cet algorithme ?
    4. Si la liste contenait 100 éléments, en combien d'étapes cet algorithme se terminerait-il ? Justifier.
    
3. Recopier et compléter le fonctionnement de cet algorithme pour chercher si $\textcolor{red}{4}$ est dans la liste $[1, 4, 7, 12, 13, 14]$ :

    |Etape | Liste | Milieu|Comparaison |
    |------|-------|--------------|------------|
    |1|$\underbrace{[\overset{\textcolor{red}{_\wedge^{...}}}{1}, 4,}_{ } \underset{_2^\uparrow}{\textcolor{darkblue}{7}} , \overbrace{12, 13, \underset{\textcolor{red}{_{...}^{\vee}}}{14}]}_{ }$| $(...+...)//2 = ...$ |$\textcolor{darkblue}{...} \geq \textcolor{red}{4}$ |
    |2|  ...  |  ...     |    ...          |   ...         |
    |3|  ...  |  ...     |    ...          |   ...         |
    |4|  ...  |  ...     |    ...          |   ...         |

4. Recopier et compléter la fonction Python suivante qui implémente l'algorithme de recherche par dichotomie.

```python linenums="1"
def recherche_dichotomie(element,liste):
    debut = ...
    fin = ...
    while ....:
        milieu = ...
        if element>liste[milieu]:
            debut=.....
        else:
            fin=.....
    if element==.....:
        return True
    else:
        return False
```

!!! aide "Aide"
    * Les variables `debut` (ligne 2) et `fin` (ligne 3) contiennent les indices de la liste entre lesquels on recherche.
    * La condition d'arrêt (ligne 4) est que l'écart entre ces deux indices est égale à 0.
    * Si `element>liste[milieu]` (condition ligne 6), alors on peut restreindre la recherche à droite de milieu (exclu).
    * Sinon on restreint la recherche à gauche de milieu (inclus)


{{ titre_activite("Complexité d'un algorithme",[]) }}

1. Graphique de comparaison de temps d'exécution 
{{ telecharger("Jupyter notebook","notebook/Recherche dans une liste.ipynb")}}
Le graphique suivant qui compare les temps d'exécution des deux algorithmes de recherche dans une liste a été construit dans le notebook précédent :
![comparaison recherche simple et dichotomique](./images/C6/comparaison.png){: .imgcentre}
2. Quel algorithme est le plus rapide ?
3. Cas de la recherche simple
    1. Pour la recherche simple, si une liste contient $n$ éléments, combien de comparaisons seront faites (au maximum) pour une recherche ?
    2. Par conséquent, si on double la taille de la liste, que dire du nombre de comparaisons ?
4. Cas de la recherche dichotomique
    1. Dans la recherche dichotomique, après chaque comparaison comment évolue la portion de la liste dans laquelle on effectue la recherche ?
    2. Par conséquent, si on double la taille de la liste, combien de comparaisons supplémentaires seront nécessaires ? 
5. Compléter le tableau suivant :

    |Taille de la liste | Nombre de comparaisons recherche simple | Nombre de comparaisons recherche dichotomique |
    |-------------------|----------------------------------------|----------------------------------------------|
    | $100$             | $100$ | $7$ |
    | $200$             |   ...    | ...    |
    | $400$             |   ...    | ...    |
    | $800$             |   ...    | ...    |


{{ titre_activite("Correction d'un algorithme",[]) }}


{{ telecharger("Fiche d'activité","pdf/C6/C6-act2.pdf")}}

{{ titre_activite("Terminaison d'un algorithme",[]) }}


{{ telecharger("Fiche d'activité","pdf/C6/C6-act2.pdf")}}

## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}
 
## Exercices

{{ exo("Parcours par indice",[],0)}}

On reprend la fonction Python de recherche d'un élément dans une liste (activité 1) :

```python linenums="1"
def recherche(element,liste):
    ''' Renvoie True si element est dans liste, False sinon '''
    for x in liste:
        if x==element: 
            return True    
    return False
```

1. Modifier la ligne 3 de façon à effectuer un parcours par indice plutôt que par élément
2. Modifier en conséquence la ligne 4 
3. Tester la fonction

{{ exo("Analyser un programme",[])}}
On considère la fonction Python suivante :
```python
    def cherche_position(element,liste):
        for pos in range(len(liste)):
            if liste[pos]==element:
                return pos
        return -1
```

1. Prédire la valeur renvoyée par `cherche_position("Y",["P","Y","T","H","O","N"])` puis vérifier en testant la fonction.
2. Même question pour `cherche_position("A",["P","Y","T","H","O","N"])`
3. Même question pour `cherche_position("M",["P","R","O","G","R","A","M","M","E"])`
4. Que fait cette fonction ? Ecrire sa chaîne de documentation.

{{ exo("Predire des temps d'exécution",[],)}}

1. Si un algorithme de recherche linéaire s'exécute environ en 0.002 s sur une liste de $10\,000$ éléments, en combien de temps environ devrait-il s'exécuter pour une liste de un million d'éléments ?
2. Si on double la taille d'une liste, le temps d'exécution d'un algorithme de recherche dichotomique va-t-il aussi doubler ? Justifier.

{{ exo("Recherche dichotomique",[]) }}
On donne ci-dessous la fonction de recherche par dichotomie vue à l'activité 2 :
```python

def recherche_dichotomie(element,liste):
    debut = 0
    fin = len(liste)-1
    while fin-debut>0:
        milieu = (debut+fin)//2
        if element>liste[milieu]:
            debut=milieu+1
        else:
            fin=milieu
    if element==liste[debut]:
        return True
    else:
        return False
```

1. Première améliorations
    1. Modifier cette fonction afin qu'elle renvoie un résultat correct lorsque la liste est vide.
    2. Ajouter une chaîne de documentation.
    3. Ajouter des préconditions sous forme d'instructions `assert`.
2. Modifier cette fonction de façon à sortir de la boucle `while` dès que l'élement cherché est égal à `liste[milieu]`.

{{ exo("Puissance",["maths"],)}}
On considère la fonction Python suivante :
```python
def puissance(x,n):
    p = 1
    for k in range(n):
        p = p * x
    return p
```

1. Que fait cette fonction ? Ecrire sa chaîne de documentation.
2. Proposer des préconditions sur les arguments.
3. Montrer que l'algorithme utilisé dans cette fonction a une complexité linéaire.


{{ exo("Factorielle",["maths"]) }}

En mathématiques, on appel *factorielle* d'un entier et $n$ et on note $n!$ le produit de cet entier par tous ceux qui le précèdent à l'exception de zéro, et on convient d'autre part que $0!=1$. Par exemple : <br>
$5!= 5 \times 4 \times 3 \times 2 \times 1 = 120.$<br>
On considère la fonction Python suivante :

```python
   def factorielle(n):
       '''Renvoie factorielle de n, avec n un entier positif ou nul'''
       if n==0:
           return 1
        else:
            fact=1
            for i in range(n):
                fact=fact*i
            return fact
```

1. Ecrire une instruction `assert` permettant de vérifier que cette fonction renvoie bien 120 pour factorielle de 5.
2. On suppose qu'on appelle `factorielle(5)`, donner les valeurs prises par la variable `fact` lors des passages successifs dans la boucle `for`.
3. Vérifier que la propriété *"la variable `fact` contient $k!$ après $k$ tours de boucle"* est un invariant de boucle.
4. Que peut-on en déduire ?

{{ exo("Nombre de chiffres d'un nombre",[]) }}
On considère la fonction suivante :

```python
def nombre_chiffres(n):
    '''Renvoie le nombre de chiffres de l'entier naturel n en base 10'''
    k=0
    while n>0:
        n=n/10
        k=k+1
    return k
```

1. Ecrire un jeu de test pour cette fonction
2. Le résultat de `nombre_chiffres(0)` est-il correct ? Sinon corriger cette fonction.
3. Ajouter des préconditions sous forme d'instruction `assert` sur la variable `n`.
4. Justifier que ce programme termine en utilisant la méthode du variant de boucle.
5. Proposer une fonction similaire qui renvoie le nombre de bits nécessaire pour écrire un entier donné en base 2.


{{ exo("Suite de Syracuse et terminaison",["maths"]) }}

On peut lire sur [wikipedia](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse){target=_blank} que :
> *"En mathématiques, on appelle suite de Syracuse une suite d'entiers naturels définie de la manière suivante : on part d'un nombre entier strictement positif ; s’il est pair, on le divise par 2 ; s’il est impair, on le multiplie par 3 et on ajoute 1. En répétant l’opération, on obtient une suite d'entiers strictement positifs dont chacun ne dépend que de son prédécesseur.<br>
Par exemple, à partir de 14, on construit la suite des nombres : 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2… C'est ce qu'on appelle la suite de Syracuse du nombre 14."* 

1. Donner la suite de Syracuse du nombre 12.
2. Même question pour le nombre 29.
3. Ecrire une fonction `syracuse` qui renvoie la liste des valeurs de la suite de syracuse d'un entier naturel postif `n` donné en paramètre. On arrêtera notre liste dès que la valeur 1 y est ajoutée.
4. Ecrire un jeu de test pour votre fonction.
5. Recherche sur le *Web* ce qu'on appelle *conjecture de Syracuse* (ou *conjecture de Collatz*). Consulter par exemple la page [wikipedia](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse){target=_blank} citée ci-dessus.
6. Que pouvez-vous en conclure sur la preuve de la terminaison de la fonction `syracuse` ?


{{ exo("Exponentiation rapide",["dur","maths"]) }}
On considère la fonction Python suivante où `x` est un nombre quelconque et `n` un entier positif :
```python
def puissance_rapide(x,n):
    p=1
    while n>0:
        if n%2==1:
            p = p *x
        x = x*x
        n = n //2
    return p
```

1. Tester cette fonction avec `x=2` et les valeurs suivantes de `n` : 4, 5, 8 et 10.
2. Que fait cette fonction ?
3. Donner les valeurs successives prises par les variables `p`, `x` et `n` lors de l'appel de cette fonction avec `x=2` et `n=9` en recopiant et en complétant le tableau suivant :

    | Variables | `p` | `x` | `n` |
    |-----------|-----|-----|-----|
    | Initialisation| 1 | 2 | 9 |
    | Tour 1 | ... | ... | ... |
    | Tour 2 | ... | ... | ... |
    | Tour 3 | ... | ... | ... |

4. Déterminer la complexité de cet algorithme (on pourra déterminer le nombre de tours de boucle nécessaire en fonction de `n`)


## Humour d'informaticien

![dichotomie](./images/C6/search.png){: .imgcentre width=500px}