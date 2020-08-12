from characters import character_base
from typing import Dict
import colorama as color
from characters.caiman import Caiman
from characters.nikaido import Nikaido
from characters.shin import Shin
from characters.noi import Noi


__all__ = ["CHARACTERS", "health_stats"]


CHARACTERS : Dict[str, character_base.CharacterBase] = dict()
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