
{% set num = 8 %}
{% set titre = "Le web"%}
{% set theme = "web" %}
{% set niveau = "premiere"%} 


{{ titre_chapitre(num,titre,theme,niveau)}}
 
## Activités 
 
{{ titre_activite("Modèle client serveur",["video"],0) }}
<div class="centre"><iframe src="https://player.vimeo.com/video/138623558?color=b50067&title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>

En faisant vos propres recherches et en vous aidant de la vidéo ci-dessus, répondre aux questions suivantes :

1. Quand et par qui a été inventé *le Web* ?
2. Peut-on dire *Internet* à la place du *Web* ?
3. Sur quel principe de fonctionnement repose *le Web* ?


{{ titre_activite("Les éléments d'une page Web",[]) }}

!!! Attention
    Dans cette activité, on commence à créer des pages HTML, pour visualiser la page produite, deux solutions s'offrent à vous :

    1. installer l'extension *HTML Preview* de VS code, dans ce cas vous pourrez afficher côte à côte dans VS Code le code source de votre page HTML ainsi que sa prévisualisation.
    2. ouvrir à l'aide de *Firefox* le fichier local de votre page HTML (taper ++ctrl+o++ dans *Firefox*). Après avoir modifié le source HTML dans VS Code, mettre à jour l'affichage dans *Firefox* en appuyant sur ++f5++ pour actualiser.

1. Squelette d'une page *Web*<br>
L'éditeur VS Code, permet d'insérer rapidement la structure de base d'une page web :

    * créer un fichier vide appelé `structure.html`,
    * ouvrir ce fichier dans VS Code,
    * taper simplement `!` et entrée (ou alors taper `html` et dans le menu d'abbreviation sélectioner `html:5`)

    Vous devriez obtenir le résultat suivant :
    ```html linenums="1"
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>
    ```

    1. Un document {{sc("html")}} est constitué d'un *en-tête*, suivi d'un *corps*. Repéré les balises permettant de délimiter :
        1. Le document {{sc("html")}}
        2. L'en-tête
        3. Le corps
    2. L'en-tête contient une balise `<title>`, quel est son rôle ? 

2. Ajout de contenu<br>
Dans le corps du document, c'est à dire entre les balises `<body>` et `<body>`, insérer le contenu suivant :

    ```html linenums="1"
    <h1> La recette du carry de poulet

        <h2> Les ingrédients
            <ul>
                <li> un poulet découpé en morceaux
                <li> 3 oignons
                <li> 1 tomate
                <li> 5 gousses d'ail
            </ul>
        
        <h2> La préparation
            <p>Dans de l'huile chaude, faire revenir le poulet</p>
    ```

3. Observer le résultat obtenu dans l'affichage et en déduire le rôle des balises suivantes :  

    1. `<h1>` et `<h2>`
    2. `<ul>` et `<li>`
    3. `<p>`

4. Ajouter un sous-titre 'Accompagnements' dans la page Web
5. Dans ce sous-titre créer une liste avec deux éléments : "riz blanc et grains", "riz jaune".
6. Ajouter un paragraphe au début de la recette dans lequelle on écrira "Le carry de poulet est une recette de cuisine traditionnel de l'ile de la Réunion"
7. Modifier le paragraphe crée à la question précédente en:

    ```html
        Le carry de poulet est une recette de cuisine traditionnel de l'<a href="https://fr.wikipedia.org/wiki/La_R%C3%A9union">ile de la Réunion</a>
    ```

8. Quelle est la modification produite dans la page ?
9. Ajouter un lien dans votre page Web sur le mot "Oignon" qui permet d'accéder à l'adresse `https://fr.wikipedia.org/wiki/Oignon`

10. Rechercher vous-même sur le *Web* la balise permettant d'insérer une image dans une page HTML puis l'utiliser pour insérer une image illustrant la recette du carry de poulet (attention à utiliser une image libre de droit)

{{ titre_activite("L'apparence d'une page Web",[]) }}

!!! Important
    Les balises HTML permettent de **structurer** le contenu d'une page web, en définissant les titres, les paragraphes, ...
    Pour modifier l'**apparence** d'une page, on a recours au *css* (cascadind style sheet) qui permettent de modifier l'apparence du contenu de la page

{{telecharger("Une courte introduction à css","./pdf/C8/Act8-2.pdf")}}

## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Corrections",[],0)}}

Corriger les erreurs dans les fragments de code HTML suivant :

1. `<h> Mon titre principal </h>`
2. `<href="http://www.wikipedia.fr">un lien vers Wikipedia</href>`
3. `<p> Ce paragraphe contient un <a href="autre_page.html">lien vers une autre page</p></a>`


{{ exo("Structurer une page Web",[]) }}

Quelles sont les balises {{sc("html")}} permettant de délimiter :

1. Un titre ou un sous titre ?
2. Un paragraphe ?
3. Un lien ?
4. Un tableau ? Une ligne d'un tableau ? Une case dans un tableau ?


{{ exo("Modifier l'apparence d'une page web",[]) }}

1. Enregistrer dans le répertoire suivant le fichier {{sc("html")}} suivant :
{{ telecharger("Le rougail saucisess","./files/C8/rougailsaucisses.html")}}
Pour cela, vous pouvez par exemple cliquer à droite sur le bouton ci-dessus, puis sélectionner "Enregistrer la cible du lien sous ..."
2. Par la méthode de votre choix (mais de préférence en créant une feuille de style dans un fichier séparé), modifier l'apparence de cette page web de sorte que:
    * Le fond de la page soit de couleur noire,
    * Les liens soient jaunes et pas soulignés,
    * Les titres de niveau 1 soient en gras et en blanc,
    * Les titres de niveau 2 soient en bleu clair, encadré avec un trait de couleur rouge


{{ exo("Créer un mini-site",[]) }}

Réaliser  un mini site *Web*, en utilisant le html et les feuilles de style. Le sujet du site est au choix, par exemple : votre CV, vos films préférés, un site de recette de cuisines, un site sur un sport ou une de vos passions, ou sur une célébrité (sportif, acteur, chanteur ...) . Respecter le cahier des charges suivant :

* au moins 5 pages reliées entre elles par des liens internes et des liens vers des sites extérieurs
* au moins 5 images, attention à utiliser des images *libres de droits* ou à créer vos propres illustrations pour votre site
* au moins une page de votre site devra contenir des informations organisées sous la forme d'un tableau et donc utiliser les balises `<table>` et `</table>`.
* L'apparence du site sera uniformisé (c'est à dire que d'une page à l'autre on retrouvera les mêmes couleurs et la même présentation). Vous devrez pour cela utiliser une feuille de style dans un fichier séparé.
