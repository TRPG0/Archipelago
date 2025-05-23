from typing import List, Dict, Set
from dataclasses import dataclass
from BaseClasses import ItemClassification as IC


@dataclass
class Blas2Item:
    name: str
    classification: IC
    count: int = 1


item_list: List[Blas2Item] = [
    # Rosary Beads
    Blas2Item("Vitrified Lightning Bolt", IC.filler), # RB01
    Blas2Item("Earring of Regret", IC.filler), # RB02
    Blas2Item("Sphere Kissed by the Storm", IC.filler), # RB03
    Blas2Item("Lips of the Golden Mask", IC.filler), # RB04
    Blas2Item("Scorched Lily", IC.filler), # RB05
    Blas2Item("Imprint of Scalopendra", IC.filler), # RB06
    Blas2Item("Perforated Liar's Tongue", IC.filler), # RB07
    Blas2Item("Ill-fated Cord", IC.filler), # RB08
    Blas2Item("Compass of the Stranded", IC.filler), # RB09
    Blas2Item("Broken Bell", IC.filler), # RB10
    Blas2Item("Bead of Whimsical Essence", IC.filler), # RB11
    Blas2Item("Scratched Face from the Canvas", IC.filler), # RB12
    Blas2Item("Votive Offering of the Miserable", IC.filler), # RB13
    Blas2Item("Votive Offering of a Hopeful Mother", IC.filler), # RB14
    Blas2Item("Votive Offering Claimed by Rust", IC.filler), # RB15
    Blas2Item("Scratched Lead Sphere", IC.filler), # RB16
    Blas2Item("Salt-covered Spear Point", IC.filler), # RB17
    Blas2Item("Pewter Tears", IC.filler), # RB18
    Blas2Item("Price of Blood", IC.filler), # RB19
    Blas2Item("Obolus of Proximo", IC.filler), # RB20
    Blas2Item("Deformed Rat Skull", IC.filler), # RB21
    Blas2Item("Embossed Rat Skull", IC.filler), # RB22
    Blas2Item("Imperfect Sphere of Guilt", IC.filler), # RB23
    Blas2Item("Concentrated Sphere of Guilt", IC.filler), # RB24
    Blas2Item("Senior Embroiderer's Thimble", IC.filler), # RB25
    Blas2Item("Miniature Pincushion", IC.filler), # RB26
    Blas2Item("Chisel-Engraved Wounds", IC.filler), # RB27

    # Rosary Beads (DLC)
    Blas2Item("Raven Amulet", IC.filler), # RB101
    Blas2Item("Blood-stained Chain Link", IC.filler), # RB102
    Blas2Item("Traitor's Gaze", IC.filler), # RB103
    Blas2Item("Pearl of the Punished", IC.filler), # RB104
    Blas2Item("Bandage of the Heretic", IC.filler), # RB105
    Blas2Item("Antique Locket", IC.filler), # RB106

    # Prayers
    Blas2Item("Galera of the Living Briar", IC.useful), # PR01
    Blas2Item("Debla of the Lights", IC.useful), # PR02
    Blas2Item("Chime of the Twisted One", IC.useful), # PR03
    Blas2Item("Bleeding Miracle", IC.useful), # PR04
    Blas2Item("Taranto to my Sister", IC.useful), # PR05
    Blas2Item("Aubade to the Sleepless Iron", IC.useful), # PR06
    Blas2Item("Liviana of the Blighted Blades", IC.useful), # PR07
    Blas2Item("Martinete of Forge and Thunder", IC.useful), # PR08
    Blas2Item("Rosa of the Three Stars", IC.useful), # PR09
    Blas2Item("Zejel of the Cruelest Thorn", IC.useful), # PR10
    Blas2Item("Serrana of the Kindled Hearth", IC.useful), # PR11
    Blas2Item("Bleeding Crown", IC.useful), # PR12
    Blas2Item("Jabera to the Poison of Jealousy", IC.useful), # PR14
    Blas2Item("Seguiriya to the Memory of your Eyes", IC.useful), # PR15
    Blas2Item("Tiento to your Thorned Hairs", IC.useful), # PR16
    Blas2Item("Mirabras of the Return to Port", IC.useful), # PR17
    Blas2Item("Peteneras to the Burial of the Lights", IC.useful), # PR18

    # Prayers (DLC)
    Blas2Item("Prayer of the Penitent One", IC.useful), # PR101
    Blas2Item("Carcelera of Tender Relief", IC.useful), # PR102
    Blas2Item("Soleá of Excommunication", IC.useful, 0), # PR103
    Blas2Item("Cante Jondo of the Polluted Heart", IC.useful), # PR104
    Blas2Item("Praviana of the Golden Dawn", IC.useful), # PR105
    Blas2Item("Cabal of the Deep Wound", IC.useful), # PR106
    Blas2Item("Rondeña to the Unyielding Pledge", IC.useful), # PR107
    Blas2Item("Bleeding Chalice", IC.useful, 0), # PR108
    Blas2Item("Temple of the Three Winds", IC.useful), # PR109

    # Figurines
    Blas2Item("The Anointed One", IC.filler), # FG01
    Blas2Item("The Veteran One", IC.filler), # FG02
    Blas2Item("The Punished One", IC.filler), # FG03
    Blas2Item("The Purified One", IC.filler), # FG04
    Blas2Item("The Tempest", IC.filler), # FG05
    Blas2Item("The Alchemist", IC.filler), # FG06
    Blas2Item("The Guide", IC.filler), # FG07
    Blas2Item("The Choirmaster", IC.filler), # FG08
    Blas2Item("The Woman of the Stolen Face", IC.filler, 0), # FG09
    Blas2Item("The Selfless Father", IC.filler, 0), # FG10
    Blas2Item("The Thurifer", IC.filler), # FG11
    Blas2Item("The Demented One", IC.filler), # FG12
    Blas2Item("The Pilgrim", IC.filler), # FG13
    Blas2Item("The Pillager", IC.filler), # FG14
    Blas2Item("The Partisan", IC.filler), # FG15
    Blas2Item("The Ecstatic Novice", IC.filler), # FG16
    Blas2Item("Viridiana", IC.filler), # FG17
    Blas2Item("The Flagellant", IC.filler), # FG18
    Blas2Item("The Confessor", IC.filler, 0), # FG19
    Blas2Item("Castula", IC.filler, 0), # FG20
    Blas2Item("Nacimiento", IC.filler), # FG21
    Blas2Item("The Scribe", IC.filler), # FG22
    Blas2Item("Trifon", IC.filler, 0), # FG23
    Blas2Item("The Traitor", IC.filler), # FG25
    Blas2Item("The Bishop", IC.filler), # FG26
    Blas2Item("Tirso", IC.filler), # FG27
    Blas2Item("The Thirst", IC.filler), # FG28
    Blas2Item("Proximo", IC.filler, 0), # FG29
    Blas2Item("Cierzo", IC.progression), # FG30
    Blas2Item("Gregal", IC.progression), # FG31
    Blas2Item("Lebeche", IC.progression), # FG32
    Blas2Item("Jaloque", IC.progression), # FG33
    Blas2Item("The Unwavering One", IC.filler), # FG36
    Blas2Item("Crisanta", IC.filler, 0), # FG44
    Blas2Item("Cobijada Mayor", IC.filler), # FG45

    # Figurines (DLC)
    Blas2Item("The Oblivion", IC.filler, 0), # FG101
    Blas2Item("The Mercy", IC.filler), # FG102
    Blas2Item("The Sisters", IC.filler), # FG103
    Blas2Item("The Beatified", IC.filler), # FG104 
    Blas2Item("The Mournful", IC.filler, 0), # FG105
    Blas2Item("The Executed", IC.filler, 0), # FG106
    Blas2Item("The Family", IC.filler), # FG107
    Blas2Item("The Prisoner", IC.filler), # FG108
    Blas2Item("The Dance", IC.filler), # FG109
    Blas2Item("The Thief", IC.filler), # FG110
    Blas2Item("The Crying", IC.filler, 0), # FG111
    Blas2Item("The Liberated", IC.filler), # FG112
    Blas2Item("The Aide", IC.filler), # FG113

    # Quest Items
    Blas2Item("Tears of Sap", IC.progression), # QI01
    Blas2Item("Immaculate Mother-of-Pearl Gouge", IC.progression), # QI02
    Blas2Item("Oils of the Blessed Mixture", IC.progression), # QI03
    Blas2Item("Remembrance of the Confessor", IC.filler), # QI04
    Blas2Item("Regula's Cloth", IC.progression), # QI05
    Blas2Item("Remembrance of Regula", IC.filler), # QI06
    Blas2Item("Scroll of the Elder", IC.progression), # QI07
    Blas2Item("Cloth of the Old Woman", IC.progression), # QI08
    Blas2Item("Remembrace of Trifon", IC.filler), # QI09
    Blas2Item("Remembrace of Castula", IC.filler), # QI10
    Blas2Item("Silver Shell File", IC.progression), # QI11
    Blas2Item("Sculptor's Resonant Gavel", IC.progression), # QI12
    Blas2Item("Cursed Letter, Page One", IC.progression), # QI14
    Blas2Item("Cursed Letter, Page Two", IC.progression), # QI16
    Blas2Item("Cursed Letter, Page Three", IC.progression), # QI18
    Blas2Item("Cursed Letter, Page Four", IC.progression), # QI20
    Blas2Item("Cursed Letter, Last Page", IC.progression), # QI22
    #Blas2Item("Unfinished Lullaby", IC.progression, 0), # QI23, QI24, QI25, QI26
    #Blas2Item("Lullably of the White Shore", IC.progression, 0), # QI27
    Blas2Item("Piece of the Lullaby", IC.progression, 5),
    Blas2Item("Broken Key", IC.progression), # QI28
    Blas2Item("Forgotten Tribute", IC.progression, 3), # QI29, QI30, QI31
    Blas2Item("Abandoned Rosary Knot", IC.progression, 4), # QI32, QI33, QI34, QI35
    Blas2Item("Stolen Pendant of Solitude", IC.filler, 0), # QI36
    Blas2Item("Fervent Kiss", IC.progression, 5), # QI37, QI38, QI39, QI40, QI41
    Blas2Item("Ornate Chalice", IC.useful, 5), # QI42, QI43, QI44, QI45, QI46
    Blas2Item("Empty Receptacle", IC.useful, 4), # QI47, QI48, QI49, QI50
    Blas2Item("Silver-Clad Crystal Shard", IC.useful, 3), # QI51, QI52, QI53
    Blas2Item("Giant Rattle", IC.progression), # QI54
    Blas2Item("Remembrance of Proximo", IC.filler), # QI55
    Blas2Item("Wax Seed", IC.progression, 6), # QI56, QI57, QI58, QI59, QI60, QI61
    Blas2Item("Remembrance of Cesareo", IC.filler), # QI62
    Blas2Item("Key of the Pilgrim", IC.progression), # QI63
    Blas2Item("Key of Endless Orison", IC.progression), # QI64
    Blas2Item("Key of Salt", IC.progression), # QI65
    Blas2Item("Key of the Council", IC.progression), # QI66
    Blas2Item("Mirrored Key", IC.progression), # QI67
    Blas2Item("Holy Oil of Everlasting Anointment", IC.progression), # QI68
    Blas2Item("Incense of the Envoys", IC.filler), # QI69
    Blas2Item("Steely Battle Lance", IC.useful, 0), # QI70
    Blas2Item("Remembrance of Crisanta", IC.filler), # QI71

    # Quest Items (DLC)
    Blas2Item("Mud Key", IC.progression), # QI101
    Blas2Item("Ceramic Key", IC.progression), # QI103
    Blas2Item("Mea Culpa Hilt", IC.filler, 0), # QI104
    Blas2Item("Imperfectus Lacrimatorio", IC.useful, 5), # QI106, QI107, QI108, QI109
    Blas2Item("Plenus Lacrimatorio", IC.useful, 0), # QI110
    Blas2Item("Beatus Lacrimatorio", IC.useful, 0), # QI111
    Blas2Item("Lump of Gold", IC.progression, 20),

    # Weapons
    Blas2Item("Veredicto", IC.progression, 3),
    Blas2Item("Ruego Al Alba", IC.progression, 3),
    Blas2Item("Sarmiento & Centella", IC.progression, 3),
    Blas2Item("Mea Culpa", IC.progression, 2), # (DLC)

    # Abilities
    Blas2Item("Ivy of Ascension", IC.progression),
    Blas2Item("Passage of Ash", IC.progression),
    Blas2Item("Mercy of the Wind", IC.progression),
    Blas2Item("Scions' Protection", IC.progression),
    Blas2Item("Broken Step", IC.progression),

    # Miscellaneous
    Blas2Item("Cherub", IC.progression, 0),
    Blas2Item("Marks of Martyrdom (5)", IC.useful, 2),
    Blas2Item("Marks of Martyrdom (4)", IC.useful, 3),
    Blas2Item("Marks of Martyrdom (3)", IC.useful, 4),
    Blas2Item("Marks of Martyrdom (2)", IC.useful, 3),
    Blas2Item("Marks of Martyrdom (1)", IC.useful, 35),
    Blas2Item("Mark of the Preceptor", IC.useful, 14), # (DLC)
    Blas2Item("Tears of Atonement (5000)", IC.filler, 5),
    Blas2Item("Tears of Atonement (3500)", IC.filler, 3),
    Blas2Item("Tears of Atonement (2000)", IC.filler, 5),
    Blas2Item("Tears of Atonement (1800)", IC.filler, 2),
    Blas2Item("Tears of Atonement (1200)", IC.filler, 3),
    Blas2Item("Tears of Atonement (800)", IC.filler, 19) # 8 
]

filler_list: List[str] = [
    "Tears of Atonement (5000)",
    "Tears of Atonement (3500)",
    "Tears of Atonement (2000)",
    "Tears of Atonement (1800)",
    "Tears of Atonement (1200)",
    "Tears of Atonement (800)"
]

group_table: Dict[str, Set[str]] = {
    "bosskeys": {"Key of the Pilgrim",
                 "Key of Endless Orison",
                 "Key of Salt",
                 "Key of the Council",
                 "Mirrored Key"},

    "tools": {"Tears of Sap",
              "Immaculate Mother-of-Pearl Gouge",
              "Oils of the Blessed Mixture",
              "Silver Shell File",
              "Sculptor's Resonant Gavel"}
}