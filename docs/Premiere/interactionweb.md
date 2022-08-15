
{% set num = 12 %}
{% set titre = "Interaction dans une page Web"%}
{% set theme = "web" %}
{% set niveau = "premiere"%} 


{{ titre_chapitre(num,titre,theme,niveau)}}
 
## Activités 

{{ titre_activite("Rappels : HTML et CSS",["rappel"],0)}}
1. Quelques rappels
    1. Lancer VSCode, créer un fichier intitulé `qcm.html`, y insérer la structure de base d'un fichier HTML (par exemple en tapant ++ctrl+space++). On trouve dans l'entête la ligne :
    ```html
    <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
    ```
    Quel est l'objectif de cette ligne ?
    2. Remplacer le nom de la feuille de style par `qcm.css` et créer le fichier correspondant.

2. Dans le fichier `qcm.html`, ajouter les élément suivants :
    1. un titre (balise `<h1> ... </h1>`)
    2. un paragraphe de présentation du {{sc("qcm")}} (balise `<p> ... </p>`)
    3. les questions de votre {{sc("qcm")}} contenant chacune un titre, un énoncé et une liste de réponses possibles. Un exemple est proposé ci-dessous :
    ```html
    <form>
        <span class="titre">Histoire de Javascript</span><br>
        <span class="enonce">En quelle année est né Javascript ?</span><br>
        <input type="radio" name="HJS"> 1990<br>
        <input type="radio" name="HJS"> 1995<br>
        <input type="radio" name="HJS"> 2000<br>
        <input type="radio" name="HJS"> 2005<br>
    </form>
    ```
    
        !!! aide
            Faites vos propres recherches sur le *Web*, sur les balises de formulaires en HTML.
    
    4. un bouton de validation du formulaire (balise `<input type="submit">`)
    5. une zone ou apparaîtra le résultat de la validation des réponses (balise `<div> .... </div>`)

3. Création du {{sc("css")}}

    1. Quel est le rôle de `class="titre"` dans la balise `<span>` entourant la question ?
    2. Ouvrir le fichier `qcm.css` crée plus haut et y créer un style `titre` permettant d'avoir les titres de questions dans la couleur et le format de votre choix.
    3. Faire de même pour les autres éléments de la page (titre, description, bouton de formulaire, ...)

4. Vers l'interaction  
Notre page web est terminée, mais pour le moment cliquer sur le bouton de validation du formulaire ne produit aucun résultat. Les données récupérées dans un formulaire peuvent être traitées du côté du serveur (on parle alors en anglais de *server-side scripting*). Dans ce cas l'un des langages les plus populaires est [php](http://www.php.net){target=_blank}. Mais les données d'un formulaire peuvent aussi être traitées sur la machine du client (*client-side scripting*) et le langage alors utilisé est **Javascript**.

    1. Quels sont les dangers potentiels lorsqu'une page Web exécute un programme sur votre ordinateur ?
    2. Peut-on configurer son navigateur pour empêcher l'exécution de script ?
    3. Quelles solutions ont été adoptées pour limiter les problèmes causées par le *server-side scripting* ?

{{ titre_activite("De l'interactivité avec Javascript",[]) }}

