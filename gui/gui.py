print (_author_)
import os
def main():
	try:
		try:
			import Tkinter
		except:
			import tkinter
		import pyglet
		os.system("cd Tools && python Gui.py")
	except Exception as e:
		print(e)
		input("")
if _name=='main_':
	main()
