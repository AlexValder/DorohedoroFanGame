import game_manager.game_manager as gm
import game_manager.output as o
import items.item_base as items
from time import sleep
from characters.character_base import CharacterBase, Sorcerer


if __name__ == "__main__":
    gm.init_game()
    
    caiman = gm.CHARACTERS["Caiman"]
    nikaido = gm.CHARACTERS["Nikaido"]
    shin = gm.CHARACTERS["Shin"]
    noi = gm.CHARACTERS["Noi"]

    # for _ in range(0, 3):
    #     sleep(1.0)
    #     gm.next_turn()
    #     print()

    caiman.add_to_inventory(items.MeleeWeapon("Knife", 45))
    caiman.add_to_inventory(items.MeleeWeapon("Knife", 45))
    caiman.add_to_inventory(items.SmokeBottle(noi))

    o.show_inventory(caiman)

    caiman.remove_from_inventory(0)
    caiman.add_to_inventory(items.SmokeBottle(noi))

    o.show_inventory(caiman)
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
