from tkinter import *
from tkinter import ttk

class Screen(ttk.Frame):
	def __init__(self, root):
		super().__init__(root)
		
		self.root = root
		
class StartScreen(Screen):
	def __init__(self, root):
		super().__init__(root)
		
		#Title
		title_lbl = ttk.Label(self, text="Open World Game")
		title_lbl.pack(pady=10)
		
		
		#Options
		options_fr = ttk.Frame(self)
		options_fr.pack()
		
		#New Game
		new_game_btn = ttk.Button(options_fr, text="New Game")
		new_game_btn.pack(side="left")
		
		#Load Game
		load_game_btn = ttk.Button(options_fr, text="Load Game")
		load_game_btn.pack(side="left", padx=10)
		
		#Exit
		exit_btn = ttk.Button(options_fr, text="Exit", command=root.destroy)
		exit_btn.pack()
		