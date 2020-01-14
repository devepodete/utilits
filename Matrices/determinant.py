def createMatrix(size):
	a = []
	for t in range(size):
		a.append([])
		for k in range(size):
			a[t].append(0)
	print("Введите элементы матрицы")
	for t in range(size):
		for k in range(size):
			a[t][k] = float(input())

	return a


def printMatrix(Matrix):
	for a in Matrix:
		print(a)


def newMatrix(Matrix,j):
	Matrix2 = []
	for t in range(len(Matrix)):
		Matrix2.append([])
		for k in range(len(Matrix[t])):
			Matrix2[t].append(Matrix[t][k])
	del Matrix2[0]
	for t in range(len(Matrix2)):
		del Matrix2[t][j]

	return Matrix2


def determinant(Matrix):
	if (len(Matrix) == 1 and len(Matrix[0]) == 1):
		return Matrix[0][0]
	else:
		det = 0
		for j in range(len(Matrix)):
			det += ((-1)**(1+j+1))*Matrix[0][j]*determinant(newMatrix(Matrix,j))

		return det

a = createMatrix(int(input('Введите размер матрицы \n')))
print("Определитель = ",determinant(a))