from subprocess import run
from re import error
import sys
import os
import re

HELP_MSG="""USAGE: python3 main.py [Command] [Params]

(No command)  Print all tasks
h[elp]        This message
i[nit]        Make .todo file
a[dd] STR     Add STR to todo list
r[m] NUM      Removes task NUM from list
r[m] NUM,NUM  Removes comma-seperated list of tasks from list
impor[t] STR  Import an existing file STR to a .todo file
s[earch] STR  Search and print tasks that match substring STR
rege[x] REG   Search and print tasks that match regex REG
c[lean]       Cleans current file of newlines and whitespace
v[im]         Open list in vim
v[im] REG     Open list in vim with regex REG highlighted
"""

def vim_open(filen, reg=None):
	if reg:
		#write temporary file with passed regex (needed for -s command in vim)
		with open(".vootodoo.tmp", "w+") as f:
			f.write("/"+reg+"\n")

		run(["vim", filen, "-s", ".vootodoo.tmp"])
		os.remove(".vootodoo.tmp") #remove temporary file

	else:
		run(["vim", filen])

def ask_path():
	paths=find(True)

	print("Choose folder to create .todo file in:\n")

	for index, val in enumerate(paths):
		print("["+str(index)+"] - "+val)

	print("") #adds newline
	choice=int(input("> "))

	if 0<=choice and choice<len(paths):
		return paths[choice] #valid selection, return it

	else:
		print("\nInvalid selection, quitting")
		exit(-1)

def find(indexing=False):
	path=os.getcwd().split("/")

	filen=None
	total=[] #stores all searched paths if indexing
	while len(path)>2: #find the closest .todo file from the current directory
		filen=""
		for directory in path:
			filen+=directory+"/"

		filen+=".todo"

		if os.path.isfile(filen):
			if not indexing:
				break #todo file was found, return the path

		else:
			total.append(filen)

		path=path[:-1]

	if not indexing:
		if len(path)==2:
			return "" #return nothing if a .todo file wasnt found

		return filen

	else:
		return total

if __name__=="__main__":
	args=sys.argv[1:] #remove filename from args

	filen=find()

	if len(args)>0: #if the first param is set, set it to lowercase
		args[0]=args[0].lower()

	if len(args)>1: #merges all args after first arg into one
		args=[
			args[0],
			" ".join(str(i) for i in args[1:])
		]

	if len(args)==0: #user just wants to print todo list
		if filen:
			with open(filen, "r") as f:
				for index, val in enumerate(f):
					print("["+str(index)+"] - "+val.strip()) #loops through and prints indexes for each line

		else:
			print("todo file not found, run\n\nmain.py init\n\nto create todo file")
			exit(-1)

	elif len(args)==1: #a command is being ran w/o params
		if args[0]=="init" or args[0]=="i":
			choice=ask_path()

			f=open(choice, "w+") #only create file
			f.close()

			print("\nCreated file", choice)

		elif args[0]=="clean" or args[0]=="c":
			data=[]
			with open(filen, "r+") as f:
				for val in f:
					data.append(val)

			with open(filen, "w+") as f:
				for val in data:
					if val.strip():
						f.write(val.strip()+"\n")

			print("Done")

		elif args[0]=="vim" or args[0]=="v":
			vim_open(filen)

		else:
			print(HELP_MSG)

	else: #len(args) is 2 (command with params is being ran)
		if args[0]=="add" or args[0]=="a": #add new task to todo file
			if filen: #if filename is set add to todo
				with open(filen, "a") as f:
					f.write("\n"+args[1])

				print("added \""+args[1]+"\" in "+filen)

			else:
				print("todo file not found, run\n\nmain.py init\n\nto create todo file")
				exit(-1)

		elif args[0]=="rm" or args[0]=="r": #removes the indicated values from list
			remove=[int(i) for i in args[1].split(",")]

			data=[]
			with open(filen, "r+") as f: #read all lines from file
				data=f.readlines()

			with open(filen, "w+") as f: #write all lines that arent about to be removed
				for index, val in enumerate(data):
					if index not in remove:
						f.write(val)

		elif args[0]=="search" or args[0]=="s": #substring based search
			with open(filen, "r+") as f:
				for index, val in enumerate(f):
					if args[1] in val:
						print("["+str(index)+"] - "+val.strip())

		elif args[0]=="regex" or args[0]=="x": #regex based search
			with open(filen, "r+") as f:
				for index, val in enumerate(f):
					stripped=val.strip()
					try:
						if re.match(args[1], stripped)[0]:
							print("["+str(index)+"] - "+stripped)

					except (re.error, TypeError):
						print("Invalid regex, skipping")

		elif args[0]=="import" or args[0]=="t":
			data=[]
			if os.path.isfile(args[1]):
				with open(args[1], "r+") as f:
					for index, val in enumerate(f):
						if val.strip(): #only grab line if not blank
							data.append(val.strip())

			else:
				print("Cannot find file: '"+args[0]+"', exitting")
				exit(-1)

			choice=ask_path()

			print(choice)
			with open(choice, "w+") as f:
				help(f)
				for line in data:
					f.write(line+"\n")

		elif args[0]=="vim" or args[0]=="v":
			vim_open(filen, args[1])

		else:
			print(HELP_MSG)