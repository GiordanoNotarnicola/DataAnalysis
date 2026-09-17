import time
import matplotlib.pyplot as plt

alpha="abcdefghijklmnopqrstuvxwyz"

def count(phrase, car):
    phrase=phrase.lower()
    for j, lettera in enumerate(car,start=0):
        contatore=0
        for i in phrase:
            if i==lettera:
                contatore+=1
        if contatore>0:
            print(f"ci sono {contatore} {car[j]}")

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

risp=input("Vuoi conoscere il numero di caratteri del tuo testo? Digita 'help' per le istruzioni, per proseguire premi un qualsiasi altro tasto"
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
risp3=input("Vuoi conoscere ora il numero di caratteri per ogni lettera? Digita 'letter' se acconsenti, un qualsiasi altro carattere" \
" per spegnere il programma")
if risp3=='letter':
    start=time.perf_counter()
    count(testo, alpha)
    fine=time.perf_counter()
    t=fine-start
    print(f"Tempo impiegato: {t:.3f}s, grazie e arrivederci")
else:
    print("Arrivederci e grazie!")
