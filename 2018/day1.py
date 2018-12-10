def part_1():
    atoi = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }


    def parse_number(number):
        sign, unsign = number[0], number[1:]
        unsign = unsign.replace("\n", "")
        unsign = unsign.replace(" ", "")
        num = 0
        for (idx, stringint) in enumerate(unsign):
            num += (atoi[stringint] * (10 ** (len(unsign) - idx - 1)))

        if "-" in sign:
            return -1 * num
        else:
            return num


    freq = 0

    with open("./day1_input.txt", "r") as file:
        for line in file:
            num = parse_number(line)
            #print(f"{line}, {num}")
            freq += num

    print(f"ending freg is {freq}")

def part_2():
    atoi = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }


    def parse_number(number):
        sign, unsign = number[0], number[1:]
        unsign = unsign.replace("\n", "")
        unsign = unsign.replace(" ", "")
        num = 0
        for (idx, stringint) in enumerate(unsign):
            num += (atoi[stringint] * (10 ** (len(unsign) - idx - 1)))

        if "-" in sign:
            return -1 * num
        else:
            return num


    freq = 0
    freq_dict = {}

    while True:
        #print('part 2 starting new file read')
        with open("./day1_input.txt", "r") as file:
            for line in file:
                num = parse_number(line)
                freq += num
                if freq in freq_dict:
                    print(f"the repeating freq is {freq}")
                    exit()
                else:
                    freq_dict[freq] = True



print("part 1:")
part_1()

print("part 2:")
part_2()
