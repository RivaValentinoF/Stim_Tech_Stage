import re
import os
import phonenumbers

#!Estrazione degli iban
def extract_iban(text):
    pattern = r"\b(?:IT|SM)[0-9]{2}[A-Za-z][0-9]{22}\b"  # Pattern to recognize an Italian or Sanmarinese IBAN

    ibans = re.findall(pattern, text)
    return ibans

def extract_iban_from_txt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    ibans = extract_iban(text)
    return ibans

def visIban(directory):
    file_list = os.listdir(directory)
    lista = []
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            ibans = extract_iban_from_txt(file_path)
            lista.append(ibans)
            
    return lista


#!Estrazione codice fiscale
def extract_codice_fiscale(text):
    pattern = r"\b[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]\b"  # Pattern per riconoscere un codice fiscale italiano

    codici_fiscali = re.findall(pattern, text)
    return codici_fiscali

def extract_codice_fiscale_from_txt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    codici_fiscali = extract_codice_fiscale(text)
    return codici_fiscali

def visCodFisc(directory):
    file_list = os.listdir(directory)
    lista = []
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            codici_fiscali = extract_codice_fiscale_from_txt(file_path)
            lista.append(codici_fiscali)

    return lista


#!Estrazione Nome e Cognome
def extract_nomi(text):
    textSplit = text.split()
    j = 0
    lista = []
    controllo = creaLista()
    for i in textSplit:
        dato = ''
        for k in controllo: 
            if i == k:
                dato = textSplit[j + 1]
                lista.append(dato)
                if textSplit[j + 2][0].isupper() and textSplit[j + 2][1].islower() and textSplit[j + 2] != 'C.F:' and textSplit[j + 2] != 'Cognome:':
                    lista.append(textSplit[j + 2])
        j += 1
    return lista

def extract_nomi_from_txt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    nomi = extract_nomi(text)
    return nomi

def visNome(directory):
    file_list = os.listdir(directory)
    lista = []
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            nomi = extract_nomi_from_txt(file_path)
            lista.append(nomi)
           
    return lista


#!Estrazione Date
def extract_dates_from_text(text):
    pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"  # Pattern to recognize dates in "dd/mm/yyyy" or "dd-mm-yyyy" format

    dates = re.findall(pattern, text)
    return dates

def extract_dates_from_txt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    dates = extract_dates_from_text(text)
    return dates

def visDate(directory):
    file_list = os.listdir(directory)
    lista = []
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            dates = extract_dates_from_txt(file_path)
            lista.append(dates)
           
    return lista


#!Estrai numero di telefono
def extract_phone_numbers_from_text(text):
    phone_numbers = []

    # Trova tutti i possibili numeri di telefono nel testo
    for match in phonenumbers.PhoneNumberMatcher(text, "IT"):
        phone_number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        phone_numbers.append(phone_number)

    return phone_numbers

def extract_phone_numbers_from_txt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    phone_numbers = extract_phone_numbers_from_text(text)
    return phone_numbers

def visPhoneNumbers(directory):
    file_list = os.listdir(directory)
    lista = []
    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join(directory, file)
            phone_numbers = extract_phone_numbers_from_txt(file_path)
            lista.append(phone_numbers)
           
    return lista


#!Metodi Generali
#?Check list
def creaLista():
    words = ["Nome:", "Cognome:", "Mittente:", "Destinatario:", "Richiedente:", "Firmatario:", "Testimone:", "Notaio:", "Debitore:", "Creditore:", "Procuratore:", "Beneficiario:", "Garante:", "Contraente:", "Testatore:", "Beneficiario effettivo:", "Amministratore:", "Titolare:", "Proprietario:", "Inquilino:", "Reclamante:", "Responsabile legale:", "Agente:", "Giudice:", "Avvocato:", "Proponente:", "Curatore:", "Supplente:", "Padrone di casa:", "Testimone oculare:", "Assicurato:", "Beneficiario fiduciario:", "Beneficiario di polizza:", "Coobbligato:", "Curatore speciale:", "Datore di lavoro:", "Difensore:", "Donante:", "Esecutore testamentario:", "Garante finanziario:", "Garante solidale:", "Intermediario:", "Legatario:", "Mediatore:", "Perito:", "Premiante:", "Promittente:", "Proposto:", "Referente:", "Richiedente asilo:", "Soggetto obbligato:", "Testimone esperto:", "Tribunale:", "Ufficiale pubblico:", "Valutatore:", "Venditore:", "Acquirente:", "Conduttore:", "Lasciatario:", "Locatore:", "Concessionario:", "Contraente principale:", "Contraente secondario:", "Locatario:", "Mandante:", "Mandatario:", "Offerta:", "Ricevente:", "Sofferente:", "Subappaltatore:", "Subentrante:", "Sublocatario:", "Sublocatore:", "Testimone di nozze:", "Promittente venditore:", "Promissario acquirente:"]

    # Duplica le parole senza i due punti
    words_no_colon = [word.replace(":", "") for word in words]

    # Unisci le due liste
    words_combined = words + words_no_colon

    return words_combined

#?Analize data
def analizza(oggetti):
    print(oggetti)


def main():
    directory = "E:/informatica/Visual Studio Code Projects/py projects/Stim Script/Txt/File/"
    oggetti = {'ibans': visIban(directory), 'codFis': visCodFisc(directory), 'nomi': visNome(directory), 'date': visDate(directory), 'num': visPhoneNumbers(directory)}

    analizza(oggetti)
    
    
main()
