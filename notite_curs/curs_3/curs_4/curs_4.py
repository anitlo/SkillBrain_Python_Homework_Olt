# Crearea unei liste
lista_cumparaturi = ["🍎 Mere", "🥛 Lapte"]

# Adăugarea unui element
lista_cumparaturi.append("🍞 Pâine")

# Accesarea unui element
primul_produs = lista_cumparaturi[0]

# Numărul de elemente
numar_produse = len(lista_cumparaturi)

# Parcurgerea listei
for produs in lista_cumparaturi:
    print(f"Cumpără: {produs}")

for i in range(3):
    #adaugarea unui element:
    lista_cumparaturi.append(f'Paine {i}')    #range(3) = 0, 1, 2; la fiecare pas, i ia pe rând aceste valori
    #f'Paine {i}' creează textul cu valoarea lui i înăuntru

