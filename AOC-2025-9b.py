# AOC 2025-9a
# floor tiling, find largest rectangle
test=1
debug=1
day="9b"

from functools import cmp_to_key

# wip

class Corner:
    def __init__(self,x,y,i):
        self.x, self.y = x, y
        self.i = i

    def __str__(self):
        s = str( [self.x,self.y,self.i] )
        return s        

    def __repr__(self):
        return self.__str__()
        
    def __lt__(self, b):
        print( self, b )
        if self.y < b.y:
            return 1
        elif self.y == b.y:
            if self.x < b.x:
                return 1
            elif self.x == b.x:
                return 0
            else:
                return -1
        else:
            return -1

class Area:
    def __init__( self, el1, el2 ):
        self.el1, self.el2 = el1, el2
        self.area = Area.area( el1, el2 )
        
    def __lt__(self, other):
        return self.area < other.area
        
    def __str__(self):
        s = str(self.el1) + "->" + str(self.el2) + ":" + str(self.area)
        return s

    def __repr__(self):
        return self.__str__()
        
    def area(el1, el2):
        dx, dy = abs(el1.x-el2.x)+1, abs(el1.y-el2.y)+1
        return dx*dy

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )

total = 0
grid = []
d = []
minx = miny = 1000000000
maxx = maxy = 0

def findNext( prev ):
    # find next element clock wise
    choose = [el for el in grid if el.x == prev.x or el.y == prev.y ]
    print( choose )
    found = prev
    for el in choose:
        print( prev, el )
        if el != prev:
            if el.x == prev.x:
                if el.x > found.x:
                    found = el
            elif el.y == prev.y:
                if el.y > found.y:
                    found = el
    print( prev, found )
    return prev
    
def findOutline():
    outline = []
    prev = grid.pop(0)
    outline.append(prev)
    while len(grid) > 0:
        # we have to take care of the search direction
        # first right, then down, then left, then up
        # test against bounding box
        el = findNext( prev )
        if el == prev:
            print( "*** circle detected", prev )
            return outLine
        if debug:
            print( el )
        outLine.append( el )
        prev = el
    return outLine            

with open( filename, "r" ) as file:
    for line in file:
        ints = list(map(int,line.split(",")))
        newEl = Corner( *ints, len(grid) )
        minx, maxx = min(minx, newEl.x), max(maxx, newEl.x)
        miny, maxy = min(miny, newEl.y), max(maxy, newEl.y)
        #print( newEl )
        grid.append( newEl )

    print( grid )
    #grid = sorted( grid, key=lambda k: [k.x, k.y])
    #print( grid )
    # renumber the points
    for i in range(len(grid)):
        grid[i].i = i
    print( grid )
        
    topLeft = Corner( minx, miny, -1 )
    bottomRight = Corner( maxx, maxy, -2 )
    print( "Bounding box:", topLeft, bottomRight )
    
    outLine = findOutline()
    print( "outline", outLine )
    
    outLine = findOutline()
    print( outLine )
        
    for i in range(0,len(grid)-1):
        for j in range(i+1, len(grid)):
            d.append( Area( grid[i], grid[j] ) )

    if debug:
        for i in range(0,10):
            print( i, d[i] )
    d.sort(reverse=True)
    
    print( len(d), d[0] )
    if debug:
        for i in range(0,10):
            print( i, d[i] )
        print()    
        
    print( len(d), d[0] )


    total = d[0].area



    print( total )

print( day, "Answer is", total )
