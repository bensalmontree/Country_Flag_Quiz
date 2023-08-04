from tkinter import *
from functools import partial  # To prevent unwanted windows
from PIL import ImageTk, Image
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
        
        else:
            self.to_play(response)
            
    def to_play(self, num_rounds):
        Play(num_rounds)

        # Hide root window (ie: hide rounds choice window).
        root.withdraw()
        

class Play:
    
    def __init__(self, how_many):
        
        self.quiz_box = Toplevel()
        
        # Placeholder
        rounds = "1"
        rounds_cap = "1"
        score = "1"
        
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"
        
        # Main frame
        self.main_frame = Frame(self.quiz_box)
        self.main_frame.grid(padx=10, pady=10)
        
        # Frame for Round and Score
        self.heading_frame = Frame(self.main_frame)
        self.heading_frame.grid(row=0, column=0)
        
        self.rounds_heading = Label(self.heading_frame, text="Round {} / {}".format(rounds, rounds_cap), font=("Arial", "16", "bold"), justify=LEFT, anchor=W)
        self.rounds_heading.grid(row=0, sticky=W, padx=20)

        self.score_heading = Label(self.heading_frame, text="Score: {}".format(score), font=("Arial", "12", "bold"), justify=LEFT, anchor=W)
        self.score_heading.grid(row=1, sticky=W, padx=20)
        
        # Seperate frame for buttons
        self.choice_frame = Frame(self.main_frame)  
        self.choice_frame.grid(row=1, column=0, columnspan=2)
        ''
        for item in range (0, 4):
            self.choice_button = Button(self.choice_frame, width=15, height=2, text="Blank")
            self.choice_button.grid(row=item // 2, column=item % 2, padx=10, pady=10)
        
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
        self.next_button.grid(row=3, column=1, padx=10, pady=10, sticky=E)
        
        new_round = self.new_round()
        print(new_round)
        
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
    
        return(chosen_flag)

# main routine
if __name__ == "__main__":
    root = Tk() 
    root.title("Country Flag Quiz")
    ChooseRounds()
    root.mainloop()


        
