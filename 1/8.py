# 8. Калькулятор матриц 2x2
def matrix_multiply(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

print("Умножение матриц 2x2")
a = [list(map(float, input("Матрица A (через пробел): ").split())),
     list(map(float, input("Строка 2: ").split()))]
b = [list(map(float, input("Матрица B (через пробел): ").split())),
     list(map(float, input("Строка 2: ").split()))]
result = matrix_multiply(a, b)
print("Результат:")
for row in result:
    print([f"{x:.1f}" for x in row])
