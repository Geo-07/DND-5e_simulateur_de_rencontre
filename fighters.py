"""ici on retrouvera tous les objets liés aux combattants et leurs méthodes
"""


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
        self.bonus_initiaitive = bonus_initiative
        self.classe_armure = classe_armure
        self.nombre_attaques = nombre_attaques
        self.pour_toucher = pour_toucher
        self.des_pour_toucher = des_pour_toucher
        self.critique_a = critique_a
        self.bonus_degats = bonus_degats
        self.nombre_des_degats = nombre_des_degats
        self.valeur_des_degats = valeur_des_degats

    def declare_ready_for_fight(self):
        """annonce un nouveau combattant prêt à se battre"""
        print(f"{self.nom} de l'équipe {self.equipe} est prêt au combat")
