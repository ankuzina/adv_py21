import numpy as np
print(1)
x = np.arange(12,43)
print(x)
print(2)
x = np.zeros(12)
x[4] = 1
print(x)
print(3)
matrix = np.array([range(0,3), range(3,6), range(6,9)])
print(matrix)
print(4)
x = np.array([1,2,0,0,4,0])
def more_than(ar,value):
     return ar[ar>value]
print(more_than(x,0))

print(5)
a = np.array([[1, 0, 3], [4, 0, 1], [4, 5, 1], [7, 2, 3], [8, 5, 1]])
b = np.array([[4, 1], [2, 2], [3, 7]])
r1 = np.dot(a, b)
print(r1)
print(6)
c = np.ones((10, 10))
c[1:-1,1:-1] = 0
print(c)

print(7)
x = np.random.randint(0, 100, (1, 10))
print(x)
x.sort()
print(x)

print(8)
x = np.arange(4).reshape(2,2)
for index, value in np.ndenumerate(x):
    print(index, value)
for index in np.ndindex(x.shape):
    print(index, x[index])

print(9)
x = np.random.randint(0, 100, (1, 10)) #random vector
print(x)
length = np.linalg.norm(x)
print(length)
norm = x/length
print(norm)

print(10)
x = np.random.randint(0, 100, (1, 10))
def nearest_value(array, number):
    array = array.ravel()
    print(array)
    idx = np.abs(array - number).argmin()
    return array[idx]
print("vvedite chislo:")
n = int(input())
print(nearest_value(x, n))

print(11)
print("vvedite chislo:")
n = int(input())
x = np.random.randint(0, 100, (1, 10))
x.sort()
print(x)
print(x[0][(n-2):])