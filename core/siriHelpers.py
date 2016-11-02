# These helpers are user to make access 
# to ressources easier on a single file

#Import required elements
import core.siriUtils as su
import core.siriConfig as sc


# This function returns the name of user
def userName():
	return sc.userName

# This function returns the name of assistant
def assistantName():
	return sc.assistantName

# Returns software's version
def softwareVersion():
	return sc.version

# Returns music folder
def musicFolder():
	return sc.musicFolder