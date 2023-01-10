import dice
from fighters import Fighter


class Fight:
    """la classe chargée de faire avancer le combat"""

    def __init__(self, fighters: []):
        """crée l'objet chargé de générer le combat

        Args:
            fighters (Fighter[]): une liste de combattants
        """
        self.fighters = fighters

    def sort_fighters_by_initiative(self):
        """sort fighters by their initiative"""
        for fighter in self.fighters:
            fighter.calculate_initiative()

        self.sorted_fighters = sorted(
            self.fighters, key=lambda fighter: fighter.initiative, reverse=True
        )

    def display_fighters_order(self):
        """display fighters by initiative"""
        for index, fighter in enumerate(self.sorted_fighters):
            print(f"{fighter.nom}: initiative: {fighter.initiative} rang: {index+1}")

    def find_first_character_of_team(self, team: str) -> Fighter:
        """selects the fighter of the given team with the highest initiative

        Args:
            team (string): the team that is attacked

        Returns:
            Fighter: the fighter that is selected
        """
        for fighter in self.sorted_fighters:
            if fighter.equipe == team:
                return fighter
