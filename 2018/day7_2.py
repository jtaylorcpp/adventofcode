def part_1():
    node_reg = {}

    class Node:
        def __init__(self, id):
            self.id = id
            self.done = False
            self.next = []
            self.prev = []

        def add_next(self, node):
            self.next.append(node)

        def add_prev(self, node):
            self.prev.append(node)

        def available(self, reg):
            if False in [reg[n].done for n in self.prev]:
                return False
            else:
                return True

        def nowdone(self):
            self.done = True

        def nprint(self):
            print(f"{self.id}, {self.next}, {self.prev}")

    with open("./day7_input.txt", "r") as file:
        for line in file:
            words = line.split(" ")
            if words[1] not in node_reg:
                node_reg[words[1]] = Node(words[1])
            if words[7] not in node_reg[words[1]].next:
                node_reg[words[1]].add_next(words[7])

            if words[7] not in node_reg:
                node_reg[words[7]] = Node(words[7])
            if words[1] not in node_reg[words[7]].prev:
                node_reg[words[7]].add_prev(words[1])

    avail_nodes = []
    for k,v in node_reg.items():
        if v.available(node_reg):
            avail_nodes.append(k)

    avail_nodes = sorted(avail_nodes)
    work =[]
    while avail_nodes:
        node = avail_nodes.pop(0)
        print(f"processing node {node}")
        node_reg[node].nowdone()
        work.append(node)
        for n in node_reg[node].next:
            if node_reg[n].available(node_reg):
                avail_nodes.append(n)

        avail_nodes = sorted(avail_nodes)
        print(avail_nodes)

    print("".join(work))

def part_2():
    print("part 2")
    node_reg = {}

    class Node:
        def __init__(self, id):
            self.id = id
            self.done = False
            self.next = []
            self.prev = []

        def add_next(self, node):
            self.next.append(node)

        def add_prev(self, node):
            self.prev.append(node)

        def available(self, reg):
            if False in [reg[n].done for n in self.prev]:
                return False
            else:
                return True

        def nowdone(self):
            self.done = True

        def nprint(self):
            print(f"{self.id}, {self.next}, {self.prev}")

    with open("./day7_input.txt", "r") as file:
        for line in file:
            words = line.split(" ")
            if words[1] not in node_reg:
                node_reg[words[1]] = Node(words[1])
            if words[7] not in node_reg[words[1]].next:
                node_reg[words[1]].add_next(words[7])

            if words[7] not in node_reg:
                node_reg[words[7]] = Node(words[7])
            if words[1] not in node_reg[words[7]].prev:
                node_reg[words[7]].add_prev(words[1])

    avail_nodes = []
    for k,v in node_reg.items():
        if v.available(node_reg):
            avail_nodes.append(k)

    print("starting avail nodes: ", avail_nodes)
    avail_nodes = sorted(avail_nodes)
    work =[]
    time = 0
    offset = -4
    workers_time = [0] * 5
    workers_node = [""] * 5
    while (len(work) < len(node_reg)):
        new_avail = []
        for (idx, val) in enumerate(workers_time):
             if val <= time:
                 if workers_node[idx] != "":
                    node_reg[workers_node[idx]].nowdone()
                    work.append(workers_node[idx])
                    for n in node_reg[workers_node[idx]].next:
                        if node_reg[n].available(node_reg):
                            new_avail.append(n)
                    workers_node[idx] = ""
        avail_nodes = sorted(new_avail + avail_nodes)

        print(time, workers_node, workers_time, avail_nodes)
        for (idx, val) in enumerate(workers_node):
            if val == "":
                if avail_nodes:
                    workers_node[idx] = avail_nodes.pop(0)
                    workers_time[idx] = time + ord(workers_node[idx]) + offset

        print(time, workers_node, workers_time, avail_nodes)




        time += 1


    print("".join(work))

part_1()
part_2()
