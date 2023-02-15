hide: - navigation  in docs.md

{% set repere_sujet = "22-NSIJ1JA1" %}

{{ corrige_sujetbac(repere_sujet) }}



{{ corrige_exobac(repere_sujet,1) }}



{{ corrige_exobac(repere_sujet,2) }}

{{ corrige_exobac(repere_sujet,3) }}

{{ corrige_exobac(repere_sujet,4) }}

1. 
```python
def ajouter_beurre(self,qt):
    self.qt_beurre += qt
```

2. 
```python
def afficher(self):
    return f"farine : {self.farine} \n oeuf : {self.nb_oeufs} \n beurre : {self.qt_beurre}"
```

3. 
```python
def stock_suffisant_brioche(self):
    return self.farine >= 350 and self.beurre >= 175 and self.nb_oeufs >= 4
```

4.  a. La valeur qui s'affiche dans la console est **2**, cette valeur est le nombre maximal de brioches qu'on peut produire    avec 1000 g de beurre, 1000g de farine et 10 oeufs (on est limité par le nombre d'oeufs).

    b. Dans la console, on aura l'affichage suivant :
        ```pycon
        >>> mon_stock.afficher()
        farine : 300
        oeuf : 2
        beurre : 650
        ```

5. 
```python
def nb_brioches(liste_stocks):
    total = 0
    for stock in liste_stocks:
        total += stock.produire()
    return total
```


{{ corrige_exobac(repere_sujet,5) }}
