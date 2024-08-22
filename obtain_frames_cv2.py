#obtain_frames_cv2 : Program to obtain frame images from a
#                    video per second
#By Kshitij Pingle
#kpingle@csu.fullerton.edu
#CWID : 885626978

#"obtain_frames_cv2.py" is a part of bee_and_pollen counting project
 

import cv2 
import os 


def create_frames(video, directory_name):
    """Function to create a folder of image frames for a mp4 video"""
    
    cam = cv2.VideoCapture(video)

    try: 	
        # creating a folder named data 
        if not os.path.exists(directory_name): 
            os.makedirs(directory_name) 

    # if not created then raise error 
    except OSError: 
        print ('Error: Creating directory of data') 

    fps = int(cam.get(cv2.CAP_PROP_FPS))
    #print("Frames per Second =", fps)
    frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    #print("Number of frames =", frames)
    seconds = round(frames / fps)

    print("\nNumber of frames =", frames)
    print("Frames per Second =", fps)
    print("Length of video in seconds =", seconds)


    # frame 
    currentframe = 0
    count = 0

    while(True): 	
        # reading from frame 
        ret, frame = cam.read() 

        if ret: #If we got a frame

            if ((count % 60) == 0): #This ensures a frame every second
                name = './data/frame' + str(currentframe) + '.jpg'
                
                if ((currentframe % 10) == 0): #Print message every 10 frames
                    print ('Creating...' + name) 

                # writing the extracted images 
                cv2.imwrite(name, frame)
                currentframe += 1

            # increasing counter so that it will show how many frames are created 
            count += 1
        else: 
            break

    #print("DEBUG: Count =", count)
    print("Finished creating frames\n")

    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows()
#End of create_frames function


#Test
##video = "hive_2_closeup.mp4"
##directory_name = "data"
##
##create_frames(video, directory_name)
