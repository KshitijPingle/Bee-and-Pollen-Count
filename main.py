#main : Start and cleans up project to count bees
#     : from a mp4 video
#By Kshitij Pingle
#kpingle@csu.fullerton.edu
#CWID : 885626978

#"main.py" is a part of bee_and_pollen counting project

from obtain_frames_cv2 import *
from bee_count_image import *
import os
import shutil

#File path
path = "C:\Kshitij_Docs\Kshitij_CSUF\Bee_Project\Final_Project_Folder"

#Assign the directory file and the video
video = "hive_2_closeup.mp4"

#Change this to rename
directory_name = "data"         

directory = directory_name + "\\\\"
delete_directory = True  #Change to false if do not want to delete directory with image frames

#Create frames from video
create_frames(video, directory_name)

#Count bees
count_bees(directory)

#Delete the directory with the image frames
print("\nDeleting the data directory")
if (delete_directory):
    file_path = path + "\\" + directory_name

    shutil.rmtree(file_path)    #Deletes the folder and all its contents
    print("File \"", end = "")
    print(directory_name, end = "")
    print("\" has been deleted")

