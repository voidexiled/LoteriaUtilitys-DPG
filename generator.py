import numpy as np
from prettytable import PrettyTable


class Generator:
    debug = False

    def __init__(self, qty=0, size="4x4", comodin=0, double="No", specificPosition="No"):
        self.qty = qty
        self.size = size
        self.comodin = comodin
        self.double = double
        self.specificPosition = specificPosition
        self.tablas = []
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
        print(self.qty)
        for _ in range(self.qty):
            a = np.arange(1, 54 + 1)
            if self.double == "Si":
                tabla = np.random.choice(np.delete(a, np.where(a == self.comodin)), size=(num_rows, num_cols), replace=False)
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
                    print(f"APARICIONES: {apariciones}")
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
                                    tabla[int(num_rows / 2), int(num_cols / 2)] = self.comodin
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
                    tabla[int(num_rows/2), int(num_cols/2)] = self.comodin

            self.tablas.append(tabla)
            if self.debug:
                self.verifyTable(tabla)
        print(self.tablas)

    def verifyTable(self, table):
        print("####### Verify Table ########")
        for row in table:
            for i in row:
                for _row in table:
                    if i in _row:
                        print("Repetido")
                        return False

        print("####### Verify Table ########")

    def __str__(self):
        msg = f"qty: {self.qty}, size: {self.size}"

        return msg + "\n" + str(self.x)
