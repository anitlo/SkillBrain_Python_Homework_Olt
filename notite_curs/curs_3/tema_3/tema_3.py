#Creați o buclă care cere un PIN de 4 cifre până e corect

#explicatie exercitiu: m-am jucat cu chatgpt si am vrut sa protejez parola cumva. 
#la inceput, am avut o eroare legata de bcrypt pt ca nu l-am putut importa
#de aceea, am mers in terminal via view>Ctrl+
#acolo am put 'python --version
#dupa am pus 'pip install bcrypt'. dupa noul cod a functionat. mai jos gasiti explicatiile fiecarei linii de cod

import bcrypt 
#bcrypt conține funcții pentru a genera salt și a crea/verifica hash-uri sigure pentru parole

# --- Setarea parolei (de obicei doar o faci o dată și salvezi hash-ul într-o bază de date)
parola_corecta = "1234".encode("utf-8")  # parola originala. 
#input() sau string-urile în Python sunt, de obicei, tip str (text). bcrypt = date brute = lucrează cu bytes, nu cu str.
#.encode("utf-8") transformă șirul "1234" într-un obiect de tip bytes, de exemplu b'1234'. De aceea facem .encode(...) înainte de a hasha.
salt = bcrypt.gensalt()                  # se generează un salt aleator
# salt este o valoare aleatorie folosită împreună cu parola la crearea hash-ului. Scopul: două parole identice să aibă hash-uri diferite (împiedică rainbow tables).
#bcrypt.gensalt() generează salt + încorporează și un cost (numit și rounds) care definește cât de „lent” e algoritmul — un cost mai mare = mai sigur dar mai lent.

hashat = bcrypt.hashpw(parola_corecta, salt)

print("Hash salvat în baza de date:", hashat)

# --- Verificarea parolei la autentificare
while True:
    parola = input("Introdu PIN: ").encode("utf-8")

    if bcrypt.checkpw(parola, hashat):   # verificăm parola introdusă cu hash-ul salvat
        print("Acces permis!")
        break
    else:
        print("Parolă greșită. Încearcă din nou!")

