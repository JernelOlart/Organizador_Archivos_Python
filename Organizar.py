import os
import shutil

# Rutas de origen y destino
carpeta_origen = r"F:\YULISSA DEL CARMEN"
carpeta_destino = r"F:\YULISSA DEL CARMEN2"

# Asegurar que la carpeta de destino existe
os.makedirs(carpeta_destino, exist_ok=True)

# Recorre todos los archivos en la carpeta de origen
for archivo in os.listdir(carpeta_origen):
    ruta_archivo = os.path.join(carpeta_origen, archivo)

    # Verifica que sea un archivo
    if os.path.isfile(ruta_archivo):
        # Obtiene la extensión del archivo (sin el punto)
        extension = archivo.split(".")[-1] if "." in archivo else "SinExtensión"
        carpeta_tipo = os.path.join(carpeta_destino, extension.upper())  # Carpeta con nombre de extensión en mayúsculas

        # Crea la carpeta si no existe
        os.makedirs(carpeta_tipo, exist_ok=True)

        # Mueve el archivo a la carpeta correspondiente
        shutil.move(ruta_archivo, os.path.join(carpeta_tipo, archivo))

print("✅ Archivos organizados por tipo en:", carpeta_destino)