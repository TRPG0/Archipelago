# Preprocessor to convert Blasphemous II Randomizer logic into a StringWorldDefinition for use with APHKLogicExtractor
# https://github.com/BrandenEK/BlasII.Randomizer
# https://github.com/ArchipelagoMW-HollowKnight/APHKLogicExtractor


import json, requests, argparse
from typing import List, Dict, Any


def load_resource_local(file: str) -> List[Dict[str, Any]]:
    print(f"Reading from {file}")
    loaded = []
    with open(file, encoding="utf-8") as f:
        loaded = read_json(f.readlines())
        f.close()

    return loaded


def load_resource_from_web(url: str) -> List[Dict[str, Any]]:
    req = requests.get(url, timeout=1)
    print(f"Reading from {url}")
    req.encoding = "utf-8"
    lines: List[str] = []
    for line in req.text.splitlines():
        while "\t" in line:
            line = line[1::]
        if line != "":
            lines.append(line)
    return read_json(lines)


def read_json(lines: List[str]) -> List[Dict[str, Any]]:
    loaded = []
    creating_object: bool = False
    obj: str = ""
    for line in lines:
        stripped = line.strip()
        if "{" in stripped:
            creating_object = True
            obj += stripped
            continue
        elif "}," in stripped or "}" in stripped and "]" in lines[lines.index(line)+1]:
            creating_object = False
            obj += "}"
            #print(f"obj = {obj}")
            loaded.append(json.loads(obj))
            obj = ""
            continue

        if not creating_object:
            continue
        else:
            try:
                if "}," in lines[lines.index(line)+1] and stripped[-1] == ",":
                    obj += stripped[:-1]
                else:
                    obj += stripped
            except IndexError:
                obj += stripped

    return loaded


def preprocess_logic(logic: str) -> str:
    while ">=" in logic:
        index: int = logic.find(">=")
        logic = logic[:index-1] + logic[index+3:]

    while ">" in logic:
        index: int = logic.find(">")
        count = int(logic[index+2])
        count += 1
        logic = logic[:index-1] + str(count) + logic[index+3:]

    while "<=" in logic:
        index: int = logic.find("<=")
        logic = logic[:index-1] + logic[index+3:]
    
    while "<" in logic:
        index: int = logic.find("<")
        count = int(logic[index+2])
        count += 1
        logic = logic[:index-1] + str(count) + logic[index+3:]

    #print(logic)
    return logic


def build_logic_conditions(logic: str) -> List[List[str]]:
    all_conditions: List[List[str]] = []

    parts = logic.split()
    sub_part: str = ""
    current_index: int = 0
    parens: int = -1
    current_condition: List[str] = []
    parens_conditions: List[List[List[str]]] = []

    for index, part in enumerate(parts):
        #print(current_index, index, parens, part)

        # skip parts that have already been handled
        if index < current_index:
            continue

        # break loop if reached final part
        try:
            parts[index+1]
        except IndexError:
            #print("INDEXERROR", part)
            if parens < 0:
                current_condition.append(part)
                if len(parens_conditions) > 0:
                    for i in parens_conditions:
                        for j in i:
                            all_conditions.append(j + current_condition)
                else:
                    all_conditions.append(current_condition)
                break

        #print(current_condition, parens, sub_part)

        # prepare for subcondition
        if "(" in part:
            # keep track of nested parentheses
            if parens == -1:
                parens = 0
            for char in part:
                if char == "(":
                    parens += 1
            
            # add to sub part
            if sub_part == "":
                sub_part = part
            else:
                sub_part += f" {part}"
            #if not ")" in part:
            continue

        # end of subcondition
        if ")" in part:
            # read every character in case of multiple closing parentheses
            for char in part:
                if char == ")":
                    parens -= 1

            sub_part += f" {part}"

            # if reached end of parentheses, handle subcondition
            if parens == 0:
                #print(current_condition, sub_part)
                parens = -1

                try:
                    parts[index+1]
                except IndexError:
                    #print("END OF LOGIC")
                    if len(parens_conditions) > 0:
                        parens_conditions.append(build_logic_subconditions(current_condition, sub_part))
                        #print("PARENS:", parens_conditions)

                        temp_conditions: List[List[str]] = []

                        for i in parens_conditions[0]:
                            for j in parens_conditions[1]:
                                temp_conditions.append(i + j)

                        parens_conditions.pop(0)
                        parens_conditions.pop(0)

                        while len(parens_conditions) > 0:
                            temp_conditions2 = temp_conditions
                            temp_conditions = []
                            for k in temp_conditions2:
                                for l in parens_conditions[0]:
                                    temp_conditions.append(k + l)
                            
                            parens_conditions.pop(0)

                        #print("TEMP:", remove_duplicates(temp_conditions))
                        all_conditions += temp_conditions
                    else:
                        all_conditions += build_logic_subconditions(current_condition, sub_part)
                else:
                    #print("NEXT PARTS:", parts[index+1], parts[index+2])
                    if parts[index+1] == "&&":
                        parens_conditions.append(build_logic_subconditions(current_condition, sub_part))
                        #print("PARENS:", parens_conditions)
                    else:
                        if len(parens_conditions) > 0:
                            parens_conditions.append(build_logic_subconditions(current_condition, sub_part))
                            #print("PARENS:", parens_conditions)

                            temp_conditions: List[List[str]] = []

                            for i in parens_conditions[0]:
                                for j in parens_conditions[1]:
                                    temp_conditions.append(i + j)

                            parens_conditions.pop(0)
                            parens_conditions.pop(0)

                            while len(parens_conditions) > 0:
                                temp_conditions2 = temp_conditions
                                temp_conditions = []
                                for k in temp_conditions2:
                                    for l in parens_conditions[0]:
                                        temp_conditions.append(k + l)
                                
                                parens_conditions.pop(0)

                            #print("TEMP:", remove_duplicates(temp_conditions))
                            all_conditions += temp_conditions
                        else:
                            all_conditions += build_logic_subconditions(current_condition, sub_part)

                    current_index = index+2
                    
                    current_condition = []
                    sub_part = ""
                    
            continue

        # collect all parts until reaching end of parentheses
        if parens > 0:
            sub_part += f" {part}"
            continue

        current_condition.append(part)

        # continue with current condition
        if parts[index+1] == "+":
            current_index = index+2
            continue
        
        # add condition to list and start new one
        elif parts[index+1] == "|":
            if len(parens_conditions) > 0:
                for i in parens_conditions:
                    for j in i:
                        all_conditions.append(j + current_condition)
                parens_conditions = []
            else:    
                all_conditions.append(current_condition)
            current_condition = []
            current_index = index+2
            continue
        
    return remove_duplicates(all_conditions)


