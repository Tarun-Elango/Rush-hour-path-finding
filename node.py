class node:
    def __init__(self, board,  previous, move, level, fuel, cost):
        self.board = board # the board
        self.previous = previous # parent of the node
        self.move = move # move that got this node
        self.level = level # what level 0,1,2,....
        self.fuel = fuel # fuel associated with this node
        self.cost = cost # cost associated with this node

    def setNode(board,  previous, move, level, fuel, cost):
        n = node(board,  previous, move, level, fuel, cost)
        return n