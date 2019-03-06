import random
import json
import pandas as pd
from pathlib import Path
from collections import Counter
import datetime
import time


def naming():
    f=open("Registry/names.txt", "w+")
    q=open("Registry/queued.txt", "a+")
    inputTimeStamp=""
    ts = time.time()
    inputTimeStamp= datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    print(inputTimeStamp)
    f.write("%s" %inputTimeStamp)
    q.write(inputTimeStamp+'\n')
    f.close()
    q.close()

def csv_input():
    name="SendDB\\finalPrediction.csv"
    df=pd.read_csv(name,sep=',')
    df.sort_values("Crop Rank",inplace=True)
    a=df[0:]
    x=a['Crop Name'].values
    return (x[0:3])

def create_txt():
    txt_file=open("Sending_Data\Suggestion_List.txt","w+")
    
    x=csv_input()
    print(x)
    for i in x:
        message=i+"\n"
        txt_file.write(message)
    txt_file.close()

def main():        
    random.seed(1)

    #input_path = Path("roll.txt")
    create_txt()


    with open("Sending_Data\Suggestion_List.txt", "r") as f:
        lines = f.readlines()
    numbers = [(e.strip()) for e in lines]
    #numbers.sort()
    farmerId=1555
    districtId='MUM'

    complete={}
    n=open("Registry/names.txt", "r")
    inputTimeStamp=n.readline()
    #data = [{i: numbers[i]} for i in range(len(numbers))]
    '''
    for i in range(len(numbers)):
        print(i)
        rn='rn'+str(i)
        data =[{rn: numbers[i]}]
    '''
    rn="rn"
    data = [{rn+str(i): numbers[i]} for i in range(len(numbers))]
    
    complete['fid'] = farmerId
    complete['disid'] = districtId
    complete['faid'] = data
    #data = Counter(random.choice(numbers) for _ in range(100))
    #print(json.dumps(data, sort_keys=True, indent=2))
    jsonopPath="JSON/"
    jsonPath=jsonopPath+inputTimeStamp+".json"
    output_path = Path(jsonPath)
    output_path.write_text(json.dumps(complete, sort_keys=False, indent=2))

naming()
main()
