# Siri programm utils

import os

# Say something function
def speak(message):
	message = message.replace('"', '\\\"')
	os.system('espeak "' + message + '"')

# Write something and then say it
def speakWrite(user, message):
	print(user + ": " + message)
	speak(message)

# Ask something to user
def askUser(user):
	return input(user + ": ")

# Parse a request to make it machine readable
def parseRequest(request):
	# To small letter
	result = request.lower()

	result = result.replace("?", "")
	result = result.replace("!", "")

	# Word parser
	result = result.replace("what's", "what is")

	# Returns result
	return result