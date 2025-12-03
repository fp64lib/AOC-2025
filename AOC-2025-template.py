# AOC 2025-xx
# xxx
test=1
debug=1
day="3a"

def doWork( s ):
    answer = ""
	#...
    return answer

filename = "AOC-2025-" + day
if test:
    filename += "-test"
filename += ".txt"
file = open( filename, "r" ).readlines()

total = 0
for line in file:
    l = line.rsplit("\n")[0]
    m = doWork( l )
    total += int(m)
    print( l, m, total )
print( day, "Answer is", total )

