# DND-5e_simulateur_de_rencontre
Simulateur de rencontre pour DND 5e

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

Created on : Sun Jan  1 10:04:20 2023
============


Versions :
==========
    v-0.1 : Appropriation d'un code g�n�r� par chat GPT qui m'a permis 
            d'apprendre � programmer en python
            
    v-0.2 : R�alisation d'un premier programme fonctionnel permettant de 
            simuler une rencontre.
            
    v-0.3 : EN COURS DE D�VELOPPEMENT
            Am�lioration des commentaires
            Inventaire des am�liorations � apporter


## le simulateur

Ce projet a pour but de créer un simulateur de rencontres pour DND 5e.

## comment l'installer

- cloner le dépôt
- créer un environnement virtuel: ``` python -m venv env ```
- activer l'environnement tout juste créé: ```source env/bin/activate # différent si sous windows```
- installer les dépendances ``` pip install -r requirements.txt```

## comment l'utiliser

```secret: j'ai aucune idée de comment c'est sensé fonctionner, donc j'ai laissé ta doc telle quelle```

```python
rencontre(fichier, verbose)
```

arguments:
- fichier : str
    Nom du fichier 'combatants.json' contenant la liste des combatants
- verbose : str ou boolean
    Niveau de d�tail du retour console :
        False : Aucun retour # @todo_Niveau_de_detail

## A faire
- BUG : Sous l'IDE Spyder, j'ai une bonne gestion des caract�res (encodage 
    UTF-8 ?) mais pas ailleurs ...
    
- Usage :
    *Remplir correctement la section 'Usage' ci-dessous dans la 
    documentation de ce programme.

- verbosité :
    * Passer verbose en type 'int' avec : 
        + 0 : pas de d�tail,
        + 1 : d�tails minimalistes,
        + 2 : un peu plus de d�taile, 
        + etc. ...
- niveau_de_detail :
    Si pas de d�tails s�lectionn�, passer le r�sultat en retour de la 
    fonction combat() plut�t que d'en forcer l'impression dans la console.
    
- Critique :
    * Gestion des coups critiques




            