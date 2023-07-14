from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Open file dialog to select the image file
file_path = askopenfilename()
img = Image.open(file_path)
myHeight, myWidth = img.size

# Resize the image
new_size = (myHeight, myWidth)
resized_img = img.resize(new_size, Image.ANTIALIAS)

# Save the compressed image
save_path = asksaveasfilename(defaultextension=".jpg")
resized_img.save(save_path)
