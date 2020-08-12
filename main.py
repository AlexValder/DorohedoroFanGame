from Characters.Caiman import Caiman
from Characters.Nikaido import Nikaido
from Characters.Shin import Shin
import GameManager.game_manager as gm


if __name__ == "__main__":
    gm.CHARACTERS["Caiman"] = Caiman()
    gm.CHARACTERS["Nikaido"] = Nikaido()
    gm.CHARACTERS["Shin"] = Shin()

    caiman = gm.CHARACTERS["Caiman"]
    nikaido = gm.CHARACTERS["Nikaido"]
    shin = gm.CHARACTERS["Shin"]

    gm.say(caiman, caiman.introduce())
    gm.say(nikaido, nikaido.introduce())

    print()

    gm.say(nikaido, "Do you want gyoza, Caiman?")
    gm.say(caiman, "Yes!🥟")

    print()

    gm.say(shin, shin.introduce())
    for char in gm.CHARACTERS.keys():
        print(f"{char}\t\t{gm.CHARACTERS[char]._health}/{gm.CHARACTERS[char]._max_health}")
