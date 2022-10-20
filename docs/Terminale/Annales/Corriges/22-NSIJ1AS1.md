hide: - navigation  in docs.md

{% set repere_sujet = "22-NSIJ1AS1" %}

{{ corrige_sujetbac(repere_sujet) }}

{{ corrige_exobac(repere_sujet,1) }}

1. Une clé primaire doit être unique pour chaque enregistrement, donc :
    * `id_mere` ne peut pas servir de clé primaire pusiqu'une même femme peut avoir plusieurs enfants, par exemple dans l'extrait de table fourni, la mère d'`idMere` 13861 apparaît deux fois.
    * `(date, rang)` peut servir de clé primaire, en effet pour un jour donné, le rang de nécessaire est unique.
    * `(poids,taille)` ne peut pas servir de clé primaire puisque deux bébés différents peuvent être nés avec le même poids et la même taille.

2. Une clé étrangère doit être toujours présente en tant que clé primaire dans la table qu'elle référence. Ici, la clé étrangère `idMere` doit donc être présente en tant que clé primaire dans la table `Patientes`. La requête
```sql
DELETE FROM Patientes WHERE numPatiente = 13858;
```
produit donc une erreur, car dans la table `Naissances`, un enregistrement ayant pour `idMere` la valeur `13858` existe.

    !!! note
        De manière moins formelle, dans ce schéma de base de données, un bébé (enregistrement de `Naissances`) à nécessairement une mère (enregistrement de `Patientes`). On ne peut donc pas supprimer un enregistrement de `Patientes` qui correspond à une naissance.

3. 
```sql
INSERT INTO Patientes VALUES(13862,"Bélanger","Ninette","La Rochelle");
```

4. 
```sql
UPDATE Naissances SET prenom = "Laurette" 
WHERE date = "01/03/2022" and rang = 1;
```

    !!! note
        On modifie le prénom en sélectionnant le bébé par sa date et son rang de naissance (qui peut servir de clé primaire d'après la question 1).

5. 
```sql
SELECT nom,prenoms FROM Patientes
WHERE commune = "Aigrefeuille d'Aunis"
```

6. 
```sql
SELECT AVG(poids) FROM Naissances
JOIN TypesAccouchement ON TypesAccouchement.idAcc = Naissances.acc
WHERE TypesAccouchement.libelleAcc = "césarienne"
```

7. Cette requête renvoie :

| nom      | prenom  |
|----------|---------|
| Berthelot| Michelle|
| Samson   | Marine  |
| Baugé    | Gaëlle  |

C'est à dire les noms et prénoms des patientes ayant eu un accouchement de type 1.

{{ corrige_exobac(repere_sujet,2) }}

!!! note
    Un patient `p` est représenté par un tuple contenant son identifiant et son ordre de priorité. Donc `p[0]` est l'identifiant et `p[1]` la priorité.

1. 
```python
attente.append((50,4))
```

2.  a. C'est le *tri par sélection* (à chaque passage dans la boucle `for i in range(len(attente)` on recherche le patient le plus prioritaire à partir du ième et on le place en position `i`)

    b. La compléxité en temps des tris par insertion et pas sélection est **quadratique** : $\mathcal{O}(n^2)$.

3.  a.
    ```python
    def quitte(attente):
        return [patient from attente if patient[1]!=1]
    ```

    b. 
    ```python
    def maj(attente):
        return [(patient[0],patient[1]-1) for patient in attente]
    ```

4.  a.
    ```python
    def priorite(attente,p):
        for patient in attente:
            if patient[0]==p:
                return patient[1]
    ```

    b. 
    ```python
    def revise(attente,p):
        nouvelle = []
        n = priorite(attente,p)
        for (patient,prio) in attente:
            if patient == p :
                nouvelle.append((patient,1))
            elif prio < n:
                nouvelle.append((patient,prio+1))
            else:
                nouvelle.append((patient,prio+1))
        return nouvelle
    ```


{{ corrige_exobac(repere_sujet,3) }}

{{ corrige_exobac(repere_sujet,4) }}

{{ corrige_exobac(repere_sujet,5) }}
