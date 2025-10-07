###PARTEA 1

# Definim clasa Contract - aceasta va reprezenta un contract juridic
# O clasă e ca un șablon/model pentru crearea obiectelor
class Contract:
    
    # Metoda __init__ e constructorul - se apelează automat când creez un obiect nou
    # Primește parametrii: self (referința la obiectul curent), nume_fisier și tip_contract
    def __init__(self, nume_fisier, tip_contract):
        
        # self.nume_fisier = atributul obiectului care stochează numele fișierului
        # Practic spun: "obiectul acesta va avea o proprietate numită 'nume_fisier'"
        self.nume_fisier = nume_fisier
        
        # Stochează tipul contractului (ex: "Contract servicii IT", "NDA", etc.)
        self.tip_contract = tip_contract
        
        # Inițializez atributul 'text' cu un string gol
        # Aici va fi stocat conținutul contractului după ce îl citesc din fișier
        self.text = ""
        
        # Creez o listă goală pentru clauze găsite
        # Aici voi pune clauze importante pe care le găsesc în contract
        self.clauze_gasite = []
        
        # Listă goală pentru problemele găsite în contract
        # Aici voi pune toate problemele/riscurile identificate
        self.probleme = []

    # Definesc o metodă (funcție) care aparține clasei Contract
    # Această metodă va citi conținutul fișierului și îl va stoca în self.text
    def citeste_fisier(self):
        
        # Deschid fișierul în modul citire ('r' = read)
        # encoding='utf-8' înseamnă că pot citi și caractere românești (ă, î, ș, etc.)
        # 'as f' înseamnă că dau un nume scurt (f) pentru fișier
        # 'with' se asigură că fișierul se închide automat după folosire
        with open(self.nume_fisier, 'r', encoding='utf-8') as f:
            
            # f.read() citește ÎNTREGUL conținut al fișierului
            # și îl atribui la self.text (atributul obiectului)
            self.text = f.read()


###PARTEA 2

# Definesc clasa care va reprezenta un standard juridic (ex: GDPR, AI Act, etc.)
# Această clasă va conține regulile pe care trebuie să le verific în contracte
class StandardJuridic:
    
    # Constructorul primește doar numele standardului
    def __init__(self, nume):
        
        # Stochează numele standardului (ex: "GDPR", "AI Act")
        self.nume = nume
        
        # Listă cu cuvintele/frazele care TREBUIE să existe în contract
        # Ex: pentru GDPR = ["consimțământ", "date personale"]
        self.cuvinte_cheie = []
        
        # Listă cu cuvinte/fraze PROBLEMATICE care indică risc
        # Ex: ["fără restricții", "în perpetuitate"]
        self.cuvinte_risc = []


### PARTEA 3
# Clasa care face analiza propriu-zisă - compară contractul cu standardul
class AnalizorSimple:
    
    # Metoda principală care verifică dacă un contract respectă un standard
    # Primește ca parametri: contractul de verificat și standardul juridic
    def verifica_contract(self, contract, standard):
        
        # Creez o listă goală unde voi pune toate problemele găsite
        probleme = []
        
        # Parcurg fiecare cuvânt cheie din standard (ce TREBUIE să existe)
        # 'for' înseamnă: "pentru fiecare element din listă"
        for cuvant in standard.cuvinte_cheie:
            
            # Verific dacă cuvântul cheie NU se găsește în textul contractului
            # 'not in' înseamnă "nu se găsește în"
            if cuvant not in contract.text:
                
                # Dacă nu găsesc cuvântul, adaug o problemă în listă
                # f"..." e un f-string - îmi permite să pun variabile în text
                probleme.append(f"Lipsește: {cuvant}")
        
        # Acum verific cuvintele de risc (ce NU trebuie să existe)
        for cuvant_risc in standard.cuvinte_risc:
            
            # Dacă găsesc un cuvânt de risc în contract
            if cuvant_risc in contract.text:
                
                # Adaug o avertizare în lista de probleme
                probleme.append(f"ATENȚIE: Conține '{cuvant_risc}'")
        
        # Atribui lista de probleme la obiectul contract
        # (astfel contractul "își amintește" problemele găsite)
        contract.probleme = probleme
        
        # Returnez lista de probleme (ca să pot să o folosesc în alt loc)
        return probleme




