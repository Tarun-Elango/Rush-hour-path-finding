from attributes import vehicle

# read input file and store data into data structure
def readInput(input):
    valuesArray = []
    f = open(f"{input}.txt", 'r')
    for i in f.read().splitlines():
            valuesArray.append(i)

    newArray=[]
    for j in range(len(valuesArray)):
        if(valuesArray[j]=='' or valuesArray[j].startswith('#')):
            continue
        else:
            newArray.append(valuesArray[j])

    return newArray


arrayPuzzle = readInput('sample-input')
size = len(arrayPuzzle)

print('number of puzzles ',size)
check = False
while(check==False):
    puzzleNumber = input(f'choose puzzle number between 1 and {size} :')
    if (int(puzzleNumber) > int(size) or int(puzzleNumber) < 1):
        print('wrong input')
    else:
        check=True

# puzzleumber has user desired puzzle
#store array into desired data structure with other details for each puzzle
#one array 6x6 to store matrix, one array 1D to store data

unique= list(set(arrayPuzzle[int(puzzleNumber)-1][0:36]))
if '.' in unique: unique.remove('.')
fuel={}
for j in range(len(unique)):
    fuel[unique[j]]=100

remaining = arrayPuzzle[int(puzzleNumber)-1][36:len(arrayPuzzle[int(puzzleNumber)-1])].replace(' ','')
#print((remaining))
if(len(arrayPuzzle[int(puzzleNumber)-1])>36):  #integer value should be until the end of file, or before another english.(we remove space)
    check= 0
    while(check<=len(remaining)/2):
        fuel[remaining[check]]=remaining[check+1]
        check = check+2



def printPuzzle(array):
    for i in range(0,len(array)):
        if(i%6==5):
            print(array[i])
        else:
            print(array[i], end =" "),



print('initial puzzle is \n')
printPuzzle(arrayPuzzle[int(puzzleNumber)-1][0:36])
print('intial fuel of each vehicle ',fuel)

#create a matrix of the given board
def boardMatrix(input):
    board = [[0]*6 for i in range(6)]
    i=0
    j=0
    k=0
    for q in range(0, len(input)):
        board[i][j] = input[q]
        j = j + 1
        if (q % 6 == 5):
            i = i + 1
            j=0

    return board


def orientation(board,i):
    lt =[]
    for k in range(6):
        for j in range(6):
            if (board[k][j] == f'{i}'):
                lt.append(k)
                lt.append(j)

    if (lt[0] != lt[2]):
        return 'vertical'
    else:
        return 'horizontal'

# following has the board
board = boardMatrix(arrayPuzzle[int(puzzleNumber)-1][0:36])
print(board)
#get all the car atrributes
def defCar(board, unique, fuel):
    cars=[] #hold object os cars
    for i in unique:
        # id, posx, posy, length, ori, fuel
        id = i
        length = sum(length.count(f'{i}') for length in board)
        gas = fuel[f'{i}']
        intermediary = a = [[0]*1]*1
        posx=[]
        posy=[]
        for k in range(6):
            for j in range(6):
                if (board[k][j] == f'{i}'):
                    posx.append(k)
                    posy.append(j)
        orient = orientation(board, i)
        obj = vehicle.setVechicle(i,posx, posy, length, orient, gas)
        cars.append(obj)
    return cars # set of car objects

cars = defCar(board, unique, fuel)
# remeber posx has all the x values of the cars. posy has all the y values of the car, cars[0].posx[0] and cars[0].posy[0]
# has the index of the first occurence of the car.


def setNode(s, p, m, d, f):
    return node(s, p, m, d, f)

class node:
    def __init__(self, state, previous, move, level, cost):
        self.state = state # the state of this node
        self.parent = previous # parent or non
        self.operator = move #move that got this node
        self.level = level # what level 0,1,2,....
        self.cost = cost




def nextNode(stateArray):
    nextLevel =[]
    # all moves up, down, right, left, add to nextLevel as new point
    #ups = checkUps(stateArray)
    return nextLevel


def ucs(start, fuel):
    # take start state, find all possible new states
    # done by checking all possible moves in entire board
    # take all those moves one by one, each state, find all other new possible moves (keep track of visited nodes)
    # keep doing till AA reaches 3,6 (matrix) or
    inital = setNode(list(arrayPuzzle[int(puzzleNumber) - 1][0:36]), None, None, 0, fuel)
    sol=[]
    searPath=[]
    sol.append(inital)
    present =  sol.pop(0)
    while(inital.state[17] != 'A' and inital.state[16] != 'A') :
        next_nodes = nextNode(present) #need a fucntion to get a list of next level nodes
        for i in next_nodes:
            i.level = inital.level+i.level
            sol.append(i)
        sol.sort(key=lambda x: x.level)
        present = sol.pop(0)

    while(present.previous!=None):
        searPath.append(present.move)
        present = present.previous

    return searPath

