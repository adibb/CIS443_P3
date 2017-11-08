__author__ = 'adibb'

# Written by Alex Dibb
# Last edited 11/8/2017
# Based on A. Hornof's Tkinter_sample.py from the Fall 2017 CIS 443 Class at UO


# IMPORTS
from tkinter import *
from ddec import *
import sound

# Application definition
class MainApp:
    # On initialization - build the actual app window
    def __init__(self, parent):
        # Define the parent and container
        self.myParent = parent
        self.myContainer = Frame(parent)

        # Bind the listeners
        self.myParent.bind("j", self.left)
        self.myParent.bind("k", self.right)
        self.myParent.bind("<space>", self.select)

        # Pack the 
        self.myContainer.pack()


    # Listener function for LEFT (J) key
    @log_event
    def left(self, _):
        print("L")


    # Listener function for RIGHT (K) key
    @log_event
    def right(self, _):
        print("R")


    # Listener function for SELECT (S) key
    @log_event
    def select(self, _):
        print("S")


root = Tk()
mainapp = MainApp(root)
root.mainloop()
