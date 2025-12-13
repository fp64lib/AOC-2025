# AOC 2025-11b
# find different paths for special paths
test=0
debug=0
day="11b"

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "b-test"
filename += ".txt"
print( day, filename )

total = 0
patches = dict()
paths = dict()
used = [ ]

with open( filename, "r" ) as file:
    for line in file:
        l = line.split(":")
        key = l[0]
        val = l[1].split()
        patches[key] = val
        paths[key] = 0
        
        def find( start, end, reset ):
            global used
            if reset:
                for key in paths:
                    paths[key] = 0
                used = [ ]
            print( "***find", start, end, reset, used )
            return addToPath( start, [], end )
		
        def addToPath( key, path, end ):
            global used
            if key == end:
                if debug:
                    print( "end", path, key, 1 )
                return 1

            if end != "out" and key == "out":
                if debug:
                    print( "end", path, key, 0 )
                return 0
                
            if key in path:
                if debug:
                    print( "cycle", key, path )
                return 0
        
            if key in used:
                if debug:
                    print( path, key, "used", paths[key] )
                return paths[key]

            used.append( key )
            path.append( key )
            if debug:
                    print( path, key, paths[key] )

            for x in patches[key]:
                    s = addToPath( x, path, end )
                    paths[key] += s
                    if debug:
                        print( path, x, s , paths[key] )
            path.remove( key )
            return paths[key]
			
    t1 = find( "svr", "fft", True )
    print( "*** src ->fft", t1 )
    if debug:
        print( paths )
    t2 = find( "fft", "dac", True )
    print( "*** fft->dac", t2 )
    if debug:
        print( paths )
    t1 *= t2
    t2 = find( "dac", "out", True )
    print( "*** dac->out", t2 )
    if debug:
        print( paths )
    t1 *= t2
    print("***", t1)
    total = t1

    t1 = find( "svr", "dac", True )
    print( "*** src ->dac", t1 )
    if debug:
        print( paths )
    t2 = find( "dac", "fft", True )
    print( "*** dac->fft", t2 )
    if debug:
        print( paths )
    t1 *= t2
    t2 = find( "fft", "out", True )
    print( "*** fft->out", t2 )
    if debug:
        print( paths )
    t1 *= t2
    print("***", t1)

    total += t1

print( day, "Answer is", total )
