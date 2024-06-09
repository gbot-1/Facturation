""" TO DO """
"""
Fix encoding month UTF-8
DB client
option to add multiple items
"""

from compile_tex import*
from date_manipulation import*
from ref_and_communication import*
import datetime

SRC_FOLDER = 'C:/Users/Win/OneDrive/Documents/Ir_Bucheron/Code_Facturation'
MAIN_FOLDER = 'C:/Users/Win/OneDrive/Documents/Ir_Bucheron/Facturation'
YEAR = str(datetime.datetime.now().year)

DATE = '08/06/2024'
CLIENT_NAME = "Angelo"
CLIENT_VAT = "BE0741.835.214"
BOOL_CLIENT_VAT = 0
CLIENT_ADDRESS = "Rue Trianoy, 8b\\\\6040 Jumet"
VAT = 6
DESCRIPTION = "Elagage du saule"
PRICE = 50.00
BOOL_CASH = 1

REF = None

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def str_bool(Bool):
    if Bool: 
        return "true"
    else:
        return "false"

quadri = determine_quadrimester(DATE)

dest_folder = os.path.join(MAIN_FOLDER, YEAR, quadri)
create_folder(dest_folder)

ref, communication = generate_ref_and_communication(dest_folder, CLIENT_NAME, DATE, REF)

invoice_data = {
    "Cash_payement" : str_bool(BOOL_CASH),
    "Ref_invoice": ref,                             #automatic fill
    "Communication": communication,                 #automatic fill
    "Date": convert_date_to_text(DATE),
    "Deadline": compute_days_difference(DATE),      #automatic fill
    "Client_name": CLIENT_NAME,
    "Bool_VAT_client": str_bool(BOOL_CLIENT_VAT),
    "Client_VAT": CLIENT_VAT,
    "Client_address": CLIENT_ADDRESS,
    "VAT": VAT,
    "Description": DESCRIPTION,
    "Price_HVAT": round(PRICE/(1+VAT/100),2),       #automatic fill
    "Price": f"{PRICE:.2f}",                 
    "Total_HVAT": round(PRICE/(1+VAT/100),2),       #automatic fill
    "Total_VAT": round(PRICE-PRICE/(1+VAT/100),2),  #automatic fill
    "Total": f"{PRICE:.2f}"                         #automatic fill
}

generate_main_latex('invoice_template.tex', 'invoice.tex', invoice_data)

compile_tex_to_pdf(SRC_FOLDER, os.path.join(SRC_FOLDER,'invoice.tex'))

move_and_rename_file(SRC_FOLDER, dest_folder, 'invoice.pdf','Facture_' + communication.replace(' - ', '_') + '.pdf')