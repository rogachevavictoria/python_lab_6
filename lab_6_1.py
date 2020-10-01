import random

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

matrix = []


def fill_matrix():
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(random.randint(1, 100)))
        matrix.append(a)


def print_matrix():
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()


def median():
    minimal = 9999
    for i in range(m):
        matrix[i].sort()
        if n % 2 == 0:
            b = (matrix[i][round(n / 2)] + matrix[i][round((n - 1) / 2)]) / 2
        else:
            b = matrix[i][round(n / 2)]
        if b < minimal:
            minimal = b
            x = i
    print('Smallest median:', minimal, '\nRow:', x)


fill_matrix()
print_matrix()
median()

