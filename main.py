from parsers import FighterParser, CLIParser
from fighters import Status

if __name__ == "__main__":
    # pour plus tard, quand il faudra prendre les arguments dans la CLI
    cli_parser = CLIParser()

    # on lit le fichier json des combattants
    fighter_parser = FighterParser(filename="combatants.json", verbosity=0)
    fighter_parser.read_fighters_from_file()
    combatants = fighter_parser.fighters
