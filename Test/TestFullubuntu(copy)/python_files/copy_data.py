import shutil
import os
#os.chdir("..")
print(os.getcwd())

def createDirectory(directory):
	dirName = directory
 
	try:
	    # Create target Directory
	    os.mkdir("working_data/json_crops/"+dirName)
	    print("Directory " , dirName ,  " Created ") 
	except FileExistsError:
	    print("Directory " , dirName ,  " already exists")

def moveFiles(directory):
        src1="cropped_1.json"
        dst1="working_data/json_crops/"+directory+"/cropped_1.json"
        #src2="cropped_2.json"
        #dst2="working_data/json_crops/cropped_2.json"
        
        shutil.move(src1,dst1)
        #shutil.move(src2,dst2)

        src1="cropped_1.ply"
        dst1="working_data/ply_crops/cropped_1.ply"
        #src2="cropped_2.ply"
        #dst2="working_data/ply_crops/cropped_2.ply"
        
        shutil.move(src1,dst1)
        #shutil.move(src2,dst2)

def main(filename):
	directory=filename
	createDirectory(directory)
	moveFiles(directory)

#main()
