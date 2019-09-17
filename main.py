import sys
import os

HELP_MSG="""USAGE: python3 main.py [Command] [Params]

(No command)  - Print all tasks
h[elp]        - This message
i[nit]        - Make .todo file
a[dd] STR     - Add STR to todo list
r[m] NUM      - Removes task NUM from list
s[earch] STR  - Search and print tasks that match substring STR
r[egex] REG   - Search and print tasks that match regex REG
v[im]         - Open list in vim
v[im] REG     - Open list in vim with regex REG highlighted
"""

def find():
	path=os.getcwd().split("/")

	filen=None
	while len(path)>2: #find the closest .todo file from the current directory
		filen=""
		for directory in path:
			filen+=directory+"/"

		filen+=".todo"

		if os.path.isfile(filen):
			break

		path=path[:-1]

	return filen

if __name__=="__main__":
	args=sys.argv[1:] #remove filename from args

	filen=find()

	if len(args)>1: #merges all args after first arg into one
		args=[
			args[0].lower(),
			" ".join(str(i) for i in args[1:])
		]

	if len(args)==0: #user just wants to print todo list
		pass

	elif len(args)==1: #a command is being ran w/o params
		if args[0]=="help":
			print(HELP_MSG)

	else: #len(args) is 3 (command with params is being ran)
		pass