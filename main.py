from Characters.Caiman import Caiman
from Characters.Nikaido import Nikaido
import GameManager.game_manager as gm


if __name__ == "__main__":
    char : Caiman = Caiman()
    nikaido : Nikaido = Nikaido()

    gm.say(char, char.introduce())
    
    char.set_partner(nikaido)

    gm.say(nikaido, "Do you want gyoza?")
    gm.say(char, "Yes!")

    gm.say(nikaido, f"Attempting to cast magic: {nikaido.cast_magic()}")

