from . import CharacterBase as chbase
__all__ = ["Caiman"]

class AiPersonalities(chbase.Enum):
    AI = 0
    KAI = 1
    AIKAWA = 2
    CAIMAN = 3


class Caiman(chbase.CharacterBase):
    def __init__(self):
        super().__init__("Caiman", chbase.Gender.MALE, chbase.Species.HUMAN, chbase.WorldAlignment.HOLE)
        self._lives = 7
        self._personality = AiPersonalities.CAIMAN
        self._kai_meter = 0.0
        self._aikawa_meter = 0.0
    
    def switch_to_kai(self) -> None:
        self._personality = AiPersonalities.KAI
        self._name = "Kai"

    def switch_to_aikawa(self) -> None:
        self._personality = AiPersonalities.AIKAWA
        self._name = "Aikawa"
    
    def switch_to_caiman(self) -> None:
        self._kai_meter = 0.0
        self._aikawa_meter = 0.0
        self._personality = AiPersonalities.CAIMAN
        self._name = "Caiman"