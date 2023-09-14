import mainWindow
from models.Tabla import Tabla
from models.TablaComodin import TablaComodin


tabla1 = Tabla("4x4")
tablaComodin = TablaComodin("4x4", 2)
if __name__ == "__main__":
    main = mainWindow.MainWindow()

    main.create()
    # main.addTextures()
    main.addFonts()
    main.registerWindows()

    # main.dpg.show_font_manager()
    main.show()
