import sys
import os

HELP_MSG="""USAGE: python3 main.py [Command] [Params]

(No command)  * Print all tasks
h[elp]        - This message
i[nit]        - Make .todo file
a[dd] STR     - Add STR to todo list
r[m] NUM      * Removes task NUM from list
s[earch] STR  * Search and print tasks that match substring STR
r[egex] REG   * Search and print tasks that match regex REG
v[im]         * Open list in vim
v[im] REG     * Open list in vim with regex REG highlighted

* Not implemented yet
"""

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

	if len(args)>0:
		args[0]=args[0].lower()

	if len(args)>1: #merges all args after first arg into one
		args=[
			args[0],
			" ".join(str(i) for i in args[1:])
		]

	if len(args)==0: #user just wants to print todo list
		print(HELP_MSG)

	elif len(args)==1: #a command is being ran w/o params
		if args[0]=="init" or args[0]=="i":
			paths=find(True)

			print("Choose folder to create .todo file in:\n")

			for index, val in enumerate(paths):
				print("["+str(index)+"] - "+val)

			print("") #adds newline
			choice=int(input("> "))

			if 0<=choice and choice<len(paths):
				f=open(paths[choice], "w+") #only create file
				f.close()

				print("\nCreated file", paths[choice])

			else:
				print("\nInvalid selection, quitting")
				exit(-1)

		else:
			print(HELP_MSG)

	else: #len(args) is 2 (command with params is being ran)
		if args[0]=="add" or args[0]=="a": #add new task to todo file
			filen=find()

			if filen: #if filename is set add to todo
				with open(filen, "a") as f:
					f.write(args[1])

				print("added \""+args[1]+"\" in "+filen)

			else:
				print("todo file not found, run\n\nmain.py init\n\nto create todo file")
				exit(-1)

		else:
			print(HELP_MSG)