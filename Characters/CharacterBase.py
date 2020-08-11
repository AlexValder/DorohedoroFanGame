from enum import Enum


class Gender(Enum):
    MALE = 0
    FEMALE = 1
    UNKNOWN = 2


class Species(Enum):
    HUMAN = 0
    SORCERER = 1
    DEVIL = 2
    OTHER = 3


class WorldAlignment(Enum):
    HOLE = 0
    SORCERER = 1
    HELL = 2
    UNKNOWN = 3


def _gender_to_str(gender : Gender) -> str:
    if gender == Gender.MALE:
        return "M"
    if gender == Gender.FEMALE:
        return "F"
    return "?"


def _species_to_str(species : Species) -> str:
    if species == Species.HUMAN:
        return "human"
    if species == Species.SORCERER:
        return "sorcerer"
    if species == Species.DEVIL:
        return "devil"
    return "?"


def _align_to_str(align : WorldAlignment) -> str:
    if align == WorldAlignment.HOLE:
        return "Hole"
    if align == WorldAlignment.SORCERER:
        return "Sorcerer World"
    if align == WorldAlignment.HELL:
        return "Hell"
    return "?"


class CharacterBase:
    def __init__(
            self,
            name : str = "???",
            gender : Gender = Gender.UNKNOWN,
            species : Species = Species.OTHER,
            align : WorldAlignment = WorldAlignment.UNKNOWN
                ):
        self._name = name
        self._gender = gender
        self._species = species
        self._align = align
    
    def introduce(self):
        print(f"Hello, I'm {self._name} ({_gender_to_str(self._gender)}), I'm {_species_to_str(self._species)} from {_align_to_str(self._align)}")

if __name__ == "__main__":
    char = CharacterBase("Dude", Gender.MALE, Species.HUMAN, WorldAlignment.HOLE)
    char.introduce()