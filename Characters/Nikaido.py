from . import CharacterBase as chbase
__all__ = ["Nikaido"]

class Nikaido(chbase.CharacterBase, chbase.Sorcerer):
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


    def cast_magic(self, *targets) -> str:
        '''
        TODO: time-reversing&rewriting magic.
        '''
        return "My psychological trauma holds me back"
