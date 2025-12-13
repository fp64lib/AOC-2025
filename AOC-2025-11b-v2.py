# AOC 2025-11b
# find different paths for special paths
# cleaned up version
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
        
        def find( start, end ):
            global used, paths
            for key in paths:
                paths[key] = 0
            used = [ ]
            if debug:
                print( "***find", start, end )
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
 
    total = 0
    for p in [ ["svr","fft","dac","out"],["svr","dac", "fft","out"]]:
        prev = p[0]
        count = 1
        for nxt in p[1:]:
            n = find( prev, nxt )
            if debug:
                print( "***", prev, "-->", nxt, n )
                print( paths )
            count *= n
            prev = nxt
        total += count
        print("***", p, total, count )

print( day, "Answer is", total )
