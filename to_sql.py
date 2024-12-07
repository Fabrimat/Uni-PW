import csv  

# File CSV da leggere  
csv_file_path = "utenti.csv"  

# Nome della tabella SQL  
table_name = "utenti"  

# Legge i dati dal file CSV  
with open(csv_file_path, mode="r", encoding="utf-8") as file:  
    reader = csv.DictReader(file)  
    columns = reader.fieldnames  # Ottieni i nomi delle colonne  
    rows = [row for row in reader]  # Leggi tutte le righe  

# Creazione della query SQL per creare la tabella  
columns_sql = ", ".join([f"{col.replace(' ', '_')} TEXT" for col in columns])  
create_table_query = f"CREATE TABLE {table_name} ({columns_sql});"  

# Creazione delle query INSERT  
insert_queries = []  
for row in rows:  
    values = ", ".join([f"'{value.replace('\'', '\'\'')}'" for value in row.values()])  
    insert_queries.append(f"INSERT INTO {table_name} VALUES ({values});")  

# Salva lo script SQL in un file  
sql_file_path = "crea_tabella_utenti.sql"  
with open(sql_file_path, mode="w", encoding="utf-8") as file:  
    file.write(create_table_query + "\n")  
    file.write("\n".join(insert_queries))  

print(f"Script SQL generato: {sql_file_path}")  
