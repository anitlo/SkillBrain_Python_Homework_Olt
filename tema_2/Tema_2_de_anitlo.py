# #calculator a doua numere de la un utilizato

x = float(input('un nr intre 1 si 100 ='))
y = float(input('un numar intre 100 si 200 ='))

print("suma= ", x + y)
print("diferenta=", y - x)
print("produs=", y * x)
print("impartire normala", y / x)
print("partea intreaga= ", y // x)
print("restul =", y % x)

# #cum calculam perimetrul si aria dreptunghiului cu formula
lungime = float(input("Lungime: "))
latime = float(input("latime:"))
perimetru = 2 * (lungime + latime)
aria = lungime * latime
print(perimetru)
print(aria)

# #compara numere - Cere două numere de la utilizator
#Afișează dacă primul este mai mare, mai mic sau egal cu al doilea (3 printuri)

nr_unu = float(input('da un numar ='))
nr_doi = float (input ('da al doilea numar ='))
print('este mai mare 1 decat 2?', bool(nr_unu>nr_doi))
print('este numarul unu mai mare decat numarul doi?', bool(nr_unu<nr_doi))
print('este numarul 1 mai mare sau egal decat numarul doi?', bool(nr_unu>=nr_doi))

# #ce varsta ai
varsta_ta = float(input('Anul nasterii?'))
an_actual = 2025
print(float(an_actual-varsta_ta))

#par impar - Cere un număr de la utilizator + Afișează dacă este par sau impar
#daca este restul 1 este impar, daca este 0 este par - cand impart cu doi

numarul_tau = int(input('Spune un numar'))
rest = numarul_tau % 2
verificare_paritate = print('Este impar?', bool(rest))


#ultimul exercitiu - Cere de la utilizator un număr de secunde și afișează: Câte ore, minute și secunde reprezintă
a=int(input('Adauga nr secunde:'))
ore=a//3600
rest_secunde=a%3600
minute=rest_secunde//60
secunde=a%60
print('Rezultat', ore, 'ore', '.', minute, 'minute', '.', 'secunde', secunde)