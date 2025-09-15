# Nevoie Client: Aplicație simplă pentru managementul prietenilor și hobbyurilor – 
# „Rămâi conectat mereu cu oamenii apropiați”.

# Scope:

# Creează o listă cu 5 prieteni (dicționare cu: nume, telefon, vârstă, ultim_contact, hobbyuri).
# Afișează lista.
# Adaugă un prieten nou.
# Schimbă numărul de telefon pentru un prieten.
# Creează un set cu toate hobbyurile unice și afișează-l.

#lista 5 prieteni cu dictionare
lista_prieteni = [
    {"nume": "Ana Popescu", "telefon": "0788393202", "varsta": 23, "ultim_contact": "3 februarie", "hobbyuri": ["karate"]},
    {"nume": "Corina Stela", "telefon": "0799393202", "varsta": 25, "ultim_contact": "2 aug", "hobbyuri": ["singing"]},
    {"nume": "Laurentiu Cioban", "telefon": "0700393202", "varsta": 24, "ultim_contact": "10 aug", "hobbyuri": ["dancing"]},
    {"nume": "Fidan Banciu", "telefon": "0722393202", "varsta": 25, "ultim_contact": "3 oct", "hobbyuri": ["karate"]},
    {"nume": "Daria Banciu", "telefon": "0733393202", "varsta": 24, "ultim_contact": "2 oct", "hobbyuri": ["teatru"]}
]



#aici am vrut sa fac lista de dictionare care au si cuvant cheie care descrie. nu s-a putut crea lista avand cuvinte cheie. Deci mai jos asta e doar un dictionar exemplu:
prietenii_mei = {
    "Ana": {
        "nume": "Ana Popescu",
        "telefon": "0788393202",
        "varsta": 23,
        "ultim_contact": "3 februarie",
        "hobbyuri": ["karate"]
    },
    "Corina": {
        "nume": "Corina Stela",
        "telefon": "0799393202",
        "varsta": 25,
        "ultim_contact": "2 aug",
        "hobbyuri": ["singing"]
    },
    "Laurentiu": {
        "nume": "Laurentiu Cioban",
        "telefon": "0700393202",
        "varsta": 24,
        "ultim_contact": "10 aug",
        "hobbyuri": ["dancing"]
    },
    "Fidan": {
        "nume": "Fidan Banciu",
        "telefon": "0722393202",
        "varsta": 25,
        "ultim_contact": "3 oct",
        "hobbyuri": ["karate"]
    },
    "Daria": {
        "nume": "Daria Banciu",
        "telefon": "0733393202",
        "varsta": 24,
        "ultim_contact": "2 oct",
        "hobbyuri": ["teatru"]
    }
}

#afiseaza lista
for prieten in lista_prieteni:  # fiecare element este un dicționar
    print(prieten)               # afișează dicționarul complet


#adauga prieten nou

lista_prieteni.append({
    "nume": 'Olga',
    "telefon": "074444444",
        "varsta": 24,
        "ultim_contact": "11 aug",
        "hobbyuri": ["eating"]
})

#schimba numarul unui prieten
for prieten in lista_prieteni:
    if prieten["nume"] == "Daria Banciu":
        prieten["telefon"] = "07111111111"

#afiseaza lista din nou dupa modificare
for prieten in lista_prieteni:  # fiecare element este un dicționar
    print(prieten)              

#Creează un set cu toate hobbyurile unice si afisează
# Creează un set gol
hobbyuri_unice = set()

# Parcurge fiecare prieten si adaugă hobbyurile in set
for prieten in lista_prieteni:
    hobbyuri_unice.update(prieten["hobbyuri"])  # update() adaugă toate elementele din listă în set

#ce face update() mai exact? Ia fiecare element dintr-o lista (sau tuplu, sau alt set) si il adaugă in set.
#update() deschide lista, ia fiecare element pe rand si ne arata setul la final

# Afisează setul cu hobbyuri unice
print("Hobbyuri unice:", hobbyuri_unice)
