from typing import Dict, List, Tuple

_Locations = List[Tuple[str,str]]
_World = Dict[str, _Locations]

HOLE : _World = {
    "" : [("","")],
}

SORCERER : _World = {
    "" : [("","")],
}

HELL : _World = {
    "" : [("","")],
}

SLUDGE : _World = {
    "" : [("","")],
}

LOCATIONS : Dict[str, _World] = {
    "HOLE" : HOLE,
    "SORCERER" : SORCERER,
    "HELL" : HELL,
    "SLUDGE" : SLUDGE,
}