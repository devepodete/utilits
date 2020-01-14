def matrixInput():
	print("Введите размерность матрицы m x n")
	m = int(input())
	n = int(input())
	a = []
	print("Введите элементы матрицы")
	for t in range(m):
		a.append([])
		for i in range(n):
			a[t].append(float(input()))

	return a


def matrixMultiply(a,b):
	result = []
	for t in range(len(a)):
		result.append([])
		for k in range(len(b[0])):
			result[t].append(0)

	for t in range(len(a)):
		for k in range(len(b[0])):
			for j in range(len(a[0])):
				result[t][k] += a[t][j]*b[j][k]

	return result


a = matrixInput()
b = matrixInput()
if len(a[0]) != len(b):
	print("Такие матрицы нельзя перемножить")
else:
	c = matrixMultiply(a,b)
	for t in range(len(c)):
		print(c[t])
