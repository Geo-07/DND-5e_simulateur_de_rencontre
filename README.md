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
    v-0.1 : Appropriation d'un code généré par chat GPT qui m'a permis 
            d'apprendre à programmer en python
            
    v-0.2 : Réalisation d'un premier programme fonctionnel permettant de 
            simuler une rencontre.
            
    v-0.3 : EN COURS DE DÉVELOPPEMENT
            Amélioration des commentaires
            Inventaire des améliorations à apporter


## le simulateur

Ce projet a pour but de créer un simulateur de rencontres pour DND 5e.

## comment l'installer

- cloner le dépôt ```git clone [repo address]```
- créer un environnement virtuel: ``` python -m venv env ```
- activer l'environnement tout juste créé: ```source env/bin/activate # différent si sous windows```
- installer les dépendances ```pip install -r requirements.txt```

## comment l'utiliser

dans le fichier main.py, configurer l'exécution dans la zone en bas, en utilisant une des deux fonctions au-dessus (ou en en créant une autre)

ensuite, depuis le terminal, lancer ```python main.py```

## A faire

- verbosité :
    * Passer verbose en type 'int' avec : 
        + 0 : pas de détail,
        + 1 : détails minimalistes,
        + 2 : un peu plus de détails, 
        + etc. ...

- niveau_de_detail cf verbosité :
    Si pas de détails sélectionnés, passer le résultat en retour de la 
    fonction combat() plutôt que d'en forcer l'impression dans la console.
    
- Critique :
    * Gestion des coups critiques

- Suppression des noms d'équipes en str, 
    * remplacer par un type énuméré un peu partout

- ajout de fonctionnalités pour lancer le script depuis la CLI (utiilsation de la lib argparse, probablement)