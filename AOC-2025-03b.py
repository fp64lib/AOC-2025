# AOC 2025-3b
# find maximum voltage

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
        #print( n, answer )
        mPos += 1
        n -= 1
    return answer
            
#file = open("AOC-2025-03a-test.txt", "r").readlines()
file = open("AOC-2025-03a.txt", "r").readlines()
total = 0
for line in file:
    battery = line.rsplit("\n")[0]
    m = findMax( battery, 12 )
    total += int(m)
    print( battery, m, total )
print( "Answer is", total )


