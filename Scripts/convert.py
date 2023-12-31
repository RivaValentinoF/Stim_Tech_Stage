import fitz 
import docxpy
import io
import os

#!Conversione file
#?Covenrsione PDF in txt
def convert_pdfs_in_folder(file, n):
    # Apri il file PDF in modalità binaria
    with open(file, 'rb') as pdf_file:
        
        # Leggi il contenuto del file PDF in una variabile di tipo bytes
        pdf_bytes = pdf_file.read()

    # Crea un oggetto lettore per il file PDF
    pdf_doc = fitz.open(stream=io.BytesIO(pdf_bytes), filetype="pdf")

    # Inizializza una stringa vuota per contenere il testo estratto
    text = ''

    # Loop attraverso tutte le pagine del file PDF
    for page_num in range(pdf_doc.page_count):
        
        # Estrai il testo dalla pagina corrente
        page = pdf_doc[page_num]
        page_text = page.get_text()
        
        # Aggiungi il testo estratto alla stringa principale
        text += page_text

    # Scrivi la stringa contenente il testo estratto in un file di testo
    with open('Txt/File/{}.txt'.format(n), 'w') as txt_file:
        txt_file.write(text)

def convertPdfTxt():
    directory = "E:/informatica/Visual Studio Code Projects/py projects/Stim Script/Pdf/File/"

    file_list = os.listdir(directory)
    i = 1
    for file in file_list:
        file_path = os.path.join(directory, file)
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        convert_pdfs_in_folder(file_path, file_name)
        i += 1


#?Covenrsione Word in txt
def convert_docx_to_txt(docx_file, n):
    # Leggi il contenuto del file DOCX
    text = docxpy.process(docx_file)

    # Scrivi il testo estratto in un file di testo
    with open('Txt/File/{}.txt'.format(n), 'w') as file:
        file.write(text)

def convertDocxTxt():
    directory = "E:/informatica/Visual Studio Code Projects/py projects/Stim Script/Docx/File/"

    file_list = os.listdir(directory)
    i = 1
    for file in file_list:
        file_path = os.path.join(directory, file)
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        convert_docx_to_txt(file_path, file_name)
        i += 1


def main():
    convertPdfTxt()
    convertDocxTxt()


main()