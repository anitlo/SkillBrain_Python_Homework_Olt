# II. Funcție care primește text → returnează:
# nr. de cuvinte
# cel mai lung cuvânt
# dacă apare „python”

def analizeaza_text(text):
    # functia primeste un text

    cuvinte = text.split()
    # impartim textul in cuvinte (despartim pe spatiu)

    nr_cuvinte = len(cuvinte)
    # aflam cate cuvinte sunt in text

    cel_mai_lung = max(cuvinte, key=len)
    # gasim cuvantul cu cele mai multe litere

    contine_python = "python" in text.lower()
    # verificam daca textul contine cuvantul "python"

    return nr_cuvinte, cel_mai_lung, contine_python
    # intoarcem cele 3 rezultate catre programul principal

# program principal
text = input("Introdu un text: ")
# cerem textul de la utilizator

nr, lung, exista = analizeaza_text(text)
# apelam functia si salvam rezultatele in variabile

print("Numar de cuvinte:", nr)
# afisam numarul de cuvinte

print("Cel mai lung cuvant:", lung)
# afisam cel mai lung cuvant

if exista:
    print("Textul contine 'python'")
    # daca exista python, afisam mesaj
else:
    print("Textul NU contine 'python'")
    # daca nu exista, afisam alt mesaj
