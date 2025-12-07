# AOC 2025-7a
# count tachyonen beams
test=1
debug=1
day="7a"

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )

total = 0
ways = 0

with open( filename, "r" ) as file:
    grid = file.readlines()
    pos = grid[0].find( "S" )
    if pos < 0:
        throw( "no starting position" )
    grid[1] = grid[1][:pos] + "|" + grid[1][pos+1:]
    print( 0, grid[0][:len(grid[0])-1])
    print( total, grid[1][:len(grid[1])-1] )
    prev = grid[1]
    for i in range(2,len(grid)):
        line = grid[i]
        newLine = list(line[:len(line)-1])
        for pos in range(0,len(prev)-1):
            c = prev[pos]
            if c == "|":
                if line[pos] == "^":
                    # split beam
                    if pos > 0:
                        if newLine[pos-1] == ".":
                            newLine[pos-1] = "|"
                            ways += 1
                    total += 1
                    newLine[pos] = "^"
                    if pos < len(line)-1:
                        if newLine[pos+1] == ".":
                            newLine[pos+1] = "|"
                            ways += 1
                    if debug:
                        print( total, ''.join(newLine), ways, pos )
                else: 
                    # beam goes further down
                    newLine[pos] =  "|"   

        # compose new line
        nl = ''.join( newLine )
        #total += nl.count( "|" )
        #if nl.find("^") > 0:
        #    ways += nl.count("|")
        print( total, nl, ways )
        prev = nl

print( day, "Answer is", ways )
