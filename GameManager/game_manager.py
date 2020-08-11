import colorama as color
from Characters import CharacterBase

__all__ = ["say"]

def say(character : CharacterBase.CharacterBase, message : str) -> None:
    print(f'{color.Fore.GREEN}[[{character._name}]]{color.Fore.RESET}\t{message}')