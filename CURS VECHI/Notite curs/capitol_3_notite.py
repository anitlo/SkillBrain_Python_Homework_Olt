#structuri de control
# IF

#este elevul promovat la o materie

nota= int(input('Care este nota dvs?:'))

#if nota >=5: 
    #aici se intampla ceva
   # print('Felicitari, ai promovat')
if nota > 10:
    print('Mergi la circ, nu ma pacalesti')

elif nota >= 9:
    print('mergi la olimpiada')

elif nota >=5:
    print('ai promovat si atat')

else:
    print('Te rog sa revizuiesti')

#if nota < 5:
   # print('te rog sa revizuiesti materialele')

#exercitiu individual
#daca utilizatorul este major ori minor?

varsta_utilizator = int(input('Cati ani ai?'))
if varsta_utilizator >= 18:
    print('esti major!')

else:
    print('esti minor')

#alt exercitiu
#printr-un input de la utilizator, determinati anotimpul in care se afla utilizatorul, bazandu-te pe luna in care se afla
#daca luna este 3 - primavara, 6 - vara, 10 - toamns, 12 - iarna

luna_anului = int(input('In ce luna a anului esti? spune a cata luna este cu numar, nu numele lunii'))

if luna_anului >= 3 < 6:
    print('primavara')

elif luna_anului >=6 <10:
    print('vara')

elif luna_anului >= 10 < 12:
    print("toamna")

elif luna_anului == 12:
    print('iarna')

elif luna_anului == 1:
    print ('iarna')

elif luna_anului == 2:
    print('iarna')

else:
    print ('input incorect')