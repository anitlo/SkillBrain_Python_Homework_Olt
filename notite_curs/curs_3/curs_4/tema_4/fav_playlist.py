#Creează un tuplu cu 4 melodii preferate.
#Parcurge-l și afișează-le numerotat (1., 2., 3., ...).

#varianta 1
print ('\nVarianta 1:\n')

playlist = ('Cold', 'Paradise', 'Amigo', 'Higher')

# Parcurgem tuplul folosind enumerate()
# enumerate() ne dă două lucruri la fiecare pas:
# 1. index → poziția elementului (începând de la 1, pentru că am scris start=1)
# 2. cantec → valoarea elementului din tuplu
for index, cantec in enumerate(playlist, start=1):
    print(f"{index}. {cantec}")

#varianta 2
print ('\nVarianta 2:\n')

playlist = ('Cold', 'Paradise', 'Amigo', 'Higher')
numar = 1 # Inițializăm un contor care va ține evidența numerelor (începem de la 1)

for cantec in playlist:
    print(f"{numar}. {cantec}") # Afișăm contorul și melodia curentă
    numar += 1 # Creștem contorul cu 1 pentru următoarea melodie