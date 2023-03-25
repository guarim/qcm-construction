hide: - navigation  in docs.md

{% set repere_sujet = "23-NSIJ1ME1" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1.  a. Un attribut doit être **unique** pour chaque enregistrement afin d'être une clé primaire

    b. Une clé étrangère est la clé primaire d'une autre relation, ici dans la relation commandes la clé étrangère `#idClient` permet de faire référence à un enregistrement de la table `Clients` et la clé étrangère `#idMeuble` permet de faire référence à un enregistrement de la table `Meubles`.

    c. **Meubles**(^^id^^, intitule, prix, stock, description)

2. Cette requête renvoie :

| id | stock | description |
|----|-------|-------------|
|62  | 2     | 'Armoire blanche 3 portes' |
|63  | 3     | 'Armoire noire 3 portes' |

3. Pour afficher les noms et prénoms des clients habitant à Paris, on peut utiliser la requête :

```sql
SELECT nom, prenom
FROM Clients 
WHERE ville = 'Paris'
```


{{ corrige_exobac(repere_sujet,2) }}


{{ corrige_exobac(repere_sujet,3) }}
