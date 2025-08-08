from tkinter import *

import screens

class Root(Tk):
	def __init__(self):
		super().__init__()
		self.title("Open World Game")
		self.state("zoomed")
		
if __name__ == "__main__":
	root = Root()
	
	root.start_screen = screens.StartScreen(root)
	root.start_screen.pack(fill=BOTH, expand=1)
	
	root.mainloop()