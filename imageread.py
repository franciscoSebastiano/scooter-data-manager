import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CheckboxApp:
    def __init__(self, root, image_directory):
        self.root = root
        self.root.title("Checkbox with Image")

        # Frame to hold widgets
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Load and resize the image
        img = Image.open(image_directory)
        img = self.resize_image(img, 800, 800)
        self.tk_img = ImageTk.PhotoImage(img)

        # Display the image
        img_label = ttk.Label(self.frame, image=self.tk_img)
        img_label.grid(row=0, column=0, rowspan=5)

        # Checkboxes
        self.check_var1 = tk.BooleanVar()
        ttk.Checkbutton(self.frame, text="No Kickstand?", variable=self.check_var1).grid(row=0, column=1, sticky="w", padx=10)

        self.check_var2 = tk.BooleanVar()
        ttk.Checkbutton(self.frame, text="Blocked Walkway?", variable=self.check_var2).grid(row=1, column=1, sticky="w", padx=10)

        # Button to close the window and get checkbox states
        ttk.Button(self.frame, text="Get Checkbox States", command=self.root.quit).grid(row=2, column=1, columnspan=2, pady=10)

    def resize_image(self, img, max_width, max_height):
        """Resize the image to fit within the specified dimensions while preserving aspect ratio."""
        w, h = img.size
        scale = min(max_width / w, max_height / h)
        return img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

    def get_states(self):
        return self.check_var1.get(), self.check_var2.get()

def get_checkbox_states(image_directory):
    root = tk.Tk()
    app = CheckboxApp(root, image_directory)
    root.mainloop()
    states = app.get_states()
    root.destroy()
    return states

# Example usage:
checkbox_states = get_checkbox_states('IMG_2822.jpg')
print(checkbox_states)




