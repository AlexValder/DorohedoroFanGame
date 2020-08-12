from typing import Dict, Callable
from . import output as ot
from characters.character_base import CharacterBase
from characters.caiman import Caiman
from characters.nikaido import Nikaido
from characters.noi import Noi
from characters.shin import Shin
import colorama as color

__all__ = ["CHARACTERS", "health_stats"]


CHARACTERS : Dict[str, CharacterBase] = dict()
PROTAG : CharacterBase
TURNS : int = 0


def init_game() -> None:
    color.init()

    CHARACTERS["Caiman"] = Caiman()
    CHARACTERS["Nikaido"] = Nikaido()
    CHARACTERS["Shin"] = Shin()
    CHARACTERS["Noi"] = Noi()

    CHARACTERS["Caiman"].set_partner(CHARACTERS["Nikaido"])
    CHARACTERS["Shin"].set_partner(CHARACTERS["Noi"])

    global PROTAG
    PROTAG = CHARACTERS["Caiman"]

    print(f"{color.Fore.RED}GAME HAS STARTED{color.Fore.RESET}")


def next_turn() -> None:
    global TURNS
    print(f"{color.Fore.YELLOW}Turn: {TURNS}{color.Fore.RESET}")

    for char in CHARACTERS.keys():
        CHARACTERS[char].action()
    
    TURNS += 1


def print_inventory() -> None:
    global PROTAG
    ot.show_inventory(PROTAG)


COMMANDS : Dict[str, Callable] = {
    "skip" : next_turn,
    "my stats" : ot.print_stats,
    "show inventory" : print_inventory,
    "exit" : exit,
}