import dice
from fighters import Fighter, Status


class Fight:
    """la classe chargée de faire avancer le combat"""

    def __init__(self, fighters: [], verbosity):
        """crée l'objet chargé de générer le combat

        Args:
            fighters (Fighter[]): une liste de combattants
        """
        self.fighters = fighters
        self.verbosity = verbosity
        self.continue_fighting = True
        self.tour = 1

    def sort_fighters_by_initiative(self, verbosity):
        """sort fighters by their initiative"""
        for fighter in self.fighters:
            fighter.calculate_initiative()

        self.sorted_fighters = sorted(
            self.fighters, key=lambda fighter: fighter.initiative, reverse=True
        )

        if verbosity >= 1:
            self.display_fighters_order()

    def display_fighters_order(self):
        """display fighters by initiative"""
        print("\n\nordre d'initiative")
        for index, fighter in enumerate(self.sorted_fighters):
            print(f"{fighter.nom}: initiative: {fighter.initiative} rang: {index+1}")

    def find_first_character_of_team_or_none(self, team: str) -> Fighter:
        """selects the fighter of the given team with the highest initiative

        Args:
            team (string): the team that is attacked

        Returns:
            Fighter: the fighter that is selected
        """
        for fighter in self.sorted_fighters:
            if fighter.equipe == team and fighter.status == Status.ALIVE:
                return fighter
        return None

    def fight_turn(self):
        """executes a table turn"""
        for fighter in self.sorted_fighters:
            if fighter.equipe == "Aventuriers":
                opponent_team = "Ennemis"
            else:
                opponent_team = "Aventuriers"

            if fighter.status == Status.ALIVE:
                # attack
                opponent = self.find_first_character_of_team_or_none(opponent_team)
                fighter.attack(opponent, self.verbosity)

            elif fighter.status == Status.KO:
                # exécute ses jets de sauvegarde
                fighter.save_against_death()
            else:
                continue

            # on regarde si à la fin de l'attaque il reste des opposants
            if not self.reste_equipe(opponent_team):
                self.continue_fighting = False
                self.declare_winning_team(fighter.equipe)
                break
        self.tour += 1

    def reste_equipe(self, equipe: str) -> bool:
        """vérifie s'il reste ou non un combattant en etat de combattre dans l'équipe donnée

        Args:
            equipe (str): nom de l'équipe

        Returns:
            bool: True s'il reste un combattant dans cette équipe, False sinon
        """
        for fighter in self.sorted_fighters:
            if fighter.status == Status.ALIVE and fighter.equipe == equipe:
                return True
        return False

    def declare_winning_team(self, equipe):
        print(f"les {equipe} ont gagné le combat en {self.tour} tours")

    def launch_fight(self):
        """after initialisation of all the fight, launches it"""
        while self.continue_fighting:
            self.fight_turn()

        if self.reste_equipe("Aventuriers"):
            return "Aventuriers"
        else:
            return "Ennemis"
