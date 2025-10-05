# Crearea unui dicționar
studenti = {
    "Ana123": {
        "nume": "Ana Popescu",
        "clasa": "10A",
        "note": [9, 8, 10]
    }
}

# Accesarea datelor
nume = studenti["Ana123"]["nume"]
note = studenti["Ana123"]["note"]

# Calcularea mediei - suma impartita la numarul notelor
medie:float = sum(note) / len(note)

for id_student, date in studenti.items():
    print(f"{id_student}: {date['nume']}")

# Adăugarea unui student nou
studenti["Maria999"] = {
    "nume": "Maria Vasile",
    "clasa": "10C"
}
print('/nParcurgere dupa adaugare:')
#

