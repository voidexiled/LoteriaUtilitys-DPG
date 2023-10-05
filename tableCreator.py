import dearpygui.dearpygui as dpg
import os
import re

assets_folder = "assets/images/"
dpg.create_context()
dpg.create_viewport(title="Table Editor", width=1000, height=800)
selected = None
images = [img for img in os.listdir(assets_folder) if img.endswith(".jpg")]


def setSelected(tag):
    global selected
    print(tag)
    selected = tag


def ordenar_nombre_archivo(archivo):
    # Extraeríamos el número en el nombre del archivo usando una expresión regular
    numero = int(re.search(r"\d+", archivo).group())
    return numero


for img in images:
    print(img)
    img = assets_folder + img
    width, height, channels, data = dpg.load_image(file=img)

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag=img)


with dpg.window(label="Current Table", width=500, height=500, pos=[0, 0]):
    with dpg.table(header_row=False):
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(1, 5):
            with dpg.table_row():
                for j in range(1, 5):
                    dpg.add_image_button(
                        texture_tag=assets_folder + images[i * j],
                        width=100,
                        height=100,
                        callback=lambda: print(selected),
                    )
                    dpg.add_table_next_column()

with dpg.window(label="Selector", width=300, height=700, pos=[520, 0]):
    jpg_files = [file for file in os.listdir(assets_folder) if file.endswith(".jpg")]
    jpg_files.sort(key=ordenar_nombre_archivo)
    print(jpg_files)

    for img in jpg_files:
        dpg.add_image_button(
            texture_tag=assets_folder + img,
            width=55,
            height=85,
            callback=setSelected(assets_folder + img),
        )
dpg.setup_dearpygui()
dpg.show_viewport()


dpg.start_dearpygui()
dpg.destroy_context()
