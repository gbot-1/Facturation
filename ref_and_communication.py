import os
import re
from datetime import datetime
from date_manipulation import determine_quadrimester


def generate_ref_and_communication(main_folder, client_name, input_date, existing_ref=None):
    """
    Generate or use an existing reference and generate the communication string.
    
    :param main_folder: Path to the main folder containing the files
    :param client_name: Name of the client
    :param input_date: Date of the invoice in format "DD/MM/YYYY"
    :param existing_ref: Existing reference (optional)
    :return: Tuple containing the reference and communication
    """
    # Get the current year and extract the last two digits
    current_year = datetime.strptime(input_date, "%d/%m/%Y").year
    year_suffix = str(current_year)[-2:]
    
    if existing_ref:
        ref = existing_ref
    else:
        # Determine the quadrimester
        quadri = determine_quadrimester(input_date)
        quadrimester_base = {"Q1": 0, "Q2": 1, "Q3": 2, "Q4": 3}
        base_number = quadrimester_base[quadri]

        # List all files in the main folder
        files = os.listdir(main_folder)
        
        # Find the highest existing reference number
        max_ref_number = base_number*100
        for file in files:
            match = re.match(rf"Facture_{year_suffix}(\d{{3}})_", file)
            if match:
                ref_number = int(match.group(1))
                if ref_number > max_ref_number:
                    max_ref_number = ref_number
        
        # Generate the next reference number
        next_ref_number = max_ref_number + 1
        
        ref = f"{year_suffix}{next_ref_number:03d}"
    
    # Generate the communication string
    family_name = client_name.split()[-1].upper()
    communication = f"{ref} - {family_name}"
    
    return ref, communication

def convert_communication_format(communication):
    """
    Convert a communication string from '24005 - MATHIEU' to '24005_MATHIEU'.
    
    :param communication: The communication string to convert
    :return: The converted communication string
    """
    return communication.replace(' - ', '_')
