#в программе используется длина строки через a[0], так как предполагается, что
#все строки в массиве равны по длине
#при использовании других видов массива, например,
#[x,x,x,x,x]
#[x,x,x]
#[x,x,x,x]
#[x,x,x,x]
#[x,x]
#необходимо полностью переработать функции moved, added, canMove, canAdd
#
#также в функция canMove имеет место быть, потому что при первом её вызове
#игровое поле уже не пустое
import os
import random
import time


LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

score = 0
addToScore = [0]

gameField = [
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
]

#создание копии массива
def copyOfArray(array):
	newArray = []
	for t in range(len(array)):
		newArray.append([])
		for k in range(len(array[t])):
			newArray[t].append(array[t][k])

	return newArray

#в одной случайной пустой(== 0) ячейке создаётся число(2 или 4)
def spawnPellet(array):
	forSpawn = [2,2,2,2,2,2,4]
	arrayOfZeros = []
	choice = []
	for t in range(len(array)):
		for k in range(len(array[t])):
			if array[t][k] == 0:
				arrayOfZeros.append([t,k])

	choice = random.choice(arrayOfZeros)
	array[choice[0]][choice[1]] = random.choice(forSpawn)

#преобразование столбца в строку
def columnToRow(array,columnNumber):
	column = []
	for t in range(len(array)):
		column.append(array[t][columnNumber])

	return column

#проверка строки (или столбца в виде строки) на завершённость хода в направлении 
#direction (Left или Right)
def finallyMoved(row,direction):
	if direction == RIGHT:
		for t in range(len(row)-1):
			if row[t] != 0 and row[t+1] == 0:
				return False
	if direction == LEFT:
		for t in range(len(row)-2,-1,-1):
			if row[t] == 0 and row[t+1] != 0:
				return False

	return True

#движение вниз или вправо
def moveDownOrRight(columnOrRow):
	#0100 -> 0100 -> 0010 -> 0001
	while(finallyMoved(columnOrRow,RIGHT)) != True:
		for t in range(len(columnOrRow)-1):
			if columnOrRow[t+1] == 0 and columnOrRow[t] != 0:
				columnOrRow[t],columnOrRow[t+1] = 0,columnOrRow[t]

	return columnOrRow

#движение вверх или влево
def moveUpOrLeft(columnOrRow):
	#0100 -> 0100 -> 0100 -> 1000
	while(finallyMoved(columnOrRow,LEFT)) != True:
		for t in range(len(columnOrRow)-2,-1,-1):
			if columnOrRow[t] == 0 and columnOrRow[t+1] != 0:
				columnOrRow[t],columnOrRow[t+1] = columnOrRow[t+1], 0

	return columnOrRow

#движение в определённую сторону (direction)
def moved(array,direction):	
	if direction == DOWN:
		for t in range(len(array)):
			newColumn = moveDownOrRight(columnToRow(array,t))
			for k in range(len(newColumn)):
				array[k][t] = newColumn[k]

	if direction == UP:
		for t in range(len(array)):
			newColumn = moveUpOrLeft(columnToRow(array,t))
			for k in range(len(newColumn)):
				array[k][t] = newColumn[k]

	if direction == LEFT:
		for t in range(len(array[0])):
			moveUpOrLeft(array[t])

	if direction == RIGHT:
		for t in range(len(array[0])):
			moveDownOrRight(array[t])

#можно ли подвинуть строку/столбец
def canMove(array):
	for t in range(len(array)):
		for k in range(len(array)):
			if array[t][k] == 0:
				return True
	return False

#проверка: было ли какое-то изменение в массиве после движения
def wasChanged(array, direction):
	wasMoved = wasAdded = True
	newArray1 = copyOfArray(array)
	newArray2 = copyOfArray(array)
	
	moved(newArray1,direction)
	if newArray1 == array:
		wasMoved = False
	if wasMoved == True:
		return True
	
	added(newArray2,direction)
	if newArray2 == array:
		wasAdded = False

	if wasAdded == True:
		return True
	
	return False

#проверка на возможность сложения
def canAdd(array):
	#проверка на возможность сложения элементов в строке
	for t in range(len(array)):
		for k in range(len(array[t])-1):
			if array[t][k] == array[t][k+1]:
				return True
	#проверка на возможность сложения элементов в столбце
	for t in range(len(array)-1):
		for k in range(len(array[t])):
			if array[t][k] == array[t+1][k]:
				return True

	return False

#сложение чисел в направлении direction
def added(array,direction):
	global addToScore
	addToScore = [0]
	if direction == LEFT:
		for t in range(len(array)):
			for k in range(len(array[0])-1):
				if array[t][k] == array[t][k+1] and array[t][k] != 0:
					array[t][k] += array[t][k+1]
					array[t][k+1] = 0
					addToScore.append(array[t][k])

		return array

	if direction == RIGHT:
		for t in range(len(array)):
			for k in range(len(array[0])-2,-1,-1):
				if array[t][k] == array[t][k+1] and array[t][k] != 0:
					array[t][k+1] += array[t][k]
					array[t][k] = 0
					addToScore.append(array[t][k+1])

		return array

	if direction == UP:
		for t in range(len(array)-1):
			for k in range(len(array[0])):
				if array[t][k] == array[t+1][k] and array[t][k] != 0:
					array[t][k] += array[t+1][k]
					array[t+1][k] = 0
					addToScore.append(array[t][k])

		return array 

	if direction == DOWN:
		for t in range(len(array)-2,-1,-1):
			for k in range(len(array[0])):
				if array[t][k] == array[t+1][k] and array[t][k] != 0:
					array[t][k] += array[t+1][k]
					array[t+1][k] = 0
					addToScore.append(array[t][k])

		return array

#отрисовка игрового поля
def drawGame(array):
	os.system('clear')
	print("  '2048' ")
	for t in array:
		print(t)
	print('score = ', score)

#приветствие
def welcome():
	hello = ["__  __           _          _           ","|  \/  | __ _  __| | ___    | |__  _   _ ",
	"| |\/| |/ _` |/ _` |/ _ \   | '_ \| | | |","| |  | | (_| | (_| |  __/   | |_) | |_| |",
	"|_|  |_|\__,_|\__,_|\___|   |_.__/ \__, |","                                   |___/",
	" _____                _                              ","|__  /___ _ __ ___   / \   _ __ _ __ ___   ___  _ __ ",
	"  / // _ \ '__/ _ \ / _ \ | '__| '_ ` _ \ / _ \| '__|"," / /|  __/ | | (_) / ___ \| |  | | | | | | (_) | |   ",
	"/____\___|_|  \___/_/   \_\_|  |_| |_| |_|\___/|_|  "]
	
	anim = "|/-\\"
	idx = 0
	while idx < 50:
		time.sleep(0.06)
		print(40*anim[idx%len(anim)] + "\r",end=' ')
		idx +=1

	print('\n')
	
#цикл, в котором всё крутится
def main():
	global score, addToScore
	while True:
		drawGame(gameField)
		if canMove(gameField) == False and canAdd(gameField) == False:
			drawGame(gameField)
			print('You Lose')
			break
		else:
			direction = input()			
			if wasChanged(gameField,direction) == True:
				moved(gameField, direction)
				added(gameField, direction)
				moved(gameField, direction)
				
				for t in range(len(addToScore)):
					score += addToScore[t]

				spawnPellet(gameField)
			else:
				continue
			
welcome()
spawnPellet(gameField)
spawnPellet(gameField)
main()
