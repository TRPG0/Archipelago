from typing import Dict, Any, List
from BaseClasses import Tutorial, Item, Location, Region, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .Items import Blas2Item, item_list, filler_list, group_table
from .Locations import location_names
from .LocationFlags import location_flags
from .Rules import Blas2Rules
from worlds.generic.Rules import set_rule
from .Options import Blasphemous2Options, blas2_option_presets
from .region_structure import regions as extracted_regions
from .region_structure import locations as extracted_locations


class Blasphemous2Web(WebWorld):
    theme = "stone"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Blasphemous 2 Randomizer and connecting to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["TRPG"]
    )]
    options_presets = blas2_option_presets


class Blasphemous2World(World):
    """
    The Penitent One awakens as Blasphemous 2 joins him once again in an endless struggle against The Miracle. Dive into a perilous new world filled with mysteries and secrets to discover, and tear your way through monstrous foes that stand between you and your quest to end the cycle once and for all.
    """

    game = "Blasphemous 2"
    web = Blasphemous2Web()

    item_name_to_id = {item.name: index+1 for index, item in enumerate(item_list)}
    location_name_to_id = {location: index+1 for index, location in enumerate(location_names.keys())}

    item_name_groups = group_table
    options_dataclass = Blasphemous2Options
    options: Blasphemous2Options


    def create_item(self, name: str) -> "Blasphemous2Item":
        classification = ItemClassification.filler
        for i in item_list:
            if i.name == name:
                classification = i.classification

        return Blasphemous2Item(name, classification, self.item_name_to_id[name], self.player)


    def create_event(self, event: str):
        return Blasphemous2Item(event, ItemClassification.progression_skip_balancing, None, self.player)
    

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_list)
    

    def generate_early(self):
        if self.options.exclude_long_quests:
            for location in location_flags["L"]:
                self.options.exclude_locations.value.add(location)

        if self.options.exclude_shops:
            for location in location_flags["S"]:
                self.options.exclude_locations.value.add(location)


    def create_items(self):
        pool = []

        for item in item_list:
            count: int = item.count

            if (item.name == "Ruego Al Alba" and self.options.starting_weapon == "ruego_al_alba")\
            or (item.name == "Veredicto" and self.options.starting_weapon == "veredicto")\
            or (item.name == "Sarmiento & Centella" and self.options.starting_weapon == "sarmiento_and_centella")\
            or (item.name == "Mea Culpa" and self.options.starting_weapon == "mea_culpa"):
                count -= 1

            if count <= 0:
                continue
            else:
                for _ in range(count):
                    pool.append(self.create_item(item.name))

        self.multiworld.itempool += pool


    def create_regions(self):
        multiworld = self.multiworld
        player = self.player

        for r in region_structure.regions:
            multiworld.regions.append(Region(r["name"], player, multiworld))

        blas2_logic = Blas2Rules(self)

        for r in extracted_regions:
            region = self.get_region(r["name"])

            for l in r["locations"]:
                if l in location_flags["C"]:
                    continue

                region.add_locations({l: self.location_name_to_id[l]}, Blasphemous2Location)

        for l in extracted_locations:
            if l["name"] in location_flags["C"]:
                continue

            location = self.get_location(l["name"])
            set_rule(location, blas2_logic.load_rule(l))

            if l["name"] == "Z1808.r6":
                multiworld.completion_condition[self.player] = blas2_logic.load_rule(l)


    def fill_slot_data(self) -> Dict[str, Any]:
        randomizerSettings = {
            "Seed": self.multiworld.seed,

            "LogicType": self.options.logic_type.value,
            "RequiredKeys": self.options.required_keys.value,
            "StartingWeapon": self.options.starting_weapon.value,

            "ShuffleLongQuests": bool(not self.options.exclude_long_quests.value),
            "ShuffleShops": bool(not self.options.exclude_shops.value),
        }

        slot_data = {
            "settings": randomizerSettings,
            "locations": [{"internal": location, "ap": index} for index, location in enumerate(location_names)]
        }

        return slot_data


class Blasphemous2Item(Item):
    game: str = "Blasphemous 2"


class Blasphemous2Location(Location):
    game: str = "Blasphemous 2"
