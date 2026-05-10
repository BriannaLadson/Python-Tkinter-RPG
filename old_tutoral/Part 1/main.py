from tkinter import *

class Root(Tk):
	def __init__(self):
		super().__init__()
		self.title("Open World Game")
		self.state("zoomed")
		
if __name__ == "__main__":
	root = Root()
	
	root.mainloop()