from parsers import FighterParser, CLIParser
from fighters import Status
from fight import Fight

if __name__ == "__main__":
    # pour plus tard, quand il faudra prendre les arguments dans la CLI
    cli_parser = CLIParser()

    # on lit le fichier json des combattants
    fighter_parser = FighterParser(filename="combatants.json", verbosity=0)
    fighter_parser.read_fighters_from_file()
    combatants = fighter_parser.fighters

    # on crée l'objet de combat, et on l'initialise
    fight_manager = Fight(combatants)
    fight_manager.sort_fighters_by_initiative()
    fight_manager.display_fighters_order()
