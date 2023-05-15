import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()

# Create a rounded button
button_image = tk.PhotoImage(file="rounded_button.png")
rounded_button = tk.Button(root, image=button_image, command=on_button_click, relief=tk.FLAT, bd=0)
rounded_button.pack()

root.mainloop()
