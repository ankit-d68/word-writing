import os

def system():
	os.system('clear')
	print("This is a Dictory automation tool!..\n\n")

	print("If you want to Quit the code Then press ctrl c Quiting,........!!!\n")

def file_open():
	file_name = raw_input("Enter the file name: ")
	if '.txt' in file_name:
		file = open(file_name,'w')
		count = 1
		while True:
			dic_word = raw_input(str(count) + ") " +  "Enter the dic word you want to write: ")
			count+=1
			if dic_word:
				word = file.write(dic_word + "\n")
			elif dic_word is "":
				print("\tBlank!!") 
		
		file.close()

	else:
		print(".txt extention is not given.")

try:
	system()
	file_open()
except KeyboardInterrupt:
	pass


