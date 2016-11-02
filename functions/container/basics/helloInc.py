# Hello functions

import core.siriHelpers as res

# Say hello to user
def hello():
	return "Hello " + res.userName() + " !"

# Present the assistant
def assistantPresentation():
	return "I am " + res.assistantName() + ". I am here to help you."