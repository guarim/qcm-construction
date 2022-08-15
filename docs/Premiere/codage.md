{% set num = 2 %}
{% set titre = "Codage des entiers et des caractères"%}
{% set theme = "typesbase"%}
{% set niveau = "premiere"%} 

{{ titre_chapitre(num,titre,theme,niveau)}}
 
## Activités 

{{ titre_activite("Numération binaire",["papier"],0) }} 
{{ telecharger("Fiche d'activité","/pdf/C2/C2-act1.pdf")}} 

{{ titre_activite("Numération hexadécimale",[]) }}
{{ telecharger("Fiche d'activité","/pdf/C2/C2-act2.pdf")}}

{{ titre_activite("Encodage des caractères",["video"]) }}
<div class="centre"><iframe width="560" height="315" src="https://www.youtube.com/embed/MijmeoH9LT4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen ></iframe></div>
En utilisant la video ci-dessus et en faisant éventuellement vos propres recherches sur le *Web*, répondre brièvement aux questions suivantes :

1. L'encodage {{ sc("ascii")}}
    1. Combien de caractères pouvaient être codés en {{ sc("ascii") }} ?
    2. Expliquer rapidement pourquoi ce système était limité et à du être étendu
2. L'encodage Latin-1
    1. Sur combien de bits était encodé chaque caractère ?
    2. Combien de caractères au maximum étaient représentés ?
    3. Ce système était-il universel ?
3. L'encodage {{ sc("utf-8")}}
    1. Un caractère est-il toujours encodé sur le même nombre de bits ?
    2. Cet encodage est-il compatible avec l'ancienne norme {{ sc("ascii")}} ?


## Cours

{{ aff_cours(num) }}

## QCM

{{qcm_chapitre(num)}}
  
## Exercices

{{ exo("Passer d'une base à l'autre",[],0) }}


Recopier et compléter le tableau de conversion suivant :

| Ecriture décimale | Ecriture binaire | Ecriture hexadécimale |
|-------------------|------------------|-----------------------|
|$(201)_{10}$   | ...           | ...               |   
|        ...    |    ...        |    $(EA)_{16}$    |
|$(57)_{10}$    |     ...       |                ...|
|               |$(00100001)_2$ |                   |
|$(128)_{10}$   | ...           | ...               |   
|$(163)_{10}$   | ...           | ...               |
|  ...          |  ...          |    $(5B)_{16}$    |   
|  ...          |$(10010101)_2$ |    ...            |
|  ...          |$(10010010)_2$ |       ...         |

{{ exo("Un peu de reflexion",[]) }}


1. Quel est le plus grand entier positif écrit en utilisant 10 chiffres en base 2 ?
2. Que peut-on dire d'un nombre dont l'écriture en base 2 ne contient qu'un seul chiffre 1 ?
3.  1. En base 10, comment reconnaît-on un nombre divisible par 10 ? 
    2. L'écriture en base 2 d'un nombre divisible par 2 se termine forcément par quel chiffre ? Justifier.
    3. De façon générale, soit $b$ un entier supérieur ou égal à 2, que peut-on dire de l'écriture en base $b$ d'un nombre divisible par $b$ .
4. En base 10, un million s'écrit avec 7 chiffres, combien en faut-il pour l'écrire en base 2 ?

{{ exo("Énigme",[]) }}

Il manque des chiffres (remplacés par des ?) dans le nombre binaire suivant : $?001??111?$

1. Retrouver les chiffres manquants en utilisant les indices suivants:
    * il n'y a pas de zéros non significatifs dans ce nombre
    * ce nombre est divisible par 2
    * il y a un nombre impair de 0 dans l'écriture binaire de ce nombre
    * l'écriture décimale de ce nombre dépasse $(600)_{10}$
2. Donner l'écriture décimale de ce nombre.
3. Donner son écriture hexadécimale

{{ exo("Un peu de Python",["python"]) }}


1. Lancer Python en ligne de commande, comme vu dans le chapitre précédent.
2. Tester la fonction `bin` de Python, en affichant par exemple `bin(201)` et `bin(57)`. Rapprocher les résultats obtenus avec les réponses de l'exercice 1. Émettre une hypothèse sur cette fonction.
3. Valider votre hypothèse en faisant afficher l'aide de la fonction `bin`.
4. Reprendre les questions précédentes pour la fonction `hex`.

{{ exo("Code ASCII",[]) }}


1. Le code {{ sc("ascii") }} de A est 65 et celui de a est 97. Ecrire ces deux codes en binaire. 
2. Sachant que l'ordre des codes suit l'ordre alphabétique (donc le code de B est 66), écrire les codes binaires de B et de b.
3. Même question pour C et c. Que remarquez-vous ?
4. Le code {{ sc("ascii") }} binaire de P est $10100000$, quel est celui de p ?
5. Le code {{ sc("ascii") }} du zéro est 48, l'écrire en binaire. Ce code a-t-il été choisi au hasard ?


{{ exo("Message secret",[]) }}
```
0x420x720x610x760x6f0x200x210x200x560x6f0x750x730x200x610x760x650x7a0x200x64
0xe90x630x6f0x640xe90x200x6c0x650x200x6d0x650x730x730x610x670x65
```
Parviendrez-vous à décoder le message secret ci-dessus ? 
!!! aide
    Un indice : {{ sc("ascii") }}

{{ exo("Algorithme des divisions successives",[]) }}

En utilisant l'*algorithme des divisions successives* :

1. Convertir $6771_{10}$ en base 2
2. Convertir $6771_{10}$ en base 16
3. Vérifier le résultat précédent en effectuant la conversion du nombre obtenu à la question 1. en base 16.
4. Mêmes questions pour $9753$

!!! Aide
    Cet exercice impose l'utilisation de l'*algorithme des divisions successives*, on pourra donc se référer au cours et refaire les exemples qui s'y trouvent en cas de difficultés.




{{ exo("Le parachute de perseverance",[]) }}


En février 2021, le robot *Perseverance* a atterrit sur Mars, en déployant un parachute :
![Parachute de perseverance](./images/C2/perseverance.png){: .imgcentre}
Le motif du parachute cache un message codé en binaire, le décoder en utilisant les informations suivantes :

* Un mot est codé sur chacun des trois anneaux intérieurs 
* les caractères sont représentés sur 10 bits 
* La lettre A est codée 1, la lettre B est codée 2 et ainsi de suite
* l'anneau extérieur code des coordonnées {{ sc("gps") }} de la forme trois groupes de chiffres suivi d'une lettre (N ou S) puis de nouveau 3 groupes de chiffres suivi d'une lettre (E ou W)

![Parachute de perseverance](./images/C2/parachute.png){: .imgcentre}

!!! lien "Pour aller plus loin"
    * Visiter le site [Msg2Mars](https://sjwarner.github.io/perseverance-parachute-generator/){target=_blank} pour coder votre propre message en suivant le même principe
    * Le service [Nominatim d'openstreetmap](https://nominatim.openstreetmap.org/ui/search.html){target=_blank} vous permettra de retrouver un lieu à partir de ces coordonnées {{ sc("gps" )}}