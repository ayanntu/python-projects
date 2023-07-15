from tkinter import *
from PIL import ImageTk, Image
import qrcode
import os

root = Tk()
root.title("QR Generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False, False)


def generate():
    global Image
    name = title.get()
    text = entry.get()

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    save_path = os.path.join("Qrcode", f"{name}.png")
    qr_image.save(save_path)

    qr_image = Image.open(save_path)
    qr_image = qr_image.resize((300, 300))

    Image = ImageTk.PhotoImage(qr_image)
    canvas.itemconfig(qr_image_item, image=Image)


Label(root, text="Title", fg="white", bg="#AE2321", font=15).place(x=50, y=120)
title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=150)

entry = Entry(root, width=28, font="arial 15")
entry.place(x=50, y=250)

Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=generate).place(x=50, y=300)

canvas = Canvas(root, width=300, height=300, bg="white")
canvas.place(x=400, y=150)

qr_image_item = canvas.create_image(0, 0, anchor=NW)

root.mainloop()
