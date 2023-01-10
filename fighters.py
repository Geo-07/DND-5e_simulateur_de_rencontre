"""ici on retrouvera tous les objets liés aux combattants et leurs méthodes
"""
import dice
from enum import Enum


class Status(Enum):
    ALIVE = (1, "en vie")
    KO = (2, "KO")
    DEAD = (3, "mort")
    STABLE = (4, "stabilisé")


class Combattant:
    "a standard fighter"

    def __init__(
        self,
        nom,
        equipe,
        points_vie,
        bonus_initiative,
        classe_armure,
        nombre_attaques,
        pour_toucher,
        des_pour_toucher,
        critique_a,
        bonus_degats,
        nombre_des_degats,
        valeur_des_degats,
    ):
        self.nom = nom
        self.equipe = equipe
        self.points_vie = points_vie
        self.bonus_initiative = bonus_initiative
        self.classe_armure = classe_armure
        self.nombre_attaques = nombre_attaques
        self.pour_toucher = pour_toucher
        self.des_pour_toucher = des_pour_toucher
        self.critique_a = critique_a
        self.bonus_degats = bonus_degats
        self.nombre_des_degats = nombre_des_degats
        self.valeur_des_degats = valeur_des_degats
        self.jdsmort = 0
        self.jdsvie = 0
        self.satus = Status.ALIVE

    def declare_ready_for_fight(self):
        """annonce un nouveau combattant prêt à se battre"""
        print(f"{self.nom} de l'équipe {self.equipe} est prêt au combat")

    def save_against_death(self):
        """when a fighter is KO, he throws a d20t each turn.
        whether it is >10 or not,
        two counters are incremented.
        the first one reaching 3 gives the status of the fighter
        """

        # roll the dice and increment the value
        if dice.roll("1d20t") < 10:
            self.jdsmort += 1
        else:
            self.jdsvie += 1

        # if a counter reaches 3, the fighter's status changes
        if self.jdsmort >= 3:
            self.status = Status.DEAD
        if self.jdsvie >= 3:
            self.status = Status.STABLE

    def calculate_initiative(self):
        self.initiative = dice.roll("1d20t") + self.bonus_initiative
