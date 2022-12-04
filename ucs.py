from vehicle import vehicle
from node import node
import copy
import time
import json
import os.path

# read input file and store data into data structure
def readInput(input):# has arrays of puzzle
    valuesArray = []
    folder = './Input'
    name = f"{input}.txt"
    path = os.path.join(folder, name)
    f = open(path,"r")
    for i in f.read().splitlines():
            valuesArray.append(i)

    newArray=[]
    for j in range(len(valuesArray)):
        if(valuesArray[j]=='' or valuesArray[j].startswith('#')):
            continue
        else:
            newArray.append(valuesArray[j])

    return newArray

#pretty print puzzle
def printPuzzle(array):
    for i in range(0,len(array)):
        if(i%6==5):
            print(array[i])
        else:
            print(array[i], end =" "),

def printPuzzleTextFile(array, text):
        for i in range(0,len(array)):
            if(i%6==5):
                text.write(array[i])
                text.write('\n')
            else:
                text.write(array[i])
                text.write('')

#create a matrix of the given board
def getBoardMatrix(input):
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

# find orientation of board
def getCarOrientation(board,i):
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

#get all the car atrributes
def defineCar(board, unique):
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
        orient = getCarOrientation(board, i)
        obj = vehicle.setVechicle(i,posx, posy, length, orient)
        cars.append(obj)
    return cars # set of car objects

#compute all possible moves for a given board
def computeMoves(board, fuel, checkerList,unique): 
    boards=[]#contains all the boards that have already been passed
    for i in checkerList: 
        boards.append(i.board) # needed to check for repeat nodes
    boardList = [] 
    movelist = [] 
    fuelList= [] 
    carlist = defineCar(board, unique) 

    #all left possible moves 
    for i in carlist:
        if( fuel[f'{i.letter}'] >0  and i.orientation=='horizontal'):
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
                    if(temp in boards)==False:
                        boardList.append(temp)
                        movelist.append(move)
                        fuelList.append(tempFuel) 
                else:
                    check=True

    return boardList, fuelList, movelist

# remove any vehicle at the exit
def valetService(board, unique):
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

#get the children node for a given node
def getNextNodes(presentNodeValue, checkerList, unique):
    boards, fuels, moves = computeMoves(presentNodeValue.board, presentNodeValue.fuel, checkerList, unique)
    newNodes=[]
    # create the children nodes with the respective attributes
    for i in range(len(boards)):
        valetBoard = valetService(boards[i],unique)
        obj = node.setNode(valetBoard, presentNodeValue, moves[i], int(presentNodeValue.level)+1, fuels[i], int(presentNodeValue.cost)+1)
        newNodes.append(obj)

    return newNodes

# ucs algorithm 
def ucs(startBoard, fuel, unique):
    initial = node.setNode(valetService(startBoard, unique), None, 'None', 0, fuel,0) # create the inital node
      
    openList=[] # the list with nodes, that have found but haven't explored( to check for goal, or to check if children exist)
    checkerList=[] # list that contains all open + close list at any point in time.
    closedList=[] # this list contains only the nodes, that have been visited

    openList.append(initial) # push inital node to open list
    checkerList.append(initial) # push inital node to open list

    present = openList.pop(0) # pop out the first node from open list to explore
    closedList.append(present)  # add it to closed list, as it will surely be explored

    while(present.board[2][5] != 'A' ) :  
        next_nodes = getNextNodes(present, checkerList, unique) # get all children for the current node
        for i in next_nodes:   
            openList.append(i) # add all children to open list. any children already present in closed or open list will be ignored (as the cost of node visited first will always be less,
            # because each move irrespective of distance move will be of cost 1)
            checkerList.append(i) # this list keeps track of closed + open list, such that the next node visited/childer generated will be compared with this to ignore duplicates
        
        if(len(openList)==0): # at this stage if the openlist is empty, i.e all possible nodes have been visited, then break
            break
        else:
            openList.sort(key=lambda x: x.cost, reverse=False) #order of the open list is chosen to be ascending lowest cost to highest
            present = openList.pop(0)  # remove the first node from open list for next iteration 
            closedList.append(present) # add all the eplored nodes to 

    
    searchMoves = [] # trace back the moves from goal to intial 
    searchPath = [] # trace back boards from goal to intial 
    while(present.previous!=None):
        searchMoves.append(present.move)
        searchPath.append(present.board)
        present = present.previous

    return searchMoves, searchPath, checkerList, closedList

