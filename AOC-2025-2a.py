# AOC-2025-2a
# check for valid ids
sum=0
debug=False
verbose=False

def isInvalid( x):
    s=str(x)
#    print(s, len(s))
    if len(s) % 2 == 0:
        # even length
        l = len(s)//2
        first = s[:l]
        second = s[l:]
        if debug:
            print(s, l, "*"+first+"*","+"+second+"+")
        return first == second
    else:
        return False


#file = open("AOC-2025-2a-ranges.txt","r").readlines()
file = open("AOC-2025-2a.txt","r").readlines()
for line in file:
    print(line)
    tokens = line.split("-")
    start, to = int(tokens[0]), int(tokens[1])
    for x in range(start, to+1):
        invalid = isInvalid(x)
        if invalid:
            sum += x
        if verbose or invalid:
            print( x, invalid, sum )

print( "Sum is ", sum )
