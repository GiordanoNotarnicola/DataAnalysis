import random as rd
import numpy as np

#Stupido codice per verificare che Jung nel suo saggio abbia trovato qualcosa di inspiegabile.
#come è possibile che fatto dal vivo con persone reali abbia trovato una media di 6.5?

jung=[]
rip=10000

for i in range(rip):
    l=list(range(1,26))
    k=list(range(1,6))
    count=0
    while len(l)>0:
        a=rd.choice(l)
        b=rd.choice(k)
        l.remove(a)
        if a<=5*b and a>5*(b-1):
            count+=1
    jung.append(count)

print(f"la media è {np.mean(jung):.2f} pm {np.std(jung, ddof=1)/np.sqrt(rip):.2f}")