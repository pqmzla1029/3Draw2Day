
import requests
import json
from pathlib import Path

#input_path = Path("Khatam.json")
fileName=""
f = open('Registry\queued.txt', 'r')
for line in f:
    fileName=line+".json"
    print (fileName)
    compoundedString=""
    fh = open(fileName, 'r')
    for line in fh:
        compoundedString=compoundedString+line

    compoundedString.replace("\n","")
    data = compoundedString
    r = requests.post("http://626009af.ngrok.io/attendances/mark/", json={'json_payload': data})

    fw = open('Registry\queued.txt', 'w')
    print (line)
    for i in fw:
        print (i)
        if i!=line:
            fw.write(i)
    fh.close()

f.close()
