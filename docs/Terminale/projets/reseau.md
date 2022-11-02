# POO et réseau

Le but du projet est la réalisation d'un programme permettant de gérer et traiter les adresses {{sc("ip")}} et les masques de sous réseau en utilisant la programmation orientée objet. En effet, *bien que ces notions ne soient pas explicitement au programme*, de nombreux exercices de baccalauréat à l'épreuve écrite incluent des questions du type :

* déterminer le nombre de machines pouvant être connectées à un réseau,
* convertir des adresses en binaire vers du décimal ou inversement,
* déterminer l'adresse d'un réseau à partir de l'adresse d'une machine et du masque, ...


## Etape 0 : revoir les notions nécessaires

Revoir et faire les exercices du chapitre de première sur les réseaux, en particulier, savoir faire les exercices suivant est indispensable pour réussir le projet :

* [exercice 1](https://fabricenativel.github.io/Premiere/reseau/#exercice-1-adresse-ip)
* [exercice 3](https://fabricenativel.github.io/Premiere/reseau/#exercice-3-masque-de-sous-reseau)

    !!! aide
        Ne pas hésiter à faire vos propres recherches sur le Web !

## Etape 1 : constructeur de la classe des adresses IP

Ecrire une classe représentant une adresse IP dont le constructeur prend en paramètre une chaîne de caractère et crée l'adresse IP correspondante *lorsque cela est possible*. Le choix des attributs d'un objet `AdresseIP` est laissé au choix du programmeur, on pourra par exemple utiliser un attribut unique (chaine de caractère) ou alors 4 entiers représentant les 4 octects de l'adresse IP. Le constructeur doit générer une erreur si la chaine passée en paramètre ne permet pas la construction d'une adresse IP valide.
A titre d'exemples voici quelques exemples d'utilisations

```pycon
>>> r1 = AdresseIP("192.168.1.2")
>>> r2 = AdresseIP("192.168.1")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in __init__
AssertionError: L'adresse IP doit contenir 4 entiers séparés par le caractère '.'
>>> r3 = AdresseIP("192.AB.1.42")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in __init__
AssertionError: AB n'est pas un entier positif
>>> r3 = AdresseIP("192.168.1.256")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in __init__
AssertionError: 256 n'est pas compris entre 0 et 255
```

!!! aide
    * On pourra utiliser la méthode `split` des chaines de caractères pour séparer chaque partie de l'adresse IP. En voici des exemples d'utilisations
    ```pycon
    >>> "un,deux,trois".split(",")
    ['un', 'deux', 'trois']
    >>> "python est vraiment super".split(" ")
    ['python', 'est', 'vraiment', 'super']
    ```
    * On pourra utiliser `isdigit` afin de vérifier que les éléments sont bien des entiers.

## Etape 2 : Méthodes de la classe des Adresse IP

Ecrire pour la classe `AdresseIP` les méthodes suivantes :

1. la méthode spéciale d'affichage spéciale `__str__` permettant lors d'un print sur un objet de type `AdresseIP` de renvoyer la chaine de caractère réprésentant cette adresse, par exemple:
    ```pycon
    >>> a = AdresseIP("192.168.1.26")
    >>> print(a)
    '192.168.1.26'
    ```

2. `binaire` qui renvoie la chaine de caractère correspondante à l'adresse IP écrite en binaire en faisant figurer les 8 chiffres de chaque octet même s'ils sont nuls. Par exemple :
    ```pycon
    >>> r1 = AdresseIP("192.168.1.2")
    >>> r1.binaire()
    '11000000.10101000.00000001.00000010'
    ```

3. `hexadécimal` qui renvoie la chaine de caractère correspondante à l'adresse IP écrite en binaire en faisant figurer les 2 chiffres de chaque octet même s'ils sont nuls. Par exemple :
    ```pycon
    >>> r1 = AdresseIP("192.168.1.2")
    >>> r1.hexadecimal()
    'c0.a8.01.02'
    ```

    !!! Attention
        Bien qu'on puisse utiliser les fonctions de conversion natives de Python (`bin` et `hex`), il est **fortement recommandé** d'écrire vos propres fonctions de conversions en vue de l'entrainement à l'épreuve pratique du baccalauréat. En effet, on rappelle que l'écriture de ce type de fonctions de conversion entre le binaire et le décimal figure aussi bien en exercice de type 1 (voir par exemple [le sujet 7](https://fabricenativel.github.io/Terminale/Annales/Corriges/2022-S07/) de 2022) qu'en exercice de type 2 (voir par exemple [le sujet 15](https://fabricenativel.github.io/Terminale/Annales/Corriges/2022-S15/) de 2022)

4. Ecrire la méthode `meme_debut` qui indique par combien de bits identiques commencent deux adressesIP. Par exemple :
    ```pycon
    >>> r1 = reseau.AdresseIP('192.168.1.2')
    >>> r2 = reseau.AdresseIP('192.168.1.26')
    >>> r1.meme_debut(r2)
    27
    ```
    En effet l'écriture binaire de `r1` est  `11000000.10101000.00000001.00000010` et celle de `r2` est `11000000.10101000.00000001.00011010`, donc les 27 premiers bits de ces deux adresses sont identiques.


## Etape 3 : classe des masques de sous réseau

1. Ecrire une classe `Masque` représentant un masque de sous réseau en notation {{sc("cidr")}} c'est à dire par un entier compris entre 0 et 32. La représentation interne de cette classe (c'est à dire le choix des attributs) est laissée au choix du programmeur. On pourra, par exemple se contenter d'un unique attribut de type entier.

2. Ecrire pour cette classe une méthode `en_adresse` qui permet de passer de la notation {{sc("cidr")}} à la notation sous forme d'adresseIP. Cette méthode renvoie donc un objet de type `AdresseIP` défini plus haut. Par exemple :
```pycon
>>> m = Masque(19)
>>> adr = m.en_adresse()
>>> print(adr)
255.255.224.0
```

## Etape 4 : classe des réseaux

1.  Ecrire une classe `Reseau` représentant un réseau, les objets de cette classe ont deux attributs :

    * adresse : du type `AdresseIP` définie à l'étape 1
    * masque : du type `Masque` définie à l'étape 2

    La méthode `init` de cette classe prendra comme argument un chaine de caractère représentant l'adresse IP  d'une machine du réseau et un entier représentant le masque en notation {{sc('cidr')}}.

2.  Ecrire pour cette classe les méthodes suivantes :

    * Une méthode d'affichage `__str__`, par exemple :
    ```pycon
    >>> r1 = Reseau("192.168.1.17/24")
    >>> print(r1)
    192.168.1.17/24
    ```
    * Une méthode `adresse_reseau` qui renvoie l'adresse réservée pour le réseau, par exemple :
    ```pycon
    >>> r1 = Reseau("192.168.1.17/24")
    >>> print(r1.adresse_reseau())
    >>> 192.168.1.0
    ```

        !!! aide
            Pour obtenir l'adresse du réseau, on peut convertir l'adresse IP de la machine ainsi que le masque en binaire, puis effectuer un et logique. Cette procédure est par exemple détaillée :

            * dans [ce sujet de bac 2022](../../officiels/Annales/EE/2022/22-NSIJ1LR1.pdf) dont voici [la correction](../../Annales/Corriges/22-NSIJ1LR1/#exercice-5-reseau-protocoles-de-routage-langage-et-programmation)
            * sur [ce site web](https://neptunet.fr/calcul-ip/)

    * Une méthode `adresse_diffusion` qui renvoie l'adresse réservée pour la diffusion, par exemple :
    ```pycon
    >>> r1 = Reseau("192.168.1.17/24")
    >>> print(r1.adresse_diffusion())
    >>> 192.168.1.255
    ```

        !!! aide
            Pour obtenir l'adresse de diffusion, on peut convertir l'adresse IP de la machine ainsi que le masque en binaire, inverser tout les bits du masque et effectuer un ou logique. 

    * Une méthode `nb_adresses` qui renvoie le nombre de machines pouvant être connectées à ce réseau, par exemple :
    ```pycon
    >>> r1 = Reseau("192.168.1.17/24")
    >>> print(r1.anb_adresses())
    >>> 254
    ```

        !!! aide
            Pour obtenir le nombre de machines possibles sur le réseau, on utilise la formule $2^{c-32} - 2$ où $c$ est l'entier de la notation {{sc("cidr")}}. Par exemple si l'adresse d'une machine est `192.154.88.133/26`, alors le nombre d'adresses possibles sur ce réseau est $2^{32-26}-2$ c'est à dire $62$. 
    

    

## Etape 5 : application

A l'aide de votre module compléter le tableau suivant :

| Adresse         | Masque (en décimal) | Adresse du réseau | Adresse de diffusion | Nombre d'hôtes |
|-----------------|---------------------|-------------------|----------------------|----------------|
|192.168.20.34/24 |                     |                   |                      |                |
|172.16.1.220/16  |                     |                   |                      |                |
|192.154.88.133/26|                     |                   |                      |                |
|131.108.78.235/21|                     |                   |                      |                |

Vous pouvez, vérifier vos résultats en ligne sur [ce site](https://www.faidherbe.org/tutoriel/ip.htm)