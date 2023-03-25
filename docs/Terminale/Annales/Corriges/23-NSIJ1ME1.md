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

1. Comme il y a toujours plusieurs chemins possibles entre deux routeurs (par exemple entre `R1` et `R2`, on peut passer directement par la liaison 1 mais aussi par `R3` avec liaison4 et liaison3)  si une liaison est coupée le réseau reste fonctionnel car un autre chemin existe.

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
| SiteB        | R2      | 1               |
| SiteB        | R2      | 2               |
| SiteD        | R3      | 2               |

4. Le protocole RIP ne tient pas compte du débit des liaisons pour relier `R2` a `R5` la liaison2 sera donc toujours privilégiée car elle minimise le nombre de routeurs traversé or si cette liaison a un débit nettement inférieur aux autres, il est possible que la route {{route(["`R2`","`R3`","`R4`","`R5`"])}} soit plus rapide.

5. Le coût d'une liaison est *inversement proportionnel* à son débit, c'est à dire que  le coût le plus élévé correspond au débit le plus faible. Ici c'est donc la liaison `Liaison2` qui a la débit le plus faible.

{{ corrige_exobac(repere_sujet,3) }}
