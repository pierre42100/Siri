# Siri functions auto-caller
# Browse folders to call functions

#Requirements
import os

#Walking into folders to import files
files = []
for (dirpath, dirnames, filesnames) in os.walk("functions/container/"):
	for processFile in filesnames:
		if processFile.count('Inc.py') != 0:
			files.insert(1, dirpath + "/" + processFile)



#Importing each files
print("\n\nAutocall script \nWill import functions, please wait...")
for importFile in files:
	name = importFile.replace('/', '.')
	name = name.replace('.py', '')
	
	#Verbose
	print("Importing module :" + name)
	__import__(name)
print ("Import terminated. \n\n")