def part_1():

    def polymer_check(poly):
        idxs = []
        removed = False
        for (idx, char) in enumerate(poly):
            # if not last character
            if idx != len(poly)-1:
                if removed:
                    removed = False
                else:
                    same = char.lower() == poly[idx+1].lower()
                    lowerUpper = char.islower() and poly[idx+1].isupper()
                    upperLower = char.isupper() and poly[idx+1].islower()
                    #print(char, poly[idx+1], same, lowerUpper, upperLower, (same and (lowerUpper or upperLower)))
                    if (same and (lowerUpper or upperLower)):
                        idxs.append(idx)
                        removed = True
        return idxs

    def polymer_reaction(polymer, idxs):
        # example 'helloworld' to remove el (idx: 1,2)
        # string[0:1]+string[3:]

        idxs_to_remove = idxs
        idxs_to_remove.reverse()

        newPolymer = polymer

        for idx in idxs_to_remove:
            #print(newPolymer[idx-2:idx+3], idx)
            newPolymer = newPolymer[0:idx] + newPolymer[idx+2:]
            #print(newPolymer[idx-2:idx+3], "removed")

        return newPolymer



    with open("./day5_input.txt", "r") as file:
        polymer = ""
        for line in file:
            polymer += line
    #polymer = "dabAcCaCBAcCcaDA"
    polymer = polymer.replace("\n","")

    idxs_to_remove = polymer_check(polymer)

    while len(idxs_to_remove) > 0:
        #print(polymer)
        polymer = polymer_reaction(polymer, idxs_to_remove)
        idxs_to_remove = polymer_check(polymer)

    print("part 1:", polymer, idxs_to_remove, len(polymer))


def part_2():
    def polymer_check(poly):
        idxs = []
        removed = False
        for (idx, char) in enumerate(poly):
            # if not last character
            if idx != len(poly)-1:
                if removed:
                    removed = False
                else:
                    same = char.lower() == poly[idx+1].lower()
                    lowerUpper = char.islower() and poly[idx+1].isupper()
                    upperLower = char.isupper() and poly[idx+1].islower()
                    #print(char, poly[idx+1], same, lowerUpper, upperLower, (same and (lowerUpper or upperLower)))
                    if (same and (lowerUpper or upperLower)):
                        idxs.append(idx)
                        removed = True
        return idxs

    def polymer_reaction(polymer, idxs):
        # example 'helloworld' to remove el (idx: 1,2)
        # string[0:1]+string[3:]

        idxs_to_remove = idxs
        idxs_to_remove.reverse()

        newPolymer = polymer

        for idx in idxs_to_remove:
            #print(newPolymer[idx-2:idx+3], idx)
            newPolymer = newPolymer[0:idx] + newPolymer[idx+2:]
            #print(newPolymer[idx-2:idx+3], "removed")

        return newPolymer



    with open("./day5_input.txt", "r") as file:
        polymer = ""
        for line in file:
            polymer += line
    #polymer = "dabAcCaCBAcCcaDA"
    polymer = polymer.replace("\n","")

    set_of_units = set()
    for char in polymer:
        set_of_units.add(char.lower())

    unit_removal_score = {}
    min_unit = ("", len(polymer))
    for unit in set_of_units:
        unit_polymer = polymer.replace(unit, "")
        unit_polymer = unit_polymer.replace(unit.upper(),"")

        idxs_to_remove = polymer_check(unit_polymer)
        while len(idxs_to_remove) > 0:
            #print(polymer)
            unit_polymer = polymer_reaction(unit_polymer, idxs_to_remove)
            idxs_to_remove = polymer_check(unit_polymer)

        #print(polymer, idxs_to_remove, len(polymer))
        unit_removal_score[unit] = len(unit_polymer)
        print(unit, len(unit_polymer))
        if len(unit_polymer) < min_unit[1]:
            min_unit = (unit, len(unit_polymer))

    print(unit_removal_score, min_unit)

part_1()
part_2()
