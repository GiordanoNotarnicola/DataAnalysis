import multiprocessing as mp
import time
import os

def doingstuff(x):
    print ("Process: "+str(x)+" "+str(os.getpid()))
    time.sleep(2)

if __name__=="__main__":
    start=time.time()
    pool = mp.Pool(processes=4)
    results = pool.map_async(doingstuff,range(1,10))#without async is another code
    end=time.time()
    print("elapsed time: "+str(end-start))
    #print(results.get())#without get is another code