from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import random


def display_and_open_img(file_name):  # opens and displays an image
    global canvas
    global img
    global photoimg
    global pix
    
    img = Image.open(file_name)
    img = img.convert("RGB")  # converts to rgb, for ease (may change)
    photoimg = ImageTk.PhotoImage(img)
    canvas.create_image((50, 50), image=photoimg)
    canvas.pack(side=TOP)
    pix = img.load()


def browse():  # opens file dialogue to open an image
    fname = filedialog.askopenfilename(filetypes=(("Bitmap files", "*.bmp"),
                                           ("All files", "*.*")))
    display_and_open_img(fname)

    
def sort_func():  # sorts the opened image, displays and saves the sorted image
    global img
    global pix

    # currently only capable of sorting by built in python tuple sort by column
    # will add more functionality, more options and more efficient sorts
    for x in range(0, img.width):
        for i in range(0, img.height):
            min = (999, 999, 999)
            y_min = i
            for j in range(i, img.height-1):
                curr_pix = pix[x, j]
                if curr_pix < min:
                    min = curr_pix
                    y_min = j
            temp = pix[x, i]
            pix[x, i] = pix[x, y_min]
            pix[x, y_min] = temp
     
    img.save("sorted.BMP", "BMP")   # add a function that also displays
                                    # the sorted image in the application
    img.show()

    
root = Tk()

root.title("My Image")

canvas = Canvas(root, width=800, height=400)

display_and_open_img("test.bmp")

browse_b = Button(root, text="Browse for BMP", command=browse)
browse_b.pack(side=LEFT)

sort_b = Button(root, text="Sort image", command=sort_func)
sort_b.pack(side=LEFT)

root.mainloop()
