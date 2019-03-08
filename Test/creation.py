import os
 
path = "./pcd_files/"
f= open("Filenames.txt","w+")
files = os.listdir(path)
for name in files:
    print(name)
    f.write(name+"\r\n")
f.close()


'''
f= open("Filenames.txt","w+")
f.write("file1\r\n")
f.write("file2\r\n")
f.close() 
'''
