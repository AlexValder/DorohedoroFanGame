from . import CharacterBase as chbase
__all__ = ["Nikaido"]

class Nikaido(chbase.CharacterBase, chbase.Sorcerer):
    def __init__(self):
        super().__init__(
                "Nikaido",
                chbase.Gender.FEMALE,
                chbase.Species.SORCERER,
                chbase.WorldAlignment.HOLE,
                80,
                80
                )
    def cast_magic(self, *targets) -> None:
        print(f"I can't...")
