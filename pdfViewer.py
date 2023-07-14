from tkinter import Tk, filedialog, Button
from pdf2image import convert_from_path
import os

# Initializing Tkinter
root = Tk()
root.geometry("630x700+400+100")
root.title("PDF Viewer")
root.configure(bg="white")

# Main part of the program
def browse_files():
    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select PDF file",
        filetype=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    images = convert_from_path(file_path)
    for image in images:
        image.show()

# Button to browse files
browse_button = Button(root, text="Browse", command=browse_files)
browse_button.pack(pady=(20, 0))

root.mainloop()
