from parsers import FighterParser

if __name__ == "__main__":

    fighter_parser = FighterParser(filename="combatants.json", verbosity=1)
    fighter_parser.read_fighters_from_file()
    combatants = fighter_parser.fighters
