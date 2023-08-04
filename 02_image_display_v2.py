# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

class Play:
    
    def __init__(self):

        # Main window
        self.main_frame = Frame()
        self.main_frame.grid()
        
        img = ImageTk.PhotoImage(Image.open("Country_Flag_Quiz/flag_images\CN-flag.gif"))

        # Create a Label Widget to display the text or Image
        label = Label(self.main_frame, image = img)
        label.grid()

# main routine
if __name__ == "__main__":
    root = Tk()         
    root.title("Country Flag Quiz") 

    Play()
    root.mainloop()
