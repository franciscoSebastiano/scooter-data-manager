#dependecy time!
import subprocess
import json
import matplotlib.pyplot as plt
import os
import csv
from PIL import Image as img
from PIL import ImageTk
from pillow_heif import register_heif_opener
import tkinter as tk
from tkinter import ttk
import argparse

#chat gpt wrote this checkboxApp class. Its for prompting the user to give qualitative data on images via checked or unchecked boxes.
class CheckboxApp:
    def __init__(self, root, image_directory):
        self.root = root
        self.root.title("Checkbox with Image")

        # Frame to hold widgets
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Load and resize the image
        photo = img.open(image_directory)
        photo = self.resize_image(photo, 800, 800)
        self.tk_img = ImageTk.PhotoImage(photo)

        # Display the image
        img_label = ttk.Label(self.frame, image=self.tk_img)
        img_label.grid(row=0, column=0, rowspan=100)

        # Checkboxes
        self.check_var1 = tk.BooleanVar()
        ttk.Checkbutton(self.frame, text="Upright Orientation?", variable=self.check_var1).grid(row=0, column=1, sticky="w", padx=10)

        self.check_var2 = tk.BooleanVar()
        ttk.Checkbutton(self.frame, text="Obstruction?", variable=self.check_var2).grid(row=5, column=1, sticky="w", padx=10)

        ttk.Label(self.frame, text="# of scooters").grid(row=10, column=1, sticky="w", padx=10)
        self.text_var = tk.StringVar()
        self.text_var.set("1")
        ttk.Entry(self.frame, text = "1", textvariable=self.text_var).grid(row=11, column=1, sticky="w", padx=10, pady=5)
        
        # Dropdown (Combobox)
        self.dropdown_var = tk.StringVar()
        self.combobox = ttk.Combobox(self.frame, textvariable=self.dropdown_var, values=["Road Verge", "Lawn", "Bike Lane", "Road", "Crosswalk", "Stairway", "Ramp", "Sidewalk", "Bike Rack", "Entrance Way", "Indoors"]
)
        self.combobox.grid(row=15, column=1, sticky="w", padx=10, pady=5)
        self.combobox.set('Parking Location')  # Default text

        # Button to close the window and get checkbox states
        ttk.Button(self.frame, text="Next Photo", command=self.root.quit).grid(row=20, column=1, columnspan=2, pady=10)

    def resize_image(self, photo, max_width, max_height):
        """Resize the image to fit within the specified dimensions while preserving aspect ratio."""
        w, h = photo.size
        scale = min(max_width / w, max_height / h)
        return photo.resize((int(w * scale), int(h * scale)), img.LANCZOS)

    def get_states(self):
        return self.check_var1.get(), self.check_var2.get(), self.dropdown_var.get(), self.text_var.get()

def get_checkbox_states(image_directory):
    root = tk.Tk()
    app = CheckboxApp(root, image_directory)
    root.mainloop()
    states = app.get_states()
    root.destroy()
    return states


def get_specific_exif_data(file_path): 
    tags = ["-GPSLatitude", "-GPSLongitude", "-DateTimeOriginal"]
    
    # Running the ExifTool command (will not work if exiftool is not in your C:\programtools directory)
    result = subprocess.run(['exiftool', '-j', *tags, file_path], capture_output=True, text=True)
    print(f"Reading EXIF data from: {file_path}")
    print("here")
    print(result.stdout)
    
    # Parse the JSON output
    data = json.loads(result.stdout)[0]  # Assuming one file, so take the first item in the list
    
    return [data.get("GPSLatitude", None), data.get("GPSLongitude", None),data.get("DateTimeOriginal", None)]

