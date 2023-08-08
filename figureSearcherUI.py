import dearpygui.dearpygui as dpg


class FigureSearcher:
    def __init__(self):
        self.windowName = "Buscador de figuras"
        self.windowSize = (500, 500)
        self.windowPos = (0, 300)
        self.dpg = dpg
        with dpg.window(label=self.windowName, min_size=self.windowSize, pos=self.windowPos):
            dpg.add_clipper(tag="clipper")
            # dpg.add_image("texture_tag_1", width=80, height=round(80*1.5))
            # for i in range(1, 55):
            #
            #     dpg.add_image(texture_tag=f"texture_tag_{i}", tag=f"image_{i}", width=100, height=100)