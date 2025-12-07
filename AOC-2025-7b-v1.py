# AOC 2025-7b
# find differnt paths of tachyonen beams
test=0
debug=0
day="7b"

# DO NOT USE
# first vesion, works correctly with test input
# but takes forever with puzzle input
# estimated solution time 24000 years on laptop

from timeit import default_timer as timer
startTime = timer()
total = 0

def findPath( myGrid, startLine, pos ):
    global total
    # a new path was created, splitted of at startLinem startPos
    if startLine >= len(myGrid):
        total += 1

        if debug or total % 1000000 == 0:
            print( total, "*** new path from", startLine, pos, timer()-startTime )
        if debug:
            for i in range(0, startLine):
                print( total, myGrid[i] )
            print( "done", total )
        return

    if debug:
        print( "*** new path from", startLine, pos )
        for i in range(0, startLine):
            print( total, myGrid[i] )

    prev = myGrid[startLine-1]
    line = myGrid[startLine]
    newLine = list(line)
    c = line[pos]
    if c == "^":
        # split beam
        if pos > 0:
            if line[pos-1] == ".":
                save = newLine
                newLine[pos-1] = "|"
                myGrid[startLine] = ''.join(newLine)
                findPath( myGrid, startLine+1, pos-1 )
                if debug:
                    print( startLine, line )
                myGrid[startLine] = line
                newLine[pos-1] = line[pos-1]

        if pos < len(line):
            if newLine[pos+1] == ".":
                save = newLine
                newLine[pos+1] = "|"
                myGrid[startLine] = ''.join(newLine)
                findPath( myGrid, startLine+1, pos+1 )
                if debug:
                    print( startLine, line )
                myGrid[startLine] = line
                newLine[pos+1] = line[pos+1]

        if debug:
            print( total, ''.join(newLine), pos )
    else:
        save = newLine
        newLine[pos] = "|"
        myGrid[startLine] = ''.join(newLine)
        findPath( myGrid, startLine+1, pos )
        if debug:
            print( startLine, line )
        myGrid[startLine] = line
        newLine[pos] = c
        
    if debug:
        for l in myGrid:
            print( total, l )
        print()

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )



with open( filename, "r" ) as file:
    grid = file.readlines()
    l = len(grid[0])
    for i in range(0,len(grid)):
        grid[i] = grid[i][0:l-1]
    pos = grid[0].find( "S" )
    if pos < 0:
        throw( "no starting position" )
    grid[1] = grid[1][:pos] + "|" + grid[1][pos+1:]
    findPath( grid, 2, pos )

print( day, "Answer is", total )
