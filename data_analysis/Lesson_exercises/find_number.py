import numpy as np
#this code find a element in a list of number ordered casually. It goes as n,
#because it will control all number. It isn't very efficient, but it works if
#we have egual number in the list.

risp1=input("inserisci la lista numerica separata da spazi, premi x se " \
"la vuoi inserire separata da virgole.")
if risp1=="x":
    risp1=input("inserisci la lista numerica separata da virgole")
    b=[int(el.strip()) for el in risp1.split(',')]
else:
    b=[int(el.strip()) for el in risp1.split()]
risp2=input("dimmi l'elemento che vuoi trovare")
def find(x, list):
    a=-1
    for i in list:
        a+=1
        if x==i:
            print(f"c'è {x} alla posizione {a}")

find(int(risp2),b)