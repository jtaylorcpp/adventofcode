def part_1():
    two = 0
    three = 0

    with open("./day2_input.txt", "r") as file:
        for line in file:
            char_dict = {}
            for char in line:
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1
            twos, threes = False, False
            for k,v in char_dict.items():
                if v == 2:
                    twos = True
                if v == 3:
                    threes = True
            if twos:
                two += 1
            if threes:
                three += 1

            #print(f"id:{line}, dict:{char_dict}, two:{two}, three:{three}")
    prod = two * three
    print(f"{two} * {three} = {prod}")

def part_2():

    def compare(string1, string2):
        strlen = len(string1)
        parity = 0
        for idx in range(0,strlen):
            if string1[idx] != string2[idx]:
                parity += 1
        return parity

    def strip(string1, string2):
        new_string = ""
        for idx, char in enumerate(string1):
            if char == string2[idx]:
                new_string += char
        return new_string

    id_list = []
    with open("./day2_input.txt", "r") as file:
        for line in file:
            id_list.append(line[:-1])

    compare_list = []

    while id_list:
        id = id_list.pop()

        def this_compare(string2):
            parity = compare(id, string2)
            return (parity, id, string2)

        compare_list += list(map(this_compare, id_list))

    ones_list = []
    for (parity, string1, string2) in compare_list:
        if parity == 1:
            new_string = strip(string1, string2)
            ones_list.append(new_string)

    print(ones_list)



part_1()
part_2()
