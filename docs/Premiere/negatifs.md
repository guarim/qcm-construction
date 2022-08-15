
{% set num = 10 %}
{% set titre = "Représentation des entiers négatifs"%}
{% set theme = "typesbase" %}
{% set niveau = "premiere"%} 


{{ titre_chapitre(num,titre,theme,niveau)}}
 
## Activités 

{{ titre_activite("Complément à deux",[],0) }}

{{ telecharger("Fiche d'activité","/pdf/C10/C10-act1.pdf")}}


## Cours

{{ aff_cours(num) }}

## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Du plus petit au plus grand",[],0) }}

1. On code les entiers en complément à deux sur 4 bits
    1. Quel est le plus petit entier représentable ?
    2. Quel est le plus grand entier représentable ?
2. Mêmes questions sur 16 bits

{{ exo("Soustraction binaire",[]) }}

1. Coder en binaire sur un octet en complément à deux $177_{10}$.
2. Même question pour $-135_{10}$.
3. Faire l'addition binaire de ces deux nombres.
4. Vérifier en écrivant le résultat en décimal qu'on obtient bien 42.

{{ exo("Un peu de programmation",[]) }}

1. Ecrire une fonction Python `binaire(entier)` qui prend en entrée un entier compris entre 0 et 127 et renvoie une chaîne de caractère contenant la représentation binaire de cet entier sur un octet. Par exemple `binaire(42)` renvoie `"00101010"`.
2. Ecrire une fonction Python `inverse_bit(chaine)` qui prend en entrée une chaîne de caractère et renvoie la chaîne dans laquelle tous les 0 ont été remplacés par des 1 et tous les 1 par des 0. Par exemple `inverse_bit("10110001")` renvoie `"01001110"`
3. Ecrire une fonction Python `ajoute_un(chaine)` qui prend en entrée une chaîne de caractères et effectuer l'addition binaire de 1 au nombre binaire représenté par cette chaine. Par exemple `ajoute_un("1001010")` renvoie `1001011`.
4. En utilisant les fonctions ci-dessus, écrire une fonction Python qui renvoie la représentation en complément à deux sur 8 bits d'un entier passé en paramètre.
