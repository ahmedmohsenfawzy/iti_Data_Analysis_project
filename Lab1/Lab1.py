import numpy as np

# 1
arrd1 = np.arange(10,51,5)
print(arrd1)

# 2
arrzero = np.zeros((4,6))
arrzero[3][3] = 99
print(arrzero)

#3
arr = np.array([12,45,7,19,88,3,56,91,24,67])

print(arr[arr > 50])

#4
i = np.eye(5)
i_new = i * [10,20,30,40,50]
print(i_new)

#5
x = np.arange(1,21).reshape(4,5)
#a
print(x[-2:])
#b
print(x[: , 2])
#c
print(x[:3 , 2:])


#6
a = np.array([1,2,3,4]) 
b = np.array([[10],
               [20],
               [30]])

print(a + b) # the a and b get casted to (3,4)

#7
data = np.array([150,220,90,300,180,45])
data_norm = (data - min(data)) / (max(data) - min(data))
print(data_norm)

#8
data_stad = (data - data.mean()) / data.std()
print(data_stad)

#9
mat = np.array([
    [4,8,1,12],
    [7,3,9,5],
    [11,2,6,10],
    [15,0,14,13]
])
#a
print(mat.mean(axis=1))
#b
print(mat.sum(axis=0))
#c
print(mat.max())
print(mat.argmax())


#10
d = np.arange(36)
d_resh  = d.reshape(3,4,3)
print(d_resh)

#11
arr = np.arange(1,17).reshape(4,4)
print(arr.T)

#12
ages=np.array([23,45,19,34,28,51,17,39])
names=np.array(["ali","sara","omar","lina","khaled","nour","yara","hassan"])
print(names[(ages<=40) & (ages>=20)])

#13
ages[ages < 20] = 20
print(ages)


#14
np.random.seed(123)
arrF = np.random.randint(1,101,(6,6))

print(arrF)

#15
np.random.seed(None)
nums = np.random.normal(loc=10,scale=15,size=10)
print(nums)

#16 
np.random.seed(None)
colors = ["red", 'blue', 'green','yellow','purple']
x = np.random.choice(colors,size=3,replace=False)
print(x)

#17
h = np.arange(1,21)
np.random.shuffle(h)
print(h)

