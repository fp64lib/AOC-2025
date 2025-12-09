# AOC 2025-9a
# floor tiling, find largest rectangle
test=0
debug=1
day="9a"

class Corner:
    def __init__(self,x,y,i):
        self.x, self.y = x, y
        self.i = i

    def __str__(self):
        s = str( [self.x,self.y,self.i] )
        return s

    def __repr__(self):
        return self.__str__()
        
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

with open( filename, "r" ) as file:
    for line in file:
        ints = list(map(int,line.split(",")))
        newEl = Corner( *ints, len(grid) )
        print( newEl )
        grid.append( newEl )
    
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
