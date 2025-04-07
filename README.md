📂 Organizador de Archivos por Tipo

Este script en Python organiza automáticamente los archivos de una carpeta en subcarpetas según su tipo (extensión de archivo).

🚀 Características

✅ Mueve archivos desde una carpeta de origen a una carpeta de destino  
✅ Agrupa archivos en subcarpetas basadas en su extensión (por ejemplo: PDF, JPG, TXT)  
✅ Crea automáticamente las carpetas si no existen

🛠 Requisitos

• Python 3.x instalado  
• Permisos de lectura y escritura en las carpetas utilizadas

🔧 Uso

1. Clona este repositorio o descarga el script.
2. Modifica las rutas en el código para que coincidan con tus carpetas locales:

   carpeta_origen = r"C:\ruta\a\tu\carpeta_origen"  
   carpeta_destino = r"C:\ruta\a\tu\carpeta_destino"

3. Ejecuta el script con Python.

📌 Ejemplo de Organización

Antes:
Contenido en la carpeta de origen:

documento.pdf  
foto.jpg  
reporte.docx

Después:
Contenido en la carpeta de destino:

📂 carpeta_destino  
├── 📂 PDF  
│   └── documento.pdf  
├── 📂 JPG  
│   └── foto.jpg  
├── 📂 DOCX  
│   └── reporte.docx
