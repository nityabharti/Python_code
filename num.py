"""
numpy --> num-py

# """
import numpy as np

# a=np.array([1,2,3])
# print(a)
# print(type(a))
# print(a.shape)
# print(a[0],a[1],a[2])

# b=np.array([[1,2,3],[4,5,6],[7,8,9],[4,5,7]])
# print(b)
# print(b.shape)
# print(b[2][1])
# print(b[3][2])

# a=np.zeros([50,50])
# print(a)

# a=np.ones([5,6])
# print(a)

# a=np.full((4,5),2000)
# print(a)

# a=np.eye(4)
# print(a)

a=np.random.randint(1,99, (2,2))
print(a)

x=np.array([[3,4],[7,6]])
y=np.array([[5,4],[9,8]])

# print(np.add(x,y))
print(x+y)
print(np.subtract(x,y))
print(np.subtract(y,x))
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.sqrt(x))
print(np.dot(x,y))



