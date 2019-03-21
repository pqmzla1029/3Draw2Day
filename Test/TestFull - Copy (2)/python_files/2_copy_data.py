import shutil
import os

os.chdir("..")
print(os.getcwd())


def createDirectory(directory):
	dirName = directory
 
	try:
	    # Create target Directory
	    os.mkdir("working_data\\"+dirName)
	    print("Directory " , dirName ,  " Created ") 
	except FileExistsError:
	    print("Directory " , dirName ,  " already exists")


def moveFiles():
        src1="pcd_files\cropped_1.json"
        dst1="working_data\json_crops\cropped_1.json"
        src2="pcd_files\cropped_2.json"
        dst2="working_data\json_crops\cropped_2.json"
        
        shutil.move(src1,dst1)
        shutil.move(src2,dst2)

        src1="pcd_files\cropped_1.ply"
        dst1="working_data\ply_crops\cropped_1.ply"
        src2="pcd_files\cropped_2.ply"
        dst2="working_data\ply_crops\cropped_2.ply"
        
        shutil.move(src1,dst1)
        shutil.move(src2,dst2)

def main():
	directory="frame0001"
	createDirectory(directory)
	moveFiles()

main()
