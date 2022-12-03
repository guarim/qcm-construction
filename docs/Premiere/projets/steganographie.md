### Manipulation d'images avec Python et steganoghraphie


#### Descriptif 
La bibliothèque   {{sc("pil")}} pour Python Imaging Library est une célèbre librairie python permettant de modifier et de créer des images sous de nombreux formats. Vous pouvez télécharger ci-dessous, un  notebook permettant de découvrir cette librairie :
{{ telecharger("Notebook découverte de PIL","./notebook/pil.ipynb") }}
Le but de ce projet est d'utiliser cette librairie afin de créer des filtres applicables sur n'importe quel image (par exemple un flou ou une pixellisation). Dans un premier temps on se familiarisera avec les fonctionnalités de la librairie en produisant des images à l'aide de PIL.
####  Critère de réussite : 

* **[8pts]**   Prise en main de la libraire à l'aide du notebook. Lire et comprendre le notebook d'introduction à {{sc("pil")}}. Réussir les exercices qui figurent dans le notebook. En particulier, il faut avoir réussi en s'inspirant de l'exemple du drapeau de la France  donné dans le notebook à créer à l'aide de {{sc("pil")}}  une image du drapeau de la suède en respectant les couleurs et les proportions.
* **[6pts]**  Ecrire et tester une fonction Python permettant à l'aide de {{sc("pil")}} de créer un "miroir" d'une image. Attention, il ne s'agit pas d'une rotation d'image. A titre d'exemple ci-dessous une image et son "miroir" en dessous, on ne doit pas utiliser une fonction qui existe déjà dans {{sc("pil")}} on doit créer le "miroir" simplement en manipulant les pixels de l'image de départ.
![logo python](./images/Projets/python-logo.png){: .imgcentre}
![logo python miroir](./images/Projets/python-logo-miroir.png){: .imgcentre}

* **[6pts]**  Réalisation d'un filtre sur image. Créer et tester le filtre sous la forme d'une fonction Python applicable à une image. Par exemple un filtre de pixellisation, voir par exemple : [le filtre de pixellisation](https://docs.gimp.org/2.8/fr/plug-in-pixelize.html){target=_blank} ou encore un filtre de flou ou de contour d'une image. Attention, il ne faut pas utiliser un filtre déjà existant dans {{sc("pil")}}, le but est d'en créer un en utilisant exclusivement les fonctions de manipulation de pixels.