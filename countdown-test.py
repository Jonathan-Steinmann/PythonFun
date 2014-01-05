#requires python 3
import unittest
from unittest.mock import patch
import random
from countdown import Countdown

class countdownTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testExample(self):
		result = 2+2
		self.assertEqual(4, result)

	def testGetArt(self):
		#action
		result = Countdown.getArt(Countdown, "art3")
		#assert
		self.assertEqual(Countdown.Art3, result)

	def testTheMostAnnoyingSoundInTheWorld(self):
		#setup
		sound = Countdown.soundFactory(Countdown, Countdown.S1500, Countdown.S2000)
		#action
		result = Countdown.theMostAnnoyingSoundInTheWorld(Countdown, 0)
		#assert
		self.assertEqual(sound, result)


if __name__ == '__main__':
    unittest.main()