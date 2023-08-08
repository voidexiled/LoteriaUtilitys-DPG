import dearpygui.dearpygui as dpg
import generator
from pdfGeneratorUI import PdfGenerator as pdfGen
import os
from PIL import Image, ImageDraw, ImageFont


class TableGenerator:
    assets_folder = "assets/images/"
    WIDTH_FIGURE = 53
    HEIGHT_FIGURE = int(WIDTH_FIGURE * 1.5)

    def __init__(self):

        self.width = 300
        self.height = 220
        self.generador = None
        self.qty = 1
        self.size = "4x4"
        self.type = "Automatico"
        self.progress = 0.0
        self.comodin = 0
        with dpg.window(label="Generador de tablas", width=self.width, height=self.height, pos=[0, 0]):
            self.typeOfGenerator = dpg.add_radio_button(items=("Vista previa", "Automatico"), horizontal=True, default_value=self.type)

            dpg.add_spacing(count=2)
            self.sizeTableInput = dpg.add_combo(label="Tamaño de la tabla", items=("4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10"), default_value=self.size, width=100)

            dpg.add_spacing(count=2)
            self.qtyTableInput = dpg.add_input_int(label="Cantidad de tablas", default_value=self.qty, step=1, min_value=1, width=100)

            dpg.add_spacing(count=2)
            self.comodinInput = dpg.add_input_int(label="Comodin", default_value=self.comodin, step=1, min_value=0, max_value=54, width=100)

            dpg.add_spacing(count=2)
            self.saveButton = dpg.add_button(label="Generar", callback=self.handleGenerate, tag="saveButton")

            dpg.add_spacing(count=4)
            self.progressBar = dpg.add_progress_bar(label="Progreso", default_value=self.progress, width=self.width)

    def handleGenerate(self):
        self.qty = dpg.get_value(self.qtyTableInput)
        self.size = dpg.get_value(self.sizeTableInput)
        self.type = dpg.get_value(self.typeOfGenerator)
        self.comodin = dpg.get_value(self.comodinInput)
        if self.comodin > 54:
            self.comodin = 54

        print(self.qty, self.size, self.type, self.comodin)
        if self.type == "Automatico":
            self.generateAutomatic()
            pdf = pdfGen(filename="test")
            pdf.generate()

        else:
            self.generatePreview()

    def generateAutomatic(self):
        self.generador = generator.Generator(self.qty, self.size, self.comodin)
        # print(self.generador)
        with dpg.window(label="Generador", width=300, height=220, pos=[self.width, 0]):
            dpg.add_text(str(self.generador))
        print("Generando...")
        self.progress = 0.0
        step = 1 / self.qty

        folder_exists = os.path.exists("tables")
        if not folder_exists:
            os.mkdir("tables")
        if folder_exists:

            size = self.size.split("x")
            num_filas = int(size[0])
            num_columnas = int(size[1])
            # ventana_ancho = num_columnas * self.WIDTH_FIGURE
            # ventana_alto = num_filas * self.HEIGHT_FIGURE

            local_image = Image.new(
                "RGB",
                (800, 1200),
                (255, 255, 255),
            )
            print("Generando tablas...")
            for tabla in self.generador.tables:
                print(self.progress)
                self.progress += step
                print(tabla)
                for i in range(num_filas):
                    for j in range(num_columnas):
                        figura = tabla[i][j]
                        ruta_imagen = f"{self.assets_folder}{figura}.jpg"
                        imagen = Image.open(ruta_imagen)
                        imagen = imagen.resize(
                            (int(800 / num_columnas), int(1200 / num_filas)), Image.LANCZOS
                        )
                        draw = ImageDraw.Draw(imagen)
                        draw.rectangle(
                            (0, 0, int(800 / num_columnas), int(1200 / num_filas)),
                            outline=(0, 0, 0),
                            width=2,
                        )
                        local_image.paste(
                            imagen, (j * int(800 / num_columnas), i * int(1200 / num_filas))
                        )
                num = len(os.listdir("tables"))
                print(num)
                local_image.save(
                    f"tables/tabla{num}_{num_filas}x{num_columnas}.jpg",
                    quality=95,
                    optimize=True,
                    dpi=(96, 96),
                )
                print(f"Progress{self.progressBar}. Value: {self.progress}")
                dpg.set_value(self.progressBar, self.progress)
            # with open(f"tables/{self.qty}x{self.size}.txt", "w") as file:
            #     file.write(str(self.generador))
            # Contar cuantas tablas hay en la carpeta
        self.progress = "completado"

    def generatePreview(self):
        pass

