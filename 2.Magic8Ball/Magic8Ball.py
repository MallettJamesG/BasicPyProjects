import time
import random
from tkinter import *

responses=[]
responses.append("No")
responses.append("Yes")
responses.append("I don't think so")
responses.append("Depends")
responses.append("Maybe")
responses.append("Try again later")
responses.append("If you want to")
responses.append("If it's cloudy outside")
responses.append("Ask a friend")
responses.append("I'm not feeling it")
responses.append("It sounds promising")
responses.append("I belive so")
responses.append("100%")
responses.append("I think it could happen")
responses.append("Try something else")
responses.append("Try asking something else")

class TheGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python Magic 8 Ball GUI")

        self.label = Label(self.master, text="Enter a Question you would like to ask (no to quit):")
        self.label.pack()

        self.enterplace = Entry(self.master)
        self.enterplace.pack()

        self.labeltext=StringVar()
        self.labeltext.set("--")
        self.response = Label(self.master,justify = CENTER,textvariable=self.labeltext)
        self.response.pack()

        self.frame = Frame(self.master)
        self.frame.pack()

        self.greet_button = Button(self.frame, text="Ask", command=self.ask)
        self.greet_button.pack(side = LEFT)

        self.close_button = Button(self.frame, text="Clear", command=self.clear)
        self.close_button.pack(side = LEFT)

        self.close_button = Button(self.frame, text="Play Again", command=self.clear)
        self.close_button.pack(side = LEFT)

        self.close_button = Button(self.frame, text="Close", command=master.quit)
        self.close_button.pack(side = LEFT)

    def ask(self):
        the_q = self.enterplace.get()

        if the_q == "no":
            self.labeltext.set("Okay, Goodbye..")
            time.sleep(2)
            self.master.quit
        else:
            self.labeltext.set("Let me think for a moment")
            self.master.update_idletasks()
            time.sleep(2)
            self.labeltext.set("---")
            self.master.update_idletasks()
            time.sleep(2)
            self.labeltext.set(random.choice(responses))
            self.master.update_idletasks()
            time.sleep(2)

    def clear(self):
        self.labeltext.set("")
        self.master.update_idletasks()


root = Tk()
my_gui = TheGUI(root)
root.mainloop()
