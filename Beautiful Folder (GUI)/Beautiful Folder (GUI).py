from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import sys

# Creating the app
root = Tk()

# Setting the title of the app
root.title('Beautiful Folder')

# Setting icon of the app
if os.name == "nt":

	root.iconbitmap("folder.ico")

# Setting the size of the app	
root.geometry('500x500')

# Making the size fixed
root.resizable(False, False)

# Setting background color
root.configure(bg='light grey')


# About info
about_txt = f"""
Beautiful Folder
version 2.0
Author: Owbird
https://github.com/owbird 
"""

def done(event):

	# Selectin folder to beautify
	dir = filedialog.askdirectory(title='Select folder to save files')
	
	try:
	
		# Changing directory to selected folder
		os.chdir(dir)
	
	except FileNotFoundError:
	
		sys.exit()

	# Going through files
	for file in os.listdir():

		# if not a directory
		if os.path.isfile(file):

			# saving extension
			ext = os.path.splitext(file)[1].strip('.')

			# creating a directory with the extension
			try:
			
				os.mkdir(f'{ext} Files')
				
			except FileExistsError:
			
				pass
			
			finally:
			
				print(f'[*] Moving {file} to {ext} Files')

				# moving files
				try:
					
					shutil.move(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), ext+' Files'))
						
				except (FileNotFoundError, shutil.Error):
					
					print(f'\n[!] {file} Exists in {ext} Files')
					print('[*] Skipping...\n')
					
					pass
	
	# Alerting user
	messagebox.showinfo('Complete', f'Beautification of {os.path.basename(dir)} is complete')

# Creating button
button = Button(root, text='BEAUTIFY!',width=80, height=20, bg='red')
button.grid(row=0, column=0)
button.bind("<Button-1>", done)
						
# Displaying the about info
about_label = Label(root, text=about_txt, bg='light grey')
about_label.grid(row=1, column=0)

# App stays till user ends it
root.mainloop()