def dms_to_dd(dms_str):
    
    # Extract degrees, minutes, seconds, and direction
    degrees = float(dms_str[0:2]) # Hard coded locations of characters
    minutes = float(dms_str[7:9])
    seconds = float(dms_str[11:16])
    direction = dms_str[-1]

    # Calculate the decimal degrees
    dd = degrees + (minutes/60) + (seconds/3600)

    # If direction is South or West, make the result negative
    if direction in ['S', 'W']:
        dd = -dd

    return dd

def list_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# I wrote most of the stuff from here down 

def heic_to_jpg_folder(folder_path): #create folder of jpg images from folder of heic images
    image_list = list_files_in_directory(folder_path)
    register_heif_opener()

    for image in image_list:
        full_path = os.path.join(folder_path, image)
        photo = img.open(full_path)

        output_folder = 'jpeg_images'
        output_filename = image.replace('.HEIC', '.jpg')
        output_path = f"{output_folder}/{output_filename}"
        if not(os.path.exists(output_folder)):
               os.makedirs(output_folder)

        photo.save(output_path, 'JPEG')


def get_folder_data(imageDirectory): #get exifdata from every image in folder & prompt user for image descriptions

    directory = imageDirectory
    image_list = list_files_in_directory(directory)
    heic_to_jpg_folder(imageDirectory)

    #intialize lists for desired image data
    latitude_dd = [] 
    longitude_dd = []
    time_list = []
    no_kickstand = []
    blocked_walkway = []
    location_list = []
    scoot_count = []

    print(image_list)

    for image in image_list:

        #initialize lists of jpg file names based on heic file names (necessary for displaying jpg images)
        output_folder = 'jpeg_images'
        output_filename = image.replace('.HEIC', '.jpg')
        output_path = f"{output_folder}/{output_filename}" 

        heic_path = full_path = os.path.join(imageDirectory, image)
        metadata = get_specific_exif_data(heic_path) #get quantitative metadata information
        checkbox_states = get_checkbox_states(output_path) #prompt user to input qualitative image information

        latitude_dms = metadata[0]
        longitude_dms = metadata[1]
        time_value= metadata[2]
        print(metadata[0])
        print(metadata[1]) 
        print(metadata[2])

        latitude_dd.append(dms_to_dd(latitude_dms)) #append image coordinates to data list & convert coordinate strings to ints
        longitude_dd.append(dms_to_dd(longitude_dms))
        time_list.append(time_value)
        no_kickstand.append(checkbox_states[0]) # append user input to data list
        blocked_walkway.append(checkbox_states[1])
        location_list.append(checkbox_states[2])
        scoot_count.append(checkbox_states[3])
        

    return [latitude_dd, longitude_dd, time_list, no_kickstand, blocked_walkway, scoot_count, location_list] #return quantitative & qualitative data for on images


def create_csv(latitude_dd, longitude_dd, time_list, no_kickstand, blocked_walkway, scoot_count, location_list): #turn lists of image data into csv file

    rows = zip(latitude_dd, longitude_dd, time_list, no_kickstand, blocked_walkway, scoot_count, location_list)
    headers = ['latitude', 'longitude', 'time', 'no kickstand', 'blocked walkway', 'num scooters', 'location'] 

    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # write the headers
        writer.writerow(headers)
        # write the rows
        writer.writerows(rows)

def main(input_folder_path):
    heic_to_jpg_folder(input_folder_path) #call function to convert heic images to jpg
    folder_data = get_folder_data(input_folder_path) #get data from each image in heic folder
    create_csv(folder_data[0], folder_data[1], folder_data[2], folder_data[3], folder_data[4], folder_data[5], folder_data[6]) # create csv with image data

    #plot coordinate data from images (not necessary to overall program)
    plt.scatter(folder_data[1], folder_data[0], c='red', marker='o')
    plt.title('Coordinates Plot')
    plt.xlabel('Longitude (°)')
    plt.ylabel('Latitude (°)')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process scooter images in a folder.')
    parser.add_argument('input_folder_path', help='Path to the folder containing scooter images')
    args = parser.parse_args()

    main(args.input_folder_path)

