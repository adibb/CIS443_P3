__author__ = 'hornof'

# From http://www.ferg.org/thinking_in_tkinter/tt070_py.txt
# Adapted by A. Hornof 2017

from tkinter import *
import sound

class MyApp:
	def __init__(self, parent):
		self.myParent = parent
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.myParent.bind("<j>", self.keyPress)  # ajh
		self.myParent.bind("<k>", self.keyPress)  # ajh

		self.button1 = Button(self.myContainer1)
		# The background colors appear in Windows but not on a Macintosh.
		self.button1.configure(text="OK", background= "green")
		self.button1.pack(side=LEFT)
		self.button1.focus_force()         ### (0)
		self.button1.bind("<Button-1>", self.button1Click)
		self.button1.bind("<j>", self.button1Click)  ### (1)

		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Cancel", background="red")
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Button-1>", self.button2Click)
		self.button2.bind("<k>", self.button2Click)  ### (2)

	# The background colors appear in Windows but not on a Macintosh.
	def button1Click(self, event):
		report_event(event)        ### (3)
		if self.button1["background"] == "green":
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"

	def button2Click(self, event):
		report_event(event)   ### (4)
		self.myParent.destroy()

	def keyPress(self, event):
		report_event(event)   ### (4)

def report_event(event):     ### (5)
	"""Print a description of an event, based on its attributes.
	"""
	event_name = {"2": "KeyPress", "4": "ButtonPress"}
	print ("Time:", str(event.time))   ### (6)
	print ("event:", event)

	# Sample sound
	sound.Play( "01_f.wav" )


root = Tk()
myapp = MyApp(root)
root.mainloop()