# sub function to pretty print moves
def parseMove(string):
    if string == 'u':
        return '   up'
    if string == 'd':
        return ' down'
    if string == 'l':
        return ' left'
    if string == 'r':
        return 'right'

# function to pretty print solution path 
def solMoveString(searchPathMoves):
    solutionPathString=''
    for i in reversed(searchPathMoves):
        solutionPathString = solutionPathString + i[0]+' '+parseMove(i[1])+' '+i[2]+' ; '
    return solutionPathString

# function to pretty print solution path moves / final board state
def solPathMoves(searchPathMoves,searchPath):
    for i in reversed(range(len(searchPath))):
        print('{}  {}'.format(searchPathMoves[i][0]+' '+parseMove(searchPathMoves[i][1])+' '+searchPathMoves[i][2]+' ',''.join(map(str,[ i for j in searchPath[i] for i in j]))))

    final = searchPath[0]
    for i in range(6):
        for j in range(6):
                print(final[i][j], end=" ")
        print('')

# function to pretty print solution path to text file
def printSolPathMovesTextFile(searchPathMoves,searchPath, text):
    for i in reversed(range(len(searchPath))):
        text.write('{}  {}'.format(searchPathMoves[i][0]+' '+parseMove(searchPathMoves[i][1])+' '+searchPathMoves[i][2]+' ',''.join(map(str,[ i for j in searchPath[i] for i in j]))))
        text.write('\n')

    text.write('\n')

    final = searchPath[0]
    for i in range(6):
        for j in range(6):
                text.write(final[i][j])
                text.write('')
        text.write('\n')

# function to pretty print search path to text file
def printSearchPathTextFile(closedList, i):
        #search path result, closedList has all the searched paths
    file = './Output/ucs/search files'
    fileName = f"ucs-search-{i}.txt"
    pathName = os.path.join(file, fileName)
    searchTextFile = open(pathName,"w+")    

    for p in closedList:
        searchTextFile.write(str(p.level))
        searchTextFile.write(' ')
        searchTextFile.write(str(p.cost))
        searchTextFile.write(' ')
        searchTextFile.write(str(0))
        searchTextFile.write(' ')
        for k in range(6):
            for j in range(6):
                searchTextFile.write(p.board[k][j])
                searchTextFile.write('')
        searchTextFile.write('\n')

def printDetailsExcel(solLength, searchLength, exeTIme):
    # each is a list print one by one and add to csv file, manually
    print(*solLength)
    print(*searchLength)
    print(*exeTIme)

