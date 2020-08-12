from . import CharacterBase as chbase
__all__ = ["Shin"]

class Shin(chbase.CharacterBase, chbase.Sorcerer):
    '''
    Class for Shin.
    '''
    def __init__(self):
        super().__init__(
                "Shin",
                chbase.Gender.MALE,
                chbase.Species.SORCERER,
                chbase.WorldAlignment.SORCERER,
                150,
                150,
                50
                )
    
    def cast_magic(self, *targets) -> str:
        '''
        TODO: makes targets immobilized?
        '''
        for target in targets:
            target.damage(10)
        return "Attack successfull."