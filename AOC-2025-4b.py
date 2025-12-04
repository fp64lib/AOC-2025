# AOC 2025-4b
# remove iteratively the rools
test=0
debug=0
day="4b"

filename = "AOC-2025-" + day[:len(day)-1] + "a"
if test:
    filename += "-test"
filename += ".txt"
file = open( filename, "r" ).readlines()
# extend the board, first vertically
for i in range(0,len(file)):
    file[i] = list( "."+file[i].replace("\n",".") )
    if debug:
        print( file[i] )

# now horizontally: add an empty line before and after the content
empty = list("."*(len(file[0])+1))
file.insert(0, empty )
file.append(empty)

neighbours = [ (-1,-1), (0,-1), (1,-1), 
               (-1, 0),         (1, 0),
               (-1, 1), (0, 1), (1, 1) ]

grandTotal = 0
round = 0
while True:
	total = 0
	round += 1
	newFile = [ empty ]
	print( "\nRound", round )
	
	for y in range(1,len(file)-1):
		answer = ""
		for x in range( 1, len(file[y])-1):
			n = 0
			if file[y][x] == "@":
				for dx,dy in neighbours:
					if file[y+dy][x+dx] == "@":
						n += 1
				if n < 4:
					answer += "x"
					total += 1
				else:
					answer += file[y][x]
			else:
				answer += file[y][x]
		print( y, answer, n, total )
		
		newFile.append( list("."+answer.replace("x", ".")+".") )

	grandTotal += total
	print( "Round", round, "Answer is", total, grandTotal )
	newFile.append( empty )
	file = newFile
	
	if total == 0:
		break

print( day, "Answer is", grandTotal )
