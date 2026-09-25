import argparse
import time
import string

file_path="Undream'd_of_shores.txt"

def process_file(file_path):
    start_time=time.time()
    count_dict={character: 0 for character in string.ascii_lowercase}
    with open(file_path,"r", encoding="utf-8") as input_file: #when finish "with", il file si chiude
        for line in input_file:
            for character in line.lower():
                if character in count_dict:
                    count_dict[character]+=1 #if also there make +1
                """ else:
                    count_dict[character]=1 #if there are not this key, this is ugual to 1 """
        print(count_dict)
    elapsed_time=time.time()-start_time
    print(elapsed_time)

if __name__=="__main__": #cerca di capire come funziona...
    parser= argparse.ArgumentParser()
    parser.add_argument('filepath')
    args=parser.parse_args()
    process_file(args.filepath)



