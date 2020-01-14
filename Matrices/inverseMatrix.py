#нахождение обратной матрицы

#создание матрицы
def createMatrix(size):
	matrix = []
	print("Введите элементы матрицы")
	for t in range(size):
		matrix.append([])
		for k in range(size):
			matrix[t].append(float(input()))

	return matrix

#создание единичной матрицы
def createE(size):
	matrix = []
	for t in range(size):
		matrix.append([])
		for k in range(size):
			if t == k:
				matrix[t].append(1)
			else:
				matrix[t].append(0)
	return matrix

#определитель матрицы Matrix
def determinant(Matrix):
	copy = copyOfMatrix(Matrix)
	if (len(copy) == 1 and len(copy[0]) == 1):
		return copy[0][0]
	else:
		det = 0
		for j in range(len(copy)):
			det += ((-1)**(1+j+1))*copy[0][j]*determinant(newMatrix(copy,0,j))

		return det

#Матрица Matrix2, полученная из Matrix вычёркиванием i строки и j столбца
def newMatrix(Matrix,i,j):
	Matrix2 = []
	for t in range(len(Matrix)):
		Matrix2.append([])
		for k in range(len(Matrix[t])):
			Matrix2[t].append(Matrix[t][k])
	del Matrix2[i]
	for t in range(len(Matrix2)):
		del Matrix2[t][j]

	return Matrix2

#создание копии матрицы
def copyOfMatrix(Matrix):
	copy = []
	for t in range(len(Matrix)):
		copy.append([])
		for k in range(len(Matrix[t])):
			copy[t].append(Matrix[t][k])

	return copy
	
#транспонирование матрцы
def transpo(Matrix):
	transpoMatrix = []
	for t in range(len(Matrix)):
		transpoMatrix.append([])
		for k in range(len(Matrix)):
			transpoMatrix[t].append(Matrix[k][t])

	return transpoMatrix

#алгебраическое дополнение к элементу A[i][j]
def algebraicAddition(Matrix, i, j):
	return (-1)**(i+j+2) * determinant(newMatrix(Matrix,i,j))

#перемножение матриц
def multiplyMatrixToMatrix(matrix1,matrix2):
	result = []
	for t in range(len(matrix1)):
		result.append([])
		for k in range(len(matrix2[0])):
			result[t].append(0)

	for t in range(len(matrix1)):
		for k in range(len(matrix2[0])):
			for j in range(len(matrix1[0])):
				result[t][k] += matrix1[t][j]*matrix2[j][k]

	return result

#умножение матрицы на число
def multiplyMatrixToNumber(Matrix, number):
	for t in range(len(Matrix)):
		for k in range(len(Matrix[t])):
			Matrix[t][k] *= number

	return Matrix

#создание обратной матрицы
def inverseMatrix(Matrix):
	MatrixStar = []
	for i in range(len(Matrix)):
		MatrixStar.append([])
		for j in range(len(Matrix)):
			MatrixStar[i].append(algebraicAddition(Matrix,i,j))


	return(multiplyMatrixToMatrix(multiplyMatrixToNumber(E, 
		(1/determinant(Matrix)) ), transpo(MatrixStar) ))

#печать матрицы в красивом виде
def printMatrix(Matrix):
	for t in Matrix:
		print(t)


size = int(input("Введите размерность матрицы m x m: "))
firstMatrix = createMatrix(size)
E = createE(size)

if determinant(firstMatrix) == 0:
	print('Определитель = 0, обратной матрицы не существует')
else:
	printMatrix(inverseMatrix(firstMatrix))
