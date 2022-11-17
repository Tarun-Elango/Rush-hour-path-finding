from attributes import vehicle
from node import node
import copy
import time

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


arrayPuzzle = readInput('input')
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

unique= sorted(set(arrayPuzzle[int(puzzleNumber)-1][0:36]))
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



print(f'initial puzzle is {arrayPuzzle[int(puzzleNumber)-1]}')
printPuzzle(arrayPuzzle[int(puzzleNumber)-1][0:36])
print('car fuel available ',fuel)
start = time.time()
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

# to get all possible moves
# go through the cars object list
def computeMoves(board,fuel):
    move = None
    values ={}
    cars = defCar(board, unique, fuel)
    for i in cars:
        if i.orientation == 'horizontal':
            if(i.length == 2):
                if((i.posy[0]-1) >=0 and (board[i.posx[0]][i.posy[0]-1]=='.')):
                    # swap board(x[0]y[0-1]) with i  and swap board(x[1]y[1] with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0]][i.posy[0] - 1] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'l'+str(1)
                    values[move]=temp
                if((i.posy[0]-2) >=0 and (board[i.posx[0]][i.posy[0]-2]=='.') and (board[i.posx[0]][i.posy[0]-1]=='.')):
                    #swap board(x[0]y[0-2] with i, board(x[0]y[0-1] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0]][i.posy[0] - 2] = i.letter
                    temp[i.posx[0]][i.posy[0] - 1] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'l' + str(2)
                    values[move] = temp
                if ((i.posy[0] - 3) >= 0 and (board[i.posx[0]][i.posy[0] - 3] == '.')and (board[i.posx[0]][i.posy[0]-2]=='.') and (board[i.posx[0]][i.posy[0]-1]=='.')):
                    #swap  board(x[0]y[0-3] with i board(x[0]y[0-2] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0]][i.posy[0] - 2] = i.letter
                    temp[i.posx[0]][i.posy[0] - 3] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'l' + str(3)
                    values[move] = temp
                if ((i.posy[0] - 4) >= 0 and (board[i.posx[0]][i.posy[0] - 4] == '.')and (board[i.posx[0]][i.posy[0] - 3] == '.')and (board[i.posx[0]][i.posy[0]-2]=='.') and (board[i.posx[0]][i.posy[0]-1]=='.')):
                    #swap  board(x[0]y[0-4] with i board(x[0]y[0-3] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0]][i.posy[0] - 4] = i.letter
                    temp[i.posx[0]][i.posy[0] - 3] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'l' + str(4)
                    values[move] = temp
                if((i.posy[1]+1) <=5 and (board[i.posx[1]][i.posy[1]+1]=='.')):
                    #swap board(x[0]y[0=1]) with i  and swap board(x[0]y[0] with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[1]][i.posy[1] + 1] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move = str(i.letter)+'r' + str(1)
                    values[move] = temp
                if((i.posy[1]+2) <=5 and (board[i.posx[1]][i.posy[1]+2] == '.') and (board[i.posx[1]][i.posy[1]+1]=='.')):
                    #swap board(x[0]y[0+2] with i, board(x[0]y[0=1] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[1]][i.posy[1] + 2] = i.letter
                    temp[i.posx[1]][i.posy[1] + 1] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'r' + str(2)
                    values[move] = temp
                if ((i.posy[1] + 3) <= 5 and (board[i.posx[1]][i.posy[1] + 3] == '.')and (board[i.posx[1]][i.posy[1]+2] == '.') and (board[i.posx[1]][i.posy[1]+1]=='.')):
                    #swap  board(x[0]y[0+3] with i board(x[0]y[0+2] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[1]][i.posy[1] + 2] = i.letter
                    temp[i.posx[1]][i.posy[1] + 3] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'r' + str(3)
                    values[move] = temp
                if ((i.posy[1] + 4) <= 5 and (board[i.posx[1]][i.posy[1] + 4] == '.')and (board[i.posx[1]][i.posy[1] + 3] == '.')and (board[i.posx[1]][i.posy[1]+2] == '.') and (board[i.posx[1]][i.posy[1]+1]=='.')):
                    #swap  board(x[0]y[0+4] with i board(x[0]y[0+3] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[1]][i.posy[1] + 4] = i.letter
                    temp[i.posx[1]][i.posy[1] + 3] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'r' + str(4)
                    values[move] = temp
            if(i.length==3):
                if ((i.posy[0] - 1) >= 0 and (board[i.posx[0] ][i.posy[0]-1] == '.')):
                    # swap board(x[0]y[0-1]) with i  and swap board(x[2]y[2] with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0]][i.posy[0] - 1] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    move = str(i.letter)+'l' + str(1)+str(3)
                    values[move] = temp
                if ((i.posy[0] - 2) >= 0 and (board[i.posx[0] ][i.posy[0]-2] == '.')and (board[i.posx[0] ][i.posy[0]-1] == '.')):
                    #swap board(x[0]y[0-2] with i, board(x[0]y[0-1] with i, x1y1 with'.' and x2y2 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0]][i.posy[0] -2] = i.letter
                    temp[i.posx[0]][i.posy[0] - 1] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[2]][i.posy[2]] = '.'
                    move = str(i.letter)+'l' + str(2)+str(3)
                    values[move] =temp
                if ((i.posy[0] - 3) >= 0 and (board[i.posx[0] ][i.posy[0]-3] == '.')and (board[i.posx[0] ][i.posy[0]-2] == '.')and (board[i.posx[0] ][i.posy[0]-1] == '.')):
                    #swap  board(x[0]y[0-3] with i board(x[0]y[0-2] with i board(x[0]y[0-1] with i, x0y0 with'.' and x1y1 with '.' x2y2 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0]][i.posy[0] - 3] = i.letter
                    temp[i.posx[0]][i.posy[0] - 2] = i.letter
                    temp[i.posx[0]][i.posy[0] - 1] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[2]][i.posy[2]] = '.'
                    move = str(i.letter)+'l' + str(3)+str(3)
                    values[move] = temp
                if ((i.posy[2] + 1) <=5 and (board[i.posx[2] ][i.posy[2]+1] == '.')):
                    # swap board(x[0]y[0+1]) with i  and swap board(x[0]y[0] with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[2]][i.posy[2] + 1] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move = str(i.letter)+'r' + str(1)+str(3)
                    values[move] = temp
                if ((i.posy[2] + 2) <=5 and (board[i.posx[2] ][i.posy[2]+2] == '.')and (board[i.posx[1] ][i.posy[1]+1] == '.')):
                    #swap board(x[0]y[0+2] with i, board(x[0]y[0+1] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[2]][i.posy[2] + 2] = i.letter
                    temp[i.posx[2]][i.posy[2] + 1] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'r' + str(2)+str(3)
                    values[move] = temp
                if ((i.posy[2] + 3) <=5 and (board[i.posx[2] ][i.posy[2]+3] == '.')and (board[i.posx[1] ][i.posy[1]+2] == '.')and (board[i.posx[1] ][i.posy[1]+1] == '.')):
                    #swap  board(x[0]y[0+3] with i board(x[0]y[0+2] with i board(x[0]y[0+1] with i, x0y0 with'.' and x1y1 with '.' x2y2 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[2]][i.posy[2] + 3] = i.letter
                    temp[i.posx[2]][i.posy[2] + 2] = i.letter
                    temp[i.posx[2]][i.posy[2] + 1] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[2]][i.posy[2]] = '.'
                    move = str(i.letter)+'r' + str(3)+str(3)
                    values[move] = temp
        else:
            if (i.length == 2):
                if ((i.posx[0] - 1) >= 0 and (board[i.posx[0]-1][i.posy[0] ] == '.')):
                    # swap board(x[0-1]y[0]) with i  and swap board(x[1]y[1] with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0]-1][i.posy[0]] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'u' + str(1)
                    values[move] = temp
                if ((i.posx[0] - 2) >= 0 and (board[i.posx[0]-2][i.posy[0]] == '.')and (board[i.posx[0]-1][i.posy[0] ] == '.')):
                    #swap board(x[0-2]y[0] with i, board(x[0-1]y[0] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0] - 2][i.posy[0]] = i.letter
                    temp[i.posx[0] - 1][i.posy[0]] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move = str(i.letter)+'u' + str(2)
                    values[move] = temp
                if ((i.posx[0] - 3) >= 0 and (board[i.posx[0]-3][i.posy[0] ] == '.')and (board[i.posx[0]-2][i.posy[0]] == '.')and (board[i.posx[0]-1][i.posy[0] ] == '.')):
                    #swap  board(x[0-3]y[0] with i board(x[0-2]y[0] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0] - 2][i.posy[0]] = i.letter
                    temp[i.posx[0] - 3][i.posy[0]] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move = str(i.letter)+'u' + str(3)
                    values[move] = temp
                if ((i.posx[0] - 4) >= 0 and (board[i.posx[0]-4][i.posy[0] ] == '.')and (board[i.posx[0]-3][i.posy[0] ] == '.')and (board[i.posx[0]-2][i.posy[0]] == '.')and (board[i.posx[0]-1][i.posy[0] ] == '.')):
                    #swap  board(x[0-4]y[0] with i board(x[0-3]y[0] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0] - 4][i.posy[0]] = i.letter
                    temp[i.posx[0] - 3][i.posy[0]] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move = str(i.letter)+'u' + str(2)
                    values[move] =temp
                if ((i.posx[1] + 1) <= 5 and (board[i.posx[1]+1][i.posy[1] ] == '.')):
                    ##swap board(x[0+1]y[0]) with i  and swap board(x[0]y[0] with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[1] + 1][i.posy[1]] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move = str(i.letter)+'d' + str(1)
                    values[move] = temp
                if ((i.posx[1] + 2) <= 5 and (board[i.posx[1]+2][i.posy[1] ] == '.')and (board[i.posx[1]+1][i.posy[1] ] == '.')):
                    # swap board(x[0+2]y[0] with i, board(x[0]y[0+1] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[1] + 2][i.posy[1]] = i.letter
                    temp[i.posx[1] + 1][i.posy[1]] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'d' + str(2)
                    values[move] = temp
                if ((i.posx[1] + 3) <= 5 and (board[i.posx[1]+3][i.posy[1] ] == '.')and (board[i.posx[1]+2][i.posy[1] ] == '.')and (board[i.posx[1]+1][i.posy[1] ] == '.')):
                    #swap  board(x[0+3]y[0] with i board(x[0+2]y[0] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[1] + 2][i.posy[1]] = i.letter
                    temp[i.posx[1] + 3][i.posy[1]] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'d' + str(3)
                    values[move] = temp
                if ((i.posx[1] + 4) <= 5 and (board[i.posx[1]+4][i.posy[1] ] == '.')and (board[i.posx[1]+3][i.posy[1] ] == '.')and (board[i.posx[1]+2][i.posy[1] ] == '.')and (board[i.posx[1]+1][i.posy[1] ] == '.')):
                    # swap  board(x[0+4]y[0] with i board(x[0+3]y[0] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[1] + 4][i.posy[1]] = i.letter
                    temp[i.posx[1] + 3][i.posy[1]] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'d' + str(4)
                    values[move] = temp
            if (i.length == 3):
                if ((i.posx[0] - 1) >= 0 and (board[i.posx[0]-1][i.posy[0]] == '.')):
                    # swap board(x[0-1]y[0]) with i  and swap board(x[2]y[2] with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0] - 1][i.posy[0]] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    move =str(i.letter)+ 'u' + str(1)+str(3)
                    values[move] = temp
                if ((i.posx[0] - 2) >= 0 and (board[i.posx[0]-2][i.posy[0] ] == '.')and (board[i.posx[0]-1][i.posy[0]] == '.')):
                    #swap board(x[0-2]y[0] with i, board(x[0-1]y[0] with i, x1y1 with'.' and x2y2 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0] - 2][i.posy[0]] = i.letter
                    temp[i.posx[0] - 1][i.posy[0]] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[2]][i.posy[2]] = '.'
                    move = str(i.letter)+'u' + str(2)+str(3)
                    values[move] = temp
                if ((i.posx[0] - 3) >= 0 and (board[i.posx[0]-3][i.posy[0] ] == '.')and (board[i.posx[0]-2][i.posy[0] ] == '.')and (board[i.posx[0]-1][i.posy[0]] == '.')):
                    # swap  board(x[0-3]y[0] with i board(x[0-2]y[0] with i board(x[0-1]y[0] with i, x0y0 with'.' and x1y1 with '.' x2y2 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[0] - 1][i.posy[0]] = i.letter
                    temp[i.posx[0] - 2][i.posy[0]] = i.letter
                    temp[i.posx[0] - 3][i.posy[0]] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move = str(i.letter)+'u' + str(3)+str(3)
                    values[move] = temp
                if ((i.posx[2] + 1) <=5 and (board[i.posx[2]+1][i.posy[2] ] == '.')):
                    # swap board(x[2+1]y[0]) with i  and swap board(x[0]y[0] with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[2] + 1][i.posy[2]] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move = str(i.letter)+'d' + str(1)+str(3)
                    values[move] = temp
                if ((i.posx[2] + 2) <=5 and (board[i.posx[2]+2][i.posy[2] ] == '.')and (board[i.posx[2]+1][i.posy[2] ] == '.')):
                    #swap board(x[2+2]y[0] with i, board(x[2+1]y[0] with i, x0y0 with'.' and x1y1 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[2] + 1][i.posy[2]] = i.letter
                    temp[i.posx[2] + 2][i.posy[2]] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    move = str(i.letter)+'d' + str(2)+str(3)
                    values[move] = temp
                if ((i.posx[2] + 3) <=5 and (board[i.posx[2]+3][i.posy[2] ] == '.')and (board[i.posx[2]+2][i.posy[2] ] == '.')and (board[i.posx[2]+1][i.posy[2] ] == '.')):
                    #swap  board(x[2+3]y[0] with i board(x[2+2]y[0] with i board(x[2+1]y[0] with i, x0y0 with'.' and x1y1 with '.' x2y2 with '.'
                    temp = copy.deepcopy(board)
                    temp[i.posx[2] + 1][i.posy[2]] = i.letter
                    temp[i.posx[2] + 2][i.posy[2]] = i.letter
                    temp[i.posx[2] + 3][i.posy[2]] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    temp[i.posx[1]][i.posy[1]] = '.'
                    temp[i.posx[2]][i.posy[2]] = '.'
                    move =str(i.letter)+ 'd' + str(3)+str(3)
                    values[move] = temp
    return values



