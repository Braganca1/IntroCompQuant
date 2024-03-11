import numpy as np

ma1=np.empty((3,3),dtype=complex)
ma2=np.empty((3,3),dtype=complex)

for i in ([0,1,2]):
    for j in ([0,1,2]):
        ma1[i][j]=complex(input("Digite os elementos da matriz1 3x3: "))

for i in ([0,1,2]):
    for j in ([0,1,2]):
        ma2[i][j]=complex(input("Digite os elementos da matriz2 3x3: "))

print(np.dot(ma1,ma2))

