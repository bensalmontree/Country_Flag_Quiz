from tkinter import *
import PIL
from PIL import ImageTk, Image
import random
import csv

class Play:
    
    def __init__(self):
        
        # Main frame
        self.main_frame = Frame()
        self.main_frame.grid(padx=10, pady=10)
        
        # Frame for flag
        self.flag_frame = Frame(self.main_frame)    
        self.flag_frame.grid(row=0, column=1)
        
        # Display Flag
        self.flag_label = Label(self.flag_frame, image="")
        self.flag_label.grid(row=0, rowspan=2, column=1, padx=10, pady=10)
        
        # Get all the flags
        self.all_flags = self.get_all_flags() 
                
        # Button to go to next question
        self.next_button = Button(self.main_frame, text="Next", height=1, justify=RIGHT, anchor=E, command=self.new_round)
        self.next_button.grid(row=2, column=1, padx=10, pady=10, sticky=E)

        # Start new round
        self.new_round()
        
    # retrieve flags from csv
    def get_all_flags(self):
        file = open("Country_Flag_Quiz/country_flags.csv", "r")
        var_all_flags = list(csv.reader(file, delimiter=","))
        file.close()    
        
        # removes first entry in list (ie: the header row)
        var_all_flags.pop(0)
        return var_all_flags
    
    def new_round(self):
        
        # Randomly choose flag from master list
        chosen_flag = random.choice(self.all_flags)
        index_chosen = self.all_flags.index(chosen_flag)
        
        # Resize image so that ALL images are in ratio to another (same length)
        img_old=Image.open("Country_Flag_Quiz/flag_images/{}".format(chosen_flag[3]))
        width, height = img_old.size
        width_new = int(150)
        height_new = int(height * width_new / width)
        img_resized = img_old.resize((width_new, height_new))
        self.flag_display = ImageTk.PhotoImage(img_resized)
    
        # Config flag label to display new flag
        self.flag_label.config(image=self.flag_display)
        self.flag_label.photo = self.flag_display
        
        # Remove item from master list (so there are no duplicate flags)
        self.all_flags.pop(index_chosen)

        
# main routine      
if __name__ == "__main__":
    root = Tk()         
    root.title("Country Flag Quiz")
    Play()      
    root.mainloop()