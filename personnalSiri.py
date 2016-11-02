#!/usr/bin/python3
#
#	a Siri personnal assistant
# 	can replace official Siri software (or not ?)
# 	(c) Pierre HUBERT 2016
import os
import core.siriHelpers as res

import functions.autocall
import functions.functions as sf

#Assistant and user name extraction
assistantName = res.sc.assistantName
userName = res.sc.userName


# Welcome message
res.su.speakWrite(assistantName, "Hello " + userName + ", my name is " + assistantName + ". I am here to help you.")
res.su.speakWrite(assistantName, "What can I do for you now ?")

#Always run this programm while user hasn't asked to quit
while 1 == 1:
	#Get user input
	request = res.su.askUser(userName)
	
	#Parse request to help it to be understood
	requestParsed = res.su.parseRequest(request)

	#Split request in an array
	requestList = requestParsed.split(" ")

	#Searching function
	elem = sf.wordsList
	for word in requestList:
		#To lower case
		word = word.lower()

		#We check if result isn't empty
		if word == "":
			break

		#If we found something in the list
		if word in elem:
			#Adding word to list
			elem = elem[word]

		#If we didn't find anything, break loop
		else:
			break

	#If element is callable, we call it
	if callable(elem):
		res.su.speakWrite(assistantName, elem())

	#Else nothing can be done, return error
	else:
		res.su.speakWrite(assistantName, "I didn't understand your request. Please reformulate it.")