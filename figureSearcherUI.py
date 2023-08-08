import dearpygui.dearpygui as dpg

class FigureSearcher:
    def __init__(self):
        self.windowName = "Buscador de figuras"
        self.windowSize = (500, 500)
        self.windowPos = (0, 300)
        self.dpg = dpg
        with dpg.window(label=self.windowName, min_size=self.windowSize, pos=self.windowPos):
            self.dpg.add_clipper(pos=[0, 0], width=500, height=500, tag="clipper")