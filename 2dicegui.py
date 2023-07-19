"""
2dice gui.py
author - will - 07/1/23
chpt 8 gui remake of 2 dice game ( random number guessing game)
"""
#imports
####MUST HAVE BREEZYPYTHONGUI IN SAME WORKING DIRECTORY#####
from breezypythongui import EasyFrame
import random
from tkinter.font import Font


#class NAME CHANGE REQUIRED!!!!!
class TwoDiceGUI(EasyFrame):
    #class constructor method
    def __init__(self):
        EasyFrame.__init__(self, background="#A5C4D4", width=350, height=250, title="Two Dice Game", resizable=False)

        self.addLabel(text="Two Dice Game",  background="#A5C4D4", foreground="#055864", row=0, column=0, font=Font(family="Monospace",size= 20),columnspan=2, sticky="NsEW")

    #Player Area
        self.addLabel(text="Your Guess",  background="#A5C4D4", foreground="#055864", row=1, column=0,sticky="we")
        self.guessbox = self.addIntegerField(row=1, column=1, value=0, state="readonly",sticky="w", width=4)

     #RNGesus area
        self.addLabel(text="Computer's Guess",  background="#A5C4D4", foreground="#055864", row=2, column=0,sticky="we")
        self.rngbox = self.addIntegerField(row=2, column=1, value=0, state="readonly",sticky="w", width=4)
        
    
    #button
        rollBtn = self.addButton(text="Roll!", row=3,column=0, columnspan=2, command = self.roll)
        rollBtn["background"] = "#055864"
        rollBtn["fg"] = "#B88B4A"

    #results
        ##B88B4A - winning text  #D8315B - losing text
        self.result = self.addLabel(text="", row=4,column=0, columnspan=2, sticky="NEWS",background="#A5C4D4", foreground="#055864" )
        



    def roll(self):
        player = random.randint(1,6)
        npc = random.randint(1,6)
        self.guessbox.setValue(player)
        self.rngbox.setValue(npc)
        if npc > player:
            self.result["text"] = "Aww you lose"
            self.result["fg"] = "#D8315B"
        elif npc < player:
          self.result["text"] = "You Win"
          self.result["fg"] = "#B88B4A"  
        else:
            self.result["text"] = "Its a tie"






















def main():
    #main run funcition
    TwoDiceGUI().mainloop()

if __name__ == "__main__":
    main()
