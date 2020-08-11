import sys
from Characters.Caiman import Caiman
from Characters.Nikaido import Nikaido



if __name__ == "__main__":
    char : Caiman = Caiman()
    nikaido : Nikaido = Nikaido()

    char.introduce()
    nikaido.introduce()

    char.set_partner(nikaido)