from multiprocessing import Process
import os
def f(name):
    print("hello " + name)

if __name__=="__main__":
    p=Process(target=f, args=("World",))#when write process, start something with threads and so on
    p.start()
    p.join()

