📂 Organizador de Archivos por Tipo

Este script en Python organiza automáticamente los archivos de una carpeta en subcarpetas según su tipo (extensión de archivo).

🚀 Características

✅ Mueve archivos de una carpeta de origen a una carpeta de destino.
✅ Agrupa archivos en subcarpetas basadas en su extensión (por ejemplo: PDF, JPG, TXT).
✅ Crea las carpetas automáticamente si no existen.

🛠 Requisitos
	•	Python 3.x instalado
	•	Permisos de lectura y escritura en las carpetas

🔧 Uso
	1.	Clona este repositorio o descarga el script.
	2.	Modifica las rutas en el código para que coincidan con tus carpetas:

carpeta_origen = r"F:\YULISSA DEL CARMEN"
carpeta_destino = r"F:\YULISSA DEL CARMEN2"

📌 Ejemplo de Organización

Si la carpeta de origen tiene estos archivos:
documento.pdf  
foto.jpg  
reporte.docx  

Después de ejecutar el script, en la carpeta de destino verás:
📂 F:\YULISSA DEL CARMEN2  
 ├── 📂 PDF  
 │    └── documento.pdf  
 ├── 📂 JPG  
 │    └── foto.jpg  
 ├── 📂 DOCX  
 │    └── reporte.docx  
