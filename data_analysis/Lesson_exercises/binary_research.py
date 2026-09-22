import numpy as np

#this code find a number in a ordered list, questa versione non funziona
#ricomincia da capo

b=np.arange(1, 30)
print(type(b))
def find(x, list):
    low=0
    high=len(list)-1
    passi=0
    for i in list:
        passi+=1
        if x==list[int((high+low)/2)]:
            print(f"abbiamo trovato il target in posizione {int(high/2)}, passi impiegati:{i+1}")
            break
        elif x<list[int((high+low)/2)]:
            high=int(high/2)
        else:
            low=int(high/2)
    
find(5,b)