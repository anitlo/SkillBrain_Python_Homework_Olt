parola_corecta = "1234"
incercari = 0
acces_permis = False

while not acces_permis:
    parola = input("Introdu parola: ")
    incercari = incercari + 1

    if parola == parola_corecta:
        print(f"Acces permis! Încercări: {incercari}")
        acces_permis = True
    else:
        print("Parolă greșită. Încearcă din nou!")
