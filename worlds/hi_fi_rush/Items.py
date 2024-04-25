from typing import TypedDict, List
from BaseClasses import ItemClassification


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification


base_id = 2412500


item_table: List[ItemDict] = [
    {"name": "Life Gauge Piece",
        "count": 3,
        "classification": ItemClassification.useful},
    {"name": "Electric Reverb Core Piece",
        "count": 3,
        "classification": ItemClassification.useful},
    {"name": "Broken Piece of a Health Tank",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Broken Armstrong Circuit",
        "count": 1,
        "classification": ItemClassification.useful},
]