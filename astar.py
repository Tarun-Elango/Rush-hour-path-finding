from vehicle import vehicle
from informedNode import informedNode
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
        fuel[remaining[check]]=int(remaining[check+1])
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
def defCar(board, unique):
    cars=[] #hold object os cars
    for i in unique:
        # id, posx, posy, length, ori, fuel
        id = i
        length = sum(length.count(f'{i}') for length in board)
        intermediary = a = [[0]*1]*1
        posx=[]
        posy=[]
        for k in range(6):
            for j in range(6):
                if (board[k][j] == f'{i}'):
                    posx.append(k)
                    posy.append(j)
        orient = orientation(board, i)
        obj = vehicle.setVechicle(i,posx, posy, length, orient)
        cars.append(obj)
    return cars # set of car objects

def computeMove(board, fuel, checkerList): #board has the current nodes board, fuel has the current nodes fuel, checkerList has all the nodes visited
    boards=[]#contains all the boards that have already been passed
    for i in checkerList:
        boards.append(i.board)
    boardList = [] 
    movelist = [] 
    fuelList= [] 
    carlist = defCar(board, unique) #this list has all the cars for the given board

    # give the board, get the car
    #consider boards visited, fuel
    #length 2
    #all left possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] >0  and i.orientation=='horizontal'):
            #for loop 1 to 4, check if for
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    if(j>1):
                        temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[0]][i.posy[0]] = '.'
                            temp[i.posx[0]][i.posy[0] - 1] = i.letter
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[3]][i.posy[3]] = '.'
                    if(j>1):
                        temp[i.posx[2]][i.posy[2]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==5) and (i.posy[0]-j)>=0 and (board[i.posx[0]][i.posy[0]-j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]][i.posy[0] - k] = i.letter
                    temp[i.posx[4]][i.posy[4]] = '.'
                    move =str(i.letter)+'l'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel)
                else:
                    check=True
                

    #all ritgh possible moves 
    for i in carlist:
        if(fuel[f'{i.letter}'] >0  and i.orientation=='horizontal'):
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posy[1]+j)<=5 and (board[i.posx[1]][i.posy[1]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[1]][i.posy[1] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posy[2]+j)<=5 and (board[i.posx[2]][i.posy[2]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[2]][i.posy[2] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[2]][i.posy[2]] = '.'
                            temp[i.posx[2]][i.posy[2] + 1] = i.letter
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posy[3]+j)<=5 and (board[i.posx[3]][i.posy[3]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[3]][i.posy[3] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel)
                elif((i.length==5) and (i.posy[4]+j)<=5 and (board[i.posx[4]][i.posy[4]+j]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[4]][i.posy[4] + k] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'r'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel)
                else:
                    check=True

    #all up possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] > 0  and i.orientation=='vertical'):
            check=False
            for j in range (1,5):
                if((i.length==2) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[1]][i.posy[1]] = '.'
                    if(j>1):
                        temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==3) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[2]][i.posy[2]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[0]][i.posy[0]] = '.'
                            temp[i.posx[0]-1][i.posy[0] ] = i.letter
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel)
                elif((i.length==4) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[3]][i.posy[3]] = '.'
                    if(j>1):
                        temp[i.posx[2]][i.posy[2]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==5) and(i.posx[0]-j)>=0 and (board[i.posx[0]-j][i.posy[0]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[0]-k][i.posy[0] ] = i.letter
                    temp[i.posx[4]][i.posy[4]] = '.'
                    move =str(i.letter)+'u'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                else:
                    check=True

    #all down possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] > 0  and i.orientation=='vertical'):
            check=False
            for j in range (1,5):
                if((i.length==2) and (i.posx[1]+j)<=5 and (board[i.posx[1]+j][i.posy[1]]=='.')  and check==False ):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[1]+k][i.posy[1] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==3) and (i.posx[2]+j)<=5 and (board[i.posx[2]+j][i.posy[2]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[2]+k][i.posy[2] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                        if(j>2):
                            temp[i.posx[2]][i.posy[2]] = '.'
                            temp[i.posx[2]+1][i.posy[2]] = i.letter
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==4) and (i.posx[3]+j)<=5 and (board[i.posx[3]+j][i.posy[3]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[3]+k][i.posy[3] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    if(j>1):
                        temp[i.posx[1]][i.posy[1]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                elif((i.length==5) and (i.posx[4]+j)<=5 and (board[i.posx[4]+j][i.posy[4]]=='.')  and check==False):
                    temp = copy.deepcopy(board)
                    for k in range(j-1,j+1):
                        temp[i.posx[4]+k][i.posy[4] ] = i.letter
                    temp[i.posx[0]][i.posy[0]] = '.'
                    move =str(i.letter)+'d'+str(j)
                    tempFuel = copy.deepcopy(fuel)
                    fl = int(tempFuel[f'{i.letter}']-j)
                    tempFuel[f'{i.letter}'] = fl 
                    #add the moves, fuel, board for each different moves
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                else:
                    check=True

    return boardList, fuelList, movelist

def h2(board): # returns the number of alphabets blocking A to the right 
    score = 0
    posy= None
    for i in range(0,6):
        if (board[2][i]=='A'):
            posy=i
    for i in range(0,6):
        if(i>posy and board[2][i]!='.' and board[2][i]!='A'):
            score = score + 1
    return score

def h1(board):
    #returns the number of vehicles blocking A to the right 1,2,3
    #blocking vehicles, check row 3, how many car elements present in the row to 'A''s right
    score = []
    posy= None
    for i in range(0,6):
        if (board[2][i]=='A'):
            posy=i
    for i in range(0,6):
        if(i>posy and board[2][i]!='.' and board[2][i]!='A'):
            score.append(board[2][i])
    return len(set(score))

def h3(board):
    #returns the number of vehicles blocking A to the right 1,2,3
    #blocking vehicles, check row 3, how many car elements present in the row to 'A''s right
    score = []
    posy= None
    for i in range(0,6):
        if (board[2][i]=='A'):
            posy=i
    for i in range(0,6):
        if(i>posy and board[2][i]!='.' and board[2][i]!='A'):
            score.append(board[2][i])
    return len(set(score))*5

def h4(board):#combination of how far A is away from [2][5], vehciles blocking a
    veh = []
    posy= None
    for i in range(0,6):
        if (board[2][i]=='A'):
            posy=i
    for i in range(0,6):
        if(i>posy and board[2][i]!='.' and board[2][i]!='A'):
            veh.append(board[2][i])
    # A's pos from end
    posFromEnd = 5-posy
    return len(set(veh))*5 + posFromEnd

def valet(board):
    veh = None
    if(board[2][5]!='.' and board[2][4]!='.' and board[2][5]!='A' and board[2][4]!='A'):
        if(board[2][5]==board[2][4]):
            veh = board[2][5]
            #replace 5 and 4 with .
            board[2][5]='.'
            board[2][4]='.'
            unique.remove(veh)
            if(board[2][3]==veh):
                #replace 3 with . 
                board[2][3] = '.'
            if(board[2][2]==veh):
                #replace 3 with . 
                board[2][2] = '.'
    return board

def nextNode(presentNodeValue, checkerList):
    boards, fuels, moves = computeMove(presentNodeValue.board, presentNodeValue.fuel, checkerList)
    newNodes=[]
    # create nodes with the new boards
    for i in range(len(boards)):
        valetBoard = valet(boards[i])
        obj = informedNode.setinfNode(valetBoard, presentNodeValue, moves[i], int(presentNodeValue.level)+1, fuels[i], h4(boards[i])+ int(presentNodeValue.level)+1 )# heu = heu + (g)level
        newNodes.append(obj)

    return newNodes


def astar(startBoard, fuel):
    iniValetBoard= valet(startBoard)
    initial = informedNode.setinfNode(iniValetBoard, None, 'None', 0, fuel,h4(startBoard)) # initial heuristic is just the heuristic cost, as g =0
    solpath=[] 
    checkerList=[]
    closedList=[]
    count =1
    solpath.append(initial) # equivalent to open list, i.e. the next node to expand is from this list
    checkerList.append(initial) #equivalent to closed list, has all the list that have been visited
    present = solpath.pop(0) 
    closedList.append(present)
    while(present.board[2][5] != 'A' ) :
        ########################################add condition inside computeMoves to break once [2][5]==A
        next_nodes = nextNode(present, checkerList)
        for i in next_nodes:    
            solpath.append(i)
            checkerList.append(i)
            count = count+1 
        if(len(solpath)==0):
            break
        else:
            #pop the smallest heu, therefore keeps the order when heu are same, without mixing 
            solpath.sort(key=lambda x: x.heu, reverse=False)
            present = solpath.pop(0)  
            closedList.append(present)
    searchMoves = []
    searchPath = []

    while(present.previous!=None):
        searchMoves.append(present.move)
        searchPath.append(present.board)
        present = present.previous

    return searchMoves, closedList, searchPath, checkerList

searchPathMoves, closedList, searchPath, allStates = astar(board, fuel)
stop = time.time()

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




def solPathMoves(searchPathMoves,searchPath):
    for i in reversed(range(len(searchPath))):
        print('{}  {}'.format(searchPathMoves[i][0]+' '+parseMove(searchPathMoves[i][1])+' '+searchPathMoves[i][2]+' ',''.join(map(str,[ i for j in searchPath[i] for i in j]))))

    final = searchPath[0]
    for i in range(6):
        for j in range(6):
                print(final[i][j], end=" ")
        print('')



if(searchPath[0][2][5]!='A'):
    print('no solution')
else:
    print('solution path ', solMoveString(searchPathMoves))
    print('execution time ',stop-start,' seconds')
    print('search path length',len(closedList), ' states')
    print('solution path length', len(searchPathMoves), ' moves')
    solPathMoves(searchPathMoves, searchPath)


