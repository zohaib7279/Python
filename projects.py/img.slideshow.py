from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk
root = tk.Tk()
root.title("Image Slidshow Viewer")
img_paths = [
    r"C:\Users\You\Desktop\images.png",
    r"E:\istockphoto-1203183537-1024x1024.jpg",
    r"C:\Users\You\Pictures\images.jpg",
    r"C:\Users\You\Desktop\download.png",
]

img_size=(1080,1080)
images= [Image.open(path). resize(img_size) for path in img_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]
label = tk.Label(root)
label.pack()
def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update
        time.sleep(2)
slidshow = cycle(photo_images)
def start_slidshow():
    for _ in range(len(img_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slidshow', command=start_slidshow)
play_button.pack()
root.mainloop()