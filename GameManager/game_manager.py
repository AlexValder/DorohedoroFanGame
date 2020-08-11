import colorama as color
from typing import Dict
from Characters import CharacterBase

__all__ = ["say"]


CHARACTERS : Dict[str, CharacterBase.CharacterBase] = dict()


def say(character : CharacterBase.CharacterBase, message : str) -> None:
    '''
    Character's replies and words. TODO: per-character reveal?
    '''
    print(f'{color.Fore.GREEN}[[{character._name}]]{color.Fore.RESET}\t{message}')