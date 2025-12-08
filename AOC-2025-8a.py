# AOC 2025-8a
# Conne t junction boxes
test=0
debug=0
day="8a"

from operator import mul
from functools import reduce 

# WIP, still too slow

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )

total = 0
stopAt = 1000
grid = []
d = []

def dist(el1, el2):
    #print( el1, el2 )
    x1, y1, z1 = el1[0], el1[1], el1[2]
    x2, y2, z2 = el2[0], el2[1], el2[2]
    dx, dy, dz = x1-x2, y1-y2, z1-z2
    return dx*dx+dy*dy+dz*dz

with open( filename, "r" ) as file:
    for l in file:
        ints = list(map(int,l.split(",")))
        #print( l, ints )
        grid.append( ints )
    d = [[dist(i,j) for i in grid] for j in grid]
    if debug:
        for i in range(len(d)):
            print( i, d[i] )
        print();

    excluded = []
    circuits = []
    count = 0
    while count < stopAt:
        ii, mm, jj = 0, 0, 0
        for i in range(len(d)):
            for j in range( i+1, len(d) ):
                if (i,j) not in excluded and i != j:
                    m = d[i][j]
                    if m < mm or mm == 0:
                        ii, mm, jj = i, m, j
        if debug:
            print( ii, jj, mm, grid[ii], grid[jj], d[ii][jj] )
        else:
            print( count, grid[ii], grid[jj], d[ii][jj] )
        excluded.append( (ii, jj) )
        excluded.append( (jj, ii) )
        if debug:
            print( count, "exc", excluded )
        # add to circuit or create a new one
        included = False
        l = []
        for a in (ii,jj):
            if included:
                break;
            for c in circuits:
                if a in c:
                    l = c
                    included = True
                    if debug:
                        print( "included", a, c )
                    break
        if included:
            if debug:
                print( "before", l )
            if ii in l and jj in l:
                continue
            l.add( ii )
            l.add( jj )
            count += 1
            if debug:
                print( "after", l )
        else:
            # create a new circuit
            circuits.append( { ii, jj } )
            count += 1

        if debug:
            print( i, "circ", circuits )

    print( "Circuits:")
    l = [len(c) for c in circuits]
    l.sort()
    print( l )
    if test:
        answer = reduce( mul, l[-1000:])
    else:
        answer = reduce( mul, l[-3:])
    for c in circuits:
        total += len( c )
        print( len(c), [grid[i] for i in c] )
    
    print( total )

print( day, "Answer is", answer )
