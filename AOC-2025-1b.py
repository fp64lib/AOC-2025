# AOC-2025-1a
# find the code by getting the number of 0
dial=50
passwd=0

file = open("AOC-2025-1a.txt","r").readlines()
print( "    ", dial, "start" )
for line in file:
    dir=line[0]
    amount=int(line[1:])
    clicks = int(amount/100)
    amount %= 100
    if dir == "L":
        if amount > dial:
            if dial != 0:
                clicks += 1
            dial = 100 + dial - amount
        else:
            dial = dial - amount
    else:
        if dial + amount > 100: # must be 100 and not 99, otherwise 0 will be counted twice
            clicks += 1
        dial = (dial + amount) % 100
    if dial == 0:
        clicks += 1
    passwd += clicks
    print( dir, amount, dial, clicks, passwd )
print( "Password is ", passwd )
