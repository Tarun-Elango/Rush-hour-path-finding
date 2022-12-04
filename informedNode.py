#node class for GBFS and A
class informedNode:
    def __init__(self, board,  previous, move, level, fuel, heu):
        self.board = board # the board 
        self.previous = previous # parent oof this node
        self.move = move # move that got this node
        self.level = level # what level 0,1,2,....
        self.fuel = fuel # fuel associated with the board
        self.heu = heu # h(n) for GBFS, and h(n) + g(n) for A

    def setinfNode(board,  previous, move, level, fuel, heu):
        n = informedNode(board,  previous, move, level, fuel, heu)
        return n