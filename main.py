""" TO DO """
"""
add bool cash or not
Fix encoding month UTF-8
DB client
"""

from compile_tex import*
from date_manipulation import*
from ref_and_communication import*
import datetime

SRC_FOLDER = 'C:/Users/Win/OneDrive/Documents/Ir_Bucheron/Code_Facturation'
MAIN_FOLDER = 'C:/Users/Win/OneDrive/Documents/Ir_Bucheron/Facturation'

DATE = '28/08/2024'
YEAR = str(datetime.datetime.now().year)
CLIENT_NAME = "Raphael Mathieu"
CLIENT_VAT = "BE0741.635.214"
CLIENT_ADDRESS = "Rue des Alloux, 14\\\\ 5060 Auvelais"
VAT = 21
DESCRIPTION = "Tonde et élagage où nöel ô de pelouse"
PRICE = 200

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

quadri = determine_quadrimester(DATE)

dest_folder = os.path.join(MAIN_FOLDER, YEAR, quadri)
create_folder(dest_folder)

ref, communication = generate_ref_and_communication(dest_folder, CLIENT_NAME, DATE)

invoice_data = {
    "Ref_invoice": ref,                             #automatic fill
    "Communication": communication,                 #automatic fill
    "Date": convert_date_to_text(DATE),
    "Deadline": compute_days_difference(DATE),      #automatic fill
    "Client_name": CLIENT_NAME,
    "Client_VAT": CLIENT_VAT,
    "Client_address": CLIENT_ADDRESS,
    "VAT": VAT,
    "Description": DESCRIPTION,
    "Price_HVAT": round(PRICE/(1+VAT/100),2),       #automatic fill
    "Price": PRICE,                 
    "Total_HVAT": round(PRICE/(1+VAT/100),2),       #automatic fill
    "Total_VAT": round(PRICE-PRICE/(1+VAT/100),2),  #automatic fill
    "Total": PRICE                                  #automatic fill
}

generate_main_latex('invoice_template.tex', 'invoice.tex', invoice_data)

compile_tex_to_pdf(SRC_FOLDER, os.path.join(SRC_FOLDER,'invoice.tex'))

move_and_rename_file(SRC_FOLDER, dest_folder, 'invoice.pdf','Facture_' + communication.replace(' - ', '_') + '.pdf')