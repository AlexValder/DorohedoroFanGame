from enum import Enum
from typing import Optional
from colorama import Fore
from abc import ABC, abstractclassmethod


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


class CharacterBase(ABC):
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

    
    def introduce(self) -> None:
        print(f"Hello, I'm {self._name} ({_gender_to_str(self._gender)}), I'm {_species_to_str(self._species)} from {_align_to_str(self._align)}")
    
    def set_partner(self, partner) -> None:
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
    def cast_magic(self, *targets) -> None:
        pass
