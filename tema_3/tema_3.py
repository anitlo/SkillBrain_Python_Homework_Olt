nume_utilizator = 'ioana2025'
parola = '12345678'

cere_username = str(input('Care este numele tau de utilizator?'))
cere_parola = str(input('Care e parola ta?'))

if cere_username == nume_utilizator and cere_parola == parola:
    print('Acces permis')

elif cere_username != nume_utilizator and cere_parola != parola:
    print('Acces respins')

elif cere_username != nume_utilizator or cere_parola == parola:
    print('User/Password incorect')

elif cere_username == nume_utilizator or cere_parola != parola:
    print('User/Password incorect')


