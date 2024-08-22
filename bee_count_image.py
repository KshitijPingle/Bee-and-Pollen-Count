#bee_count_image : Program to count bees from a folder
#                  of images
#By Kshitij Pingle
#kpingle@csu.fullerton.edu
#CWID : 885626978

#"bee_count_images.py" is a part of bee_and_pollen counting project


import os
#from os import listdir
from roboflow import Roboflow
import supervision as sv

rf = Roboflow(api_key="cjXDsIF5cny5qHIFUaAj")
project = rf.workspace().project("bee_and_pollen_counting")
model = project.version(1).model



def count_bees(directory):
    """Function to count bees for a folder of images"""
    
    bee_count = 0
    count= 0

    print("Starting to analyze image frames using Roboflow model")

    try:
        for image in os.listdir(directory):
            image = directory + image
            result = model.predict(image, confidence=40, overlap=30).json()
            detections = sv.Detections.from_inference(result)
            detect_count = len(detections)
            bee_count += detect_count
            #print("Detected", detect_count, "bees in image", count)

            if (((count % 10) == 0) and (count != 0)):
                #Print message for every 10 images analyzed
                print("Done analyzing", count, "images")
            count += 1

    except FileNotFoundError:
        print("Data File not found!")

    print("\nTotal number of bees =", bee_count)
#End of count_bees function



#Test
##directory = "data\\"
##    
##count_bees(directory)
