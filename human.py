from tkinter.colorchooser import Chooser
from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__()
        self.score = 0

        
       

    def gesture_choice(self):

        gesture_status = True
        
        while gesture_status == True:
            self.choice = input()
            if self.choice == "0":
                self.gesture_choice = self.gestures[int((0))]
                gesture_status = False
                print(f'{self.name} has chosen {self.gesture_choice}\n')
            elif self.choice == "1":
                self.gesture_choice = self.gestures[int((1))]
                gesture_status = False
                print(f'{self.name} has chosen {self.gesture_choice}\n')
            elif self.choice == "2":
                self.gesture_choice = self.gestures[int((2))]
                gesture_status = False
                print(f'{self.name} has chosen {self.gesture_choice}\n')
            elif self.choice == "3":
                self.gesture_choice = self.gestures[int((3))]
                gesture_status = False
                print(f'{self.name} has chosen {self.gesture_choice}\n')
            elif self.choice == "4":
                self.gesture_choice = self.gestures[int((4))]
                gesture_status = False
                print(f'{self.name} has chosen {self.gesture_choice}\n')
            else:
                print("Invalid Selection, please choose again\n")
                


            
        