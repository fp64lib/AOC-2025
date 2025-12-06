# AOC 2025-6b
# celaphopod math: column wise operations, right to left digits
test=0
debug=0
day="6b"

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
    # read in all the contents
    for line in file:
        l = line.rsplit("\n")[0]
        if l[0] == "+" or l[0] == "*":
            break;
        work.append( list(l) )
        if debug:
            print( l )
        
    # transpose columns to rows
    work = list(zip(*work))
    if debug:
        print( work )
    work = list(map(''.join,work))
    if debug:
        print(work)
        
    # get right to left numbers
    newWork = []
    temp = []
    for el in work:
        if debug:
            print(el)
        if el ==  ' '*len(el):
            if len(temp):
                newWork.append(temp)
            temp = []
        else:
            temp.append(int(el))
    newWork.append(temp)
    if debug:
        print(newWork)
    
    # perform math operations
    work = newWork
    l = l.split()
    for i in range(0,len(l)):
        if l[i] == "+":
            res = sum(work[i])
        else:
            res = reduce( mul, work[i] )
        total += res
        print( l[i], work[i], res, total ) 
            
print( day, "Answer is", total )
