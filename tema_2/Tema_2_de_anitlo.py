# #calculator

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
latime = float(input("latime"))
perimetru = 2 * (lungime + latime)
aria = lungime * latime
print(perimetru)
print(aria)

# #compara numere
nr_unu = float(input('da un numar ='))
nr_doi = float (input ('da al doilea numar ='))
print(bool(nr_unu>nr_doi))
print(bool(nr_unu<nr_doi))
print(bool(nr_unu>=nr_doi))

# #ce varsta ai
varsta_ta = float(input('Anul nasterii?'))
an_actual = 2025
print(float(an_actual-varsta_ta))

#par impar
numarul_tau = int(input('Spune un numar'))
rest = numarul_tau % 2
verificare_paritate = print('Este impar?', bool(rest))
