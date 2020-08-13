from typing import Dict, List, Tuple, Set
from enum import Enum
from ..characters import character_base as chbase


class World(Enum):
    '''
    Enumuration of all possible worlds.
    '''
    HOLE = 0
    SORCERER = 1
    HELL = 2
    SLUDGE = 3

    def __str__(self) -> str:
        if self.value == 0:
            return "HOLE"
        if self.value == 1:
            return "SORCERER"
        if self.value == 2:
            return "HELL"
        if self.value == 3:
            return "SLUDGE"
        return "???"


class Location:
    '''
    Class for all locations in the game.
    '''
    def __init__(self, world : World, name : str, *connected_with : Tuple[World, str]):
        self.__world : World = world
        self.__name : str = name
        self.__characters : List[chbase.CharacterBase] = []
        self.__connected_with : Set[Tuple[World, str]] = set(connected_with)


LOCATIONS : Dict[Tuple[World, str], Location] = {

    (World.HOLE, "Main Square") : Location(
                                    World.HOLE,
                                    "Main Square",
                                    (World.HOLE, "Road West"),
                                    (World.HOLE, "Road East"),
                                    (World.HOLE, "Road North"),
                                    (World.HOLE, "Road South"),
                                    ),

    (World.HOLE, "Road West") : Location(
                                    World.HOLE,
                                    "Road West",
                                    (World.HOLE, "Main Square"),
                                    (World.HOLE, "Hungry Bug"),
                                    ),

    (World.HOLE, "Road East") : Location(
                                    World.HOLE,
                                    "Road East",
                                    (World.HOLE, "Main Square"),
                                    ),

    (World.HOLE, "Road North") : Location(
                                    World.HOLE,
                                    "Road North",
                                    (World.HOLE, "Main Square"),
                                    ),

    (World.HOLE, "Road South") : Location(
                                    World.HOLE,
                                    "Road South",
                                    (World.HOLE, "Main Square"),
                                    ),
    
    (World.HOLE, "Hungry Bug") : Location(
                                    World.HOLE,
                                    "Hungry Bug",
                                    (World.HOLE, "Road West"),
                                    ),
}