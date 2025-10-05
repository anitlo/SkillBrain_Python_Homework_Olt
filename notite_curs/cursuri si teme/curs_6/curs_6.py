class Student:
    def __init__(self, nume, clasa):
        self.nume = nume
        self.clasa = clasa
        self.note = []

    def adauga_nota(self, nota):
        self.note.append(nota)

    def media(self):
        return sum(self.note) / len(self.note)

s1 = Student("Andreea", 10)
s1.adauga_nota(9)
s1.adauga_nota(10)
print(s1.media())