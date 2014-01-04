import unittest
from countdown import Countdown

class testCountdown(unittest.TestCase):

	def setUp(self):
		pass

	def testExample(self):
		result = 2+2
		self.assertEqual(4, result)

	def testGetArt(self):
		result = Countdown.getArt(Countdown, "art3")
		self.assertEqual(Countdown.Art3, result)



if __name__ == '__main__':
    unittest.main()