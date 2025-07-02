from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions
from typing import Dict, Any


class LogicType(Choice):
    """
    Choose if difficult tricks will be required in logic.
    """
    display_name = "Logic Type"
    option_normal = 0
    default = 0


class RequiredKeys(Range):
    """
    Choose how many keys will be required to open the door to Crimson Rains.
    """
    display_name = "Required Keys"
    range_start = 0
    range_end = 5
    default = 4


class Ending(Choice):
    """
    Choose which ending is required to complete the game.
    """
    display_name = "Ending"
    option_any_ending = 0
    option_ending_a = 1
    option_ending_c = 2
    default = 0


class StartingWeapon(Choice):
    """
    Choose which weapon to start with.
    """
    display_name = "Starting Weapon"
    option_ruego_al_alba = 1
    option_veredicto = 0
    option_sarmiento_and_centella = 2
    option_mea_culpa = 3
    default = "random"

    @classmethod
    def get_option_name(cls, value: int) -> str:
        if value == 2:
            return "Sarmiento & Centella"
        return super().get_option_name(value)


class ExcludeLongQuests(Toggle):
    """
    Automatically exclude locations from quests that take a long time to complete.
    """
    display_name = "Exclude Long Quests"


class ExcludeShops(DefaultOnToggle):
    """
    Automatically exclude locations in shops.
    """
    display_name = "Exclude Shops"


@dataclass
class Blasphemous2Options(PerGameCommonOptions):
    logic_type: LogicType
    required_keys: RequiredKeys
    ending: Ending
    starting_weapon: StartingWeapon
    exclude_long_quests: ExcludeLongQuests
    exclude_shops: ExcludeShops


blas2_option_presets: Dict[str, Dict[str, Any]] = {
    "Quick":    {"logic_type": 1,
                 "required_keys": 1,
                 "ending": 0,
                 "starting_weapon": 0,
                 "exclude_long_quests": True,
                 "exclude_shops": True}
}