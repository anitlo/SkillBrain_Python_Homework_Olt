# #I. Adapteaza-ti un exercitiu la alegere din temele trecute, implementand functii.

# Foloseste-ti imaginatia, 
# am putea pune fiecare linie intr-o functie separata, 
# dar Arta este sa distingem acele parti cheie compuse din secvente de actiuni care compun 
# o Actiune mai mare - Re-utilizabila, Organizata, Modulara

# Ex: Functie pentru meniu, functie pentru adaugare(), functie pentru filtrare, cautare, etc.


# II. Funcție care primește text → returnează (nu printeaza, de print ne ocupam in programul principal unde o apelam):

# nr. de cuvinte
# cel mai lung cuvânt
# dacă apare „python”

#LISTA DE CUMPARATURI ADAPTAT

# Lista de cumpărturi
# Pasi: am scris problema pe hartie, am impartit in pasi logici, m-am gandit la o functie
# pe care o pot refolosi
# am conversat cu ChatGPT sa gasesc solutii 
# am folosit lectia de pe heartbeat skillbrain 
cos_cumparaturi = [] #lista goala in python, container ordonat si care poate fi modificat

def afiseaza_meniu(): #def defineste functia, iar afiseaza_meniu e numele functiei
    #parantezele delimiteaza lista de parametri, aici functia e goala si nu primeste argumente
    """ 
    Vezi optiunile disponibile pentru utilizator
    """ # """..""" - aceste ghilimele triple se numesc docstring, aceeste stringuri explica ce va face functia
    #docstring sunt diferite de '#' pt ca explica ce face o functie si de ce e necesara, in timp ce comentariile explica ce face un cod de strings
    #In other words, code comments are for people who want to modify the code, and docstrings are for people who want to use the code.
    print("\n MENIU LISTA DE CUMPARATURI ")
    print("1. Adauga produs")
    print("2. Afisează toate produsele")
    print("3. Cauta produs")
    print("4. sterge produs")
    print("5. Iesire")

def adauga_produs():
    """
    Cere utilizatorului un produs si il adaugă in lista
    """
    produs = input("Introdu produsul: ")
    cos_cumparaturi.append(produs)
    print(f" {produs} a fost adaugat in cos!")

def afiseaza_produse():
    """
    Afișează toate produsele din lista de cumpărături
    """
    if not cos_cumparaturi:
        print("⚠️ Lista este goală.")
    else:
        print("🛒 Ai cumpărat:", ", ".join(cos_cumparaturi))

def cauta_produs():
    """
    Caută un produs în listă
    """
    produs = input("Ce produs cauți? ")
    if produs in cos_cumparaturi:
        print(f"✅ {produs} se află în listă.")
    else:
        print(f"❌ {produs} nu este în listă.")

def sterge_produs():
    """
    Șterge un produs din listă, dacă există
    """
    produs = input("Introdu produsul de șters: ")
    if produs in cos_cumparaturi:
        cos_cumparaturi.remove(produs)
        print(f"🗑️ {produs} a fost șters din coș.")
    else:
        print(f"⚠️ {produs} nu există în listă.")

# === Program Principal ===
while True:
    afiseaza_meniu()
    optiune = input("Alege opțiunea: ")

    if optiune == "1":
        adauga_produs()
    elif optiune == "2":
        afiseaza_produse()
    elif optiune == "3":
        cauta_produs()
    elif optiune == "4":
        sterge_produs()
    elif optiune == "5":
        print("👋 La revedere!")
        break
    else:
        print("⚠️ Opțiune invalidă, încearcă din nou.")
