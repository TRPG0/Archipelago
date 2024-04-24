from typing import Any, Dict
from BaseClasses import MultiWorld, Region, Location, Item, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .Items import base_id, item_table
from .Locations import location_table
from .Options import HiFiRushOptions


class HiFiRushWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Hi-Fi RUSH randomizer and connecting to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["TRPG"]
    )]


class HiFiRushWorld(World):
    """Feel the beat as wannabe rockstar Chai and his ragtag team fight against evil megacorp with raucous rhythm combat!"""

    game = "Hi-Fi RUSH"
    web = HiFiRushWeb()

    item_name_to_id = {item["name"]: (base_id + index) for index, item in enumerate(item_table)}
    location_name_to_id = {loc["name"]: (base_id + index) for index, loc in enumerate(location_table)}

    # item_name_groups = 
    options_dataclass = HiFiRushOptions
    options: HiFiRushOptions


    def set_rules(self):
        pass


    def create_item(self, name: str) -> "HiFiRushItem":
        pass


    def create_event(self, event: str) -> "HiFiRushItem":
        return HiFiRushItem(event, ItemClassification.progression_skip_balancing, None, self.player)


    def get_filler_item_name(self) -> str:
        pass


    def create_items(self):
        pass


    def create_regions(self):
        pass


    def fill_slot_data(self) -> Dict[str, Any]:
        pass


class HiFiRushItem(Item):
    game: str = "Hi-Fi RUSH"


class HiFiRushLocation(Location):
    game: str = "Hi-Fi RUSH"