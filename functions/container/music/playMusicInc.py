# Music player

import core.siriHelpers as res
from os import walk
import os

# Get assistant name
assistantName = res.assistantName()
userName = res.userName()

# Get music folders
def getMusicFolders():
	# Get music listing
	folders = []
	for (dirpath, dirnames, filenames) in walk(res.musicFolder()):
		for processDir in dirnames:
			folders.insert(1, [processDir, dirpath + processDir])

	# Return result
	return folders

# List musics from folders
def listFolderMusics(folder):
	# Get music listing
	musics = []
	for (dirpath, dirnames, filenames) in walk(folder):
		for processMusic in filenames:
			musics.insert(1, [processMusic, dirpath + processMusic])

	# Return result
	return musics

# Launch a music
def launchMusic(music):
	os.system('mpg123 "' + music + '"')

# Play musics from a specified folder
def playMusicsFolder(folder):
	#Get folder's 
	musics = listFolderMusics(folder);

	#Play musics
	for music, path in musics:
		#Inform user
		res.su.speakWrite(assistantName, "You are now listening: " + music)

		#Play music
		launchMusic(path)


# Play music
def playMusic():
	#Get musics list
	foldersList = getMusicFolders()

	#Ask user to know what does he want
	res.su.speakWrite(assistantName, userName + ", which folder would you like to listen ?")
	c = 0
	for folder, path in foldersList:
		res.su.speakWrite(assistantName, str(c) + " - " + folder)
		c += 1
	# Every musics
	res.su.speakWrite(assistantName, "A - All the musics")

	#User input
	choice = res.su.askUser(userName)

	#Interpret choice
	if choice == "A":
		musicFolder = res.musicFolder()
	else:
		musicFolder = foldersList[int(choice)][1] + "/"

	#Inform user
	res.su.speakWrite(assistantName, "You have chosen to listen to the following folder: " + musicFolder)

	#Play the music
	playMusicsFolder(musicFolder)

	return "You have finished to listen to music."