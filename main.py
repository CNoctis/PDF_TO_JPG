import fitz
import os

def pdf_to_png(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    file_name = os.path.basename(pdf_path).split('.')[0]  # Obtiene el nombre del archivo PDF sin extensión
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        image = page.get_pixmap()
        image.save(f"{output_folder}/{file_name}_page_{page_num + 1}.jpg")

    pdf_document.close()

def batch_convert_pdfs(input_folder, output_folder):
    # Comprueba si la carpeta de salida existe, si no, la crea
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Recorre los archivos en la carpeta de entrada
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(".pdf"):  # Verifica si es un archivo PDF
                pdf_file_path = os.path.join(root, file)
                pdf_to_png(pdf_file_path, output_folder)

# Ruta de la carpeta que contiene los archivos PDF que quieres convertir
input_folder_path = 'input'

# Carpeta de salida para las imágenes PNG
output_folder_path = 'output'

batch_convert_pdfs(input_folder_path, output_folder_path)
