import numpy as np

myList = [1,2,3,4]

arr = np.array(myList)
print(arr)
print(type(arr))
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.argmin())
print(arr.argmax())
print(arr.reshape(2,2))

print(np.zeros((5,5)))

print(np.ones((2,2)))

print(np.random.randint(0,100))

print(np.random.randint(0,100,(5,5)))

print(np.random.seed(101))

print(np.random.rand)

print(np.linspace(0,10,6))

print(np.linspace(0,10,102))

mat = np.arange(0,100).reshape(10,10)

print(mat>50)
print(mat[mat>50])