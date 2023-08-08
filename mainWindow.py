import dearpygui.dearpygui as dpg
import tableGeneratorUI as tableGenerator
import figureSearcherUI as figureSearcher
import os

class MainWindow:
    def __init__(self):
        self.title = "Loteria Utilitys"
        self.windowWidth = 1000
        self.windowHeight = 700
        self.dpg = dpg
        self.windows = []
        self.addWindows()

    def create(self):
        self.dpg.create_context()
        self.dpg.create_viewport(title=self.title, width=self.windowWidth, height=self.windowHeight)


    def show(self):
        self.dpg.setup_dearpygui()
        self.dpg.show_viewport()
        self.dpg.start_dearpygui()
        self.dpg.destroy_context()

    def addWindows(self):
        self.windows.append(tableGenerator.TableGenerator)
        # self.windows.append(figureSearcher.FigureSearcher)

    def registerWindows(self):
        for window in self.windows:

            window()

    def addTextures(self):
        if not os.path.exists("assets/images/"):
            os.mkdir("assets/images/")
        num_files = len(os.listdir("assets/images/"))

        with dpg.texture_registry(show=False):
            for i in range(num_files):
                if 0 < i < 55:
                    _data = dpg.load_image(f"assets/images/{i}.jpg")
                    dpg.add_static_texture(
                        width=_data[0],
                        height=_data[1],
                        default_value=_data[3],
                        tag="texture_tag_{}".format(i),
                    )
                    # print(type(_data))

    def addFonts(self):
        with self.dpg.font_registry():
            default_font = self.dpg.add_font("assets/fonts/OpenSans-Regular.ttf", 18, default_font=True)

        dpg.bind_font(default_font)