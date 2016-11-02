# This file define Siri skills 
# Functions autocall
import functions.autocall

#Prepare file
wordsList = {

	"exit": exit,

	"good": {
		"bye": exit,
	},

	"hello": functions.container.basics.helloInc.hello,

	"i": {
		
		"hate": {
			"you": functions.container.basics.relationsInc.hateYou,
		},

		"love": {
			"you": functions.container.basics.relationsInc.loveYou,
		},
	},

	"play": {
		"music": functions.container.music.playMusicInc.playMusic,
	},

	"quit": exit,

	"who": {
		"are": {
			"you" : functions.container.basics.helloInc.assistantPresentation,
		},
	},

	"what": {
		"is": {
			"the": {
				"current": {
					"version": functions.container.system.versionInc.printVersion
				},
			},
		},
	},
}