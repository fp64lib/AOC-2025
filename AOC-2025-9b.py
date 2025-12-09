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

class Rectangle:
    def __init__( self, el1, el2 ):
        self.el1, self.el2 = el1, el2
        x1 = min(self.el1.x, self.el2.x)
        x2 =´max(self.el1.x, self.el2.x)
        y1 = min(self.el1.y, self.el2.y)
        y2 =´max(self.el1.y, self.el2.y)
        self.area = Rectangle.area( el1, el2 )
        
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
        
    def check( self, x1, y1, x2, y2, checkVertical )
        if checkVertical:
            # assume y1 = y2, touching is not intersecting
            if self.x1 >= x2 or self.x2 <= x1:
                # line is right or left of us, no intersection
                return False 
            elif self.y1 >= y2 or self.y2 <= y1
                # line below or above us, no intersection
                return False
            else:
                # we intersect            
                return True                # 
        
    def intersects( self, other ):
        # works only for rectangles       
        cut =         self.check( other.x1, other.y1, other.x2, other.y1, True ) # top
        cut = cut and self.check( other.x2, other.y1, other.x2, other.y2, False ) # right
        cut = cut and self.check( other.x1, other.y2, other.x2, other.y2, True ) # bottom
        cut = cut and self.check( other.x1, other.y1, other.x2, other.y2, False ) # left
        return cut
   

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
           
    for i in range(0,len(grid)-1):
        for j in range(i+1, len(grid)):
            d.append( Rectangle( grid[i], grid[j] ) )

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
    
    # find all x and y lines
    # check first rectangle against all vertices
    
    for el in d:
        for g in grid:
            ok = 
    
    
    total = d[0].area



    print( total )

print( day, "Answer is", total )
