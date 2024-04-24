from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions


class RandomizeVlogs(Toggle):
    """Randomizes the vlogs around Vandelay campus."""
    display_name = "Randomize Vlogs"


@dataclass
class HiFiRushOptions(PerGameCommonOptions):
    randomize_vlogs: RandomizeVlogs