# runs all the puzzle from input.txt
def runAllPuzzle(): # will not disply on terminal, output in the text files
    arrayPuzzle = readInput('input') # has all the puzzles
    solExcel = [] 
    searchExcel= []
    exeExcel =[]
    for i in range(1, len(arrayPuzzle)+1):
        folder = './Output/ucs/solution files'
        name = f"ucs-sol-{i}.txt"
        path = os.path.join(folder, name)
        textFile = open(path,"w+")
        unique= sorted(set(arrayPuzzle[int(i)-1][0:36]))
        if '.' in unique: unique.remove('.')
        fuel={}
        for j in range(len(unique)):
            fuel[unique[j]]=100
        remaining = arrayPuzzle[int(i)-1][36:len(arrayPuzzle[int(i)-1])].replace(' ','')
        #print((remaining))s
        if(len(arrayPuzzle[int(i)-1])>36):  #integer value should be until the end of file, or before another english.(we remove space)
            check= 0
            while(check<=len(remaining)/2):
                fuel[remaining[check]]=int(remaining[check+1])
                check = check+2
        print(f'initial puzzle is {arrayPuzzle[int(i)-1]}')
        textFile.write(f'initial puzzle is {arrayPuzzle[int(i)-1]}')
        textFile.write('\n\n')
        printPuzzle(arrayPuzzle[int(i)-1][0:36])
        printPuzzleTextFile(arrayPuzzle[int(i)-1][0:36], textFile)
        textFile.write('\n\n')
        print('car fuel available ',fuel)
        textFile.write('car fuel available: ')
        textFile.write(json.dumps(fuel))
        textFile.write('\n')
        start = time.time()
        board = getBoardMatrix(arrayPuzzle[int(i)-1][0:36])
        searchPathMoves, searchPath, allStates, closedList = ucs(board, fuel, unique)
        stop = time.time()
        if(searchPath[0][2][5]!='A'):
            textFile.write('no solution')
            solExcel.append('NA')
            searchExcel.append('NA')
            exeExcel.append('NA')
        else:
            textFile.write('execution time : ')
            textFile.write(str(stop-start))
            textFile.write(' seconds')
            textFile.write('\n')
            textFile.write('search path length: ' ) # all the states have been assigned  g(n)
            textFile.write(str(len(allStates)))
            textFile.write(' states')
            textFile.write('\n')
            textFile.write('solution path length: ')
            textFile.write(str(len(searchPathMoves)))
            textFile.write(' moves')
            textFile.write('\n')
            textFile.write('solution path: ')
            textFile.write(solMoveString(searchPathMoves))
            textFile.write('\n')
            textFile.write('\n\n')            
            printSolPathMovesTextFile(searchPathMoves, searchPath, textFile)
            solExcel.append(len(searchPathMoves))
            searchExcel.append(len(allStates))
            exeExcel.append(stop-start)
            solPathMoves(searchPathMoves, searchPath)
        textFile.close()
        printSearchPathTextFile(closedList,i)
        
    
    #printDetailsExcel(solExcel, searchExcel, exeExcel)

#runs the user chosen puzzle form input.txt
def runChosenPuzzle(): #output will be displayed on the terminals
    arrayPuzzle = readInput('input')
    size = len(arrayPuzzle)
    print('number of puzzles ',size)

    #user chooses puzzle
    check = False
    while(check==False):
        puzzleNumber = input(f'choose puzzle number between 1 and {size} :')
        if (int(puzzleNumber) > int(size) or int(puzzleNumber) < 1):
            print('wrong input')
        else:
            check=True
    # find unique, initial fuel 
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
    print(f'initial puzzle is {arrayPuzzle[int(puzzleNumber)-1]}')
    printPuzzle(arrayPuzzle[int(puzzleNumber)-1][0:36])
    print('car fuel available ',fuel)
    start = time.time()
    board = getBoardMatrix(arrayPuzzle[int(puzzleNumber)-1][0:36])
    searchPathMoves, searchPath, allStates, closedList = ucs(board, fuel, unique)
    stop = time.time()
    if(searchPath[0][2][5]!='A'):
        print('no solution')
    else:
        print('solution path ', solMoveString(searchPathMoves))
        print('execution time ',stop-start,' seconds')
        print('search path length',len(allStates), ' states') # all the states have been assigned  g(n)
        print('solution path length', len(searchPathMoves), ' moves')
        solPathMoves(searchPathMoves, searchPath)

if __name__ == '__main__':
    optionFlag= False
    while(optionFlag==False):
        runOption = input("Enter 1 to run all puzzle, Enter 2 to select puzzle number to run, Enter 3 to exit: ")
        if(runOption=='1'):
            runAllPuzzle()
            runOption=True
        elif(runOption=='2'):
            runChosenPuzzle()
            runOption = True
        elif(runOption=='3'):
            break
        else:
            print('Wrong input, Redo options')
