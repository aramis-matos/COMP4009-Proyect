from tkinter import *
from PIL import ImageTk, Image
from Character import Character

#idea: use config to change to different Frames and thus access others
class Character_select:
    def __init__(self):
        self.root = Tk()
        self.root.title("SkyBoundDB")

        self.frame = Frame(self.root)
        self.frame2 = Frame(self.root)

        # Default packed frame
        self.frame.pack()

        self.skyfarer = Character_select.character_images(self)
        self.print_buttons = Character_select.button_mapping(self)
        self.print_button_list = Character_select.example_selection_mapping(self)
        self.root.mainloop()

    def character_images(self):
        roster_list = ['Gran.(Granblue.Fantasy).jpg', 'Ferry.(Granblue.Fantasy).jpg', 'Djeeta.(Granblue.Fantasy).jpg']
        New_Character_photo = []

        for i in range(0, len(roster_list)):
            Character_photo = Image.open(roster_list[i])
            Character_resized = Character_photo.resize((138,138), Image.ANTIALIAS)
            New_Character_photo.append(ImageTk.PhotoImage(Character_resized))

        return New_Character_photo

    def button_mapping(self):
        # Ferry Button
        Ferrybutton = Button(self.frame, image = self.skyfarer[1], command = lambda:[self.change_state(1)])
        Ferrybutton.pack(side = LEFT, anchor = N)
        # Gran Button that prints out the frame data
        Granbutton = Button(self.frame, image = self.skyfarer[0], command = lambda:[self.change_state(0)])
        Granbutton.pack(side = LEFT, anchor = N)
        # Djeeta Button that prints out the frame data
        Djeetabutton = Button(self.frame, image = self.skyfarer[2], command = lambda:[self.change_state(2)])
        Djeetabutton.pack(side = LEFT, anchor = N)

    def example_selection_mapping(self):
        move_2Lbutton = Button(self.frame2, text = "Moves Printed in Terminal", command = self.change_state2)
        move_2Lbutton.pack(pady = 10)

    def change_state(self, state):
        print("From Character_Select to Move_Select")
        if (state == 1):
            pass
        elif (state == 0):
            Character(0,"gran").print_fd()
        elif (state == 2):
            Character(0,"djeeta").print_fd()
        self.frame.pack_forget()
        self.frame2.pack()

    def change_state2(self):
        print("From Move_Select to Character_Select")
        self.frame2.pack_forget()
        self.frame.pack()


p = Character_select()