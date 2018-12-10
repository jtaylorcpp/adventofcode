def part_1():
    class Node:
        def __init__(self, nnodes, nmeta):
            self.nnodes = nnodes
            self.nmeta = nmeta
            self.nodes = []
            self.meta = []

        def nprint(self, ind=0):
            print("\t"*ind, f"node:")
            print("\t"*ind ,"\tsub nodes: ")
            for node in self.nodes:
                node.nprint(ind + 1)
            print("\t"*ind, "\tmeta:")
            for meta in self.meta:
                print("\t"*ind, "\t\t", meta)

        def sum_meta(self):
            meta_sum = sum([int(x) for x in self.meta])
            for node in self.nodes:
                meta_sum += node.sum_meta()
            return meta_sum

        def value(self):
            if self.nodes:
                value = 0
                for elem in self.meta:
                    idx = int(elem) - 1
                    if (idx >= 0) and (idx < len(self.nodes)):
                        value += self.nodes[idx].value()
                return value
            else:
                return sum([int(x) for x in self.meta])

    def parse_nodes(node_ls):
        new_node = Node(int(node_ls[0]), int(node_ls[1]))
        new_ls = node_ls[2:]
        for n in range(new_node.nnodes):
            node, new_ls = parse_nodes(new_ls)
            new_node.nodes.append(node)
        for n in range(new_node.nmeta):
            new_node.meta.append(new_ls[0])
            new_ls = new_ls[1:]
        return new_node, new_ls

    node_str = ""
    with open("./day8_input.txt", "r") as file:
        for line in file:
            node_str += line

    node_str = node_str.replace("\n", " ")
    node_str = node_str.replace("  ", " ")
    print(node_str)
    node, left = parse_nodes(node_str.split(" "))
    node.nprint()
    print(node.sum_meta())

    print(node.value())


part_1()
