

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
print((remaining))
if(len(arrayPuzzle[int(puzzleNumber)-1])>36):  #integer value should be until the end of file, or before another english.(we remove space)
    check= 0
    while(check<=len(remaining)/2):
        fuel[remaining[check]]=remaining[check+1]
        check = check+2

print('intial fuel of each vehicle ',fuel)

