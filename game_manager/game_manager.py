from characters import CharacterBase
from typing import Dict
import colorama as color
from characters.Caiman import Caiman
from characters.Nikaido import Nikaido
from characters.Shin import Shin
from characters.Noi import Noi


__all__ = ["CHARACTERS", "health_stats"]


CHARACTERS : Dict[str, CharacterBase.CharacterBase] = dict()
TURNS : int = 0

def init_game() -> None:
    TURNS = 0

    color.init()

    CHARACTERS["Caiman"] = Caiman()
    CHARACTERS["Nikaido"] = Nikaido()
    CHARACTERS["Shin"] = Shin()
    CHARACTERS["Noi"] = Noi()

    CHARACTERS["Caiman"].set_partner(CHARACTERS["Nikaido"])
    CHARACTERS["Shin"].set_partner(CHARACTERS["Noi"])


    print(f"{color.Fore.RED}GAME HAS STARTED{color.Fore.RESET}")


def next_turn() -> None:
    global TURNS
    print(f"{color.Fore.YELLOW}Turn: {TURNS}{color.Fore.RESET}")

    for char in CHARACTERS.keys():
        CHARACTERS[char].action()
    
    TURNS += 1