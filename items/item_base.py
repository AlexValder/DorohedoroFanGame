from abc import ABC, abstractclassmethod
from typing import Iterable
from characters.CharacterBase import CharacterBase, Sorcerer
from numpy.random import randint


class ItemBase(ABC):
    '''
    Abstract base class for all items.
    '''
    def __init__(self, name : str):
        self._name : str = name


class SmokeBottle(ItemBase):
    '''
    Class for smoke bottles.
    '''
    def __init__(self, name : str, sorcerer : Sorcerer):
        super().__init__(name)
        self._sorcerer : Sorcerer = sorcerer
    

    def use(self, targets : Iterable) -> None:
        '''
        Casting magic on someone via bottle.
        '''
        self._sorcerer.cast_magic(targets)


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