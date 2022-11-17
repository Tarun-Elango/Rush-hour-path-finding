class node:
    def __init__(self, board,  previous, move, level, cost, fuel):
        self.board = board # the state of this node
        self.previous = previous # parent or non
        self.move = move #move that got this node
        self.level = level # what level 0,1,2,....
        self.cost = cost
        self.fuel = fuel

    def setNode(s,c, p, m, d, f):
        n = node(s,c, p, m, d, f)
        return n