from parsers import FighterParser, CLIParser
from fighters import Status
from fight import Fight


def one_simulation(verbosity):
    # on lit le fichier json des combattants
    fighter_parser = FighterParser(filename="combatants.json", verbosity=1)
    fighter_parser.read_fighters_from_file()
    fighters = fighter_parser.fighters

    # on crée l'objet de combat, et on l'initialise
    fight_manager = Fight(fighters, verbosity=1)
    fight_manager.sort_fighters_by_initiative(verbosity=1)
    # et on lance le combat
    fight_manager.launch_fight()


def n_simulations(n: int):
    """effectue un certain nombre de simulations et affiche les statistiques de résultats

    Args:
        n (int): nombre de simulations
    """
    adventurers_win = 0
    ennemies_win = 0
    for i in range(n):
        # on recopie la liste, au lieu de la passer en référence.
        # ça permet de garder la liste du parser intacte pour les simulations suivantes
        fighter_parser = FighterParser(filename="combatants.json", verbosity=0)
        fighter_parser.read_fighters_from_file()
        fighters = fighter_parser.fighters

        # on crée l'objet de combat, et on l'initialise
        fight_manager = Fight(fighters, verbosity=0)
        fight_manager.sort_fighters_by_initiative(verbosity=0)

        # et on le lance
        winner = fight_manager.launch_fight()

        adventurers_win += 1 if winner == "Aventuriers" else 0
        ennemies_win += 1 if winner == "Ennemis" else 0

    print(f"\n\nles aventuriers ont gagné {adventurers_win} fois sur {n}")
    print(f"les ennemis ont gagné {ennemies_win} fois sur {n}")


if __name__ == "__main__":
    # pour plus tard, quand il faudra prendre les arguments dans la CLI
    cli_parser = CLIParser()

    n_simulations(10)
