from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

try:
    # Open file dialog to select the image file
    file_path = askopenfilename()

    # Check if a file was selected
    if file_path:
        img = Image.open(file_path)
        myHeight, myWidth = img.size

        # Resize the image
        new_size = (myHeight, myWidth)
        resized_img = img.resize(new_size, Image.ANTIALIAS)

        # Save the compressed image
        save_path = asksaveasfilename(defaultextension=".jpg")

        # Check if a file name was provided for saving
        if save_path:
            resized_img.save(save_path)
        else:
            print("No file name provided. Image not saved.")
    else:
        print("No file selected.")

except (FileNotFoundError, OSError) as e:
    print("Error:", e)
