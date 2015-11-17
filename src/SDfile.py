import time
import os.path
#Class that represents a csv file on the SDcard
#Each line represents a row in the table
class SDfile(file):
	f = ""
	relfilePath = "EMPTY"
	__fileExtension = ".csv"
	__currentDate = ""
	__locationID = ""

	def __init__(self, relativePath, location):
		self.relfilePath = relativePath
		self.__currentDate = self.getCurrentDate()
		self.__locationID = location
		
	def getCurrentDate():
		return self.__currentDate

	def isCurrentDate(self, date):
		return self.__currentDate == date
	
	def setCurrentDate(self, date):
		self.__currentDate = date
		
	#init the file with headers
	def quickInit(self, filePath):
		headers = "ID,Location,Date,Time"
		self.f = open(filePath, 'w')
		self.f.write(headers + '\n')
		self.f.close()

	#opens the file, write the string to end of file, closes file
	def quickAppend(self, target):
		self.f = open(self.relfilePath + self.getCurrentDate + self.__fileExtension, 'a')
		self.f.write(target)
		self.f.close()

	#opens the file, writes each string in the buffer to the file, closes file
	def quickAppendBuffer(self, target):
		date = time.strftime("%x") #get current date
		if not self.isCurrentDate(date): #check if the date has changed
			self.setCurrentDate(date)
		for line in target:
			parseSignal = getattr(Signal(), 'parseSignal')
			signal = parseSignal(line)
			color = signal[0]
			filePath = self.relfilePath + self.getCurrentDate + self.__locationID + color + self.__fileExtension #create file according to date and bin color
			if not os.path.isfile(filePath): #create a new file if new date
				self.quickInit(filePath)
			currentFile = open(filePath, 'a')
			currentFile.write(line + '\n')
			currentFile.close()

	#open file, read everything, close file, return result
	def quickRead(self):
		result = []
		self.f = open(self.filePath, 'r')
		#result = self.f.relfilePath + self.getCurrentDate + self.__fileExtension( )
		for line in self.f:
			editedLine = line.split('\n')
			result.append(editedLine[0])
		self.f.close()
		return result
		

	#Reads the specified line and returns an array of strings where each entry represents a column
	def readLine(self,number):
		self.f = open(self.relfilePath + self.getCurrentDate + self.__fileExtension, 'r')
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
		
