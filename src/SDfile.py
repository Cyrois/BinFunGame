#Class that represents a csv file on the SDcard
#Each line represents a row in the table
class SDfile(file):
	f = ""
	filePath = "EMPTY"

	def __init__(self, path):
		self.filePath = path

	#init the file with headers
	def quickInit(self, headers):
		self.f = open(self.filePath, 'w')
		self.f.write(headers + '\n')
		self.f.close()

	#opens the file, write the string to end of file, closes file
	def quickAppend(self, target):
		self.f = open(self.filePath, 'a')
		self.f.write(target)
		self.f.close()

	#opens the file, writes each string in the buffer to the file, closes file
	def quickAppendBuffer(self, target):
		self.f = open(self.filePath, 'a')
		for line in target:
			self.f.write(line + '\n')
		self.f.close()

	#open file, read everything, close file, return result
	def quickRead(self):
		result = []
		self.f = open(self.filePath, 'r')
		#result = self.f.readlines( )
		for line in self.f:
			editedLine = line.split('\n')
			result.append(editedLine[0])
		self.f.close()
		return result
		

	#Reads the specified line and returns an array of strings where each entry represents a column
	def readLine(self,number):
		self.f = open(self.filePath, 'r')
		count = 0
		result = []
		for line in self.f:
			count = count + 1
			if count == number:
				line = line.strip() #remove whitespace
				result = line.split(",")
				break
		self.f.close()
		return result
	
	#Probably don't need to implement this
	#Takes as input which column to search under, and what you want to search for.
	def getLinesByID(self, column, searchString):
		print "not implemented yet"
		
