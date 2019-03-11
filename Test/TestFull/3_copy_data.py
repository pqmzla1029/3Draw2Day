import shutil

def moveFiles():
        src1="pcd_files\cropped_1.json"
        dst1="pcd_files\json_crops\cropped_1.json"
        src2="pcd_files\cropped_2.json"
        dst2="pcd_files\json_crops\cropped_2.json"
        
        shutil.move(src1,dst1)
        shutil.move(src2,dst2)

        src1="pcd_files\cropped_1.ply"
        dst1="pcd_files\ply_crops\cropped_1.ply"
        src2="pcd_files\cropped_2.ply"
        dst2="pcd_files\ply_crops\cropped_2.ply"
        
        shutil.move(src1,dst1)
        shutil.move(src2,dst2)

def main():
	moveFiles()

main()
