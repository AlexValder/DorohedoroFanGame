import colorama as color
import textwrap as tw
from typing import Dict
from characters import CharacterBase
from .game_manager import CHARACTERS


__all__ = ["say"]


def say(character : CharacterBase.CharacterBase, message : str) -> None:
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

def show_inventory(char : CharacterBase.CharacterBase) -> None:
    '''
    Showing character's inventory.
    '''
    if not char._inventory:
        print(f"{char._name} has empty inventory.")
        return

    print(f"{char._name}'s inventory:")
    for item_id in char._inventory.keys():
        name : str = char._inventory[item_id]._name
        if len(name) <= 10:
            print(f"\n{color.Fore.CYAN}{char._inventory[item_id]._name}{color.Fore.RESET}\t\t{char._inventory[item_id]}", end="")
        else:
            shown_name = tw.wrap(name, 10)
            for line in shown_name:
                print(f"\n{color.Fore.CYAN}{line}{color.Fore.RESET}", end="")
            print(f"\t\t{char._inventory[item_id]}", end="")
    print()