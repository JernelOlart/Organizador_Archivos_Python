import os
import shutil
# Dev Elian Olart
#JernelOlart@proton.me

# Rutas de origen y destino
carpeta_origen = r"C:\CARPETA_DE_ORIGEN"
carpeta_destino = r"C:\CARPETA_DE_DESTINO"

# Asegurar que la carpeta de destino existe
os.makedirs(carpeta_destino, exist_ok=True)

# Recorrer todos los archivos en la carpeta de origen
for archivo in os.listdir(carpeta_origen):
    ruta_archivo = os.path.join(carpeta_origen, archivo)

    # Verificar que sea un archivo
    if os.path.isfile(ruta_archivo):
        # Obtiene la extensión del archivo (sin el punto)
        extension = archivo.split(".")[-1] if "." in archivo else "SinExtensión"
        carpeta_tipo = os.path.join(carpeta_destino, extension.upper())  # Carpeta con nombre de extensión en mayúsculas

        # Crear la carpeta si no existe
        os.makedirs(carpeta_tipo, exist_ok=True)

        # Mueve el archivo a la carpeta correspondiente
        shutil.move(ruta_archivo, os.path.join(carpeta_tipo, archivo))

print(" Archivos organizados por tipo en:", carpeta_destino)

