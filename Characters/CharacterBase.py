from enum import Enum
from typing import Optional
from colorama import Fore
from abc import ABC, abstractclassmethod


class Gender(Enum):
    '''
    Possible values of Gender field for characters
    '''
    MALE = 0
    FEMALE = 1
    UNKNOWN = 2

    def __str__(self) -> str:
        if self.value == 0:
            return "M"
        if self.value == 1:
            return "F"
        return "?"


class Species(Enum):
    '''
    Possible values of Species field for characters
    '''
    HUMAN = 0
    SORCERER = 1
    DEVIL = 2
    OTHER = 3

    def __str__(self) -> str:
        if self.value == 0:
            return "human"
        if self.value == 1:
            return "sorcerer"
        if self.value == 2:
            return "devil"
        return "?"


class WorldAlignment(Enum):
    '''
    Possible values of Alignment field for characters
    '''
    HOLE = 0
    SORCERER = 1
    HELL = 2
    UNKNOWN = 3

    def __str__(self) -> str:
        if self.value == 0:
            return "Hole"
        if self.value == 1:
            return "Sorcerer world"
        if self.value == 2:
            return "Hell"
        return "?"


class CharacterBase(ABC):
    '''
    Abstract base class for all characters, that contains general functions and fields, appliable for all characters.
    '''
    def __init__(
            self,
            name : str = "???",
            gender : Gender = Gender.UNKNOWN,
            species : Species = Species.OTHER,
            align : WorldAlignment = WorldAlignment.UNKNOWN,
            max_health : int = 100,
            health : int = 100,
            partner = None
                ):

        self._name : str = name
        self._gender : Gender = gender
        self._species : Species = species
        self._align : WorldAlignment = align

        self._max_health : int = max_health
        self._health : int = health

        self._partner = partner

    
    def introduce(self) -> str:
        '''
        Mostly testing method for character introduction.
        '''
        return f"Hello, I'm {self._name} ({self._gender}), I'm {self._species} from {self._align}"
    
    def set_partner(self, partner: CharacterBase) -> None:
        '''
        Setting partner. This function affects partner's object as well, if any is set.
        '''
        if partner == None:
            if self._partner == None:
                print(f"{self._name} already has no partner!")
            else:
                self._partner._partner = None
                self._partner = None
                print(f"{self._name} now has no partner!")
        else:
            if self._partner != None:
                self._partner._partner = None
            self._partner = partner
            print(f"{partner._name} is now {self._name}'s partner!")

class Sorcerer(ABC):
    '''
    Abstract base class for all sorcerer characters, that contains functions and fields, appliable to all sorcerers.
    '''
    def cast_magic(self, *targets) -> str:
        pass
