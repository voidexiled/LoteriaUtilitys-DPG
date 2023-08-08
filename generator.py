import numpy as np
from prettytable import PrettyTable


class Generator:
    debug = False

    def __init__(self, qty=0, size="4x4", comodin=0):
        self.qty = qty
        self.size = size
        self.comodin = comodin
        self.tables = []
        self.generateTables()

        ########### PRINT TABLES ############
        self.x = PrettyTable()
        for row in self.tables:
            self.x.add_row(row)

    def generateTables(self):
        size = self.size.split("x")

        # for i in range(self.qty):
        #     table = []
        #     for j in range(int(size[0])):
        #         table.append(np.random.randint(1, 54, size=int(size[1])))
        #     self.tables.append(table)
        num_rows = int(size[0])
        num_cols = int(size[1])
        # "4x4"
        # [4,4]

        for _ in range(self.qty):
            tabla = np.random.choice(
                np.arange(1, 54 + 1), size=(num_rows, num_cols), replace=False
            )

            # Colocar el comodín en una posición aleatoria
            if self.comodin > 0:
                apariciones = 0
                for row in tabla:
                    for i in row:
                        if i == self.comodin:
                            apariciones += 1
                print(f"APARICIONES: {apariciones}")
                if apariciones == 0:
                    row = np.random.randint(num_rows)
                    col = np.random.randint(num_cols)
                    tabla[row, col] = self.comodin

            self.tables.append(tabla)
            if self.debug:
                self.verifyTable(tabla)

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
