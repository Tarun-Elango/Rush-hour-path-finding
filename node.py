class node(object):
    def __init__(self, board, previous, move, level, cost):
        self.state = board # the state of this node
        self.parent = previous # parent or non
        self.operator = move #move that got this node
        self.level = level # what level 0,1,2,....
        self.cost = cost

    def setNode(s, p, m, d, f):
        n = node(s, p, m, d, f)
        return n