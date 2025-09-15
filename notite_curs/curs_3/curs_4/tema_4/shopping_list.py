#Cere 3 produse prin input() și adaugă-le într-o listă.
#Afișează lista cu mesajul „Ai cumpărat: ...”.

print ('\nVarianta 1:\n')

produs_1 = input('Primul tau produs dorit:')
produs_2 = input('Al doilea produs dorit:')
produs_3 = input('Al treilea produs dorit:')

shopping_list = [produs_1, produs_2, produs_3]
for produs in shopping_list:
    print(f"Ai cumparat: {produs}")


#alta varianta mai jos
print ('\nVarianta 2:\n')

# Crearea unei liste goale
lista_cumparaturi = []

# Cererea a 3 produse de la utilizator
for i in range(3):
    produs = input("Introdu produsul: ")
    lista_cumparaturi.append(produs)

# Transformăm lista într-un șir de caractere, separate prin virgulă și spațiu
produse_text = ", ".join(lista_cumparaturi)

# Afișarea listei
print(f"Ai cumpărat: {produse_text}") #ca sa fie una dupa alta