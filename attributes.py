class vehicle(object):
    def __init__(self, letter, posx, posy, length, orientation):
        self.letter = letter
        self.posx = posx
        self.posy = posy
        self.length = length
        self.orientation = orientation


    def setVechicle(letter, posx, posy, length, orientation):
        v = vehicle(letter, posx, posy, length, orientation)
        return v