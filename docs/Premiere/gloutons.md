
{% set num = 13 %}
{% set titre = "Algorithmes gloutons"%}
{% set theme = "algorithmique" %}
{% set niveau = "premiere"%} 


{{ titre_chapitre(num,titre,theme,niveau)}}
 
## Activités 

{{ titre_activite("Introduction",["oral"],0) }}

![Problème du sac à dos](./images/C13/pbsac.png){: .imgcentre}

1. Quel est le problème illustré par l'image ci-dessous ?
2. Proposer une réponse à ce problème.

{{ titre_activite("Problème du sac à dos",["notebook"]) }}

{{ telecharger("Jupyter notebook","notebook/SacDos.ipynb")}}



{{ titre_activite("Problème du rendu de monnaie",["notebook"]) }}
{{ telecharger("Jupyter notebook","notebook/RenduMonnaie.ipynb")}}


## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Rendu de monnaie",[],0) }}

1. On se place dans le système monétaire européen

    1. Donner le résultat de l'algorithme glouton pour le rendu de monnaie si on doit rendre 8,40 €
    2. En citant un résultat du cours, justifier que l'algorithme fournit toujours une solution optimale dans ce système monétaire.

2. On se place dans le système monétaire suivant : 10,8,4,3, et 1

    1. Donner le résultat de l'algorithme glouton si on doit rendre 6
    2. Le résultat obtenu est-il optimal ?


{{ exo("Un problème du sac à dos",[]) }}

On considère un problème du sac à dos avec les objets suivants et un sac ayant un **poids maximal de 4kg** :

![Pb_Sac](./images/C13/pbsac_ex2.png){: .imgcentre}

1. Classer ces objets par valeur décroissante et donner la solution de l'algorithme glouton avec ce critère de classement.
2. Même question avec un classement par poids croissant.
3. Même question avec un classement par valeur/poids croissant.
4. A-t-on obtenu la solution optimale ?


{{ exo("Implémentation du rendu de monnaie en Python",[]) }}
Le but de l'exercice est de compléter une fonction `rendu` écrite en Python qui implémente l'algorithme glouton pour le problème du rendu de monnaie. La fonction prend en argument :

* un flottant `somme` qui est la somme à rendre
* une liste `valeurs` contenant la somme des valeurs du système monétaire utilisé.

Et elle doit renvoyer comme résultat une liste contenant les pièces à utiliser. On renvoie une liste vide lorsque l'algorithme échoue à trouver une solution.

1. Questions préliminaires
    a. Que doit renvoyer `rendu(18,[15,10,5,2,1])` ? Quelle est la solution optimale à ce problème ?
    a. Que doit renvoyer `rendu(17,[10,9,8,3])` ? Quelle est la solution optimale à ce problème ?

2. Recopier et compléter le code de la fonction ci-dessous :

```python linenums="1"
def rendu(somme,valeurs):
	#la solution de l'algorithme initialisée à la liste vide
    solution = .....
    #la position dans la liste valeurs de la pièce testée
    indice = ....
    while somme!=0 and indice<len(valeurs):
        piece = valeurs[.....]
        # on teste si la piece est inférieure à la somme à rendre
        if piece<=......:
        	# Si oui l'ajouter à la solution et diminuer la somme à rendre
            somme=...............
            solution...........(.....)
        else:
        	# Sinon passer à la pièce suivante
            indice = ........
    if somme==0:
        return solution
    else:
        return []
```

3. Quel est le rôle du test `somme==0` en ligne 16 ? Que renverrait cette fonction pour le problème de la question **1.b)** si on supprime entièrement ce test (lignes 16 à 19) et qu'on le remplace par `return solution` ?
4. Tester cette fonction sur les exemples de l'exercice **1**.

{{ exo("Force brute pour le problème du sac à dos",["maths"]) }}

Soit $n$ le nombre d'objet d'un problème du sac à dos.

1. Déterminer en fonction de $n$ le nombre de combinaisons possibles d'objets dans le cas.
    !!! Aide
        Affecter à chaque combinaison un numéro en binaire en mettant 1 si l'objet est dans le sac et 0 sinon. Par exemple pour 5 objets, 10110 signifie que les objets 1,3 et 4 sont dans le sac et pas les objets 2 et 5. Déduire de cette numérotation le nombre de combinaisons

2. On suppose qu'un programme informatique teste 100000 combinaisons en une seconde. En combien de temps donnerait-il la solution optimale par force brute pour un problème à 50 objets ? Et pour 100 objets ?



