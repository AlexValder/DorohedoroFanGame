from enum import Enum
from typing import Iterable, Dict, Tuple
from abc import ABC, abstractclassmethod
import random


__all__ = ["CharacterBase", "Gender", "Species", "Sorcerer"]


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
            max_attack : int = 10,
            location : Tuple[str, str] = ("", ""),
            partner = None
                ):

        self._name : str = name
        self._gender : Gender = gender
        self._species : Species = species
        self._align : WorldAlignment = align

        self._max_health : int = max_health
        self._health : int = health

        self._partner = partner

        self._max_attack : int = max_attack

        self._inventory : dict = dict()

    
    def attack(self, target) -> None:
        if hasattr(target, "damage"):
            target.damage(random.randint(0, self._max_attack))


    def heal(self, heal_value : int) -> None:
        self._health += heal_value
        if self._health > self._max_health:
            self._health = self._max_health
    

    def damage(self, damage_value : int) -> None:
        self._health -= damage_value
        if self._health <= 0:
            self._die()
    

    def add_to_inventory(self, new_item) -> None:
        self._inventory[new_item._id] = new_item


    def remove_from_inventory(self, index : int) -> None:
        keys : list = list(self._inventory.keys())
        if index in range(0, len(keys)):
            self._inventory.pop(keys[index])


    def _die(self) -> str:
        return f"{self._name} died!"
    

    def introduce(self) -> str:
        '''
        Mostly testing method for character introduction.
        '''
        return f"Hello, I'm {self._name} ({self._gender}), I'm {self._species} from {self._align}"
    

    def set_partner(self, partner) -> None:
        '''
        Setting partner. This function affects partner's object as well, if any is set.
        '''
        if partner == None:
            if self._partner == None:
                return
            else:
                self._partner._partner = None
                self._partner = None
        else:
            if self._partner != None:
                self._partner._partner = None
            self._partner = partner
    
    @abstractclassmethod
    def action(self) -> None:
        pass


class Sorcerer(CharacterBase):
    '''
    Abstract base class for all sorcerer characters, that contains functions and fields, appliable to all sorcerers.
    '''
    @abstractclassmethod
    def cast_magic(self, targets : Iterable) -> str:
        pass
