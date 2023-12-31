from xml.etree.ElementTree import tostring
import dearpygui.dearpygui as dpg
import generator
from lib.file import get_file_path
from pdfGeneratorUI import PdfGenerator as pdfGen
import os
from PIL import Image, ImageDraw, ImageFont


class TableGenerator:
    assets_folder = "assets/images/"
    WIDTH_FIGURE = 53
    HEIGHT_FIGURE = int(WIDTH_FIGURE * 1.5)

    def __init__(self):
        self.width = 320
        self.height = 300
        self.generator = None
        self.qty = 1
        self.size = "4x4"
        self.type = "Automatico"
        self.progress = 0.0
        self.comodin = 0
        self.double = "No"
        self.specificPosition = "No"
        self.withModel = "No"
        self.manualFromFile = "No"
        self.mode = 0
        self.pdfSizeTable = (0, 0)
        self.outputDir = ""
        with dpg.window(
            label="Generador de tablas",
            width=self.width,
            height=self.height,
            pos=[0, 0],
        ):
            self.typeOfGenerator = dpg.add_radio_button(
                items=("Vista previa", "Automatico"),
                horizontal=True,
                default_value=self.type,
            )

            dpg.add_spacing(count=2)
            self.sizeTableInput = dpg.add_combo(
                label="Tamaño de la tabla",
                items=("4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10"),
                default_value=self.size,
                width=100,
            )
            dpg.add_spacing(count=2)
            self.widthTablePdfInput = dpg.add_combo(
                label="Tamaño de impresión",
                items=(
                    "7.6, 12.4",
                    "7.3, 11.3",
                    "5.4, 9.4",
                    "4.2, 7.2",
                    "7, 10",
                    "5, 8",
                    "6, 8.5",
                    "6.5, 9",
                    "3.4, 5.4",
                    "2.8, 4.8",
                ),
                default_value="7.6, 12.4",
                width=140,
            )

            dpg.add_spacing(count=2)
            self.qtyTableInput = dpg.add_input_int(
                label="Cantidad de tablas",
                default_value=self.qty,
                step=1,
                min_value=1,
                width=100,
            )

            dpg.add_spacing(count=2)
            self.comodinInput = dpg.add_input_int(
                label="Comodin",
                default_value=self.comodin,
                step=1,
                min_value=0,
                max_value=54,
                width=100,
            )

            dpg.add_spacing(count=2)
            self.label1 = dpg.add_text("¿Doble comodin?")
            self.doubleComodin = dpg.add_radio_button(
                items=("No", "Si"), horizontal=True, default_value="No"
            )

            dpg.add_spacing(count=2)
            self.saveButton = dpg.add_button(
                label="Generar", callback=self.handleGenerate, tag="saveButton"
            )
            self.generateFullComodin = dpg.add_button(
                label="Generar 54 comodines dobles",
                callback=self.handleGenerateFull,
                tag="generateFullComodin",
            )
            self.generateComodin = dpg.add_button(
                label="Generar con 1 comodin en medio o esquinas",
                callback=self.handleGenerateComodinSpecific,
                tag="generateComodinMiddle",
            )
            self.generateWithModel = dpg.add_button(
                label="Generar con modelo pozo1-esquinas2",
                callback=self.handleGenerateWithModel,
                tag="generateWithModel",
            )
            dpg.add_spacing(count=4)
            self.manualFromFileButton = dpg.add_button(
                label="Generar desde archivo",
                callback=self.handleGenerateManual,
                tag="manualFromFile"
            )
            self.progressBar = dpg.add_progress_bar(
                label="Progreso", default_value=self.progress, width=self.width
            )


    def handleGenerateManual(self):
        self.mode = 4
        self.handleGenerate()

    def handleGenerateWithModel(self):
        self.mode = 3
        self.handleGenerate()

    def handleGenerateComodinSpecific(self):
        self.mode = 2
        self.handleGenerate()

    def handleGenerateFull(self):
        self.mode = 1
        self.handleGenerate()

    def handleGenerate(self):
        self.qty = dpg.get_value(self.qtyTableInput)
        self.size = dpg.get_value(self.sizeTableInput)
        self.type = dpg.get_value(self.typeOfGenerator)
        self.comodin = dpg.get_value(self.comodinInput)
        self.double = dpg.get_value(self.doubleComodin)
        if self.comodin > 54:
            self.comodin = 54

        if self.mode == 0:
            self.generateAutomatic()
        if self.mode == 1:
            if self.size == "5x5":
                self.qty = 1

                self.comodin = 1
                for i in range(1, 55):
                    self.generateAutomatic()
                    self.comodin = i + 1
        if self.mode == 2:
            self.specificPosition = "Si"
            self.generateAutomatic()
        if self.mode == 3:
            self.withModel = "Si"
            self.generateAutomatic()
        if self.mode == 4:
            self.manualFromFile = "Si"
            self.generateAutomatic()

        w = float(dpg.get_value(self.widthTablePdfInput).strip().split(",")[0])
        h = float(dpg.get_value(self.widthTablePdfInput).strip().split(",")[1])
        fileName = input("***/ Nombre del archivo: ")
        pdf = pdfGen(filename=str(fileName).strip(), size=(w, h), folder=self.outputDir)
        pdf.generate()

    def generateAutomatic(self):
        self.generator = generator.Generator(
            self.qty,
            self.size,
            self.comodin,
            self.double,
            self.specificPosition,
            self.withModel,
            self.manualFromFile
        )

        with dpg.window(label="Generador", width=300, height=220, pos=[self.width, 0]):
            dpg.add_text(str(self.generator))
        print("Generando...")
        self.progress = 0.0
        step = 1 / self.qty

        folder_exists = os.path.exists("tablas")
        if not folder_exists:
            os.mkdir("tablas")
        if folder_exists:
            size = self.size.split("x")
            num_filas = int(size[0])
            num_columnas = int(size[1])

            w, h = 800, 1200
            # w, h = 300, 600
            local_image = Image.new(
                "RGB",
                (w, h),
                (255, 255, 255),
            )
            print("Generando tablas...")
            self.outputDir = get_file_path()

            for tabla in self.generator.tablas:
                print(tabla)
                # print("TABLA:   " + str(tabla) + "\n *********************")
                # print(self.progress)
                self.progress += step
                # print(tabla)
                for i in range(num_filas):
                    for j in range(num_columnas):
                        figura = tabla[i][j]
                        ruta_imagen = f"{self.assets_folder}{figura}.jpg"
                        imagen = Image.open(ruta_imagen)
                        imagen = imagen.resize(
                            (int(w / num_columnas), int(h / num_filas)),
                            Image.LANCZOS,
                        )
                        draw = ImageDraw.Draw(imagen)
                        draw.rectangle(
                            (0, 0, int(w / num_columnas), int(h / num_filas)),
                            outline=(0, 0, 0),
                            width=2,
                        )
                        local_image.paste(
                            imagen,
                            (j * int(w / num_columnas), i * int(h / num_filas)),
                        )

                outFolder = os.path.exists(self.outputDir)
                if outFolder:
                    num = len(os.listdir(self.outputDir))
                else:
                    num = 0

                local_image.save(
                    self.outputDir + f"/tabla{num}_{num_filas}x{num_columnas}.jpg",
                    quality=95,
                    optimize=True,
                    dpi=(96, 96),
                )
                print(
                    self.outputDir
                    + f"/tabla{num}_{num_filas}x{num_columnas}.jpg"
                    + "  guardado....."
                )

                # print(f"Progress{self.progressBar}. Value: {self.progress}")
                dpg.set_value(self.progressBar, self.progress)
            # with open(f"tablas/{self.qty}x{self.size}.txt", "w") as file:
            #     file.write(str(self.generador))
            # Contar cuantas tablas hay en la carpeta
        self.progress = "completado"

    def generatePreview(self):
        pass
