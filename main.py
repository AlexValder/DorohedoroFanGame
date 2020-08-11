from Characters.Caiman import Caiman
from Characters.Nikaido import Nikaido
import GameManager.game_manager as gm


if __name__ == "__main__":
    gm.CHARACTERS["Caiman"] = Caiman()
    gm.CHARACTERS["Nikaido"] = Nikaido()

    caiman = gm.CHARACTERS["Caiman"]
    nikaido = gm.CHARACTERS["Nikaido"]

    gm.say(caiman, caiman.introduce())
    gm.say(nikaido, nikaido.introduce())

    print()

    gm.say(nikaido, "Do you want gyoza, Caiman?")
    gm.say(caiman, "Yes!🥟")