def build_logic_subconditions(current_condition: List[str], subcondition: str) -> List[List[str]]:
    #print("STARTED SUBCONDITION", current_condition, subcondition)
    subconditions = build_logic_conditions(subcondition[1:-1])
    final_conditions = []

    for condition in subconditions:
        final_condition = current_condition + condition
        final_conditions.append(final_condition)

    #print("ENDED SUBCONDITION")
    #print(final_conditions)
    return final_conditions


def remove_duplicates(conditions: List[List[str]]) -> List[List[str]]:
    final_conditions: List[List[str]] = []
    for condition in conditions:
        final_conditions.append(list(dict.fromkeys(condition)))

    return final_conditions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--local', action="store_true", help="Use local files in the same directory instead of reading resource files from the BrandenEK/BlasII.Randomizer repository.")
    args = parser.parse_args()
    return args


def main(args: argparse.Namespace):
    locations = []

    if args.local:
        locations = load_resource_local("item-locations.json")

    else:
        locations = load_resource_from_web("https://raw.githubusercontent.com/BrandenEK/BlasII.Randomizer/refs/heads/main/resources/data/Randomizer/itemlocations.json")

    output: Dict[str, Any] = {}
    logic_objects: List[Dict[str, Any]] = []
    location_flags: Dict[str, List[str]] = {}

    for location in locations:
        if location.get("flags") != None:
            flags: str = location.get("flags")
            
            if not flags in location_flags.keys():
                location_flags[flags] = [location.get("id")]
            else:
                list = location_flags[flags]
                list.append(location.get("id"))
                location_flags[flags] = list


        obj = {
            "Name": location.get("id"),
            "Logic": [],
            "Handling": "Location"
        }

        if location.get("logic") != None:
            for condition in build_logic_conditions(preprocess_logic(location.get("logic"))):
                logic = {
                    "StateProvider": None,
                    "Conditions": condition,
                    "StateModifiers": []
                }
                obj["Logic"].append(logic)
        else:
            logic = {
                "StateProvider": None,
                "Conditions": [],
                "StateModifiers": []
            }
            obj["Logic"].append(logic)

        logic_objects.append(obj)
        
    output["LogicObjects"] = logic_objects

    sorted_flags = {i: location_flags[i] for i in sorted(location_flags)}
    #print(str(sorted_flags))

    with open("StringWorldDefinition.json", "w") as file:
        print("Writing to StringWorldDefinition.json")
        file.write(json.dumps(output, indent=4))

    with open("LocationFlags.py", "w") as file:
        print("Writing to LocationFlags.py")
        file.write("# This file is programatically generated\n")
        file.write("from typing import Dict, List\n\n\n")
        file.write("location_flags: Dict[str, List[str]] = ")
        file.write(json.dumps(sorted_flags, indent=4))


if __name__ == "__main__":
    #test = "censer + rapier + doublejump"
    #print(preprocess_logic(test))
    #print(build_logic_conditions(preprocess_logic(test)))
    main(parse_args())