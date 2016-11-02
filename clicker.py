try:
	import pyautogui, sys
	import tkinter as tk
except ImportError:
	print('Please install pyautogui with `pip install pyautogui`')

VERSION = '0.1'
pyautogui.PAUSE = 0.075

class main_frame:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.master.geometry('200x400')
		self.master.wm_title('George\'s Autoclicker')
		self.load_modules()
		self.position_widgets()
		self.master.bind('<space>', self.getPos)
		self.master.bind('<Escape>', self.close)

	def load_modules(self):
		self.button_click = tk.Button(self.master, text='Start', command=self.click)
		self.label_info = tk.Label(self.master, text='Press space to get mouse co-ords')
		self.spinbox_amount = tk.Spinbox(self.master, from_=0, to=500)
		self.label_amount = tk.Label(self.master, text='Clicks: ')
		self.entry_x = tk.Entry(self.master)
		self.entry_y = tk.Entry(self.master)
		self.label_x = tk.Label(self.master, text='Mouse X')
		self.label_y = tk.Label(self.master, text='Mouse Y')
		self.label_version = tk.Label(self.master, text='Version: ' + VERSION)
		self.label_name = tk.Label(self.master, text='Created by G.B')


	def position_widgets(self):
		self.spinbox_amount.place(x=10, y=35, width=180, height=20)
		self.button_click.place(x=50, y=250, width=100, height=25)
		self.label_info.place(x=0, y=380, width=200, height=20)
		self.label_amount.place(x=10, y=10, width=50, height=20)
		self.label_x.place(x=25, y=100, width=50, height=15)
		self.entry_x.place(x=25, y=120, width=150, height=25)
		self.label_y.place(x=25, y=160, width=50, height=15)
		self.entry_y.place(x=25, y=180, width=150, height=25)
		self.label_version.place(x=50, y=350, width=100, height=20)
		self.label_name.place(x=50, y=310, width=100, height=20)

	def click(self):
		for x in range(int(self.spinbox_amount.get())):
			pyautogui.click(x=int(self.entry_x.get()), y=int(self.entry_y.get()), clicks=int(self.spinbox_amount.get()), interval=0, button='left')

	def getPos(self, event):
		self.entry_x.delete(0, 'end')
		self.entry_y.delete(0, 'end')
		self.mouse_pos = pyautogui.position()
		self.entry_x.insert(0, self.mouse_pos[0])
		self.entry_y.insert(0, self.mouse_pos[1])

	def close(self, event):
		sys.exit()

def Main():
	root = tk.Tk()
	app = main_frame(root)
	root.resizable(width=False, height=False)
	root.focus_set()
	root.mainloop()

if(__name__ == '__main__'):
	Main()