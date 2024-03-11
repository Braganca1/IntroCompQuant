import numpy as np

ma=np.empty((3,3),dtype=complex)

for i in ([0,1,2]):
    for j in ([0,1,2]):
        ma[i][j]=complex(input("Digite os elementos da matriz 3x3: "))


print(f"Matria inserida:\n {ma}")
print(f"Conjugada transposta:\n {np.conjugate(np.transpose(ma))}")