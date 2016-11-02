#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Documentation is like sex.
#   When it's good, it's very good.
#   When it's bad, it's better than nothing.
#   When it lies to you, it may be a while before you realize something's wrong.
#
#   from: raw.githubusercontent.com/beagerr/AutoClicker/master/clicker.py
#


import pyautogui
import sys

try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	# must be running python2
	import Tkinter as tk
	import ttk

__version__ = (0,1)
pyautogui.PAUSE = 0.075

class MainFrame(tk.Frame): #subclass Frame; MainFrame is now a type of Frame.
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.load_modules()

		self.bind('<space>', self.getPos)
		self.bind('<Escape>', self.quit)

	def load_modules(self):
		label_amount = tk.Label(self, text='Clicks: ')
		label_amount.place(x=10, y=10, width=50, height=20)

		self.spinbox_amount = tk.Spinbox(self, from_=0, to=500)
		self.spinbox_amount.place(x=10, y=35, width=180, height=20)

		label_x = tk.Label(self, text='Mouse X')
		label_x.place(x=25, y=100, width=50, height=15)

		self.entry_x = ttk.Entry(self)
		self.entry_x.place(x=25, y=120, width=150, height=25)

		label_y = tk.Label(self, text='Mouse Y')
		label_y.place(x=25, y=160, width=50, height=15)

		self.entry_y = ttk.Entry(self)
		self.entry_y.place(x=25, y=180, width=150, height=25)

		self.button_click = ttk.Button(self, text='Start', command=self.click)
		self.button_click.place(x=50, y=250, width=100, height=25)

		label_version = tk.Label(self, text='Version: ' + '.'.join(map(str,__version__)))
		label_version.place(x=50, y=350, width=100, height=20)

		label_name = tk.Label(self, text='Created by G.B')
		label_name.place(x=50, y=310, width=100, height=20)

		label_info = tk.Label(self, text='Press space to get mouse co-ords')
		label_info.place(x=0, y=380, width=200, height=20)

	def click(self):
		pyautogui.click(
			x=int(self.entry_x.get()),
			y=int(self.entry_y.get()),
			clicks=int(self.spinbox_amount.get()),
			interval=0,
			button='left')

	def getPos(self, event):
		self.entry_x.delete(0, 'end')
		self.entry_y.delete(0, 'end')
		self.mouse_pos = pyautogui.position()
		self.entry_x.insert(0, self.mouse_pos[0])
		self.entry_y.insert(0, self.mouse_pos[1])

def main():
	root = tk.Tk()
	app = MainFrame(root)
	app.pack(fill=tk.BOTH, expand=True)
	root.resizable(width=False, height=False)
	root.geometry('200x400')
	root.wm_title("George's Autoclicker")
	root.focus_set()
	root.mainloop()

if __name__ == '__main__':
	main()
