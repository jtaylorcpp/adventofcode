def part_1():

    def parse_record(record):
        import re
        nodere = re.compile(r'Step ([A-z]) must be finished before step ([A-Z]) can begin.')
        vals = nodere.search(record).groups()
        return vals


    nodes = {}
    roots = {}

    with open("./day7_input.txt", "r") as file:
        for line in  file:
            new_nodes = parse_record(line)

            if new_nodes[0] not in nodes:
                nodes[new_nodes[0]] = [new_nodes[1]]
                roots[new_nodes[0]] = True
            else:
                nodes[new_nodes[0]].append(new_nodes[1])

            if new_nodes[1] not in nodes:
                nodes[new_nodes[1]] = []

            if new_nodes[1] in roots:
                del roots[new_nodes[1]]

    print(nodes, roots)

    node_order=[]
    nodes_to_use = sorted(roots.keys())

    while nodes_to_use:
        # get next alpha node
        next_node = nodes_to_use.pop(0)

        # get its children
        next_nodes = nodes[next_node]
        del nodes[next_node]

        child_nodes = []
        for k,v in nodes.items():
            child_nodes += v

        for possible_node in next_nodes:
            if possible_node not in child_nodes:
                nodes_to_use.append(possible_node)


        node_order.append(next_node)
        nodes_to_use = sorted(nodes_to_use)

    print(node_order)
    print("".join(node_order))

def part_2():

    alphanum ={
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
    }

    def parse_record(record):
        import re
        nodere = re.compile(r'Step ([A-z]) must be finished before step ([A-Z]) can begin.')
        vals = nodere.search(record).groups()
        return vals


    nodes = {}
    roots = {}

    with open("./day7_input.txt", "r") as file:
        for line in  file:
            new_nodes = parse_record(line)

            if new_nodes[0] not in nodes:
                nodes[new_nodes[0]] = [new_nodes[1]]
                roots[new_nodes[0]] = True
            else:
                nodes[new_nodes[0]].append(new_nodes[1])

            if new_nodes[1] not in nodes:
                nodes[new_nodes[1]] = []

            if new_nodes[1] in roots:
                del roots[new_nodes[1]]

    #print(nodes, roots)

    worker_times = {
        0 : -1, 1 : -1, 2 : -1, 3 : -1, 4 : -1
    }
    worker_work = {
        0 : "", 1 : "", 2 : "", 3 : "", 4 : ""
    }
    nodes_to_use = sorted(roots.keys())

    time = 0
    num_nodes = len(nodes)
    node_order = []
    while len(node_order) < num_nodes:
        # assign work to unused workers
        # close out done nodes
        for w,t in worker_times.items():
            if t <= time:
                if worker_work[w] != "":
                    # clear out last order before reassigning
                    #print(f"time {time}, worker  {w} finished {worker_work[w]}")
                    nodes_to_add = nodes[worker_work[w]]
                    del nodes[worker_work[w]]

                    child_nodes = []
                    for k,v in nodes.items():
                        child_nodes += v

                    for possible in nodes_to_add:
                        if possible not in child_nodes:
                            nodes_to_use.append(possible)

                    node_order.append(worker_work[w])
                    worker_work[w] = ""

        nodes_to_use = sorted(nodes_to_use)
        #print(nodes_to_use)

        # ready to schedule new nodes
        for w,t in worker_times.items():
            if t <= time:
                # worker is ready
                if nodes_to_use:
                    worker_work[w] = nodes_to_use.pop(0)
                    worker_times[w] = time + alphanum[worker_work[w]] + 60


        print(time,worker_work,worker_times,node_order)
        time += 1

    print(node_order, nodes)
    print("".join(node_order))

part_1()
part_2()

# CGKMUWXFAIHSYDNLJQTREOPZBV
# CGMUXKFWSAIHYNDLQJTREOPZBV
