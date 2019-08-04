import os
import shutil
import sys


print('            #####################################')
print('            #                                   #')
print('            #        Beautiful Folder           #')
print('            #        version 1.0                #')
print('            #        Author: Owbird             #')
print('            #        https://github.com/owbird  #')
print('            #                                   #')
print('            #####################################')

# validating path
try:

	if os.chdir(input('[+] Enter path to folder to beautify: ')) == '':
	
		print('[-] Path cannot be empty')
		
		sys.exit()
		
except (FileNotFoundError, OSError):

	print('[-] check path')
	
	sys.exit() 

# path to folder
path = os.getcwd()

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

print(f'[+] Beautification of {os.path.basename(path)} is complete')
