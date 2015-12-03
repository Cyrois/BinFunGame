from Buffer import Buffer

class test_sd:

	def getEmptyFlagTest(self):
		testBuffer = Buffer("location", "black", "green", "blue", "grey")
		self.assertTrue(testBuffer.getEmptyFlag())

