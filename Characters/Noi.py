from . import character_base as chbase
from typing import Iterable
__all__ = ["Noi"]

class Noi(chbase.Sorcerer):
    '''
    Class for Noi.
    '''
    def __init__(self):
        super().__init__(
                "Noi",
                chbase.Gender.FEMALE,
                chbase.Species.SORCERER,
                chbase.WorldAlignment.SORCERER,
                250,
                250,
                40
                )
    
    def action(self) -> None:
        print("Noi wants to fight strong enemies.")
    
    def cast_magic(self, targets : Iterable) -> str:
        '''
        TODO: makes targets immobilized?
        '''
        for target in targets:
            target.heal(50)
        return "Heal successfull."