import config
import sqlite3

def manual_input_new_client():
    client_info = {
        "first_name": input("Prénom du client : "),
        "last_name": input("Nom de famille du client : "),
        "vat_number": input("Numéro de TVA (si non applicable, taper 0) : "),
        "address": input("Rue et numéro de maison du client : "),
        "town": input("Code postal et localité du client : ")
    }

    client_info["vat_bool"] = 0 if isinstance(client_info["vat_number"], bool) else 1
 
    new_client = add_client(**client_info)
    return new_client

def add_client(first_name, last_name, vat_number, vat_bool, address, town):
    conn = sqlite3.connect('Clients.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO clients (first_name, last_name, vat_number, vat_bool, address, town)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, vat_number, vat_bool, address, town))
    
    conn.commit()
    conn.close()

def get_clients():   #function to retrieve all clients
    conn = sqlite3.connect('Clients.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()
    
    conn.close()
    return clients

def find_client_family_name(family_name):
    print("family name")
    conn = sqlite3.connect('Clients.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM clients WHERE last_name = ?', (family_name,))
    clients = cursor.fetchall()
    
    conn.close()
    
    if not clients:
        print("pas trouvé... sorry bro soit il y a une erreur soit il faut le créer", family_name)
        return None

    # Display the list of matching clients with corresponding numbers
    print("Liste de clients:")
    print("0) Créer un nouveau client")
    for index, client in enumerate(clients, start=1):
        print(f"{index}) {client}")

    # Prompt the user to select a client by number
    while True:
        try:
            choice = int(input("Choisir le numéro de client dans la liste : "))
            if choice == 0:
                return manual_input_new_client()
            if 1 <= choice <= len(clients):
                selected_client = clients[choice - 1]
                print(f"Client choisi: {selected_client}")
                return selected_client
            else:
                print(f"Entrer un numéro entre 1 et {len(clients)}.")
        except ValueError:
            print("PTDR IL FAUT UN CHIFFRE, pas autre chose")

def find_client_VAT(vat_number):
    conn = sqlite3.connect('Clients.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM clients WHERE vat_number = ?', (vat_number,))
    client = cursor.fetchone()

    conn.close()

    if not client:
        print("pas trouvé par TVA... sorry bro  soit il y a une erreur soit il faut le créer")
        return None
    
    return client

def check_string_and_execute(input_string):
    # Check if the first three characters are "BE0" or "BE1"
    if input_string[:3] == "BE0" or input_string[:3] == "BE1":
        client = find_client_VAT(input_string)
    else:
        client = find_client_family_name(input_string)
    if client == None: 
        client = manual_input_new_client()
    return client

def set_client_variables(client):
    global CLIENT_NAME, CLIENT_VAT, BOOL_CLIENT_VAT, CLIENT_ADDRESS
    
    if client:
        first_name = client[1]
        last_name = client[2]
        vat_number = client[3]
        vat_bool = client[4]
        address = client[5]
        town = client[6]

        config.CLIENT_NAME = f"{first_name} {last_name}"
        config.CLIENT_VAT = vat_number
        config.BOOL_CLIENT_VAT = str(vat_bool)
        config.CLIENT_ADDRESS = f"{address}\\\\{town}"
    else:
        print("Client not found.")