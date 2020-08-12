import colorama as color
import textwrap as tw
from typing import Dict
from characters import character_base
from .game_manager import CHARACTERS


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
    for char in CHARACTERS.keys():
        print(f'{color.Fore.YELLOW}{char}{color.Fore.RESET}\t\t{CHARACTERS[char]._health}/{CHARACTERS[char]._max_health}')

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