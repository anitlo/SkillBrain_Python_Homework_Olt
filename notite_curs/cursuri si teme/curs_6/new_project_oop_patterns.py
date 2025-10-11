###import tkinter

###tkinter python

###PARTEA 1

# fac clasa Contract (aceasta va fi un contract juridic)
class Contract:

    # Primeste parametrii: self (refer la obiectul curent), nume_fisier si tip_contract
    def __init__(self, nume_fisier, tip_contract):
        
        # self.nume_fisier = atributul obiectului care stocheaza numele fisierului
        self.nume_fisier = nume_fisier
        
        # tipul contractului ("Contract servicii IT", NDA, etc.)
        self.tip_contract = tip_contract
        
        # Initializez atributul 'text' cu string gol
        # Aici va fi stocat continutul contractului după ce il citesc din fisier
        self.text = ""
        
        # Creez o lista goala pentru clauze gasite
        # Aici voi pune clauze importante pe care le găsesc in contract
        self.clauze_gasite = []
        
        # Lista goala pentru problemele gsite în contract
        # Aici voi pune toate problemele identificate
        self.probleme = []

    # Definesc o metoda (functie) care apartine clasei Contract
    # Această metoda va citi continutul fisierului si il va stoca in self.text
    def citeste_fisier(self):
        
        # Deschid fisierul in modul citire ('r' = read)
        # encoding='utf-8' inseamna ca pot citi si caractere romanesti (ă, î, ș, etc.)
        # 'as f' inseamna ca dau un nume scurt (f) pentru fisier
        # 'with' inseamna ca fisierul se inchide automat dupa folosire
        with open(self.nume_fisier, 'r', encoding='utf-8') as f:
            
            # f.read() citește INTREGUL continut al fisierului
            # si il atribui la self.text (atributul obiectului)
            self.text = f.read()


###PARTEA 2

# Definesc clasa care va reprezenta un standard juridic (ex: GDPR, AI Act, etc.)
# Aceasta clasa va contine regulile pe care trebuie sa le verific in contracte
class StandardJuridic:
    
    # Init ia doar numele standardului
    def __init__(self, nume):
        
        # Stocheaza numele standardului (ex: "GDPR")
        self.nume = nume
        
        # Lista cu cuvintele/frazele care TREBUIE sa existe in contract
        # Ex: pentru GDPR = ["consent", "personal data"]
        self.cuvinte_cheie = []
        
        # Lista cu cuvinte/fraze PROBLEMATICE care indica risc
        # Exemple... ["without restrictions", "in perpetuity"]
        self.cuvinte_risc = []


### PARTEA 3
# Clasa care face analiza propriu zisa - compară contractul cu standardul
class AnalizorSimplu:
    
    # Metoda principala care verifica dacă un contract respecta un standard
    # Primeste ca parametri: contractul de verificat si standardul juridic
    def verifica_contract(self, contract, standard):
        
        # Creez o lista goala unde voi pune toate problemele gasite
        probleme = []
        
        # Parcurg fiecare cuvânt imp din standard (ce TREBUIE sa existe)
        # 'for' inseamna: "pentru fiecare element din lista"
        for cuvant in standard.cuvinte_cheie:
            
            # Verific daca cuvantul cheie NU se gaseste on textul contractului
            # 'not in' inseamnă "nu se găsește in"
            if cuvant not in contract.text:
                
                # Dacă nu gasesc cuvantul, adaug o problema în lista
                # f"..." e un f-string - imi permite sa pun variabile in text
                probleme.append(f"Lipseste: {cuvant}")
        
        # Acum verific cuvintele de risc (ce NU trebuie sa existe)
        for cuvant_risc in standard.cuvinte_risc:
            
            # Dacă gssesc un cuvânt de risc in contract
            if cuvant_risc in contract.text:
                
                # Adaug o avertizare in lista de probleme
                probleme.append(f"Atentie: Contine '{cuvant_risc}'")
        
        # Atribui lista de probleme la obiectul contract
        # (astfel contractul "isi aminteste" problemele găsite)
        contract.probleme = probleme
        
        # Returnez lista de probleme (ca să pot s o folosesc in alt loc)
        return probleme

### PARTEA 4: Exemplu de utilizare si meniu interactiv

# Aceasta conditie verifica daca scriptul este rulat direct (nu importat)
# Daca da, atunci porneste codul din interiorul acestui bloc
if __name__ == "__main__":

    # Definesc un standard simplu GDPR (fac obiect cu numele GDPR care va contine lista de termeni obligatorii + risk)
    standard_gdpr = StandardJuridic("GDPR")
    standard_gdpr.cuvinte_cheie = [
        "consent",
        "personal data",
        "right to be forgotten"
    ]
    standard_gdpr.cuvinte_risc = [
        "for any goal",
        "without restrictions",
        "in perpetuity"
    ]

    # fac analizorul pt comparatie - are metoda verifica_contract facuta mai sus - AnalizorSimpl()
    analizor = AnalizorSimplu()

    # Meniu interactiv
    def meniu_analiza():
        # tin evidenta tuturor contractelor si a problemelor lor
        istoric = []

        while True:
            print("\n=== ANALIZA CONTRACTE ===")
            print("1. Analizeaza un contract nou")
            print("2. Afiseaza istoricul analizelor")
            print("3. Iesire")
            optiune = input("Alege: ")

            if optiune == "1":
                # Citesc datele de la utilizator
                nume_fisier = input("Nume fisier contract (.txt): ")
                tip_contract = input("Tip contract: ")
                # fac obiectul Contract si citesc fisierul
                contract = Contract(nume_fisier, tip_contract)
                contract.citeste_fisier()
                # Verific conformitatea cu GDPR
                probleme = analizor.verifica_contract(contract, standard_gdpr)
                # Afisez rezultatele
                print(f"\nRezultate analiza pentru '{nume_fisier}':")
                for p in probleme:
                    print(f" - {p}")
                if not probleme:
                    print("Nicio problema găsita!")
                # Salvez in istoric
                istoric.append((nume_fisier, probleme))

            elif optiune == "2":
                # Afisez rezultatele tuturor analizelor
                print("\n=== Istoric Analize ===")
                for nume, prob in istoric:
                    print(f"{nume}: {len(prob)} probleme")
                if not istoric:
                    print("Nu existr analize in istoric.")

            elif optiune == "3":
                break
            else:
                print("Optiune invalida.")

    # start meniului
    meniu_analiza()


