def part_1():
    import numpy
    class Node:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.label = ''

        def distance(self, x,y):
            return abs(self.x - x) + abs(self.y - y)

        def rate(self,x1,y1,x2,xy):
            d1 = self.distance(x1,y1)
            d2 = self.distance(x2,y2)
            return ((d2 * 1.0) - (d1 * 1.0))/1.0

    nodes = []
    with open("./day6_input.txt", "r") as file:
        for line in file:
            strNode = line.replace("\n","").split(", ")
            nodes.append(Node(int(strNode[0]), int(strNode[1])))

    node_map = {}
    map_edges = [0,0]
    for (idx, node) in enumerate(nodes):
        node.label = str(idx)
        node_map[str(idx)] = node
        if node.x > map_edges[0]:
            map_edges[0] = node.x
        if node.y > map_edges[1]:
            map_edges[1] = node.y

    map_edges = [int(map_edges[0] * 2), int(map_edges[1] * 2)]
    #print(map_edges)
    map = numpy.empty(shape=(map_edges[1],map_edges[0]), dtype=object)

    #print(nodes)

    for x in range(map_edges[0]):
        for y in range(map_edges[1]):
            closest_node = ["", sum(map_edges)]
            #print(f"map point {x},{y}")
            for node in nodes:
                #print(f"node: {node.label}, {node.x}, {node.y}, {node.distance(x,y)}, {sum(map_edges)}")
                if node.distance(x,y) < closest_node[1]:
                    #print(f"node {node.label} is closest!")
                    closest_node = [node.label, node.distance(x,y)]
                elif node.distance(x,y) == closest_node[1]:
                    #print(f"node {node.label} is same distance to {closest_node}")
                    closest_node = ["*", node.distance(x,y)]
            map[y,x] = closest_node[0]
            #print(f"map point ({x},{y}) is closest to node {closest_node[0]}")

    # find infinite nodes
    # for every node find closest edge
    # if there is a closer node to to that edge than you are not infinite
    #print(map)
    #print(node_map)
    eval_nodes = {}
    for node in nodes:
        eval_nodes[node.label] = 0
    #check borders
    for x in range(map_edges[0]):
        if map[0,x] in eval_nodes:
            del eval_nodes[map[0,x]]
        if map[map_edges[1]-1,x] in eval_nodes:
            del eval_nodes[map[map_edges[1]-1,x]]
    for y in range(map_edges[1]):
        if map[y,0] in eval_nodes:
            del eval_nodes[map[y,0]]
        if map[y,map_edges[0]-1] in eval_nodes:
            del eval_nodes[map[y,map_edges[0]-1]]

    #print(eval_nodes)

    for x in range(map_edges[0]):
        for y in range(map_edges[1]):
            if map[y,x] in eval_nodes:
                eval_nodes[map[y,x]] += 1

    #print(eval_nodes)

    max_node = ("",0)
    for k,v in eval_nodes.items():
        if v > max_node[1]:
            max_node = (k,v)

    print(max_node)

def part_2():
    import numpy
    class Node:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.label = ''

        def distance(self, x,y):
            return abs(x - self.x) + abs(y - self.y)

        def rate(self,x1,y1,x2,xy):
            d1 = self.distance(x1,y1)
            d2 = self.distance(x2,y2)
            return ((d2 * 1.0) - (d1 * 1.0))/1.0

    nodes = []
    padding = 1001
    with open("./day6_input.txt", "r") as file:
        for line in file:
            strNode = line.replace("\n","").split(", ")
            nodes.append(Node(int(strNode[0])+padding, int(strNode[1])+padding))

    map_edges = [0,0]

    for (idx, node) in enumerate(nodes):
        node.label = str(idx)
        if node.x > map_edges[0]:
            map_edges[0] = node.x
        if node.y > map_edges[1]:
            map_edges[1] = node.y

    map_edges = [map_edges[0] + padding, map_edges[1] + padding]

    map_edges = [int(map_edges[0] * 1), int(map_edges[1] * 1)]
    #print(map_edges)
    map = numpy.empty(shape=(map_edges[1],map_edges[0]), dtype=object)

    #print(nodes)

    for x in range(map_edges[0]):
        for y in range(map_edges[1]):
            node_sum = 0
            map[y,x] = ""
            for node in nodes:
                if (node.x == x) and (node.y == y):
                    map[y,x] += node.label
                node_sum += node.distance(x,y)
            if node_sum < 10000:
                map[y,x] += "#"
            elif node_sum >= 10000:
                map[y,x] += "."
            print(f"cord: {x},{y} sum: {node_sum}")
    print(map)

    lessthan = 0

    for x in range(map_edges[0]):
        for y in range(map_edges[1]):
            if "#" in map[y,x]:
                lessthan += 1

    print(lessthan)


#part_1()
part_2()
