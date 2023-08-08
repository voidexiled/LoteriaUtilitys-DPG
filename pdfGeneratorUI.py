from fpdf import FPDF
import os

class PdfGenerator:
    xOffset = 0
    yOffset = 0
    ekis = 3
    ye = 1
    tablascontadas = 0

    def __init__(self, filename="test"):
        self.pdf = FPDF(orientation='P', unit='cm', format='A4')
        self.filename = filename


    def generate(self):
        tablas = os.listdir("tables")

        self.pdf.add_page()
        for tabla in tablas:
            if self.tablascontadas == 0:
                self.xOffset = 0 + self.ekis
                self.yOffset = 0 + self.ye
            if self.tablascontadas == 1:
                self.xOffset = 7.6 + self.ekis
                self.yOffset = 0 + self.ye
            if self.tablascontadas == 2:
                self.xOffset = 0 + self.ekis
                self.yOffset = 12.4 + self.ye
            if self.tablascontadas == 3:
                self.xOffset = 7.6 + self.ekis
                self.yOffset = 12.4 + self.ye
            print(f"tabla: {tabla}, xOffset: {self.xOffset}, yOffset: {self.yOffset}")
            self.pdf.image(f'tables/{tabla}', x=self.xOffset, y=self.yOffset, w=7.6, h=12.4)
            self.tablascontadas += 1
            if self.tablascontadas == 4:
                self.tablascontadas = 0

                self.pdf.add_page()
        self.pdf.output(self.filename+".pdf")
