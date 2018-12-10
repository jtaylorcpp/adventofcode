'''
.#####...#....#..#####......###...####...#.......#####...######
.#....#..#....#..#....#......#...#....#..#.......#....#..#.....
.#....#..#....#..#....#......#...#.......#.......#....#..#.....
.#....#..#....#..#....#......#...#.......#.......#....#..#.....
.#####...######..#####.......#...#.......#.......#####...#####.
.#....#..#....#..#...........#...#..###..#.......#.......#.....
.#....#..#....#..#...........#...#....#..#.......#.......#.....
.#....#..#....#..#.......#...#...#....#..#.......#.......#.....
.#....#..#....#..#.......#...#...#...##..#.......#.......#.....
.#####...#....#..#........###.....###.#..######..#.......######

10831
'''

def part_1():
    def parse_record(record):
        import re

        pvregex = re.compile(r"<([ \-0-9]+),([ \-0-9]+)> velocity=<([ \-0-9]+),([ \-0-9]+)>")

        return pvregex.search(record).groups()

    def plot_map(points, time):
        min_max = [0, 0, 0, 0]
        coords = []
        for point, vals in points.items():
            this_coords = vals["current"]
            this_coords = (this_coords[0] + (time * vals["velocity"][0]),this_coords[1] + (time * vals["velocity"][1]))
            coords.append(this_coords)
            if this_coords[0] < min_max[0]:
                min_max[0] = this_coords[0]
            if this_coords[0] > min_max[1]:
                min_max[1] = this_coords[0]

            if this_coords[1] < min_max[2]:
                min_max[2] = this_coords[1]
            if this_coords[1] > min_max[3]:
                min_max[3] = this_coords[1]

        sky = (min_max[1] - min_max[0] + 1, min_max[3] - min_max[2] + 1)
        x_pad = -1 * min_max[0]
        y_pad = -1 * min_max[2]
        print(time, min_max, sky, x_pad, y_pad)

        import numpy as np
        sky_map = np.memmap("./tmp", dtype=np.int8, mode="w+", shape=(sky[0], sky[1]))
        #sky_map = [ [" "]*sky[0] for y in range(sky[1])]
        #sky_map[y][x]
        for coord in coords:
            #print(coord, x_pad + coord[0], y_pad + coord[1])
            sky_map[x_pad + coord[0], y_pad + coord[1]] = 1

        if sky[0] * sky[1] <= len(points) ** 2:
            '''
            import matplotlib.pyplot as plt

            xs = []
            ys = []
            for y in range(sky[1]):
                for x in range(sky[0]):
                    if sky_map[x,y] == 1:
                        xs.append(x)
                        ys.append(y)
            plt.plot(x,y,"ro")
            plt.axis([sky[0],x_pad,sky[1],y_pad])
            plt.show()
            '''
            for y in range(sky[1]):
                line= ""
                for x in range(sky[0]):
                    if sky_map[x,y] == 1:
                        line += "#"
                    else:
                        line += "."
                print(line)

            cont = input("continue? [y/n] ")
            if "n" in cont.lower():
                exit()

    points = {}
    with open("./day10_input.txt", "r") as file:
        for (idx, line) in enumerate(file):
            record = parse_record(line)
            #print(record)
            points[idx] = {
                "current" : (int(record[0]), int(record[1])),
                "velocity" : (int(record[2]), int(record[3]))
            }

    #print(points)

    time = 10825
    while True:
        plot_map(points, time)
        time += 1


part_1()