Nous devons commencer par indiquer que le bouton de validation de notre formulaire doit exécuter du code javascript (noter bien que ce bouton peut aussi permettre d'envoyer les données du formulaire vers un script coté serveur). La fonction de traitement des résultats du {{sc("qcm")}} doit être appelée lorsque l'utilisateur clique sur le bouton de validation du formulaire. 

1. Modifier le bouton de validation du formulaire en :
```html
<input type="submit" value="valider" onclick="javascript : resultat()">
```
Nous venons d'indiquer que lorsque l'utilisateur clique sur ce bouton, il faut exécuter la fonction `resultat()`. Un clic sur un bouton est un **événement**, et nous verrons que Javascript peut en gérer bien d'autres. La fonction `resultat()` reste bien sur encore à définir !
2. Dans l'entête de la page HTML obtenu dans VSCode se trouve la ligne :
```html
<script src='main.js'></script>
```
    1. Quel est l'objectif de cette ligne ?
    2. Changer le nom du fichier javascript en `qcm.js` (au lieu de `main.js`) créer ce fichier y taper les lignes suivantes :
```javascript
function resultat()
{
    alert("Javascript est dans la place !!!");
}
```
    3. Tester alors l'effet produit par un clic dans votre page sur le bouton de validation
    4. Comparer la syntaxe de définition d'une fonction en javascript à celle de Python.
    5. Faire vos propres recherches sur les événements en Javascript, est-il possible de lancer l'exécution de la fonction `resultat()` lors d'un double clic ? lors d'un simple survol ? Quels sont les événements associés ? Tester

3. Modifier le code de la fonction `resultat()` dans le fichier `qcm.js` en :
```javascript
function resultat() 
{
        // on récupère le contenu du bouton radio de la question  'HJS'
        reponse_question1 = document.getElementsByName("HJS")
        // c'est la bonne réponse lorsque la 2eme proposition (numérotée à partir de 0) est cochée 
        if (reponse_question1[1].checked) 
            {alert("bonne réponse")}
        else 
            {alert("mauvaise réponse")}
}
```
    1. Comment insère-t-on des commentaires en Javascript ?
    2. Comment a-t-on récupéré l'état du bouton radio de la question identifié par `name='HJS'` ?

4. Inventer un {{sc("qcm")}} de plusieurs questions, prévoir une zone de réponse (balise `<div>...</div>`) dans la page html. Cette zone pourrait contenir au départ un message comme "Votre score apparaitra ici lorsque vous aurez valider vos réponses". Puis, introduire une variable javascript permettant de compter le nombre de bonnes réponses de l'utilisateur et afficher le score dans cette zone.

## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Corriger un programme Javascript",[],0)}}

Une page {{sc("html")}} contient une balise `<div id="message">...</div>`, le programme suivant doit modifier cette zone de texte et y afficher "Bravo !" mais il comporte de nombreuses erreurs, les corriger.

```javascript
function affiche():
        document.GetElementByid("message").innerHTML="Bravo !";
```

{{ exo("Quelques événements",[])}}

1. Recopier puis tester, dans le squelette d'une page {{sc("html")}} les lignes suivantes :
```html
<form>
        <input type="button" onclick="javascript:alert('Hello world !');" value="un bouton">
</form>
```
2. Que se passe-t-il si on clique plusieurs fois successivement sur ce bouton, pourquoi ?
3. Modifier le code de la page de façon à ce que la boîte d'alerte s'affiche :
    * lors d'un double clic
    * lorsque la souris survole le bouton
    * lorsque la souris quitte le bouton

{{ exo("Indice de masse corporelle",[]) }}
1. Créer une page {{sc("html")}} contenant un formulaire demandant à l'utilisateur son poids et sa taille.
2. Créer un script Javascript traitant les données de ce formulaire pour calculer l'indice de masse corporelle ({{sc("imc")}}) c'est à dire poids sur taille au carré
3. Suivant la valeur de l'{{sc("imc")}}, créer une variable Javascript contenant l'interprétation associée (dénutrition, maigreur, poids ideal, ...) 

    !!! aide 
        On pourra consulter par exemple la [page wikipedia sur ce sujet](https://fr.wikipedia.org/wiki/Indice\_de\_masse\_corporelle){target=_blank}

4. Communiquer les résultats à l'utilisateur par une modification d'un élément de la page ou via une boîte d'alerte.


{{ exo("Idées de mini projet",[])}}
Créer en utilisant Javascript, une page web permettant de :

1.  mesurer son temps de réaction. 

    !!! aide
        [Ce site](http://www.msc.univ-paris-diderot.fr/~olivier/TE1_TP2/) montre un exemple (très abouti) de ce qui est attendu.

2. convertir des unités par exemples francs en euros, ou degrés Celsius en degrés Fahrenheit.
3. afficher une couleur en donnant son code (R,G,B)


