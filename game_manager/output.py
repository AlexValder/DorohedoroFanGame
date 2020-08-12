import colorama as color
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