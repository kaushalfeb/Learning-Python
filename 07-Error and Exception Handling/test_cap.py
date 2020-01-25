import unittest	
import cap

class Test(unittest.TestCase):
	
	def test_one_word(self):
		text = 'python'
		result = cap.cap_test(text)
		self.assertEqual(result,'Python')

	def test_each_word(self):
		text = 'monty python'
		result = cap.cap_test(text)
		self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
	unittest.main()