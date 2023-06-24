import os

def system():
	os.system('clear')
	print("This is a word writing script!..\n\n")
	print("If you want to Quit the code Then press ctrl c Quiting,........!!!\n")

def file_open():
	file_name = str(input("Enter the file name: "))
	if '.txt' in file_name:
		file = open(file_name,'w')
		count = 1
		while True:
			dic_word = str(input((str(count) + ") " +  "Enter the  word you want to write: ")))
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


