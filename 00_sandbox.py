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
        
        # List holder (rounds and scores are placeholders)
        score = ""

        # Variables used to work out statistics, when game ends etc
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # Initially set rounds played and rounds won to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)
         
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
        
        self.rounds_heading = Label(self.heading_frame, text="Round 1 / {}".format(how_many), font=("Arial", "16", "bold"), justify=LEFT, anchor=W)
        self.rounds_heading.grid(row=0, sticky=W, padx=20)

        self.score_heading = Label(self.heading_frame, text="Score: {}".format(score), font=("Arial", "12", "bold"), justify=LEFT, anchor=W)
        self.score_heading.grid(row=1, sticky=W, padx=20)
        
        # Seperate frame for buttons
        self.choice_frame = Frame(self.main_frame)  
        self.choice_frame.grid(row=1, column=0, columnspan=2)
        
        # List to hold references for buttons so that they can be configured for new rounds etc
        self.choice_button_ref = []
        
        # get colours for buttons for first round ...
        self.button_countries_list = []
        
        for item in range (0, 4):
            
            self.choice_button = Button(self.choice_frame, width=15, height=2, text="", command=lambda i=item: self.to_compare(self.button_countries_list[i], i))

            # Add button to reference list for later configuration
            self.choice_button_ref.append(self.choice_button)
            
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

        # Start new round
        new_round = self.new_round()
        
        
    # retrieve flags from csv
    def get_all_flags(self):
        
        file = open("Country_Flag_Quiz/country_flags.csv", "r")
        var_all_flags = list(csv.reader(file, delimiter=","))
        file.close()    
        
        # removes first entry in list (ie: the header row)
        var_all_flags.pop(0)
        return var_all_flags
    
    def resize_flag(self, chosen_flag):
        
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
          
    # DO IT ALL
    def get_round_flag(self):    
        
        all_answers = []
        
        # Generate correct answer and fisplay flag
        chosen_flag = random.choice(self.all_flags) 
        index_chosen = self.all_flags.index(chosen_flag)
        self.correct_ans = chosen_flag[0]
        all_answers.append(self.correct_ans)
        
        print("Correct Answer:", self.correct_ans)
        
        # Display flag image
        flag_image = self.resize_flag(chosen_flag)
        
        # Remove item from master list (so there are no duplicate flags)
        self.all_flags.pop(index_chosen)
        
        # Generate 3 more countries / wrong answers
        while len(all_answers) < 4:
            wrong_choice_entry = random.choice(self.all_flags)
            wrong_choice = wrong_choice_entry[0]
            if wrong_choice not in all_answers:
                all_answers.append(wrong_choice)
                
                # Remove item from master list (so there are no duplicate flags)
                self.all_flags.pop(index_chosen)
                
        # Shuffle list
        random.shuffle(all_answers)
        
        print("Countries:", all_answers)
        
        return all_answers
        
    # Set up new round when 'next' button is pressed
    def new_round(self):  
        
        # disable next button (renable it at the end of the round
        # self.next_button.config(state=DISABLED)
        
        # empty button list so we an get new countries
        self.button_countries_list = self.get_round_flag()
        
        # set button bg, fg and text
        count = 0 
        for item in self.choice_button_ref:
            item['bg'] = "white"
            item['text'] = self.button_countries_list[count]
            item['state'] = NORMAL

            count += 1 
            
        # retrieve number of rounds wanted / played and update heading.
        how_many = self.rounds_wanted.get()
        current_round = self.rounds_played.get()
        new_heading = "Round {} of {}".format(current_round + 1, how_many)
        self.rounds_heading.config(text=new_heading)
        
        # Add one to number of rounds played
        current_round = self.rounds_played.get()
        current_round += 1
        self.rounds_played.set(current_round)
        
    def to_compare(self, user_choice, button_num):
        
        # # enable stats button
        # self.to_stats_btn.config(state=NORMAL)
        
        # remove user choice from button colours list
        to_remove = self.button_countries_list.index(user_choice)
        self.button_countries_list.pop(to_remove)
        
        # If button pressed is the correct answer, change button colour to green
        if user_choice == self.correct_ans:
            self.choice_button_ref[button_num].config(bg="#7CC671")
        
        # Otherwise find the correct answer
        else:
            
            count = 0
            for item in self.choice_button_ref:
                
                # Retrieve text from button
                button_text = self.choice_button_ref[count].cget('text')
                print(button_text)
                
                # Check if answer is correct (Button = red if wrong)
                if button_text != self.correct_ans:
                     self.choice_button_ref[count].config(bg="#D21F3C")
                
                # Button = green if right
                else:
                    self.choice_button_ref[count].config(bg="#7CC671")
                         
                count += 1
                    
                    
    
# main routine
if __name__ == "__main__":
    root = Tk()     
    root.title("Country Flag Quiz")
    ChooseRounds()
    root.mainloop()


        
