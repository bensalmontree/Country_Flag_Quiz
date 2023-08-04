import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Load the image
img = Image.open("image.png")
tkimg = ImageTk.PhotoImage(img)

# Create a label to display the image
img_label = tk.Label(root, image=tkimg)

# Display the label over two rows
img_label.grid(row=0, column=0, rowspan=2)

# Add other widgets to the GUI
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=1)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=1, column=1)

root.mainloop()
