# AOC 2025-12
# Fit minimumSpace into space
test=0
debug=0
day="12"

filename = "AOC-2025-" + day
if test:
    filename += "-test"
filename += ".txt"
print( day, filename )

def doShapesFit( content ):
    sections = content.strip().split("\n\n")
    if not sections:
        print( "*** Invalid file, missing empty line between minimumSpace and/or regions" )
        return 0

    # 1: Assume all shapes fit perfectly, what is the miminum space needed per shape
    minimumSpace = [section.count("#") for section in sections[:-1]]
    if debug:
        print( minimumSpace )

    regions = 0
    for line in sections[-1].split("\n"):
        if  ": " not in line or "x" not in line:
            if debug:
                print( "invalid line:", line )
            continue

        dimensions, quantity = line.split(": ", 1)
        if debug > 1:
            print( dimensions, quantity )

        width, height = map(int, dimensions.split("x"))
        area = width * height
        if debug > 1:
            print( "w, h, a", width, height, area )

        quantities = list(map(int, quantity.split()))
        size = sum(q * m for q, m in zip( quantities, minimumSpace ))

        if size > area:
            if debug > 1:
                print( "area exceeded!", area, size, area-size )
        else:
            regions += 1
            if debug:
                print( regions, "fit", dimensions, area, quantity, size, area-size )

    return regions

total = 0

with open( filename, "r" ) as file:
    # as the file might need several passes, read it in completely
    content = file.read()
    
    total = doShapesFit( content )

print( day, "Answer is", total )
