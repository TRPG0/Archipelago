from typing import Dict, TypedDict

class LocationDict(TypedDict, total=False):
    name: str
    scene_name: str
    region: int 

location_table: Dict[int, LocationDict] = {
    # Waynehouse
    200622: {'name': "Waynehouse: Toilet",
             'scene_name': 'StartHouse_Room1',
             'region': 2},
    200623: {'name': "Waynehouse: Basement Pot 1",
             'scene_name': 'StartHouse_Room1',
             'region': 2},
    200624: {'name': "Waynehouse: Basement Pot 2",
             'scene_name': 'StartHouse_Room1',
             'region': 2},
    200625: {'name': "Waynehouse: Basement Pot 3",
             'scene_name': 'StartHouse_Room1',
             'region': 2},
    200626: {'name': "Waynehouse: Sarcophagus",
             'scene_name': 'StartHouse_Room1',
             'region': 2},
    200627: {'name': "Waynehouse: TV",
             'scene_name': 'StartHouse_Room1',
             'region': 2},

    # Afterlife
    200628: {'name': "Afterlife: Mangled Wayne",
             'scene_name': 'Afterlife_Island',
             'region': 1},
    200629: {'name': "Afterlife: Jar near Mangled Wayne",
             'scene_name': 'Afterlife_Island',
             'region': 1},
    200630: {'name': "Afterlife: Jar under Pool",
             'scene_name': 'Afterlife_Island',
             'region': 1},
    200631: {'name': "Afterlife: TV",
             'scene_name': 'Afterlife_Island',
             'region': 1},

    # New Muldul
    200632: {'name': "New Muldul: Shop Ceiling Pot 1",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200633: {'name': "New Muldul: Shop Ceiling Pot 2",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200634: {'name': "New Muldul: Flag Banana",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200635: {'name': "New Muldul: Pot near Vault",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200636: {'name': "New Muldul: Underground Pot",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200637: {'name': "New Muldul: Underground Chest",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200638: {'name': "New Muldul: Juice Trade",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200639: {'name': "New Muldul: Basement Suitcase",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200640: {'name': "New Muldul: Upper House Chest 1",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200641: {'name': "New Muldul: Upper House Chest 2",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},
    200642: {'name': "New Muldul: TV",
             'scene_name': 'Town_Scene_WithAdditions',
             'region': 4},

    # New Muldul Vault
    200643: {'name': "New Muldul: Talk to Pongorma",
             'scene_name': 'Town_VaultOnly',
             'region': 4},
    #200644: {'name': "New Muldul: Pongorma Joins",
    #         'scene_name': 'Town_VaultOnly',
    #         'region': 4},
    200645: {'name': "New Muldul: Rescued Blerol",
             'scene_name': 'Town_VaultOnly',
             'region': 4},
    200646: {'name': "New Muldul: Rescued Blerol 2",
             'scene_name': 'Town_VaultOnly',
             'region': 4},
    200647: {'name': "New Muldul: Vault Left Chest",
             'scene_name': 'Town_VaultOnly',
             'region': 5},
    200648: {'name': "New Muldul: Vault Right Chest",
             'scene_name': 'Town_VaultOnly',
             'region': 5},
    200649: {'name': "New Muldul: Vault Bomb",
             'scene_name': 'Town_VaultOnly',
             'region': 5},

    # Viewax's Edifice
    200650: {'name': "Viewax's Edifice: Fountain Banana",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200651: {'name': "Viewax's Edifice: Dedusmuln's Suitcase",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200652: {'name': "Viewax's Edifice: Dedusmuln's Campfire",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200653: {'name': "Viewax's Edifice: Talk to Dedusmuln",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    #200654: {'name': "Viewax's Edifice: Dedusmuln Joins",
    #         'scene_name': 'BanditFort_Scene',
    #         'region': 6},
    200655: {'name': "Viewax's Edifice: Canopic Jar",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200656: {'name': "Viewax's Edifice: Cave Sarcophagus",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200657: {'name': "Viewax's Edifice: Shielded Key",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200658: {'name': "Viewax's Edifice: Tower Pot",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200659: {'name': "Viewax's Edifice: Tower Jar",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200660: {'name': "Viewax's Edifice: Tower Chest",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200661: {'name': "Viewax's Edifice: Sage Fridge",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200662: {'name': "Viewax's Edifice: Sage Item 1",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200663: {'name': "Viewax's Edifice: Sage Item 2",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200664: {'name': "Viewax's Edifice: Viewax Pot",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200665: {'name': "Viewax's Edifice: Defeat Viewax",
             'scene_name': 'BanditFort_Scene',
             'region': 6},
    200666: {'name': "Viewax's Edifice: TV",
             'scene_name': 'BanditFort_Scene',
             'region': 6},

    # Viewax Arcade Minigame
    200667: {'name': "Arcade 1: Key",
             'scene_name': 'LD44 Scene',
             'region': 6},
    200668: {'name': "Arcade 1: Coin Dash",
             'scene_name': 'LD44 Scene',
             'region': 6},
    200669: {'name': "Arcade 1: Burrito Alcove 1",
             'scene_name': 'LD44 Scene',
             'region': 6},
    200670: {'name': "Arcade 1: Burrito Alcove 2",
             'scene_name': 'LD44 Scene',
             'region': 6},
    200671: {'name': "Arcade 1: Behind Spikes Banana",
             'scene_name': 'LD44 Scene',
             'region': 6},
    200672: {'name': "Arcade 1: Pyramid Banana",
             'scene_name': 'LD44 Scene',
             'region': 6},
    200673: {'name': "Arcade 1: Moving Platforms Muscle Applique",
             'scene_name': 'LD44 Scene',
             'region': 6},
    200674: {'name': "Arcade 1: Bed Banana",
             'scene_name': 'LD44 Scene',
             'region': 6},

    # Airship
    200675: {'name': "Airship: Talk to Somsnosa",
             'scene_name': 'Airship_Scene',
             'region': 7},
    
    # Arcade Island
    200676: {'name': "Arcade Island: Shielded Key",
             'scene_name': 'SecondArcade_Scene',
             'region': 8},
    200677: {'name': "Arcade 2: Flying Machine Banana",
             'scene_name': 'LD44_ChibiScene2_TheCarpetScene',
             'region': 8},
    200678: {'name': "Arcade 2: Paper Cup Detour",
             'scene_name': 'LD44_ChibiScene2_TheCarpetScene',
             'region': 8},
    200679: {'name': "Arcade 2: Peak Muscle Applique",
             'scene_name': 'LD44_ChibiScene2_TheCarpetScene',
             'region': 8},
    200680: {'name': "Arcade 2: Double Banana 1",
             'scene_name': 'LD44_ChibiScene2_TheCarpetScene',
             'region': 8},
    200681: {'name': "Arcade 2: Double Banana 2",
             'scene_name': 'LD44_ChibiScene2_TheCarpetScene',
             'region': 8},
    200682: {'name': "Arcade 2: Cave Burrito",
             'scene_name': 'LD44_ChibiScene2_TheCarpetScene',
             'region': 8},

    # TV Island
    200683: {'name': "TV Island: TV",
             'scene_name': 'BigTV_Island_Scene',
             'region': 9},

    # Juice Ranch
    200684: {'name': "Juice Ranch: Juice 1",
             'scene_name': 'SomsnosaHouse_Scene',
             'region': 10},
    200685: {'name': "Juice Ranch: Juice 2",
             'scene_name': 'SomsnosaHouse_Scene',
             'region': 10},
    200686: {'name': "Juice Ranch: Juice 3",
             'scene_name': 'SomsnosaHouse_Scene',
             'region': 10},
    200687: {'name': "Juice Ranch: Ledge Rancher",
             'scene_name': 'SomsnosaHouse_Scene',
             'region': 10},
    200688: {'name': "Juice Ranch: Battle with Somsnosa",
             'scene_name': 'SomsnosaHouse_Scene',
             'region': 10},
    #200689: {'name': "Juice Ranch: Somsnosa Joins",
    #         'scene_name': 'SomsnosaHouse_Scene',
    #         'region': 10},
    200690: {'name': "Juice Ranch: Fridge",
             'scene_name': 'SomsnosaHouse_Scene',
             'region': 10},
    200691: {'name': "Juice Ranch: TV",
             'scene_name': 'SomsnosaHouse_Scene',
             'region': 10},

    # Worm Pod
    200692: {'name': "Worm Pod: Key",
             'scene_name': 'MazeScene1',
             'region': 12},

    # Foglast
    200693: {'name': "Foglast: West Sarcophagus",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200694: {'name': "Foglast: Underground Sarcophagus",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200695: {'name': "Foglast: Shielded Key",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200696: {'name': "Foglast: Buy Clicker",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200697: {'name': "Foglast: TV",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200698: {'name': "Foglast: Shielded Chest",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200699: {'name': "Foglast: Cave Fridge",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200700: {'name': "Foglast: Roof Sarcophagus",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200701: {'name': "Foglast: Under Lair Sarcophagus 1",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200702: {'name': "Foglast: Under Lair Sarcophagus 2",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200703: {'name': "Foglast: Under Lair Sarcophagus 3",
             'scene_name': 'Foglast_Exterior_Dry',
             'region': 13},
    200704: {'name': "Foglast: Sage Sarcophagus",
             'scene_name': 'Foglast_SageRoom_Scene',
             'region': 13},
    200705: {'name': "Foglast: Sage Item 1",
             'scene_name': 'Foglast_SageRoom_Scene',
             'region': 13},
    200706: {'name': "Foglast: Sage Item 2",
             'scene_name': 'Foglast_SageRoom_Scene',
             'region': 13},

    # Drill Castle
    200707: {'name': "Drill Castle: Ledge Banana",
             'scene_name': 'DrillCastle',
             'region': 14},
    200708: {'name': "Drill Castle: Island Banana",
             'scene_name': 'DrillCastle',
             'region': 14},
    200709: {'name': "Drill Castle: Island Pot",
             'scene_name': 'DrillCastle',
             'region': 14},
    200710: {'name': "Drill Castle: Cave Sarcophagus",
             'scene_name': 'DrillCastle',
             'region': 14},
    200711: {'name': "Drill Castle: Roof Banana",
             'scene_name': 'DrillCastle',
             'region': 14},
    200712: {'name': "Drill Castle: TV",
             'scene_name': 'DrillCastle',
             'region': 14},

    # Sage Labyrinth
    200713: {'name': "Sage Labyrinth: 1F Chest Near Fountain",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200714: {'name': "Sage Labyrinth: 1F Hidden Sarcophagus",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200715: {'name': "Sage Labyrinth: 1F Four Statues Chest 1",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200716: {'name': "Sage Labyrinth: 1F Four Statues Chest 2",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200717: {'name': "Sage Labyrinth: B1 Double Chest 1",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200718: {'name': "Sage Labyrinth: B1 Double Chest 2",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200719: {'name': "Sage Labyrinth: B1 Single Chest",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200720: {'name': "Sage Labyrinth: B1 Enemy Chest",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200721: {'name': "Sage Labyrinth: B1 Hidden Sarcophagus",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200722: {'name': "Sage Labyrinth: B1 Hole Chest",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200723: {'name': "Sage Labyrinth: B2 Hidden Sarcophagus 1",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200724: {'name': "Sage Labyrinth: B2 Hidden Sarcophagus 2",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200725: {'name': "Sage Labyrinth: Motor Hunter Sarcophagus",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200726: {'name': "Sage Labyrinth: Sage Item 1",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200727: {'name': "Sage Labyrinth: Sage Item 2",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200728: {'name': "Sage Labyrinth: Sage Left Arm",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200729: {'name': "Sage Labyrinth: Sage Right Arm",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200730: {'name': "Sage Labyrinth: Sage Left Leg",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},
    200731: {'name': "Sage Labyrinth: Sage Right Leg",
             'scene_name': 'Dungeon_Labyrinth_Scene_Final',
             'region': 15},

    # Sage Airship
    200732: {'name': "Sage Airship: Bottom Level Pot",
             'scene_name': 'BigAirship_Scene',
             'region': 16},
    200733: {'name': "Sage Airship: Flesh Pot",
             'scene_name': 'BigAirship_Scene',
             'region': 16},
    200734: {'name': "Sage Airship: Top Jar",
             'scene_name': 'BigAirship_Scene',
             'region': 16},
    200735: {'name': "Sage Airship: TV",
             'scene_name': 'BigAirship_Scene',
             'region': 16},

    # Hylemxylem
    200736: {'name': "Hylemxylem: Jar",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200737: {'name': "Hylemxylem: Lower Reservoir Key",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200738: {'name': "Hylemxylem: Fountain Banana",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200739: {'name': "Hylemxylem: East Island Banana",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200740: {'name': "Hylemxylem: East Island Chest",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200741: {'name': "Hylemxylem: Upper Chamber Banana",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200742: {'name': "Hylemxylem: Across Upper Reservoir Chest",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200743: {'name': "Hylemxylem: Drained Lower Reservoir Chest",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200744: {'name': "Hylemxylem: Drained Lower Reservoir Burrito 1",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200745: {'name': "Hylemxylem: Drained Lower Reservoir Burrito 2",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200746: {'name': "Hylemxylem: Lower Reservoir Hole Pot 1",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200747: {'name': "Hylemxylem: Lower Reservoir Hole Pot 2",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200748: {'name': "Hylemxylem: Lower Reservoir Hole Pot 3",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200749: {'name': "Hylemxylem: Lower Reservoir Hole Sarcophagus",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200750: {'name': "Hylemxylem: Drained Upper Reservoir Burrito 1",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200751: {'name': "Hylemxylem: Drained Upper Reservoir Burrito 2",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200752: {'name': "Hylemxylem: Drained Upper Reservoir Burrito 3",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17},
    200753: {'name': "Hylemxylem: Upper Reservoir Hole Key",
             'scene_name': 'FlyingPalaceDungeon_Scene',
             'region': 17}
}