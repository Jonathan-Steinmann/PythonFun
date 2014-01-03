import sys
import time
import winsound

Art1 = [
	" ", " _   _| |__  _   _ _ __ | |_ _   _ ", "| | | | '_ \| | | | '_ \| __| | | |", 
	"| |_| | |_) | |_| | | | | |_| |_| |", " \__,_|_.__/ \__,_|_| |_|\__|\__,_|", " "
]

S120 = 120
S1500 = 1500
S2000 = 2000
S2500 = 2500

def napTime(ms=1):
	time.sleep(ms)

def soundFactory(freq, dur):
	winsound.Beep(freq, dur)

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
		print("anti-Windows sequence started... ")
		theMostAnnoyingSoundInTheWorld(1)
		napTime(1)
		theLessAnnoyingSoundSequence(4)
		for row in Art1:
			napTime(1)
			print(row)

# run option
if __name__ == '__main__':
	try:
		seconds = (int(sys.argv[1]))
		sanityCountdown(seconds)
	except IndexError:
		print("How to use: countdown.py <number>")