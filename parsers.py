""" tout ce qui a à voir avec l'import des combattants"""

import json
from fighters import Combattant


class CLIParser:
    """objet qui sera chargé de récupérer les arguments depuis la CLI"""

    pass


class FighterParser:
    "objet chargé d'importer les combattants"

    def __init__(self, filename="combatants.json", verbosity=0):
        """constructeur

        Args:
            filename (_type_): nom du fichier contenant les combattants
            verbosity (_type_): verbosité souhaitée
        """
        self.filename = filename
        print(f"le fichier {self.filename} sera utilisé pour importer les combattants")
        self.verbosity = verbosity
        self.fighters = []

    def read_fighters_from_file(self) -> []:
        """
        méthode permettant à la classe d'importer une liste de combattants
        """
        with open(self.filename, "r", encoding="utf-8") as file:
            donnees = json.load(file)

        for data in donnees:
            fighter = Combattant(
                nom=data.get("nom"),
                equipe=data.get("equipe"),
                points_vie=data.get("pv"),
                bonus_initiative=data.get("bonus_initiative"),
                classe_armure=data.get("ca"),
                nombre_attaques=data.get("nombre_attaques"),
                pour_toucher=data.get("pour_toucher"),
                des_pour_toucher=data.get("des_pour_toucher"),
                critique_a=data.get("critique_a"),
                bonus_degats=data.get("bonus_degats"),
                nombre_des_degats=data.get("nombre_des_degats"),
                valeur_des_degats=data.get("valeur_des_degats"),
            )
            self.fighters.append(fighter)
            if self.verbosity >= 1:
                fighter.declare_ready_for_fight()

    def get_fighters(self):
        """return fighters from thyis class"""
        return self.fighters
