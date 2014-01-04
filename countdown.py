class Countdown:

	import time
	import os

	S120 = 120
	S1500 = 1500
	S2000 = 2000
	S2500 = 2500
	FAIL = '\033[91m'
	OKGREEN = '\033[92m'
	ENDC = '\033[0m'
	WIN8 = "I MUST USE WINDOWS 8 AS INSTRUCTED.           "
	ALERT = "CODE RED... MAJOR FAIL DETECTION ALERT... MUST ABORT WINDOWS 8..."
	START = "ANTI-WINDOWS SEQUENCE STARTING..."

	Art1 = [
		" ", WIN8,  "                           \                  ", 
		"                                .....         ", "                               C C  /         ", "                              /<   /          ", 
		"               ___ __________/_#__=o          ", "              /(- /(\_\________   \           ", "              \ ) \ )_      \o     \          ", 
		"              /|\ /|\       |'     |          ", "                            |     _|          ", "                            /o   __\          ", 
		"                           / '     |          ", "                          / /      |          ", "                         /_/\______|          ", 
		"                        (   _(    <           ", "                         \    \    \          ", "                          \    \    |         ", 
		"                           \____\____\        ", "                           ____\_\__\_\       ", "                         /`   /`     o\       ", 
		"                         |___ |_______|       ", " "
	]

	Art2 = [
		" _   _| |__  _   _ _ __ | |_ _   _ ", "| | | | '_ \| | | | '_ \| __| | | |", 
		"| |_| | |_) | |_| | | | | |_| |_| |", " \__,_|_.__/ \__,_|_| |_|\__|\__,_|"
	]

	Art3 = [
		" _   _| |__  _   _ _ __ | |_ _   _ ", "| | | | '_ \| | | | '_ \| __| | | |", "| |_| | |_) | |_| | | | | |_| |_| |", 
		" \__,_|_.__/ \__,_|_| |_|\__|\__,_|", " ", "               | |       ", "  _ __ __   ___| | _____ ", "| '__/ _ \ / __| |/ / __|", 
		"| | | (_) | (__|   <\__ \.", "|_|  \___/ \___|_|\_\___/", " ", " "
	]

	def checkOS(self):
		if os.name == 'nt':
			import winsound
			return True
		else:
			return False

	def napTime(self, ms=1):
		self.time.sleep(ms)

	def soundFactory(self, freq, dur):
		if self.checkOS == True:
			self.winsound.Beep(freq, dur)
		else:
			print("\a")

	def theMostAnnoyingSoundInTheWorld(self, n=0):
		for value in range(n):
			self.soundFactory(self.S1500, self.S2000); 

	def theLessAnnoyingSoundSequence(self, n=0):
		for value in range(n):
			self.soundFactory(self.S1500, self.S120)
			self.soundFactory(self.S2000, self.S120)
			self.soundFactory(self.S2500, self.S120)

	def getArt(self, arg):
		if arg == "art1":
			return self.Art1
		elif arg == "art2":
			return self.Art2
		else:
			return self.Art3

	def sanityCountdown(self, seconds=0):
		while seconds > 0:
			self.napTime(1)
			print (" " + str(seconds))
			seconds = seconds-1
		else:
			self.napTime(1)
			for row1 in self.getArt("art1"):
				self.napTime(1)
				print(row1)
			print(self.FAIL + self.ALERT + self.ENDC)
			self.napTime(1)
			self.theMostAnnoyingSoundInTheWorld(1)
			self.napTime(1)
			self.theLessAnnoyingSoundSequence(3)
			self.napTime(3)
			print(self.OKGREEN + self.START + self.ENDC)
			self.napTime(3)
			for x in range(0,70000):
				for row2 in self.getArt("art2"):
					print(row2)
			for y in range(0,50):
				print("\r\n")
			for row3 in self.getArt("art3"):
				self.napTime(1)
				print(self.OKGREEN + row3)
			print(":) \r\n" + self.ENDC)


#run option - no requirements
if __name__ == '__main__':
	countdown = Countdown()
	countdown.sanityCountdown()

# run option - require countdown
# if __name__ == '__main__':
# 	try:
# 		import sys
# 		countdown = Countdown()
# 		seconds = (int(sys.argv[1]))
# 		countdown.sanityCountdown(seconds)
# 	except IndexError:
# 		print("How to use: countdown.py <number>")


