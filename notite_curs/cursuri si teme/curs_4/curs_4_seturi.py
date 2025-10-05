#Lista cu duplicate
raspunsuri = ["Da", "Nu", "Da", "Poate"]

# Crearea unui set (elimină automat duplicatele)
raspunsuri_unice = set(raspunsuri)

# Adăugarea unui element în set
raspunsuri_unice.add("Da") # Nu se va duplica!

# Verificarea existenței
if "Da" in raspunsuri_unice:
    print("Răspunsul 'Da' există")

# Numărul de elemente unice
numar_unic = len(raspunsuri_unice)
print('numarul unic de raspunsuri:', numar_unic)

# Operații pe seturi - cum putem uni niste seturi
set1: set[int] = {1, 2, 3}
set2: set[int]= {3, 4, 5}
intersectie = set1 & set2 # 3
print(intersectie)