hide: - navigation  in docs.md

{% set repere_sujet = "23-NSIJ2LR1" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1.  En suivant l'arbre comme indiqué dans l'énoncé, on trouve :

    * le code de la lettre `N` est `-o`
    * le code de la lettre `S` est `ooo`
    * le code de la lettre `I` est `oo`

    Donc, le code morse de `NSI` est `-o ooo oo`

2. Représentation du sous arbre pour les lettres `G`, `M`, `O`, `Q`, `Z` :

```mermaid
    graph TD
    R1[" "] --> V1[" "]
    R1-- - --> T["T"]
    T --> V2[" "]
    T -- - --> M["M"]
    M -- - --> O["O"]
    M -- o --> G["G"]
    G -- - --> Q["Q"]
    G -- o --> Z["Z"]
    style V1 fill:#FFFFFF, stroke:#FFFFFF
    linkStyle 0 stroke:#FFFFFF,stroke-width:0px
    style V2 fill:#FFFFFF, stroke:#FFFFFF
    linkStyle 2 stroke:#FFFFFF,stroke-width:0px
```

3. 

{{ corrige_exobac(repere_sujet,2) }}


{{ corrige_exobac(repere_sujet,3) }}
