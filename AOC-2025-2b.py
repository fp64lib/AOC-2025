# AOC-2025-2a
# check for valid ids
sum=0
debug=False
verbose=False
maxLines=0

def isInvalid( x):
    s=str(x)
    for i in range(1,len(s)//2+1):
        if debug:
            print(s, len(s), "checking for", i)
        if len(s) % i == 0:
            # can be split into patterns of length id
            l = len(s)//i
            first = s[:i]
            match = True
            for j in range(1,l):
                pos = i*j
                second = s[pos:pos+i]
                if debug:
                    print(s, l, j, "*"+first+"*","+"+second+"+")
                match = match and (first == second)
            if match:
                return True
    return False

#file = open("AOC-2025-2a-ranges.txt","r").readlines()
file = open("AOC-2025-2a.txt","r").readlines()
cnt=0
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
    cnt += 1
    if maxLines and cnt >= maxLines:
        break
    
print( "Sum is ", sum )
