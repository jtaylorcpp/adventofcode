def part_1():
    map_lines = []
    with open("./day13_input.txt","r") as file:
        for line in file:
            map_lines.append(line.replace("\n",""))
    print map_lines

part_1()
