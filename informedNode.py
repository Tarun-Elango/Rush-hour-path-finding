class informedNode:
    def __init__(self, board,  previous, move, level, fuel, heu):
        self.board = board # the board 
        self.previous = previous # parent oof this node
        self.move = move # move that got this node
        self.level = level # what level 0,1,2,....
        self.fuel = fuel # fuel associated with the board
        self.heu = heu # heuristic score for this node

    def setinfNode(board,  previous, move, level, fuel, heu):
        n = informedNode(board,  previous, move, level, fuel, heu)
        return n