import numpy as np
import random


def generar_matriz(comodin=0, size=0):
    if comodin < 1 or size < 1:
        return
    matrices = []
    lastPozo = []
    for i in range(2):
        np.random.shuffle(lastPozo)
        print(lastPozo)
        print(i)
        numeros = [i for i in range(1, 55) if i != comodin and i not in lastPozo]
        np.random.shuffle(numeros)
        if i == 0:
            matriz = np.random.choice(numeros, size=(size, size), replace=False)
            position = np.random.randint(4)
            if position == 0:
                matriz[1, 1] = comodin
            elif position == 1:
                matriz[1, 2] = comodin
            elif position == 2:
                matriz[2, 1] = comodin
            elif position == 3:
                matriz[2, 2] = comodin
            lastPozo = [matriz[1, 1], matriz[1, 2], matriz[2, 1], matriz[2, 2]]
        elif i == 1:
            matriz = np.random.choice(numeros, size=(size, size), replace=False)
            positions = [0, 1, 2, 3]
            for i in range(4):
                position = random.choice(positions)
                positions.remove(position)
                randomChoice = random.choice(lastPozo)
                print(randomChoice)
                lastPozo.remove(randomChoice)
                if position == 0:
                    matriz[0, 0] = randomChoice
                elif position == 1:
                    matriz[0, 3] = randomChoice
                elif position == 2:
                    matriz[3, 0] = randomChoice
                elif position == 3:
                    matriz[3, 3] = randomChoice
            lastPozo = []
        matrices.append(matriz)

    return matrices[0], matrices[1]


def generar_N_matrices(n=0, comodin=0, size=0):
    matrices = []

    for i in range(int(n / 2)):
        matriz1, matriz2 = generar_matriz(comodin=comodin, size=size)
        matrices.append(matriz1)
        matrices.append(matriz2)
    return matrices


# Uso de las funciones:
matrices = generar_N_matrices(n=4, comodin=1, size=4)
for i, matriz in enumerate(matrices):
    print(f"Matriz {i+1}:\n{matriz}\n")
