#*************************************************************
# This is just a simple word writing script
#
#
# To run the script in linux type python3 word_writing.py
# and  windows type python word_writing.py
#
#*************************************************************
import subprocess

def system():
	if subprocess.run("cls",shell=True):#This is window command
		pass
	elif subprocess.run("clear",shell=True):#This is linux command
		pass
	print("This is a word writing script!..\n\n")
	print("If you want to Quit the code Then press ctrl c Quiting,........!!!\n")

def file_open():
	file_name = str(input("Enter the file name: "))
	if '.txt' in file_name:
		file = open(file_name,'w')
		count = 1
		while True:
			word_write = str(input((str(count) + ") " +  "Enter the  word you want to write: ")))
			count+=1
			if word_write:
				word = file.write(word_write + "\n")
			elif word_write in "":
				print("\tBlank!!") 
		file.close()
	else:
	      print(".txt extention is not given.")

try:
    system()
    file_open()
except KeyboardInterrupt:
	pass


