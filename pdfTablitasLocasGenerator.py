from fpdf import FPDF
import os
import json
import sys


class PDFGenerator:
    charset = "utf-8"

    def __init__(self, filename="tablitasLocas", size=(7.6, 12.4)):
        self.pdf = FPDF(orientation="P", unit="cm", format="A4")
        self.pdf.add_font(
            "NunitoSansRegular", "", "assets/fonts/NunitoSans_7pt-Regular.ttf", uni=True
        )
        self.filename = filename
        self.size = size
        with open("figuras.json", "r", encoding=self.charset) as json_file:
            self.data = json.load(json_file)

    def generate(self):
        texts = [value.get("name") for key, value in self.data.items()]
        print(texts)
        self.pdf.add_page()

        self.pdf.set_font("NunitoSansRegular", size=18)
        for text, figureSrc in self.data.items():
            self.pdf.cell(0, 2, f"Doble comodin", ln=True, align="L")
            x, y = self.pdf.get_x(), self.pdf.get_y() - 2
            # Añadir imagen
            self.pdf.image(f"{figureSrc.get('src')}", x=8, y=y, w=1.26, h=1.26 * 1.5)
            self.pdf.line(x, y + 3, x + 19, y + 3)
            self.pdf.set_xy(x, y + 4)

        self.pdf.output(self.filename + ".pdf")


if __name__ == "__main__":
    pdf = PDFGenerator(filename="tablitasLocas", size=(7.6, 12.4))
    # for key, value in pdf.data.items():
    #     print(key, value.get("src"))

    pdf.generate()
