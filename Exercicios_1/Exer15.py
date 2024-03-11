import numpy as np

def adicao_matrizes(matriz1, matriz2):
   
    if matriz1.shape != matriz2.shape:
        return "As matrizes devem ter o mesmo formato para realizar a adição."
    else:
        return matriz1 + matriz2

def inversa_matriz(matriz):
   
    if matriz.shape[0] != matriz.shape[1]:
        return "A matriz deve ser quadrada para calcular a inversa."
    else:
        try:
            inversa = np.linalg.inv(matriz)
            return inversa
        except np.linalg.LinAlgError:
            return "A matriz não é inversível."

def multiplicacao_escalar(matriz, escalar):
   
    return matriz * escalar

matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
escalar = 2

print("Adição de matrizes:")
print(adicao_matrizes(matriz1, matriz2))

print("\nInversa da matriz:")
print(inversa_matriz(matriz1))

print("\nMultiplicação escalar:")
print(multiplicacao_escalar(matriz1, escalar))
