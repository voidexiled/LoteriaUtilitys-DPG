import numpy as np
from prettytable import PrettyTable
import random


class Generator:
    debug = False

    def __init__(
        self,
        qty=0,
        size="4x4",
        comodin=0,
        double="No",
        specificPosition="No",
        withModel="No",
    ):
        self.qty = qty
        self.size = size
        self.comodin = comodin
        self.double = double
        self.specificPosition = specificPosition
        self.tablas = []
        self.withModel = withModel
        self.generateTablas()

        ########### PRINT TABLES ############
        self.x = PrettyTable()
        for row in self.tablas:
            self.x.add_row(row)

    def generateTablas(self):
        size = self.size.split("x")

        num_rows = int(size[0])
        num_cols = int(size[1])
        # "4x4"
        # [4,4]

        if self.withModel == "Si":
            if self.double != "Si" and self.specificPosition != "Si":
                self.generar_N_matrices(n=self.qty, size=num_rows, comodin=self.comodin)
                return

        for _ in range(self.qty):
            a = np.arange(1, 54 + 1)
            if self.double == "Si":
                tabla = np.random.choice(
                    np.delete(a, np.where(a == self.comodin)),
                    size=(num_rows, num_cols),
                    replace=False,
                )
            else:
                tabla = np.random.choice(a, size=(num_rows, num_cols), replace=False)

            # Colocar el comodín en una posición aleatoria
            if self.double == "No":
                if self.comodin > 0:
                    apariciones = 0
                    for row in tabla:
                        for i in row:
                            if i == self.comodin:
                                apariciones += 1

                    if apariciones == 0:
                        if self.specificPosition == "No":
                            row = np.random.randint(num_rows)
                            col = np.random.randint(num_cols)
                            tabla[row, col] = self.comodin
                        else:
                            ## 0 = ARRIBA IZQUIERDA, 1 = ARRIBA DERECHA, 2 = ABAJO IZQUIERDA, 3 = ABAJO DERECHA, 4 = EN MEDIO ##
                            place = np.random.randint(5)
                            if place == 0:
                                tabla[0, 0] = self.comodin
                            elif place == 1:
                                tabla[0, num_cols - 1] = self.comodin
                            elif place == 2:
                                tabla[num_rows - 1, 0] = self.comodin
                            elif place == 3:
                                tabla[num_rows - 1, num_cols - 1] = self.comodin
                            elif place == 4:
                                if self.size == "5x5":
                                    ## COMODIN EN LA FIGURA DE EN MEDIO ##
                                    tabla[
                                        int(num_rows / 2), int(num_cols / 2)
                                    ] = self.comodin
                                elif self.size == "4x4":
                                    ## COMODIN EN UNO DE LOS 4 FIGURAS DE EN MEDIO ##
                                    square = np.random.randint(4)
                                    if square == 0:
                                        tabla[1, 1] = self.comodin
                                    elif square == 1:
                                        tabla[1, 2] = self.comodin
                                    elif square == 2:
                                        tabla[2, 1] = self.comodin
                                    elif square == 3:
                                        tabla[2, 2] = self.comodin
            if self.double == "Si":
                if self.comodin > 0:
                    ## COMODIN EN UNA DE LAS 4 ESQUINAS ##
                    esquina = np.random.randint(4)
                    if esquina == 0:
                        tabla[0, 0] = self.comodin
                    elif esquina == 1:
                        tabla[0, num_cols - 1] = self.comodin
                    elif esquina == 2:
                        tabla[num_rows - 1, 0] = self.comodin
                    elif esquina == 3:
                        tabla[num_rows - 1, num_cols - 1] = self.comodin

                    ## COMODIN EN EL CENTRO ##
                    tabla[int(num_rows / 2), int(num_cols / 2)] = self.comodin

            self.tablas.append(tabla)
            if self.debug:
                self.verifyTable(tabla)

    def generar_matriz(self, comodin=0, size=0):
        if comodin < 1 or size < 1:
            return
        matrices = []
        lastPozo = []
        for i in range(2):
            np.random.shuffle(lastPozo)

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
            self.verifyTable(matriz)
            matrices.append(matriz)

        return matrices[0], matrices[1]

    def generar_N_matrices(self, n=0, comodin=0, size=0):
        matrices = []

        for i in range(int(n / 2)):
            matriz1, matriz2 = self.generar_matriz(comodin=comodin, size=size)
            matrices.append(matriz1)
            matrices.append(matriz2)
        self.tablas = matrices

    # Uso de las funciones:

    def verifyTable(self, table):
        print("####### Verify Table ########")
        # Aplanamos la matriz a una lista
        lista = table.flatten()

        # Convertir la lista a un conjunto para eliminar duplicados
        conjunto = set(lista)

        if len(lista) != len(conjunto):
            print("Hay elementos repetidos en la matriz.")

        print("####### Verify Table ########")

    def __str__(self):
        msg = f"qty: {self.qty}, size: {self.size}"

        return msg + "\n" + str(self.x)
