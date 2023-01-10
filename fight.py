import dice


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
