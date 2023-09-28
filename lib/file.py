import os
import datetime
import locale

locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")


def get_file_path(filename=""):
    current_date = datetime.datetime.now()
    folder_name = current_date.strftime("tablas/%A%d%m%Y-%H%M/")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        return os.path.join(folder_name, filename)
