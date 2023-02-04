hide: - navigation  in docs.md

{% set repere_sujet = "22-NSIJ1NC1" %}

{{ corrige_sujetbac(repere_sujet) }}



{{ corrige_exobac(repere_sujet,1) }}

{{ corrige_exobac(repere_sujet,2) }}

{{ corrige_exobac(repere_sujet,3) }}

{{ corrige_exobac(repere_sujet,4) }}

{{ corrige_exobac(repere_sujet,5) }}

**Partie 1 : Création de la classe compte**

1. 
```python linenums="1"
def crediter(self, montant):
    self.solde = self.solde + montant
```

2. 
```python
def debiter(self, montant):
    self.solde = self.solde - montant
```

3. 
```python linenums="1"
def est_positif(self):
    return self.montant >= 0
```

    !!! note
        On pourrait aussi écrire :
        ```python
        def est_positif(self):
            if self.montant >= 0:
                return True
            else:
                return False
        ```

**Partie 2 : Utilisation de la classe compte**

1. `cpt_0123456A = Compte("0123456A","MARTIN Dominique","12 rue des sports")`

    !!! note
        On rappelle que la méthode `__init__` de la classe `Compte` ne prend pas en argument le solde (il est fixé à zéro initialement dans la méthode)
    
2. `cpt_01234561.crediter(200)`

3. 
```python linenums="1"
def transferer(self,autre_compte,montant):
    self.debiter(self,montant)
    autre_compte.crediter(montant)
```

    !!! note
        L'énoncé précise de ne pas modifier directement les attributs.

**Partie 3 : Gestion des comptes**

1. 
```python linenums="1"
def recherche_debiteurs(liste_comptes):
    liste_debiteurs = {} #(1)
    for compte in liste_comptes: #(2)
        if not compte.est_positif(): #(3)
            liste_debiteurs[compte.adherent] = compte.solde #(4)
    return liste_debiteurs

```
    1. On crée un dictionnaire vide
    2. On parcourt la liste des comptes
    3. Si le solde n'est pas positif
    4. On ajoute dans le dictionnaire la clé nom de l'adhérent avec pour valeur le solde du compte.

2. 
```python
def urgent_debiteur(liste_debiteurs):
    mini = 0
    nom_mini = None
    for debiteur in liste_debiteurs:
        if liste_debiteurs[debiteur] < mini:
            nom_mini = debiteur
    return nom_mini
```

!!! note
    Le sujet ne précise pas comment traiter le cas où le dictionnaire `liste_debiteurs` est pas vide (il n'y   aucun débiteur). Dans cette correction la fonction renverra `None`.