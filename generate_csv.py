import random
import string
import csv

# Funzioni di supporto per generare dati casuali  
def generate_random_name(length=6):  
    return ''.join(random.choices(string.ascii_letters, k=length)).capitalize()  

def generate_random_email(name, surname):  
    domains = ["esempio.com", "test.com", "demo.com"]  
    return f"{name.lower()}.{surname.lower()}@{random.choice(domains)}"  

def generate_random_phone():  
    return f"+39 {random.randint(300, 399)} {random.randint(1000000, 9999999)}"  

# Genera dati casuali per 10 utenti  

data = [  
    {  
        "Nome": generate_random_name(),  
        "Cognome": generate_random_name(),  
        "Email": generate_random_email(generate_random_name(), generate_random_name()),  
        "Telefono": generate_random_phone()  
    }  
    for _ in range(10)  
]

# Scrive i dati in un file CSV  
csv_file_path = "utenti.csv"  
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:  
    writer = csv.DictWriter(file, fieldnames=["Nome", "Cognome", "Email", "Telefono"])  
    writer.writeheader()  # Scrive l'intestazione  
    writer.writerows(data)  # Scrive i dati riga per riga  

print(f"File CSV generato: {csv_file_path}")  
