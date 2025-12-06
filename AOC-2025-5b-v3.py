# AOC 2025-5b
# find id in ranges
test=0
debug=0
day="5b"

# v3 works on competition input
# smart solution for merging overlapping ranges    
def insertRange( newf, newt ):
    if len(ranges) == 0:
        ranges.append( (newf, newt) )
        return
        
    for i in range(0,len(ranges)):
        f, t = ranges[i]
        #print( i, f, t )
        if newt < f:
            # new range is before current range
            # (but above previous range)
            # --> insert new range between previous and current one
            ranges.insert( i, (newf,newt) )
            if debug: 
                print( "insert before", i, newf, newt )
            return
        elif newf > t:
            # new range is above current range
            # --> skip to next range
            if debug:
                print( "after", i, f, t, newf, newt )
        else: 
            # new range somehow overlaps with current range
            # --> extend the current range
            if debug: 
                print( "extend", i, f, t, newf, newt )
            # take care both of overlapping and extending
            mf = min( f, newf)
            mt = max( t, newt )
            # two cases, both taking care in recursive call:
            # 1. insert new range at same position when distict
            # 2. merge with next range due when overlapping
            ranges.pop( i )
            insertRange( mf, mt )
            return
            
    # bigger than any previous range, append to end
    ranges.append( (newf, newt) )

total = 0
ranges = []
filename = "AOC-2025-" + day[:len(day)-1] + "a"
if test:
    filename += "-test"
filename += ".txt"
print( day, filename, "v3" )

with open(filename, "r") as file:
    for line in file:
        line = line.replace("\n"," ").strip()
        #print( ">"+line+"<" )
        if len(line) == 0:
            break
        elif "-" in line:
            parts = line.split("-")
            f, t = int(parts[0]), int(parts[1])
            insertRange( f, t )
            
            print( len(ranges) )
        else:
            break

# finally, calculate number of items in ranges            
for f, t in ranges:
    total += t - f + 1
    print( f, t, total )
    
print( day, "Answer is", total )
