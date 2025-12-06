# AOC 2025-6a
# celaphopod math, do operations on columns
test=0
debug=0
day="6a"

from operator import mul
from functools import reduce 


filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )

total = 0
res = 0
work = []
with open( filename, "r" ) as file:
    # read in all the contents and convert it to numbers
    for line in file:
        l = line.rsplit("\n")[0].split()
        if l[0] == "+" or l[0] == "*":
            break;
        intLine = list(map(int,l))
        work.append( intLine )

    # transpose columns to rows
    work = list(zip(*work))
    if debug:
        print( *work )
    
    # perform math operations
    for i in range(0,len(l)):
        if l[i] == "+":
            res = sum(work[i])
        else:
            res = reduce( mul, work[i] )
        total += res
        print( l[i], work[i], res, total ) 
            
print( day, "Answer is", total )
