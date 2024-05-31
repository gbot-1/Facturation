""" TO DO """
"""
rewrite template tex 
fill dictionnary
add bool cash or not
Def folder based on date of invoicing and not on the creation of the file
"""

from compile_tex import*

SRC_FOLDER = 'C:/Users/Win/OneDrive/Documents/Ir_Bucheron/Code_Facturation'
SRC_FILENAME = 'invoice.pdf'

invoice_data = {
    "Ref_invoice": "a",
    "Communication": "a",
    "Date": "a",
    "Deadline": "a",
    "Client_name": "a",
    "Client_VAT": "a",
    "Client_address": "a",
    "VAT": 1,
    "Description": "a",
    "Price_HVAT": 1,
    "Price": 1,
    "Total_HVAT": 1,
    "Total_VAT": 1,
    "Total": 1
}


compile_tex_to_pdf('Code_Facturation', 'invoice.tex')


dest_folder = 'C:/Users/Win/OneDrive/Documents/Ir_Bucheron/Facturation/2024/TEST'
move_and_rename_file(SRC_FOLDER, dest_folder, SRC_FILENAME,'FACTURE_TEST.pdf')