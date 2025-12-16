# AOC 2025-10
# xxx
test=0
debug=0
day="10a"

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )

total = 0

with open( filename, "r" ) as file:
    for line in file:
        
        l = line.split()
        bitLen = len(l[0])-2
        target = int(l[0].replace(".","0").replace("#","1")[1:bitLen+1],2)
        print( l[0], bitLen, "bits, target:", target )
        masks = []
        for i in range(1,len(l)-1):
            nn = eval(l[i].replace("(","[").replace(")","]"))
            m = 0
            for x in nn:
                m |= 1 << (bitLen-1-x)
            if debug:
                print( l[i], nn, "{0:b}".format(m), m )
            masks.append( m )
        if debug:
            print( "bitsmasks", masks )
        
        aTry = [ 0, [] ]
        status = [ aTry ]
        if debug:
            print( status )
        found = False
        iter = 0
        while not(found):
            newStatus = []
            iter += 1
            for s in status:
                if found:
                    break
              
                val, attempts = s[0], s[1]
                for j in range(len(masks)):
                    if debug:
                        print( i, j, "{0:b}".format(val), "{0:b}".format(masks[j]), attempts )
                    newVal = val ^ masks[j]
                    newAttempts = attempts.copy()
                    newAttempts.append( j )
                    newStatus.append( [newVal, newAttempts ] )
                    if debug:
                        print( iter, j, "{0:b}".format(newVal), newAttempts )
                    if newVal == target:
                        print( "*** Solution found", iter, newStatus[-1], [l[ii+1] for ii in newAttempts] )
                        found = True
                        break
            status = newStatus
            if debug:
                print( status )
                print()
         
        total += iter
        print( total, l )
        print()

print( day, "Answer is", total )
