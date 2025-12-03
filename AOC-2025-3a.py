# AOC-2025-3a
# find the maaximum voltage of batteries
dial=50
total=0

file = open("AOC-2025-3a-test.txt","r").readlines()
for line in file:
    line = line.rstrip("\n")
    battery=list(map( int, list(line) ))
    #print( battery )
    max1 = battery[0]
    prev = 0
    for x in battery[1:]:
        volt = max1 * 10 + x
        if volt > prev:
            prev = volt
        if x > max1:
            max1 = x
        #print( max1, x, prev, volt )
    total += prev
    print( line, prev, total )
print( "Result is ", total )
