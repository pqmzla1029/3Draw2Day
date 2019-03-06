import datetime
import time

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
