from typing import TypedDict, List


class LocationDict(TypedDict):
    name: str
    region: str
    game_id: str


location_table: List[LocationDict] = [
    {"name": "Track 1: Life Gauge Piece #3",
        "region": "T1",
        "game_id": "LifeCoreItem_BP3_2"},
    {"name": "Track 1: Life Gauge Piece #1",
        "region": "T1",
        "game_id": "LifeCoreItem_BP1"},
    {"name": "Track 1: Life Gauge Piece #2",
        "region": "T1",
        "game_id": "LifeCoreItem_BP2"},
    {"name": "Track 1: Reverb Core #1",
        "region": "T1",
        "game_id": "ReverbPieceItem_BP_2"},
    {"name": "Track 1: Health Tank #1",
        "region": "T1",
        "game_id": "LifeTankPieceItem_BP_C_2147271128"},
    {"name": "Track 1: Broken Circuit #3",
        "region": "T1",
        "game_id": ""},

    {"name": "Track 2: Reverb Core #1",
        "region": "T2",
        "game_id": "ReverbPieceItem_BP1"},
    {"name": "Track 2: Reverb Core #2",
        "region": "T2",
        "game_id": "ReverbPieceItem_BP2_5"},
]
