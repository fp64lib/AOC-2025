# AOC 2025-5b
# find id in ranges
test=1
debug=0
day="5b"

# DO NOT USE!!!!
# variant with adding ranges, works on test input
# takes forever on competetion input
def isNewId( id ):
    for f, t in ranges:
        if id in range(f,t+1):
            if debug:
                print( "Found", id, f, t );
            return False
    return True
    
total = 0
ranges = []
filename = "AOC-2025-" + day[:len(day)-1] + "a"
if test:
    filename += "-test"
filename += ".txt"
print( day, filename, "v2" )

with open(filename, "r") as file:
    for line in file:
        line = line.replace("\n"," ").strip()
        #print( ">"+line+"<" )
        if len(line) == 0:
            break
        elif "-" in line:
            parts = line.split("-")
            f, t = int(parts[0]), int(parts[1])
            start = -1
            for id in range(f,t+1):
                if isNewId(id):
                    if start == -1:
                        start = id
                else:
                    if start != -1:
                        ranges.append( (start, id-1 ) )
                        total += id - start
                        print( "add", start, id-1, total )
                        start = -1
                if debug or id % 1000000 == 1:
                    print( id, total, "X" )
            if start != -1:
                ranges.append( (start, t ) )
                total += t - start + 1
                print( "add", start, t, total )
            print( f, t, total )
        else:
            break
print( day, "Answer is", total )
