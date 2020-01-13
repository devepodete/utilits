import os
gameField =[[1,2,7, 0,5,0, 0,0,0],
			[5,0,0, 0,0,7, 0,0,0],
			[0,0,0, 0,3,1, 5,6,0],
					 
			[0,8,0, 0,6,5, 7,0,0],
			[0,4,5, 0,0,0, 0,9,1],
			[0,3,0, 1,0,0, 0,5,0],
			 
			[2,0,4, 0,8,0, 0,0,6], 
			[3,0,9, 0,0,0, 0,8,5],
			[0,0,0, 0,0,2, 0,0,0]]

candies = []
lastIarr = []
lastJarr = []
status = []

for t in range(len(gameField)):
	status.append([])
	for k in range(len(gameField[t])):
		status[t].append(True)

for t in range(len(gameField)):
	candies.append([])
	for k in range(len(gameField[t])):
		candies[t].append([])

def solve(array):
	global candies, lastIarr, lastJarr, status
	t = k = 0
	while t < 9:
		if array[t][k] == 0:
			if status[t][k] != False:
				candies[t][k] = [x for x in candidates(array[t][k], t, k)]

			if len(candies[t][k]) == 0:
				array[lastIarr[-1]][lastJarr[-1]] = 0
				status[lastIarr[-1]][lastJarr[-1]] = False
				del lastIarr[-1]
				del lastJarr[-1]
				t = 0
				k = -1
			else:
				array[t][k] = candies[t][k][0]
				for i in range(len(array)):
					for j in range(len(array[i])):
						if i > t or j > k:
							status[i][j] = True
				lastIarr.append(t)
				lastJarr.append(k)
				candies[t][k].remove(candies[t][k][0])
		k += 1
		if k == 9:
			t += 1
			k = 0
			
def candidates(elem, i, j):
	global gameField
	res = [1,2,3,4,5,6,7,8,9]
	for t in range((i//3)*3,(i//3)*3+3):
		for k in range((j//3)*3,(j//3)*3+3):
			if gameField[t][k] in res:
				res.remove(gameField[t][k])

	for t in range(len(res)):
		if checkRow(res[t],i,j) == False:
			res[t] = '0'

	while('0' in res):
		res.remove('0')

	return res
	
def printField(arr):
	print("-------------------------")
	for t in range(len(arr)):
		print("|", end = " ")
		for k in range(len(arr[t])):
			print(arr[t][k], end = " ")
			if (k+1)%3 == 0:
				print("|", end = " ")
		print("")
		if (t-2)%3 == 0:
			print("-------------------------")
	
def checkRow(elem, i, j):
	global gameField  
	for t in range(len(gameField)):
		if t!= j and gameField[i][t] == elem:
			return False
	for t in range(len(gameField)):
		if t!= i and gameField[t][j] == elem:
			return False
	return True

def checkSudo(array):
	for t in range(len(array)):
		for k in range(len(array[t])):
			if not (checkRow(array[t][k],t,k) and checkSquare(array[t][k],t,k)):
				return False
	return True

def checkSquare(elem, i, j):
	global gameField
	for t in range((i//3)*3,(i//3)*3+3):
		for k in range((j//3)*3,(j//3)*3+3):
			if (t != i or k != j) and gameField[t][k] == elem:
				return False
	return True

printField(gameField)
print("Processing...")
solve(gameField)
os.system('clear')
printField(gameField)
print("Success")
