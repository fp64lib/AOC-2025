# AOC-2025-1a
# find the code by getting the number of 0
dial=50
passwd=0

file = open("AOC-2025-1a.txt","r").readlines()
for line in file:
	dir=line[0]
	amount=int(line[1:])
	if dir=="L":
		amount = -amount
	dial = (dial + amount + 100) % 100
	if dial == 0:
		passwd += 1
	print( dir, abs(amount), dial, passwd )
print( "Password is ", passwd )
