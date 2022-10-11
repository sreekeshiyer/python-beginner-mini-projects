import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename(title = "Select PDF")         # Choose PDF to work on
file_name  = file.split("/")[-1]
file_name = file_name.split(".")[0]

pdf = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)

pages = pdfReader.numPages
s=""
numbering = input("Print page numbers? (Y/n) ").lower()
for pg in range(pages):
    if numbering=="y":
        s += "Page " + str(pg+1) + ":\n\n"
    pageObj = pdfReader.getPage(pg)
    texts = pageObj.extractText()
    s += texts + "\n\n\n"

folder_selected = filedialog.askdirectory(title = "Select directory to save converted text file")  # Select directory to store the newly created text file
with open(os.path.join(folder_selected, f"{file_name}.txt"), "w") as file_obj:
    file_obj.write(s)
print("PDF converted succesfully and stored at", folder_selected)
