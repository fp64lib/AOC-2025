# AOC 2025-3b
# find maximum voltage
test=0
debug=0
day="3a"

def findMax( s, n ):
    answer = ""
    mPos = 0
    while n > 0:
        mx=s[mPos]
        for pos in range(mPos+1, len(s)-n+1):
            if s[pos] > mx:
                mPos = pos
                mx = s[mPos]
        answer = answer + mx
        if debug:
            print( n, answer )
        mPos += 1
        n -= 1
    return answer

filename = "AOC-2025-" + day
if test:
    filename += "-test"
filename += ".txt"
file = open( filename, "r" ).readlines()

total = 0
for line in file:
    battery = line.rsplit("\n")[0]
    m = findMax( battery, 2 )
    total += int(m)
    print( battery, m, total )
print( "03a Answer is", total )
print()

total = 0
for line in file:
    battery = line.rsplit("\n")[0]
    m = findMax( battery, 12 )
    total += int(m)
    print( battery, m, total )
print( "03b Answer is", total )


