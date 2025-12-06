# AOC 2025-5a
# find id in ranges
test=1
debug=0
day="5a"

# DO NOT USE!!!!
# simplest variant, works on test input
# takes forever on competition input
def doWork( id ):
    answer = False
    for f, t in ranges:
        if id in range(f,t+1):
            if debug:
                print( "Found", id, f, t );
            answer = True
    return answer

ranges = []
total = 0

filename = "AOC-2025-" + day
if test:
    filename += "-test"
filename += ".txt"
print( day, filename, "v1" )

with open(filename, "r") as file:
    for line in file:
        line = line.replace("\n"," ").strip()
        
        if len(line) == 0:
            if debug:
                print()
        elif "-" in line:
            parts = line.split("-")
            f, t = int(parts[0]), int(parts[1])
            ranges.append( (f,t) )
            if debug:
                print( f, t )
        else:
            id = int(line)
            notSpoiled = doWork( id )
            if notSpoiled:
                total += 1
            print( id, notSpoiled, total )

print( day, "Answer is", total )
