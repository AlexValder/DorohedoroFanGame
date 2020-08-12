import game_manager.game_manager as gm
import game_manager.output as o
import items.item_base as items
from time import sleep
from characters.character_base import CharacterBase, Sorcerer


if __name__ == "__main__":
    gm.init_game()
    
    caiman = gm.PROTAG
    nikaido = gm.CHARACTERS["Nikaido"]
    shin = gm.CHARACTERS["Shin"]
    noi = gm.CHARACTERS["Noi"]

    caiman.add_to_inventory(items.MeleeWeapon("Knife", 45))
    caiman.add_to_inventory(items.MeleeWeapon("Knife", 45))
    caiman.add_to_inventory(items.SmokeBottle(noi))

    command : str
    while True:
        command = input()
        if command in gm.COMMANDS.keys():
            gm.COMMANDS[command]()