from fpdf import FPDF
import os
import re

# from lib.file import get_file_path


class PdfGenerator:
    elementoscontados = 0
    pagcontadas = 0
    margin_left = 1
    margin_top = 0.5

    def __init__(self, filename="", size=(5, 7), folder="tablas"):
        self.pdf = FPDF(orientation="P", unit="cm", format="A4")
        self.filename = filename
        self.folder = folder
        self.size = size
        self.paperSize = (21, 28)
        self.margin = 0

    def ordenar_nombre_archivo(self, archivo):
        # Extraeríamos el número en el nombre del archivo usando una expresión regular
        numero = int(re.search(r"\d+", archivo).group())
        return numero

    def generate(self):
        jpg_files = [file for file in os.listdir(self.folder) if file.endswith(".jpg")]
        jpg_files.sort(key=self.ordenar_nombre_archivo)
        print(jpg_files)

        img_width, img_height = self.size
        effective_paper_width = self.paperSize[0] - self.margin_left
        effective_paper_height = self.paperSize[1] - self.margin_top
        images_per_row = int(effective_paper_width // img_width)
        images_per_column = int(effective_paper_height // img_height)
        max_images_per_page = images_per_row * images_per_column
        print(max_images_per_page)

        for index, tabla in enumerate(jpg_files):
            if index % max_images_per_page == 0:
                self.pdf.add_page()

            ind_in_page = index % max_images_per_page
            xOffset = self.margin_left + (ind_in_page % images_per_row) * img_width
            yOffset = self.margin_top + (ind_in_page // images_per_row) * img_height

            self.pdf.image(
                f"{self.folder}/{tabla}",
                x=xOffset,
                y=yOffset,
                w=img_width,
                h=img_height,
            )

        if not os.path.exists("tablas/_PDF/"):
            os.mkdir("tablas/_PDF/")
        self.pdf.output(f"tablas/_PDF/{self.filename}.pdf")


if __name__ == "__main__":
    filename = str(input("Filename: "))
    width = float(input("Width: "))
    height = float(input("Height: "))
    folderName = str(input("Folder: "))
    size = (width, height)
    pdf = PdfGenerator(filename=filename, size=size, folder=folderName)
    pdf.generate()
