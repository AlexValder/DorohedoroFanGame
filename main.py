import GameManager.game_manager as gm
import GameManager.output as o
from time import sleep


if __name__ == "__main__":
    gm.init_game()
    
    caiman = gm.CHARACTERS["Caiman"]
    nikaido = gm.CHARACTERS["Nikaido"]
    shin = gm.CHARACTERS["Shin"]

    for _ in range(0, 10):
        sleep(1.0)
        gm.next_turn()
        print()

    # o.say(caiman, caiman.introduce())
    # o.say(nikaido, nikaido.introduce())

    # print()

    # o.say(nikaido, "Do you want gyoza, Caiman?")
    # o.say(caiman, "Yes!🥟")

    # print()

    # o.say(shin, shin.introduce())
    
    # print()

    # o.health_stats()

    # print("Shin is about to attack Caiman and Nikaido!\n")

    # shin.attack(caiman)
    # shin.attack(nikaido)

    # o.health_stats()
