from typing import TypedDict, List
from .Regions import Tracks


class LocationDict(TypedDict):
    name: str
    track: Tracks


location_table: List[LocationDict] = [
    
]
