Bee and Pollen Count
Summer 2024 Project
By Kshitij Pingle

Background:-
Our camera setup is run by a Raspberry Pi 4. The camera is attached to the hive to record the entrance of the hive. The Camera setup is made by Marwan Ahmed.

Aim of our project:-
This code is supposed to analyze the videos obtained by the camera setup attached onto the hive. The analysis will include counting the number of bees and bees with pollen entering the hive.
Ultimately, we hope to create a system where we can analyze the health of a bee hive through the number of bees and the amount of pollen entering.

Code Outline:-
The code is split into three parts according to the respective files
1. Main :
   Runs the program and calls the two functions. Later deletes the image file
2. Obtain_frames_cv2 :
   Makes image frames out of mp4 videos stored in a file
3. Bee_count_image :
   Analyze each image to count bees and pollen with an AI model
