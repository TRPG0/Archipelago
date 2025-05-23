from typing import Dict, List, Tuple, Any, Callable, TYPE_CHECKING
from BaseClasses import CollectionState
from worlds.generic.Rules import CollectionRule

if TYPE_CHECKING:
    from . import Blasphemous2World
else:
    Blasphemous2World = object


class Blas2Rules:
    player: int
    world: Blasphemous2World
    string_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: "Blasphemous2World") -> None:
        self.player = world.player
        self.world = world
        self.multiworld = world.multiworld
        self.indirect_conditions: List[Tuple[str, str]] = []

        # BrandenEK/BlasII.Randomizer/Shuffle/BlasphemousInventory.cs
        self.string_rules = {
            # Weapons
            "censer": self.censer,
            "rosary": self.rosary,
            "rapier": self.rapier,
            "meaculpa": self.meaculpa,

            # Abilities
            "wallclimb": self.wallclimb,
            "doublejump": self.doublejump,
            "airdash": self.airdash,
            "ringclimb": self.ringclimb,
            "glasswalk": self.glasswalk,

            # Bosses
            "bosskeys5": lambda state: self.bosskeys(state, 5),

            # Cherub quest
            # cherubs - not used?
            "rattle": self.rattle,

            # Elder quest
            "elderscroll": self.elderscroll,
            "eldercloth": self.eldercloth,

            # Gold quest
            "goldlumps10": lambda state: self.goldlumps(state, 10),
            "goldlumps20": lambda state: self.goldlumps(state, 20),

            # Hand quest
            "kisses5": lambda state: self.kisses(state, 5),
            "brokenkey": self.brokenkey,

            # Letter quest
            "letter1": self.letter1,
            "letter2": self.letter2,
            "letter3": self.letter3,
            "letter4": self.letter4,
            "letter5": self.letter5,

            # Lullaby quest
            "lullabies5": lambda state: self.lullabies(state, 5),

            # Mud quest
            "mudkey": self.mudkey,
            "ceramickey": self.ceramickey,

            # Regula quest
            "regulacloth": self.regulacloth,

            # Sculptor quest
            "tools5": lambda state: self.tools(state, 5),

            # Tribute quest
            "tributes1": lambda state: self.tributes(state, 1),
            "tributes2": lambda state: self.tributes(state, 2),
            "tributes3": lambda state: self.tributes(state, 3),

            # Wax quest
            "waxseeds6": lambda state: self.waxseeds(state, 6),

            # Yerma quest
            "holyoil": self.holyoil,

            # Rooms
            "daughterrooms1": lambda state: self.daughter_rooms(state, 1),
            "daughterrooms2": lambda state: self.daughter_rooms(state, 2),
            "daughterrooms3": lambda state: self.daughter_rooms(state, 3),
            "daughterrooms4": lambda state: self.daughter_rooms(state, 4),
            "daughterrooms5": lambda state: self.daughter_rooms(state, 5),

            "shoprooms1": lambda state: self.shop_rooms(state, 1),
            "shoprooms2": lambda state: self.shop_rooms(state, 2),
            "shoprooms3": lambda state: self.shop_rooms(state, 3),
            "shoprooms4": lambda state: self.shop_rooms(state, 4),
            "shoprooms5": lambda state: self.shop_rooms(state, 5),
            "shoprooms6": lambda state: self.shop_rooms(state, 6),
            "shoprooms7": lambda state: self.shop_rooms(state, 7)
        }

    def load_rule(self, obj: Dict[str, Any]) -> Callable[[CollectionState], bool]:
        clauses = []
        for clause in obj["logic"]:
            reqs = []
            for req in clause["item_requirements"]:
                reqs.append(self.string_rules[req])
            if len(reqs) == 1:
                clauses.append(reqs[0])
            else:
                clauses.append(lambda state, reqs=reqs: all(req(state) for req in reqs))
        if not clauses:
            return lambda state: True
        elif len(clauses) == 1:
            return clauses[0]
        else:
            return lambda state: any(clause(state) for clause in clauses)

    # Weapons
    def censer(self, state: CollectionState) -> bool:
        return state.has("Veredicto", self.player)
    
    def rosary(self, state: CollectionState) -> bool:
        return state.has("Ruego Al Alba", self.player)
    
    def rapier(self, state: CollectionState) -> bool:
        return state.has("Sarmiento & Centella", self.player)
    
    def meaculpa(self, state: CollectionState) -> bool:
        return state.has("Mea Culpa", self.player)
    
    # Abilities
    def wallclimb(self, state: CollectionState) -> bool:
        return state.has("Ivy of Ascension", self.player)
    
    def doublejump(self, state: CollectionState) -> bool:
        return state.has("Passage of Ash", self.player)
    
    def airdash(self, state: CollectionState) -> bool:
        return state.has("Mercy of the Wind", self.player)
    
    def ringclimb(self, state: CollectionState) -> bool:
        return state.has("Scions' Protection", self.player)
    
    def glasswalk(self, state: CollectionState) -> bool:
        return state.has("Broken Step", self.player)
    
    # Bosses
    def bosskeys(self, state: CollectionState, count: int) -> bool:
        return state.count_group_unique("bosskeys", self.player) >= count
    
    # Cherub quest
    def cherubs(self, state: CollectionState, count) -> bool:
        return state.has("Cherub", self.player, count)
    
    def rattle(self, state: CollectionState) -> bool:
        return state.has("Giant Rattle", self.player)
    
    # Elder quest
    def elderscroll(self, state: CollectionState) -> bool:
        return state.has("Scroll of the Elder", self.player)
    
    def eldercloth(self, state: CollectionState) -> bool:
        return state.has("Cloth of the Old Woman", self.player)
    
    # Gold quest
    def goldlumps(self, state: CollectionState, count: int) -> bool:
        return state.has("Lump of Gold", self.player, count)
    
    # Hand quest
    def kisses(self, state: CollectionState, count) -> bool:
        return state.has("Fervent Kiss", self.player, count)
    
    def brokenkey(self, state: CollectionState) -> bool:
        return state.has("Broken Key", self.player)
    
    # Letter quest
    def letter1(self, state: CollectionState) -> bool:
        return state.has("Cursed Letter, Page One", self.player)
    
    def letter2(self, state: CollectionState) -> bool:
        return state.has("Cursed Letter, Page Two", self.player)
    
    def letter3(self, state: CollectionState) -> bool:
        return state.has("Cursed Letter, Page Three", self.player)
    
    def letter4(self, state: CollectionState) -> bool:
        return state.has("Cursed Letter, Page Four", self.player)
    
    def letter5(self, state: CollectionState) -> bool:
        return state.has("Cursed Letter, Last Page", self.player)
    
    # Lullaby quest
    def lullabies(self, state: CollectionState, count: int) -> bool:
        return state.has("Piece of the Lullaby", self.player, count)
    
    # Mud quest
    def mudkey(self, state: CollectionState) -> bool:
        return state.has("Mud Key", self.player)
    
    def ceramickey(self, state: CollectionState) -> bool:
        return state.has("Ceramic Key", self.player)
    
    # Regula quest
    def regulacloth(self, state: CollectionState) -> bool:
        return state.has("Regula's Cloth", self.player)
    
    # Sculptor quest
    def tools(self, state: CollectionState, count: int) -> bool:
        return state.count_group_unique("tools", self.player) >= count
    
    # Tribute quest
    def tributes(self, state: CollectionState, count: int) -> bool:
        return state.has("Forgotten Tribute", self.player, count)
    
    # Wax quest
    def waxseeds(self, state: CollectionState, count: int) -> bool:
        return state.has("Wax Seed", self.player, count)
    
    # Yerma quest
    def holyoil(self, state: CollectionState) -> bool:
        return state.has("Holy Oil of Everlasting Anointment", self.player)
    
    # Rooms
    def daughter_rooms(self, state: CollectionState, count: int) -> bool:
        rooms: int = 0

        if self.wallclimb(state) and self.doublejump(state):
            rooms += 1
        if self.wallclimb(state) and self.doublejump(state) and self.censer(state) and self.rosary(state) and self.rapier(state):
            rooms += 1
        if self.wallclimb(state) and self.doublejump(state) and self.airdash(state) and self.rosary(state):
            rooms += 1
        if self.doublejump(state) and self.airdash(state) and self.ringclimb(state):
            rooms += 1
        if self.wallclimb(state) and self.doublejump(state) and self.airdash(state) and self.ringclimb(state) and self.censer(state) and self.rosary(state) and self.rapier(state):
            rooms += 1
        
        return rooms >= count
    
    def shop_rooms(self, state: CollectionState, count: int) -> bool:
        if not self.wallclimb(state):
            return count >= 0
        if not self.rosary(state):
            return count >= 1
        if not self.doublejump(state) or not self.censer(state):
            return count >= 2
        if not self.airdash(state):
            return count >= 3
        if not self.ringclimb(state) or not self.rapier(state):
            return count >= 4
        if not self.bosskeys(state, 5):
            return count >= 6
        return count >= 7