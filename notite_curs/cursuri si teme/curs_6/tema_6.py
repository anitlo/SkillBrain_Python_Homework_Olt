#lasa student

class Student:
    def __init__(self, nume, email):
        self.nume = nume
        self.email = email
        self.note = []

    def adauga_nota(self, nota):
        self.note.append(nota)

    def media(self):
        if not self.note:
            return 0
        return sum(self.note) / len(self.note)

    def __str__(self):
        return f"{self.nume} ({self.email}) - Media: {self.media():.2f}"

#clasa trainer
class Trainer(Student):
    def __init__(self, nume, email, expertiza):
        super().__init__(nume, email)
        self.expertiza = expertiza
        self.__parola = parola

    def autentifica(self, parola_introdusa):
        return parola_introdusa == self.__parola

    def __str__(self):
        return f"[Trainer] {self.nume} ({self.expertiza})"

#clasa curs
class Curs:
    def __init__(self, titlu, trainer):
        self.titlu = titlu
        self.trainer = trainer
        self.studenti = []

    def adauga_student(self, student):
        self.studenti.append(student)

    def sterge_student(self, email):
        self.studenti = [s for s in self.studenti if s.email != email]

    def cauta_student(self, email):
        for s in self.studenti:
            if s.email == email:
                return s
        return None

    def cel_mai_bun_student(self):
        if not self.studenti:
            return None
        return max(self.studenti, key=lambda s: s.media())

    def afiseaza_studenti(self):
        print(f"\nCurs: {self.titlu}\nTrainer: {self.trainer}\n--- Studenți ---")
        for s in self.studenti:
            print(s)

    def exporta_studenti(self, fisier):
        with open(fisier, "w") as f:
            for s in self.studenti:
                note_text = ",".join(map(str, s.note))
                f.write(f"{s.nume},{s.email},{note_text},{s.media():.2f}\n")
        print(f"Studenții au fost exportați în {fisier}")

    def importa_studenti(self, fisier):
        try:
            with open(fisier, "r") as f:
                for linie in f:
                    date = linie.strip().split(",")
                    nume, email = date[0], date[1]
                    note = list(map(int, date[2:-1]))
                    student = Student(nume, email)
                    for nota in note:
                        student.adauga_nota(nota)
                    self.adauga_student(student)
            print(f"Studenții au fost încărcați din {fisier}")
        except FileNotFoundError:
            print(f"Fișierul {fisier} nu a fost găsit.")

    def exporta_doar_studenti(self, fisier="studenti.csv"):
        """Exportă doar numele și emailul studenților."""
        with open(fisier, "w") as f:
            f.write("nume,email\n")
            for s in self.studenti:
                f.write(f"{s.nume},{s.email}\n")
        print(f"Studenții au fost exportați în {fisier}")

    def exporta_doar_note(self, fisier="note.csv"):
        """Exportă fiecare notă a fiecărui student pe câte un rând."""
        with open(fisier, "w") as f:
            f.write("nume_student,email,nota\n")
            for s in self.studenti:
                for nota in s.note:
                    f.write(f"{s.nume},{s.email},{nota}\n")
        print(f"Notele au fost exportate în {fisier}")

    def exporta_rapoarte(self, fisier="rapoarte.csv"):
        """Exportă raport sumativ: nume, email, nr_note, media, status."""
        with open(fisier, "w") as f:
            f.write("nume,email,nr_note,media,status\n")
            for s in self.studenti:
                nr = len(s.note)
                med = s.media()
                status = "Promovat" if med >= 5 else "Nepromovat"
                f.write(f"{s.nume},{s.email},{nr},{med:.2f},{status}\n")
        print(f"Rapoartele au fost exportate în {fisier}")

#MENIU INTEACTIC CLI
def meniu(curs):
    while True:
        print("\n=== MENIU CURS ===")
        print("1. Adaugă student")
        print("2. Afișează toți studenții")
        print("3. Caută student după email")
        print("4. Șterge student")
        print("5. Notează student")
        print("6. Afișează cel mai bun student")
        print("7. Exportă studenți în fișier")
        print("8. Încarcă studenți din fișier")
        print("9. Ieșire")
        print("10. Exportă doar studenți")
        print("11. Exportă doar note")
        print("12. Exportă rapoarte")
        print("13. Ieșire")

        opt = input("Alege opțiunea: ")

#PENTRU PAROLA TRAINER
        if opt in ("4", "5"):
            parola = input("Parolă trainer: ")
            if not curs.trainer.autentifica(parola):
                print("Autentificare eșuată.")
                continue

        if opt == "1":
            nume = input("Nume student: ")
            email = input("Email student: ")
            curs.adauga_student(Student(nume, email))

        elif opt == "2":
            curs.afiseaza_studenti()

        elif opt == "3":
            email = input("Email student: ")
            s = curs.cauta_student(email)
            print(s if s else "Studentul nu a fost găsit.")

        elif opt == "4":
            email = input("Email student de șters: ")
            curs.sterge_student(email)
            print("Șters cu succes.")

        elif opt == "5":
            email = input("Email student: ")
            s = curs.cauta_student(email)
            if s:
                nota = int(input("Introduceți nota: "))
                s.adauga_nota(nota)
            else:
                print("Studentul nu există.")

        elif opt == "6":
            top = curs.cel_mai_bun_student()
            if top:
                print("Cel mai bun student:", top)
            else:
                print("Niciun student introdus încă.")

        elif opt == "7":
            fisier = input("Nume fișier (ex: studenti_all.csv): ")
            curs.exporta_studenti(fisier)

        elif opt == "8":
            fisier = input("Fișier de încărcat: ")
            curs.importa_studenti(fisier)

        elif opt == "9":
            break

        elif opt == "10":
            curs.exporta_doar_studenti()

        elif opt == "11":
            curs.exporta_doar_note()

        elif opt == "12":
            curs.exporta_rapoarte()

        elif opt == "13":
            break

        else:
            print("Opțiune invalidă.")



#TESTARE RAPIDA
if __name__ == "__main__":
    trainer = Trainer("Bogdan", "bogdan@academy.ro", "Python & AI")
    curs = Curs("Python pentru AI", trainer)
    meniu(curs)
