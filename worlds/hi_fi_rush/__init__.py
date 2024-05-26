from typing import Any, Dict
from BaseClasses import MultiWorld, Region, Location, Item, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .Items import base_id, item_table
from .Locations import location_table
from .Regions import region_table
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
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id

        return HiFiRushItem(name, item_table[id]["classification"], item_id, self.player)


    def create_event(self, event: str) -> "HiFiRushItem":
        return HiFiRushItem(event, ItemClassification.progression_skip_balancing, None, self.player)


    def get_filler_item_name(self) -> str:
        names = [
            "Gears x4,000",
            "Gears x5,000",
            "Gears x6,000",
            "Gears x7,500",
            "Gears x8,500",
            "Gears x10,000",
            "Gears x12,500",
            "Gears x15,000",
            "Gears x17,500",
            "Gears x20,000",
            "Gears x25,000",
            "Gears x30,000",
            "Gears x35,000",
            "Gears x40,000",
            "Gears x45,000",
            "Gears x50,000",
            "Gears x60,000",
            "Gears x65,000",
            "Gears x80,000"
        ]

        return self.random.choice(names)


    def create_items(self):
        pool = []

        for item in item_table:
            for _ in range(item["count"]):
                pool.append(self.create_item(item["name"]))

        for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)):
            pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += pool


    def create_regions(self):
        player = self.player
        multiworld = self.multiworld

        menu = Region("Menu", player, multiworld)

        for _, name in region_table.items():
            multiworld.regions += [Region(name, player, multiworld)]
            menu.add_exits({name})

        multiworld.regions += [menu]

        for loc in location_table:
            if "VLog" in loc["name"] and not self.options.vlog_rewards:
                continue
            if "Graffiti" in loc["name"] and not self.options.graffiti_rewards:
                continue
            id = base_id + location_table.index(loc)
            region: Region = self.get_region(region_table[loc["region"]])
            location: HiFiRushLocation = HiFiRushLocation(player, loc["name"], id, region)
            region.locations.append(location)



    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "locations": {loc["flag"]: (base_id + index) for index, loc in enumerate(location_table)}
        }

        return slot_data


class HiFiRushItem(Item):
    game: str = "Hi-Fi RUSH"


class HiFiRushLocation(Location):
    game: str = "Hi-Fi RUSH"