import mainWindow

if __name__ == "__main__":
    main = mainWindow.MainWindow()

    main.create()
    # main.addTextures()
    main.addFonts()
    main.registerWindows()

    # main.dpg.show_font_manager()
    main.show()
