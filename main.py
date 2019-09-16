import sys
import os

if __name__=="__main__":
	args=sys.argv[1:]
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

	print(filen)