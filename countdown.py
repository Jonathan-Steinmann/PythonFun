import time
import os

S120 = 120
S1500 = 1500
S2000 = 2000
S2500 = 2500
FAIL = '\033[91m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'

Art1 = [
	" ", "I MUST USE WINDOWS 8 AS INSTRUCTED.           ",  "                           \                  ", 
	"                                .....         ", "                               C C  /         ", "                              /<   /          ", 
	"               ___ __________/_#__=o          ", "              /(- /(\_\________   \           ", "              \ ) \ )_      \o     \          ", 
	"              /|\ /|\       |'     |          ", "                            |     _|          ", "                            /o   __\          ", 
	"                           / '     |          ", "                          / /      |          ", "                         /_/\______|          ", 
	"                        (   _(    <           ", "                         \    \    \          ", "                          \    \    |         ", 
	"                           \____\____\        ", "                           ____\_\__\_\       ", "                         /`   /`     o\       ", 
	"                         |___ |_______|       ", " "
]

Art2 = [
	" ", " ", " _   _| |__  _   _ _ __ | |_ _   _ ", "| | | | '_ \| | | | '_ \| __| | | |", "| |_| | |_) | |_| | | | | |_| |_| |", 
	" \__,_|_.__/ \__,_|_| |_|\__|\__,_|", " ", "               | |       ", "  _ __ __   ___| | _____ ", "| '__/ _ \ / __| |/ / __|", 
	"| | | (_) | (__|   <\__ \.", "|_|  \___/ \___|_|\_\___/", " ", " "
]

def checkOS():
	if os.name == 'nt':
		import winsound
		return True
	else:
		return False

def napTime(ms=1):
	time.sleep(ms)

def soundFactory(freq, dur):
	if checkOS == True:
		winsound.Beep(freq, dur)
	else:
		print '\a'

def theMostAnnoyingSoundInTheWorld(n=0):
	for value in range(n):
		soundFactory(S1500, S2000); 

def theLessAnnoyingSoundSequence(n=0):
	for value in range(n):
		soundFactory(S1500, S120)
		soundFactory(S2000, S120)
		soundFactory(S2500, S120)

def sanityCountdown(seconds=0):
	while seconds > 0:
		napTime(1)
		print (" " + str(seconds))
		seconds = seconds-1
	else:
		napTime(1)
		for row1 in Art1:
			napTime(1)
			print(row1)
		print(FAIL + "MAJOR FAIL DETECTION ALERT... MUST STOP WINDOWS 8..." + ENDC)
		napTime(1)
		theMostAnnoyingSoundInTheWorld(1)
		napTime(1)
		theLessAnnoyingSoundSequence(3)
		napTime(3)
		print(OKGREEN + "anti-Windows sequence started..." + ENDC)
		napTime(3)
		for x in range(0,20000):
			for row2 in Art2:
				print(row2)
		for row3 in Art2:
			napTime(1)
			print(OKGREEN + row3)
		print(":) \r\n" + ENDC)


#run option - no requirements
if __name__ == '__main__':
	sanityCountdown()

# run option - require countdown
# if __name__ == '__main__':
# 	try:
#		import sys
# 		seconds = (int(sys.argv[1]))
# 		sanityCountdown(seconds)
# 	except IndexError:
# 		print("How to use: countdown.py <number>")


