__author__ = 'adibb'

# Written by Alex Dibb
# Last edited 11/8/2017
# Based on A. Hornof's Tkinter_sample.py from the Fall 2017 CIS 443 Class at UO


# GLOBALS
TMP_WAV = "tmp_file_p782s8u.wav"


# IMPORTS
from tkinter import *
from sound import *
from menu_helpers import *
from sys import exit
from time import sleep
from ddec import log_event


# Application class definition
class MainApp:
    # On initialization - build the actual app window
    def __init__(self, parent):
        # Define the parent and container
        self.myParent = parent
        self.myContainer = Frame(parent, width=300, height=100)

        # Prevent resizing
        self.myParent.resizable(0, 0)

        # Create the options menu
        self.options = build_menu()

        # Set the active list to options
        self.activeList = self.options
        
        # Place the three labels for text display
        self.l_label = build_label(self.myParent, 0, 0, 100, 100)
        self.l_label.configure(fg='grey')
        
        self.c_label = build_label(self.myParent, 100, 0, 100, 100)
        
        self.r_label = build_label(self.myParent, 200, 0, 100, 100)
        self.r_label.configure(fg='grey')

        # Use the text update function to set it initially
        self.update()

        # And immediately play the actual Main Menu entry phrase
        combine_wav_files(TMP_WAV, 
            MISC_PATH + "Entering_main_menu_Current_day_and_time_are_f.wav",
            self.options.head.data.get_domain().handle.data.get_wav(),
            self.options.head.next.data.get_domain().handle.data.get_wav(), 
            self.options.head.next.next.data.get_domain().handle.data.get_wav(), 
            self.options.look().get_wav())
        Play(TMP_WAV)

        # Bind the listeners
        self.myParent.bind("j", self.left)
        self.myParent.bind("k", self.right)
        self.myParent.bind("<space>", self.select)

        # Pack the window to its elements
        self.myContainer.pack()


    # Listener function for LEFT (J) key
    @log_event
    def left(self, _):
        self.activeList.move_left()
        self.update()


    # Listener function for RIGHT (K) key
    @log_event
    def right(self, _):
        self.activeList.move_right()
        self.update()


    # Listener function for SELECT (S) key
    @log_event
    def select(self, _):
        # Identify the selected item
        selection = self.activeList.look()

        # Respond depending on the selection
        if type(selection) is MenuDatum:
            # Selection was on main menu - activate chosen submenu or quit

            if selection.get_domain():
                self.activeList = selection.get_domain()
                # DEVNOTE: Here is where you should concatenate the state entry wav files...
                self.update()
                # DEVNOTE: Here is where you should actually play it, to overwrite the normal
                # one played by the update() function. 
                # DEVNOTE: There aren't the right wav files to do this for every menu, so I'm
                # leaving it alone as a 'thing to do if I have the time'. Unlikely.
            else:
                # User has prompted program to exit
                Play(MISC_PATH + "Exiting_program_f.wav")
                sleep(1.53)
                exit()

        elif type(selection) is Datum:
            # Selection was on submenu

            # As nasty as the concatenation looks, we're really just pulling the current
            # handles from the appropriate submenus and asking for their respective
            # wav file locations. 
            combine_wav_files(TMP_WAV, 
                MISC_PATH + "Entering_main_menu_Current_day_and_time_are_f.wav",
                self.options.head.data.get_domain().handle.data.get_wav(),
                self.options.head.next.data.get_domain().handle.data.get_wav(), 
                self.options.head.next.next.data.get_domain().handle.data.get_wav(), 
                self.options.look().get_wav())

            self.activeList = self.options
            self.update()
            Play(TMP_WAV)


    # Helper function to update the text and play sound when called
    def update(self):

        # Set the center label
        self.c_label['text'] = self.activeList.look().get_text()
        Play(self.activeList.look().get_wav())
        
        # Check for text to the left
        if self.activeList.peek_left():
            self.l_label['text'] = self.activeList.peek_left().get_text()
        else:
            self.l_label['text'] = ""

        # Check for text to the right
        if self.activeList.peek_right():
            self.r_label['text'] = self.activeList.peek_right().get_text()
        else:
            self.r_label['text'] = ""



# Helper function for making labels sized using frames
# Drawn from StackOverflow ('Label width in tkinter')
def build_label(master, x, y, h, w, *args, **kargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)
    f.place(x=x, y=y)
    label = Label(f, *args, **kargs)
    label.pack(fill=BOTH, expand=1)
    return label


# Main body of code, where execution starts
def main():
    # Create the application and run it
    root = Tk()
    mainapp = MainApp(root)
    root.mainloop()

# Execute the code
main()
