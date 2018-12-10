def part_1():
    game_board = []
    score_board = {}
    max_marble = 1618
    players = 10
    current_marble = 0

    with open("./day9_input.txt", "r") as file:
        for line in file:
            words = line.split(" ")
            players = int(words[0])
            max_marble = int(words[6])

    for player in range(players):
        score_board[player] = []

    for marble in range(max_marble + 1):
        if marble == 0:
            game_board.append(0)

        elif marble % 23 == 0:
            #print("23!!!")
            score_board[marble%players].append(marble)
            remove_idx = current_marble - 7
            while remove_idx < 0:
                remove_idx += len(game_board)
            current_marble = remove_idx
            score_board[marble%players].append(game_board.pop(current_marble))
            #print(marble, current_marble, marble%players, score_board[marble%players])

        else:
            insert_idx = current_marble + 2
            while insert_idx > len(game_board):
                insert_idx -= len(game_board)
            current_marble = insert_idx
            game_board.insert(insert_idx, marble)

            #print((marble, current_marble, marble%players), game_board)

    winner = ("", 0)
    for player, val in score_board.items():
        if sum(val) > winner[1]:
            winner = (player, sum(val))
    print(winner)


def part_2():

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None


        def insert_after(self, node):
            if (self.next == None) and (self.prev == None):
                self.next, self.prev = node, node
                node.next, node.prev = self, self
            else:
                self.next.prev = node
                node.next = self.next
                self.next = node
                node.prev = self



        def remove(self):
            next = self.next
            self.next.prev = self.prev
            self.prev.next = self.next
            return self.val, next

        def printdll(self):
            node = self.next
            nodestr = str(self.val)
            while node.val != self.val:
                nodestr += f" {node.val}"
                node = node.next
            print(nodestr)

        def printr(self):
            node = self.prev
            nodestr = str(self.val)
            while node.val != self.val:
                #print(f"reverse, node {node.val}, next {node.next.val}, prev {node.prev.val}")
                nodestr += f" {node.val}"
                node = node.prev
            print("reverse: ",nodestr)

    marble_node = None
    score_board = {}
    max_marble = 25
    players = 9
    current_marble = 0

    with open("./day9_input.txt", "r") as file:
        for line in file:
            words = line.split(" ")
            players = int(words[0])
            max_marble = int(words[6]) * 100

    for player in range(players):
        score_board[player] = []

    for marble in range(max_marble + 1):
        if marble == 0:
            marble_node = Node(0)
        elif (marble % 23) == 0:
            #print("23!!!")
            score_board[marble % players].append(marble)
            for i in range(7):
                #print("rewind: ", marble_node.val)
                marble_node = marble_node.prev
            score, marble_node = marble_node.remove()
            score_board[marble % players].append(score)
            #marble_node.printdll()

        elif marble == 1:
            marble_node.insert_after(Node(marble))
            marble_node = marble_node.next
            #marble_node.printdll()
            #marble_node.printr()
        else:
            marble_node = marble_node.next
            marble_node.insert_after(Node(marble))
            marble_node = marble_node.next
            #marble_node.printdll()
            #marble_node.printr()


    winner = ("", 0)
    for player, val in score_board.items():
        if sum(val) > winner[1]:
            winner = (player, sum(val))
    print(winner)

part_2()
