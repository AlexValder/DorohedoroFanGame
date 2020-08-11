from . import CharacterBase as chbase
__all__ = ["Caiman"]

class AiPersonalities(chbase.Enum):
    '''
    Possible values of Caiman's\Ai's personalities.
    '''
    AI = 0
    KAI = 1
    AIKAWA = 2
    CAIMAN = 3


class Caiman(chbase.CharacterBase):
    '''
    Class for Caiman\Kai\Aikawa\Ai.
    '''
    def __init__(self):
        super().__init__(
                "Caiman",
                chbase.Gender.MALE,
                chbase.Species.HUMAN,
                chbase.WorldAlignment.HOLE,
                100,
                100
                )
        self._lives = 7
        self._personality = AiPersonalities.CAIMAN
        self._kai_meter = 0.0
        self._aikawa_meter = 0.0
    
    def switch_to_kai(self) -> Caiman:
        '''
        Switch to Kai.
        '''
        self._personality = AiPersonalities.KAI
        self._name = "Kai"
        self._species = chbase.Species.OTHER
        self._align = chbase.WorldAlignment.UNKNOWN
        return self

    def switch_to_aikawa(self) -> Caiman:
        '''
        Switch to Aikawa.
        '''
        self._personality = AiPersonalities.AIKAWA
        self._name = "Aikawa"
        self._species = chbase.Species.SORCERER
        self._align = chbase.WorldAlignment.SORCERER
        return self
    
    def switch_to_caiman(self) -> Caiman:
        '''
        Switch to (normal) Caiman with amnesia. For Nikaido's magic.
        '''
        self._kai_meter = 0.0
        self._aikawa_meter = 0.0
        self._personality = AiPersonalities.CAIMAN
        self._name = "Caiman"
        self._species = chbase.Species.HUMAN
        self._align = chbase.WorldAlignment.HOLE
        return self
    
    def switch_to_ultimate_caiman(self) -> Caiman:
        '''
        Switch to (end-of-the-story) Caiman without amnesia.
        '''
        self._kai_meter = -1.0
        self._aikawa_meter = -1.0
        self._personality = AiPersonalities.CAIMAN
        self._name = "Caiman"
        self._species = chbase.Species.OTHER
        self._align = chbase.WorldAlignment.HOLE
        return self
