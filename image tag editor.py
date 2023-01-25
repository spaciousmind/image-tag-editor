from tkinter import *
from tkinter import filedialog
from tkinter import font
from PIL import ImageTk, Image

from pathlib import Path

from tkinter.filedialog import *
import tkinter as tk
import os

text = ""

# Open an image using the PIL library
image_dir = Path.cwd()

image_files = [f for f in os.listdir(image_dir) if f.endswith('.png') or f.endswith('.jpg')]
image_names = [file[:-4] for file in image_files]
text_file_paths = [os.path.join(image_dir, image_file[:-4] + '.txt') for image_file in image_files]

images = []
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    img = Image.open(image_path)
    images.append(img)

# Create a variable to keep track of the current image
current_image = None

# Create a variable to keep track of the current image index
current_image_index = 0


canvas = tk.Tk()
canvas.grid()
canvas.geometry("1448x768")
canvas.title("tag editor")
canvas.config(bg='white')

frame = tk.Frame(canvas)
frame.grid(row=0, column=0, sticky="nsew")


# Create a bottom frame to hold the text editor and image
text_frame = Frame(frame)
text_frame.grid(row=1, column=1, sticky="ew")
text_frame.grid_rowconfigure(0, weight=0)
text_frame.grid_columnconfigure(1, weight=0)


def create_text_file(text, file_path):
    with open(file_path, "w") as file:
        file.write(text)

def update_text_file(text, file_path):
    with open(file_path, "w") as file:
        file.write(text)



# Function to update the image displayed in the 
def update_image():
    global current_image
    if current_image:
        canvas.delete(current_image)
    img = images[current_image_index]

    current_text_file = text_file_paths[current_image_index]

    if os.path.exists(current_text_file):
        load_text_file(current_text_file)
    else:
        text = ""
        create_text_file("", current_text_file)
        print("created " + image_names[current_image_index] + ".txt")


    img = img.resize((512, 768), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)


    label = Label(text_frame, image=img)
    label.grid(row=0,column=0,sticky="nsew")
    label.image = img  # Keep a reference to the image



# Bind the arrow keys to change the current image
def on_key_press(event):
    global current_image_index
    current_text_file = text_file_paths[current_image_index]
    if event.keysym == 'Prior':
        save_text_file(current_text_file)
        clearFile();
        current_image_index -= 1
        current_image_index = (current_image_index + len(images)) % len(images)
    elif event.keysym == 'Next':
        save_text_file(current_text_file)
        clearFile();
        current_image_index += 1
        current_image_index %= len(images)
    update_image()

canvas.bind("<Prior>", on_key_press)
canvas.bind("<Next>", on_key_press)


def load_text_file(file):
    with open(file, "r") as f:  
        content = f.read()
    entry.insert(INSERT, content)

def save_text_file(file):
    text = str(entry.get(1.0, END))
    with open(file, "w") as f:  
        f.write(text)

def clearFile():
    entry.delete(1.0, END)

def saveFileButton():
    new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFileButton():
    file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

def clearFileButton():
    entry.delete(1.0, END)

def saveAndExitButton():
    current_text_file = text_file_paths[current_image_index]
    save_text_file(current_text_file)
    exit()



# Create a top frame to hold the buttons
button_frame = Frame(text_frame, bg="#1e1319")
button_frame.grid(row=0, column=1, sticky="nsew")
button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=0)
button_frame.grid_columnconfigure(2, weight=0)
button_frame.grid_columnconfigure(3, weight=1)

b5 = Button(button_frame, text="  Save and Exit  ", bg = "#4f2d3f", command = saveAndExitButton)
b4 = Button(button_frame, text="  Exit  ", bg = "#4f2d3f", command = exit)
b3 = Button(button_frame, text="  Clear  ", bg = "#4f2d3f", command = clearFileButton)
b2 = Button(button_frame, text="  Save  ", bg = "#4f2d3f", command = saveFileButton)
b1 = Button(button_frame, text="  Open  ", bg = "#4f2d3f", command = openFileButton)

b5.grid(row=1, column=4, padx=20, pady=20, sticky="W")
b4.grid(row=1, column=3, padx=20, pady=20, sticky="W")
b3.grid(row=1, column=2, padx=20, pady=20, sticky="W")
b2.grid(row=1, column=1, padx=20, pady=20, sticky="W")
b1.grid(row=1, column=0, padx=(450, 20), pady=20, sticky="W")

entry = Text(text_frame, wrap = WORD, bg = "#281b22", fg="#d8adc3", insertbackground="yellow", font = ("poppins", 15), padx=10, pady=10)
entry.grid(row=0,column=1,sticky="nsew", padx=15, pady=(15, 60))

update_image()
canvas.mainloop()