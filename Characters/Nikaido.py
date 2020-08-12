from . import character_base as chbase
from typing import Iterable
__all__ = ["Nikaido"]

class Nikaido(chbase.Sorcerer):
    '''
    Class for Nikaido.
    '''
    def __init__(self):
        super().__init__(
                "Nikaido",
                chbase.Gender.FEMALE,
                chbase.Species.SORCERER,
                chbase.WorldAlignment.HOLE,
                80,
                80
                )


    def action(self) -> None:
        print("Nikaido wants to watch people eat.")


    def cast_magic(self, targets : Iterable) -> str:
        '''
        TODO: time-reversing&rewriting magic.
        '''
        return "My psychological trauma holds me back"
