from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random

class ChooseRounds:
    
    def __init__(self):
        
        # Common format for all buttons
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # Heading
        self.intro_heading_label = Label(self.intro_frame, text="Country Flag Quiz", font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0, columnspan=2)
        
        # Enter rounds
        self.intro_entry = Entry(self.intro_frame, font=("Arial","14"))
        self.intro_entry.grid(row=1, column=0, padx=10, pady=10)   
        
        # Go button
        self.confirm = Button(self.intro_frame, text="Go", width=5, bg="#90EE90", command=lambda: self.num_check())
        self.confirm.grid(row=1, column=1)
        
        # Error message
        self.output_label = Label(self.intro_frame, text="", fg="#9C0000")
        self.output_label.grid(row=2, columnspan=2)
    
    # Checks if user input is valid    
    def num_check(self):
        
        has_error = "no"
               
        # Check that user has entered a valid number...
        response = self.intro_entry.get()
        try:
            response = float(response)
            
            if response < 1 or response > 50:
                has_error = "yes"
                
        except ValueError:
            has_error = "yes"
        
        # Error message (REMOVE FG CHANGE AFTER TEST)
        if has_error == "yes":
            self.output_label.config(text="Rounds must be greater than 0 but less than 50", fg="#9C0000")
        
        # FOR TESTING PURPOSES SHOW THAT ERROR MESSAGE WORKS
        else:
            self.output_label.config(text="VALID", fg="green")
        
# main routine
if __name__ == "__main__":
    root = Tk() 
    root.title("Temperature Converter")
    ChooseRounds()
    root.mainloop()

        
