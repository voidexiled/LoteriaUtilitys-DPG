import dearpygui.dearpygui as dpg
import numpy as np
import cv2


# Crear una matriz
matrix = np.zeros((4,4), dtype=int)

# Variable para la imagen seleccionada
selected_image = None

# Ruta a las imagenes
image_dir = "assets/images/"

# Función para seleccionar una imagen
def select_image(sender, app_data):
    global selected_image
    selected_image = int(sender.split("_")[-1]) # obtener el índice de la imagen desde el nombre del remitente


# Iniciar la GUI
dpg.create_context()
dpg.create_viewport(title='Matrix Editor', width=800, height=600)

# Función para configurar una celda de la matriz
def set_cell(sender, app_data):
    if selected_image is not None:
        row, col = map(int, sender.split("_")[1:]) # obtener fila/columna desde el nombre del remitente
        matrix[row][col] = selected_image
        # cargar imagen
        image = cv2.imread(f"{image_dir}/{selected_image}.jpg")
        image_texture = dpg.texture_registry[sender]
        dpg.modify_item(image_texture, default_value=image)

# Crear la matriz de widgets de imágen
for i in range(4):
    for j in range(4):
        # crear un widget de imágen vacía y guardarlo en el registro de texturas
        image_texture = dpg.generate_uuid()
        dpg.add_texture_registry(id=image_texture, tag=image_texture)
        dpg.add_image(texture_id=image_texture, id=f"cell_{i}_{j}", width=50, height=50, callback=set_cell, user_data=f"{i}_{j}", texture_tag=image_texture)

# Crear botones de imagen para seleccionar una imágen
for i in range(1, 55):
    image = cv2.imread(f"{image_dir}/{i}.jpg")
    image = cv2.resize(image, (50, 50))
    image_texture = dpg.generate_uuid()
    dpg.add_texture_registry(id=image_texture)
    dpg.load_image(image, id=image_texture)
    dpg.add_image_button(texture_id=image_texture, id=f"selector_{i}", callback=select_image)

# Función para guardar la matriz a un archivo de texto cuando se cierra el programa
def on_closing(sender, app_data):
    np.savetxt('matrix.txt', matrix, fmt='%d')



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
print("bye")
