import time
import os.path
from Signal import Signal

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
		self.setCurrentDate(time.strftime("%d_%m_%Y"))
		self.__locationID = location
		
	def getCurrentDate(self):
		return self.__currentDate

	def isCurrentDate(self, date):
		return self.__currentDate == date
	
	def setCurrentDate(self, date):
		self.__currentDate = date
		
	#init the file with headersls
	def quickInit(self, filePath):
		headers = "ID,Location,Date,Time"
		file = open(filePath, 'w+')
		file.write(headers + '\n')
		file.close()

	#opens the file, write the string to end of file, closes file
	def quickAppend(self, target):
		self.f = open(self.relfilePath + self.getCurrentDate + self.__fileExtension, 'a')
		self.f.write(target)
		self.f.close()

	#opens the file, writes each string in the buffer to the file, closes file
    #TODO need to edit the filePath to include the bin color, not the signal
	def quickAppendBuffer(self, target):
		date = time.strftime("%d_%m_%Y") #get current date
		if not self.isCurrentDate(date): #check if the date has changed
			self.setCurrentDate(date)
			
		#create file according to date, location and bin color
		filePathBlue = self.relfilePath + self.getCurrentDate() + "_" + self.__locationID + "_" + "blue" + self.__fileExtension
		filePathGreen = self.relfilePath + self.getCurrentDate() + "_" + self.__locationID + "_" + "green" + self.__fileExtension
		filePathGrey = self.relfilePath + self.getCurrentDate() + "_" + self.__locationID + "_" + "grey" + self.__fileExtension
		filePathBlack = self.relfilePath + self.getCurrentDate() + "_" + self.__locationID + "_" + "black" + self.__fileExtension
		if not os.path.isfile(filePathBlue): #create a new file if new date
			self.quickInit(filePathBlue)
		if not os.path.isfile(filePathGreen): #create a new file if new date
			self.quickInit(filePathGreen)
		if not os.path.isfile(filePathGrey): #create a new file if new date
			self.quickInit(filePathGrey)
		if not os.path.isfile(filePathBlack): #create a new file if new date
			self.quickInit(filePathBlack)
		currentBlueFile = open(filePathBlue, 'a')
		currentGreenFile = open(filePathGreen, 'a')
		currentGreyFile = open(filePathGrey, 'a')
		currentBlackFile = open(filePathBlack, 'a')
		
		for line in target:
			color = Signal.parseSignal(line)[0]
			if not color:
				return
			if color == "blue"
				currentFileBlue.write(line + '\n')
			elif color is "green":
				currentFileGreen.write(line + '\n')
			elif color is "black":
				currentFileBlack.write(line + '\n')
			elif color is "grey":
				currentFileGrey.write(line + '\n')
			
		currentBlueFile.close()
		currentGreenFile.close()
		currentGreyFile.close()
		currentBlackFile.close()

	#open file, read everything, close file, return result
    #TODO need to edit the filePath to include the bin color, not the signal
	def quickRead(self, filePath):
		result = []
		self.f = open(filePath, 'r')
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
		
