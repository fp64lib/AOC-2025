# AOC 2025-7b
# count tachyonen beams
test=0
debug=0
day="7b"

# final version, counts correctly the different path possibilities
# all in one pass through the file

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )

total = 0

with open( filename, "r" ) as file:
    grid = file.readlines()
    pos = grid[0].find( "S" )
    if pos < 0:
        throw( "no starting position" )
    grid[1] = grid[1][:pos] + "|" + grid[1][pos+1:]
    print( 0, grid[0][:len(grid[0])-1])
    l = len(grid[0])-1
    counts = [0] * l
    prevCounts = [0] * l
    prevCounts[pos] = 1
    prev = grid[1]
    for i in range(1,len(grid)):
        line = grid[i]
        counts = [0] * l
        newLine = list(line[:len(line)-1])
        for pos in range(0,len(prev)-1):
            c = prev[pos]
            if c == ".":
                # do nothing
                continue
            elif c == "|":
                if line[pos] == "^":
                    # split beam
                    if pos > 0:
                        if newLine[pos-1] == ".":
                            newLine[pos-1] = "|"
                        counts[pos-1] += prevCounts[pos]
                    total += 1
                    newLine[pos] = "^"
                    counts[pos] = 0
                    if pos < len(line)-1:
                        if newLine[pos+1] == ".":
                            newLine[pos+1] = "|"
                        counts[pos+1] += prevCounts[pos]
                    if debug:
                        print( total, ''.join(newLine), pos )
                else: 
                    # beam goes further down
                    newLine[pos] =  "|"   
                    counts[pos] += prevCounts[pos]
                    
        # compose new line
        nl = ''.join( newLine )
        #total += nl.count( "|" )
        print( total, nl, counts ) #''.join(map(str,counts)) )
        prev = nl
        prevCounts = counts

print( day, "Answer is", sum(counts)+1 )
