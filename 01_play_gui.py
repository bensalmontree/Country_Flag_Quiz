from tkinter import *
from PIL import ImageTk, Image

class Play:
    
    def __init__(self):
        
        # placeholder
        rounds = "1"
        rounds_cap = "1"
        score = "1"
        
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"
        
        # Main frame for rounds, score, and flag
        self.main_frame = Frame()
        self.main_frame.grid(padx=10, pady=10)
        
        self.rounds_heading = Label(self.main_frame, text="Round {} / {}".format(rounds, rounds_cap), font=("Arial", "16", "bold"), justify=LEFT, anchor=W)
        self.rounds_heading.grid(row=0, sticky=W)

        self.score_heading = Label(self.main_frame, text="Score: {}".format(score), justify=LEFT, anchor=W)
        self.score_heading.grid(row=1, sticky=W)
                
        # Seperate frame for buttons
        self.choice_frame = Frame(self.main_frame)  
        self.choice_frame.grid(row=2)
        
        for item in range (0, 4):
            self.choice_button = Button(self.choice_frame, width=15, height=2, text="Blank")
            self.choice_button.grid(row=item // 2, column=item % 2, padx=10, pady=10)
        
        self.next_button = Button(self.main_frame, text="Next", height=1, justify=RIGHT, anchor=E)
        self.next_button.grid(row=3, padx= 10, pady=10, sticky=E)
        
        # Display flag
        self.flag_display = ImageTk.PhotoImage(Image.open("Country_Flag_Quiz/flag_images\CN-flag.gif").resize((150,100), Image.ANTIALIAS))
        flag_label = Label(self.main_frame, image=self.flag_display)
        flag_label.photo = self.flag_display
        flag_label.grid(row=0, column=1)

# main routine  
if __name__ == "__main__":
    root = Tk()         
    root.title("Country Flag Quiz")
    Play()
    root.mainloop()