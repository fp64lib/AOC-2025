# AOC 2025-11
# find different paths
test=0
debug=0
day="11a"

filename = "AOC-2025-" + day[:len(day)-1]
if test:
    filename += "-test"
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
		
        def addToPath( key, path ):
            if key == "out":
                if debug:
                    print( path, key, 1 )
                return 1
                
            if key in path:
                if debug:
                    print( "cycle", key, path )
                return 0
        
            if key in used:
                print( path, key, "used", paths[key] )
                return paths[key]

            used.append( key )
            path.append( key )
            if debug:
                    print( key, paths[key] )

            for x in patches[key]:
                    s = addToPath( x, path )
                    paths[key] += s
                    if debug:
                        print( path, x, s , paths[key] )
            path.remove( key )
            return paths[key]
			
    total = addToPath( "you", [] )
    if debug:
        print( paths )

print( day, "Answer is", total )
