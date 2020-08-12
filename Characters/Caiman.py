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
                100,
                20
                )
        self._lives = 7
        self._personality = AiPersonalities.CAIMAN
        self._kai_meter = 0.0
        self._aikawa_meter = 0.0
    
    def action(self) -> None:
        print("Caiman wants gyoza.")
    
    def switch_to_kai(self):
        '''
        Switch to Kai.
        '''
        self._personality = AiPersonalities.KAI
        self._name = "Kai"
        self._species = chbase.Species.OTHER
        self._align = chbase.WorldAlignment.UNKNOWN
        return self

    def switch_to_aikawa(self):
        '''
        Switch to Aikawa.
        '''
        self._personality = AiPersonalities.AIKAWA
        self._name = "Aikawa"
        self._species = chbase.Species.SORCERER
        self._align = chbase.WorldAlignment.SORCERER
        return self
    
    def switch_to_caiman(self):
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
    
    def switch_to_ultimate_caiman(self):
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
    
    def _die(self) -> str:
        if self._lives > 0:
            self._lives -= 1
            if self._personality == AiPersonalities.KAI:
                self.switch_to_aikawa()
            elif self._personality == AiPersonalities.AIKAWA:
                self.switch_to_kai()
            else:
                if self._kai_meter > .5 and self._kai_meter > self._aikawa_meter:
                    self.switch_to_kai()
                elif self._aikawa_meter > .5 and self._aikawa_meter > self._kai_meter:
                    self.switch_to_aikawa()
            return f"{self._name} died but still alive! Wow!"
        else:
            return "Caiman is gone. Game Over."
