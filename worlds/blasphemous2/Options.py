from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions, Visibility
from typing import Dict, Any


class LogicType(Choice):
    """
    Choose if difficult tricks will be required in logic.
    """
    display_name = "Logic Type"
    option_normal = 0
    default = 0
    visibility = Visibility.none


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
    

class ShopMultiplier(Choice):
    """
    Choose how expensive shop items will be.
    """
    display_name = "Shop Costs"
    option_free = 0
    option_cheap = 1
    option_standard = 2
    option_expensive = 3
    option_vanilla = 4
    default = 2


class MartyrdomXP(Choice):
    """
    Choose how the 40 additional Marks of Martyrdom unlocked from gaining XP will be handled.

    Vanilla: Marks use the original XP system.
    Double XP: Marks use the original XP system, but at double the rate.
    From Items: No marks are earned from XP. The 40 marks are distributed into the item pool.
    From Bosses: No marks are earned from XP. The 40 marks are given by defeating the eight main bosses.
    """
    display_name = "Martyrdom XP"
    option_vanilla = 0
    option_double_xp = 1
    option_from_items = 2
    option_from_bosses = 3
    default = 2

    @classmethod
    def get_option_name(cls, value: int) -> str:
        if value == 1:
            return "Double XP"
        return super().get_option_name(value)


class AddPenitenceRewards(DefaultOnToggle):
    """
    Choose if the rewards for completing True Torment Penitences should be in the item pool.
    """
    display_name = "Add Penitence Rewards"


class ShuffleCherubs(DefaultOnToggle):
    """
    Choose if cherubs should be shuffled or in their default locations.
    """
    display_name = "Shuffle Cherubs"


#class ExcludeLongQuests(Toggle):
#    """
#    Automatically exclude locations from quests that take a long time to complete.
#    """
#    display_name = "Exclude Long Quests"


#class ExcludeShops(DefaultOnToggle):
#    """
#    Automatically exclude locations in shops.
#    """
#    display_name = "Exclude Shops"


@dataclass
class Blasphemous2Options(PerGameCommonOptions):
    logic_type: LogicType
    required_keys: RequiredKeys
    ending: Ending
    starting_weapon: StartingWeapon
    shop_multiplier: ShopMultiplier
    martyrdom_xp: MartyrdomXP
    add_penitence_rewards: AddPenitenceRewards
    shuffle_cherubs: ShuffleCherubs
    #exclude_long_quests: ExcludeLongQuests
    #exclude_shops: ExcludeShops


blas2_option_presets: Dict[str, Dict[str, Any]] = {
    "Quick":    {"logic_type": 1,
                 "required_keys": 1,
                 "ending": 0,
                 "starting_weapon": 0,
                 "shop_multiplier": 1,
                 "martyrdom_xp": 2,
                 "add_penitence_rewards": True,
                 "shuffle_cherubs": False}
}