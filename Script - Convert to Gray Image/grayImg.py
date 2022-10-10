import cv2
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title = "Select image to start with")         # Choose image

file = file_path.split("/")[-1]
print(file)
img = cv2.imread(file_path)                             # reads image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)         # recoloring image to gray

folder_selected = filedialog.askdirectory(title = "Select directory to save image")  # Select directory to store gray image

image_name = os.path.join(folder_selected, f"gray-{file}")
print(f"Saving image at {folder_selected} as gray-{file}")

cv2.imwrite(image_name, grayImg)                        # saving gray image