def nextNode(nodeValue):
    newBoards = computeMoves(nodeValue.board, nodeValue.fuel)
    newNodes=[]
    keys = []#stores all the moves
    value = []# stores all the boards
    for i in newBoards:
        keys.append(i)
        value.append(newBoards[i])
    # create nodes with the new boards
    for i in range(len(newBoards)):
        obj = node.setNode(value[i], nodeValue, keys[i][0:3], int(nodeValue.level + 1), int(keys[i][2]), nodeValue.fuel)
        newNodes.append(obj)

    return newNodes


def ucs(startBoard, fuel):
    initial = node.setNode(startBoard, None, 'None', 0, 0, fuel) #previ, move, level, cost
    solpath=[]
    searchMoves=[]
    searchPath=[]
    count =1
    solpath.append(initial)
    present =  solpath.pop(0)
    while(present.board[2][5] != 'A' ) :
        next_nodes = nextNode(present)
        for i in next_nodes:
            solpath.append(i)
            count = count+1
        solpath.sort(key=lambda x: x.level)
        present = solpath.pop(0)

    while(present.previous!=None):
        searchMoves.append(present.move)
        searchPath.append(present.board)
        present = present.previous

    return searchMoves, count, searchPath


stop = time.time()
searchPathMoves, statecount, searchPath= ucs(board, fuel)
print('execution time ',stop-start,' seconds')
print('search path length',statecount, ' states')
print('solution path length', len(searchPathMoves), ' moves')

def parseMove(string):
    if string == 'u':
        return '   up'
    if string == 'd':
        return ' down'
    if string == 'l':
        return ' left'
    if string == 'r':
        return 'right'

def solMoveString(searchPathMoves):
    solutionPathString=''
    for i in reversed(searchPathMoves):
        solutionPathString = solutionPathString + i[0]+' '+parseMove(i[1])+' '+i[2]+' ; '
    return solutionPathString


print('solution path ', solMoveString(searchPathMoves))

def solPathMoves(searchPathMoves,searchPath):
    moves = searchPathMoves


    for i in reversed(range(len(searchPath))):
        print('{}  {}'.format(searchPathMoves[i][0]+' '+parseMove(searchPathMoves[i][1])+' '+searchPathMoves[i][2]+' ',''.join(map(str,[ i for j in searchPath[i] for i in j]))))

    final = searchPath[0]
    for i in range(6):
        for j in range(6):
                print(final[i][j], end=" ")
        print('')


solPathMoves(searchPathMoves, searchPath)
