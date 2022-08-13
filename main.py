from tkinter import Tk, Label, Entry, Button, messagebox
from PIL import Image


def add_watermark():
    """Merge photo from path with watermark."""
    try:
        img = Image.open(entry.get())
    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message="No Data File Found.")

    watermark = Image.open("watermark.png")

    watermark.convert("RGBA")
    img.paste(watermark, (0, 0), watermark)

    img.save(f"watermarked/{entry.get()}")

    messagebox.showinfo(title="Success",
                        message="Watermarked image "
                                "in folder watermarked")
    entry.delete(0, 'end')

    return img

#------------------------------------UI---------------------------------------#


window = Tk()
window.title("WaterMarker")
window.config(padx=50, pady=50, bg="white")

label = Label(text="Enter photo's path to add watermark",
              bg="white",
              font=("Arial", 14))

label.grid(column=0, row=0)

entry = Entry(width=42)
entry.grid(column=0, row=1, pady=10)
entry.focus()

button = Button(text="Add Watermark",
                width=14,
                command=add_watermark,
                font=("Arial", 12))

button.grid(sticky='w', column=0, row=2,
            columnspan=2, pady=10)

stop = Button(text="Quit",
              command=window.destroy,
              font=("Arial", 12))

stop.grid(sticky='e', column=0, row=2,
          columnspan=2, pady=10)


window.mainloop()
