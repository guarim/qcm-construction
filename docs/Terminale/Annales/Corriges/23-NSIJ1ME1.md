hide: - navigation  in docs.md

{% set repere_sujet = "23-NSIJ1ME1" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1.  a. Un attribut doit être **unique** pour chaque enregistrement afin d'être une clé primaire.

    b. Une clé étrangère est la clé primaire d'une autre relation, ici dans la relation commandes la clé étrangère `#idClient` permet de faire référence à un enregistrement de la table `Clients` et la clé étrangère `#idMeuble` permet de faire référence à un enregistrement de la table `Meubles`. Ces deux clés permettent de mettre en relation les meubles et les clients qui les ont achetés.

    c. **Meubles**(^^id^^ : {{sc("int")}}, intitule : {{sc("txt")}}, prix : {{sc("float")}}, stock : {{sc("int")}}, description : {{sc("txt")}})

2. Cette requête renvoie :

    | id | stock | description |
    |----|-------|-------------|
    |62  | 2     | 'Armoire blanche 3 portes' |
    |63  | 3     | 'Armoire noire 3 portes' |

3. Pour afficher les noms et prénoms des clients habitant à Paris, on peut utiliser la requête :
```sql
SELECT nom, prenom
FROM Clients 
WHERE ville = 'Paris';
```

4. Pour mettre à jour la base de données :
```sql
UPDATE Meubles
SET stock=50
WHERE id=98;
```

5. Pour ajouter l'article à la relation `Meubles` :
```sql
INSERT INTO Meubles
VALUES (65, "matta", 95.99, 25, "Tapis vert à pois rouge");
```

    !!! Note
        Dans la requête précédente, comme on insère les valeurs pour toutes les colonnes on a pas précisé les noms des colonnes. On peut aussi utiliser :

        ```sql
        INSERT INTO Meubles (id, intitule, prix, stock, description)
        VALUES (65, "matta", 95.99, 25, "Tapis vert à pois rouge");
        ```

6. Les noms et prénoms des clients se trouvent dans la table `Clients` et la date de la commande dans la table `Commandes`, on fait donc un `JOIN` entre ces deux tables 
```sql
SELECT Clients.nom, Clients.prenom
FROM Clients
JOIN Commandes ON Clients.id = Commandes.idClient
WHERE Commandes.date = "30/04/2021"
```

    !!! Note
        Si un client a commandé plusieurs meubles le 30/04/2021 alors il apparaîtra plusieurs fois, on peut éviter ce problème en ajoutant `DISTINCT` après `SELECT`.

{{ corrige_exobac(repere_sujet,2) }}

1. Comme il y a toujours plusieurs chemins possibles entre deux routeurs (par exemple entre `R1` et `R2`, on peut passer directement par  `Liaison1` mais aussi par `R3` avec `Liaison4` et `Liaison3`)  si une liaison est coupée le réseau reste fonctionnel car un autre chemin existe.

2. On consulte les tables de routage :
* Le siteB est relié au routeur `R2` qui indique `R3` lorsque la destination est SiteC
* Le routeur `R3` indique `R4` lorsque la destination est siteC
* Le routeur `R4` indique `R5` lorsque la destination est siteC
* Le routeur `R5` indique `Local` lorsque la destination est siteC

Le chemin suivi sera donc : {{route(["SiteB","`R2`","`R3`","`R4`","`R5`","SiteC"])}}

3. Puisque le protocole RIP minimise le nombre de routeurs traversés, la table de routage du routeur `R1` sera : 

| Destination  | Suivant | Nombre de sauts |
|--------------|---------|-----------------|
| SiteA        | Local   | 0               |
| SiteB        | `R2`    | 1               |
| SiteC        | `R2`    | 2               |
| SiteD        | `R3`    | 2               |

4. Le protocole RIP ne tient pas compte du débit des liaisons pour relier `R2` a `R5` la `Liaison2` sera donc toujours privilégiée car elle minimise le nombre de routeurs traversé or si cette liaison a un débit nettement inférieur aux autres, il est possible que la route {{route(["`R2`","`R3`","`R4`","`R5`"])}} soit plus rapide.

5.  a. Le coût d'une liaison est *inversement proportionnel* à son débit, c'est à dire que  le coût le plus élevé correspond au débit le plus faible. Ici c'est donc la liaison `Liaison2` qui a la débit le plus faible.

    b. Liste des 4 chemins possibles pour aller de SiteA à SiteC avec leurs coûts :

    * {{route(["`R1`","`R2`","`R5`"])}} avec un coût de $1\,100\,000$
    * {{route(["`R1`","`R3`","`R2`","`R5`"])}} avec un coût de $1\,050\,005$
    * {{route(["`R1`","`R3`","`R4`","`R5`"])}} avec un coût de $50\,015$
    * {{route(["`R1`","`R2`","`R3`","`R4`","`R5`"])}} avec un coût de $100\,020$

    c. Table de routage OSPF du routeur `R1` :

    | Destination  | Suivant | Coût |
    |--------------|---------|-----------------|
    | SiteA        | Local   | 0               |
    | SiteB        | `R3`    | $50\,005$        |
    | SiteC        | `R3`    | $50\,015$       |
    | SiteD        | `R3`    | $50\,005$        |




{{ corrige_exobac(repere_sujet,3) }}

**Partie 1**

1. `nom`, `tab_voisines`, `tab_couleurs_disponibles` et `couleur_attribuee`  sont des *attributs* (de la classe `Region`)

2. Le paramètre `nom_region` est de type `str` (chaine de caractères)

3. `ge = Region("Grand Est")`

4. `return self.tab_couleurs_disponibles[0]`

5. `return len(self.tab_voisines)`

6. `return self.couleur_attribuee != None`

    !!! note
        On peut aussi écrire :
        ```python
        if self.couleur_attribuee != None:
            return True
        else:
            return False
        ```

7. 
```python
if couleur in self.tab_couleurs_disponibles:
    self.tab_couleurs_disponibles.remove(couleur)
```

    !!! note
        Comme rappelé dans l'énoncé `remove` provoque une erreur lorsque l'élément à enlever ne se trouve pas dans la liste. On vérifie donc la présence de la couleur à l'aide de `in` avant de la supprimer.

8. 
```python
for voisine in self.tab_voisines:
    if voisine == region:
        return True
return False
```

    **Partie 2**

9. 
```python
non_coloriees = []
for region in self.tab_regions:
    if not region.est_coloriee():
        non_coloriees.append(region)
return non_coloriees
```

    !!! note
        On peut proposer une version utilisant les listes définies par compréhension :
        ```python
        return [region for region in self.tab_regions if not region.est_coloriee()]
        ```

10. a. Cette méthode renvoie `None` lorsqu'il n'y a plus aucune région non coloriée.

    b. La région renvoyée n'est pas encore coloriée et possède le plus de regions voisines.

11. 
```python
def colorie(self):
    while self.renvoie_max() != None:
        a_colorier = self.renvoie_max()
        couleur_choisie = a_colorier.renvoie_premiere_couleur_disponible()
        for voisine in a_colorier.tab_voisines:
            voisine.retire_couleur(couleur_choisie)
```