class vehicle(object):
    def __init__(self, letter, posx, posy, length, orientation, fuel):
        self.letter = letter
        self.posx = posx
        self.posy = posy
        self.length = length
        self.orientation = orientation
        self.fuel = fuel


    def setVechicle(letter, posx, posy, length, orientation, fuel):
        v = vehicle(letter, posx, posy, length, orientation, fuel)
        return v