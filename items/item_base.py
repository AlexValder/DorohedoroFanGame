from abc import ABC, abstractclassmethod
from typing import Iterable, Optional
from characters.CharacterBase import CharacterBase, Sorcerer, Species
from numpy.random import randint


__all__ = ["SmokeBottle", "MeleeWeapon", "DistantWeapon", "Remains"]


class ItemBase(ABC):
    '''
    Abstract base class for all items.
    '''
    __item_count : int = 0

    def __init__(self, name : str):
        self._name : str = name
        self._id = ItemBase.__item_count
        ItemBase.__item_count += 1
    
    @abstractclassmethod
    def __str__(self) -> str:
        pass


class SmokeBottle(ItemBase):
    '''
    Class for smoke bottles.
    '''
    def __init__(self, sorcerer):
        super().__init__(f"Smoke Bottle")
        self._sorcerer : Sorcerer = sorcerer
    

    def use(self, targets : Iterable) -> None:
        '''
        Casting magic on someone via bottle.
        '''
        self._sorcerer.cast_magic(targets)
    

    def __str__(self) -> str:
        return f"Bottle of {self._sorcerer._name}'s smoke."


class MeleeWeapon(ItemBase):
    '''
    Class for all knives, swords, katanas etc.
    '''
    def __init__(self, name : str, max_attack : int):
        super().__init__(name)
        self._max_attack : int = max_attack
    

    def attack(self, targets : Iterable[CharacterBase]) -> None:
        '''
        Attacking people with melee weapon.
        '''
        for target in targets:
            target.damage(randint(0, self._max_attack))
    

    def __str__(self) -> str:
        return f"{self._name} with max attack of {self._max_attack}."


class DistantWeapon(ItemBase):
    '''
    Class for all shoting or throwable items.
    '''
    def __init__(self, name : str, magazine : int, number_of_magazines : int):
        super().__init__(name)
        self._magazine : int = magazine
        self._num_of_magazines : int = number_of_magazines
    

    def shoot(self, target : CharacterBase) -> None:
        '''
        Shooting target.
        '''
        target.damage(randint(0, 100))
    

    def __str__(self) -> str:
        return f"{self._name} with {self._num_of_magazines}x{self._magazine} rounds."


class Remains(ItemBase):
    '''
    Class for all kinds of remains (bodies, heads, devil tumors).
    '''
    def __init__(self, name : str, species : Species, devil_tumor_fine : bool):
        super().__init__(name)
        self._species : Species = species
        self._devil_tumor : bool = devil_tumor_fine
        
        if self._species != Species.SORCERER:
            self._devil_tumor = False
    
    def resurrect(self) -> Optional[Sorcerer]:
        if self._species == Species.SORCERER:
            return Sorcerer()
        else:
            print(f"Cannot ressurect a {self._species}")
            return None
    

    def __str__(self) -> str:
        return f"{self._name}'s remains. Resurrectable: {self._devil_tumor}."