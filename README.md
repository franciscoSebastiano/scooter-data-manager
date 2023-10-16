# scooter-data-manager
This repo is for a school group project -- Research Thinking 2023, Fall, Group 4.
The entire project is in the main-scoot.py file.  

To make it easier for everyone to run the data manager, I didn't seperate the classes and defs into different functions.

Dependecies:  

Pillow library ~ pip install pillow  

Pillow_heif ~ pip install pillow-heif  

matplotlib - pip install matplotlib  

All of the other libraries are pre-installed with python

# Usage
Program inputs -- folder of heic images with location and date/time meta data preserved from each image.  
program outputs -- csv file 'output.csv' with image data, plot of coordinate locations from image metadata, folder 'jpeg_images' with heic images converted to jpeg  

To use the program you must define the correct path for your folder of images. Go to line 182 of main-scoot.py and you can define your folder path. 


# Trouble Shooting Exiftool
If the program returns an error when trying to use the exiftool, you likely do not have exiftool installed. 
exiftool is a windows program that gets exif data from images. It is not a python specific tool.
You need to download exiftool and put it in your path. Here is a tutorial: https://exiftool.org/install.html 
exiftool must be in the c:\Windows path. exiftool won't run if its in a folder. the path must be c:\exiftool.


<img width="572" alt="exiftool_path_example" src="https://github.com/franciscoSebastiano/scooter-data-manager/assets/137376492/cc2218ab-bb92-43b1-a563-e941be67bd1e">
