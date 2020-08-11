import sys
from Characters import Caiman


if __name__ == "__main__":
    char = Caiman.Caiman()
    char.switch_to_caiman().introduce()
    char.switch_to_aikawa().introduce()
    char.switch_to_kai().introduce()
    char.switch_to_ultimate_caiman().introduce()