import colorama as color
import textwrap as tw
from typing import Dict
from characters import character_base
from . import game_manager as gm


__all__ = ["say"]


def say(character : character_base.CharacterBase, message : str) -> None:
    '''
    Character's replies and words. TODO: per-character reveal?
    '''
    print(f'{color.Fore.GREEN}[[{character._name}]]{color.Fore.RESET}\t{message}')


def health_stats() -> None:
    '''
    Displaying characters' current health
    '''
    for name, char in gm.CHARACTERS.items():
        print(f'{color.Fore.YELLOW}{name}{color.Fore.RESET}\t\t{char._health}/{char._max_health}')


def print_stats() -> None:
    __stas : Dict[str, str] = {
        "Name" : gm.PROTAG._name,
        "Gender" : gm.PROTAG._gender,
        "Species" : gm.PROTAG._species,
        "Health" : f"{gm.PROTAG._health}/{gm.PROTAG._max_health}",
    }

    for stat in __stas:
        print("{:<20}".format(f"{color.Fore.CYAN}{stat}{color.Fore.RESET}"), __stas[stat], sep = "")
    print()


def show_inventory(char : character_base.CharacterBase) -> None:
    '''
    Showing character's inventory.
    '''
    if not char._inventory:
        print(f"{char._name} has empty inventory.")
        return

    print(f"{char._name}'s inventory:")
    for item_id in char._inventory.keys():
        name : str = char._inventory[item_id]._name
        if len(name) <= 25:
            print("\n{:<25}".format(f"{color.Fore.CYAN}{name}{color.Fore.RESET}"), f"{char._inventory[item_id]}", sep="", end="")
        else:
            shown_name = tw.wrap(name, 25)
            for line in shown_name:
                print(f"\n{color.Fore.CYAN}{line}{color.Fore.RESET}", end="")
            print(f"{char._inventory[item_id]}", end="")
        print(f" [ID: {item_id}]", end="")
    print("\n")