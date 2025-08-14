username_correct = 'ioana2025'
password_correct = '12345678'

#incepe cu cel mai relevant nume
username_required = str(input('Care este numele tau de utilizator?'))
password_required = str(input('Care e parola ta?'))

if username_required == username_correct and password_correct == password_required:
    print('Acces permis')

elif username_required != username_correct and password_required!= password_correct:
    print('Acces respins')

else:
    print('User/Password incorect')



