import argparse
import time
import string


def process_file(file_path):
    start_time=time.time()
    count_dict={character: 0 for character in string.ascii_lowercase + ".!?"} #character è la chiave del dizionario, 0 il valore
    with open(file_path,"r", encoding="utf-8") as input_file: #when finish "with", il file si chiude
        for line in input_file:
            for character in line.lower():
                if character in count_dict:
                    count_dict[character]+=1 #if also there make +1
        print(count_dict)
    elapsed_time=time.time()-start_time
    print(elapsed_time)

if __name__=="__main__": #clearly useful when you import the file and you don't want to execute the script
    parser= argparse.ArgumentParser()#questa parte di codice non mi serve...
    parser.add_argument('filepath')#necessaria solo per vedere in tempo reale cosa 
    args=parser.parse_args()#succede al mio codice se lo runno da terminale
    process_file(args.filepath)



