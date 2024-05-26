from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions


class RandomizeVlogs(Toggle):
    """
    Adds rewards for finding the VLogs around Vandelay campus.
    """
    display_name = "VLog Rewards"


class RandomizeGraffiti(Toggle):
    """
    Adds rewards for finding the graffiti around Vandelay campus.
    """
    display_name = "Graffiti Rewards"


@dataclass
class HiFiRushOptions(PerGameCommonOptions):
    vlog_rewards: RandomizeVlogs
    graffiti_rewards: RandomizeGraffiti