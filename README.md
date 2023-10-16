# scooter-data-manager
This repo is for a school group project -- Research Thinking 2023, Fall, Group 4.
The entire project is in the main-scoot.py file. 

To make it easier for everyone to run the data manager, I didn't seperate the classes and defs into different functions.

Dependecies:  

Pillow library ~ pip install pillow  

Pillow_heif ~ pip install pillow-heif  

matplotlib - pip install matplotlib  

All of the other libraries are pre-installed with python

# inputs/outputs
Program inputs -- folder of heic images with location and date/time meta data preserved from each image.  
program outputs -- csv file 'output.csv' with image data, plot of coordinate locations from image metadata, folder 'jpeg_images' with heic images converted to jpeg

# IDE usage

Go to line 182 of main-scoot-ide.py and define the folder path as the path to your folder of heic scooter images. Run the program and it should work. 


# command prompt usage

The program is written to be run in the command prompt. If you are comfortable with and have an IDE, use that, but this will also work if you don't already have an IDE.  

To run it, download the main-scoot.py file and place it in a folder. The folder should contain main-scoot.py and a different folder of scooter heic images. It doesn't matter what the folder is -- it could just be your downloads folder. Just make sure the main-scoot.py and your image folder are in the same larger folder. In my case the folder was titled scooter_project.  

enter this command in your command prompt to go to said folder. Obviously replace the path with your folder path:
cd C:\Users\cisco\scooter_project  

then enter this command to run the program. Again, replace the path to the image folder with your machines path:
python main-scoot.py C:\Users\cisco\scooter_folder\scooter_heic_images

the program will now run.

# Trouble Shooting Exiftool
If the program returns an error when trying to use the exiftool, you likely do not have exiftool installed. 
exiftool is a windows program that gets exif data from images. It is not a python specific tool.
You need to download exiftool and put it in your path. Here is a tutorial: https://exiftool.org/install.html 
exiftool must be in the c:\Windows path. exiftool won't run if its in a folder. the path must be c:\exiftool.


<img width="572" alt="exiftool_path_example" src="https://github.com/franciscoSebastiano/scooter-data-manager/assets/137376492/cc2218ab-bb92-43b1-a563-e941be67bd1e">
