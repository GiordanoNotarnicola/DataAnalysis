import time
import matplotlib.pyplot as plt

alpha="abcdefghijklmnopqrstuvxwyz"
nalpha=0
for i in alpha:
    nalpha+=1


def count(phrase, car):
    phrase=phrase.lower()
    occorrenze=[]
    for j, lettera in enumerate(car,start=0):
        contatore=0
        for i in phrase:
            if i==lettera:
                contatore+=1
        print(f"ci sono {contatore} {car[j]}")
        occorrenze.append(contatore)
    return occorrenze

def totin(phrase):
    all=0
    for i in phrase:
        all+=1
    return print(all)

def totex(phrase):
    all=0
    for i in phrase:
        if i!=" ":
            all+=1
        else:
            continue
    return print(all)



risp=input("Vuoi conoscere il numero di caratteri del tuo testo? Digita 'help' per le istruzioni, premi un qualsiasi altro tastoper proseguire."
"'z' per terminare.")
if risp=="help":
    print("Benvenuto nel conta caratteri di G.N., puoi ottenere il numero di caratteri del testo in memoria con o senza spazi" \
    " e anche il numero di lettere, inserisci il percorso del tuo testo, poi digita 'con' per ottenere il conteggio con gli spazi," \
    " 'senza' per quello senza spazi. In seguito digita 'letter' per conoscere il numero di ogni lettera presente nel testo.")
elif risp=="z":
    quit()
file_path=input("Inserisci il percorso del testo")
with open(file_path, "r", encoding="utf-8") as file:
    testo = file.read()
risp2=input("Digita 'con' o 'senza' per conoscere il numero di caratteri del testo, altrimenti digita un carattere qualsiasi.")
if risp2=="con":
    start=time.perf_counter()
    totin(testo)
    fine=time.perf_counter()
    t=fine-start
    print(f"Tempo impiegato: {t:.3f}s")
elif risp2=="senza":
    start=time.perf_counter()
    totex(testo)
    fine=time.perf_counter()
    t=fine-start
    print(f"Tempo impiegato: {t:.3f}s")
else:
    print("Va bene, proseguiamo!")
risp3=input("Vuoi conoscere ora il numero di caratteri per ogni lettera? Digita 'letter' se acconsenti, digita 'hist' per vederlo in un istogramma.")
if risp3=='letter':
    start=time.perf_counter()
    count(testo, alpha)
    fine=time.perf_counter()
    t=fine-start
    print(f"Tempo impiegato: {t:.3f}s, arrivederci e grazie")
if risp3=='hist':
    start=time.perf_counter()
    plt.figure()
    plt.bar(list(alpha), count(testo, alpha) ,label="Istogramma delle occorrenze delle lettere"  )
    fine=time.perf_counter()
    plt.xlabel("Lettere dell'alfabeto")
    plt.ylabel("Occorrenze")

    plt.show()
    t=fine-start
    print(f"Tempo impiegato: {t:.3f}s, arrivederci e grazie.")
else:
    print("Arrivederci e grazie!")
