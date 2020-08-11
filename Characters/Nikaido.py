from . import CharacterBase as chbase
__all__ = ["Nikaido"]

class Nikaido(chbase.CharacterBase):
    def __init__(self):
        super().__init__(
                "Nikaido",
                chbase.Gender.FEMALE,
                chbase.Species.SORCERER,
                chbase.WorldAlignment.HOLE,
                80,
                80
                )