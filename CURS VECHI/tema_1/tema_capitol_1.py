#Într-un fișier Python numit tema_capitol_1.py, scrieți un program care să conțină 4 
# variabile cu valori introduse de utilizator folosind funcția input(). 
# În funcția input() trebuie scrise întrebări adresate utilizatorului, 
# pe care să le ajustați astfel încât răspunsurile să corespundă tipurilor variabilelor: 
# una de tip str (text), una convertită cu int(), una cu float() și una cu bool(). 
# Programul va afișa apoi fiecare variabilă împreună cu tipul acesteia, 
# folosind funcțiile print() și type(). 



tara_ta = input('In ce tara locuiesti?')
print(type(tara_ta)) #str

inaltimea_ta = input('Ce inaltime ai exact?')
print(float(inaltimea_ta)) #float

numar_camere_in_apartament = input('Cate camere ai in apartament?')
print(int(numar_camere_in_apartament)) #int

mancare_azi = input ('Ai mancat azi?')
print(bool(mancare_azi)) #bool

print ('\t Survey \n' 'tara participantului in survey:', tara_ta, 'inaltimea:', inaltimea_ta, 'numarul camerelor:', numar_camere_in_apartament, 'a mancat participantul?:', mancare_azi)
