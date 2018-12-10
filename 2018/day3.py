def part_1():
    import numpy
    cloth = numpy.empty(shape=(1000,1000), dtype=object)
    for i in range(1000):
        for j in range(1000):
            cloth[i,j] = []
    # cloth(h, w)

    def parse_req(req):
        import re
        phrase = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        msg = phrase.search(req)
        #tuple(order, left in, top in, width, height)
        return msg.groups()

    def insert(tup):
        id = tup[0]
        sleft = int(tup[1])
        stop = int(tup[2])
        mleft = int(tup[3])
        mdown = int(tup[4])

        print(f"inserting id: {id}, start left: {sleft}, start top: {stop}, over left: {mleft}, down: {mdown}")
        for width in range(mleft):
            for height in range(mdown):
                #print(id, height + stop, width + sleft)
                cloth[height + stop, width + sleft].append(id)
        #print(cloth)



    with open("./day3_input.txt", "r") as file:
        #with open("./test.txt", "r") as file:
        for line in file:
            req = parse_req(line)
            insert(req)

    overlap = 0
    for i in range(1000):
        for j in range(1000):
            if len(cloth[i,j]) > 1:
                print(f"overlap at {i},{j},{cloth[i,j]}")
                overlap += 1
    print("overlap: ", overlap)
    print(cloth)

def part_2():
    import numpy
    cloth = numpy.empty(shape=(1000,1000), dtype=object)
    for i in range(1000):
        for j in range(1000):
            cloth[i,j] = []
    # cloth(h, w)

    def parse_req(req):
        import re
        phrase = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
        msg = phrase.search(req)
        #tuple(order, left in, top in, width, height)
        return msg.groups()

    def insert(tup):
        id = tup[0]
        sleft = int(tup[1])
        stop = int(tup[2])
        mleft = int(tup[3])
        mdown = int(tup[4])

        print(f"inserting id: {id}, start left: {sleft}, start top: {stop}, over left: {mleft}, down: {mdown}")
        for width in range(mleft):
            for height in range(mdown):
                #print(id, height + stop, width + sleft)
                cloth[height + stop, width + sleft].append(id)
        #print(cloth)



    with open("./day3_input.txt", "r") as file:
        #with open("./test.txt", "r") as file:
        for line in file:
            req = parse_req(line)
            insert(req)

    non_overlap = set()
    overlap = set()
    for i in range(1000):
        for j in range(1000):
            # if a request was put in
            if len(cloth[i,j]) > 0:
                # if there is only one request
                if len(cloth[i,j]) == 1:
                    # add to set
                    non_overlap.add(cloth[i,j][0])
                # more than 1 request
                else:
                    # remove all from set
                    for r in cloth[i,j]:
                        overlap.add(r)

    print(f" non overlapping request: {non_overlap - overlap}")


part_1()
part_2()
