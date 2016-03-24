import time
import os.path

#Class that represents a csv file
#Each line represents a row in the table
class CSVfile(file):
	f = ""
	relfilePath = "EMPTY"
	__filePath = ""
	__fileExtension = ".csv"
	__startDate = ""
	__endDate = ""
	__locationID = ""
	__color = ""

	def __init__(self, relativePath, start, end, location, color):
		self.relfilePath = relativePath
		self.__startDate = start
		self.__endDate = end
		self.__locationID = location
		self.__color = color
		self.__filePath = self.relfilePath + self.__startDate + "_" + self.__endDate + "_" + self.__locationID + "_" + self.__color + self.__fileExtension
		self.quickInit()
		
	#CREATE and init the file with headers
	def quickInit(self):
		headers = "ID,Location,Date,Time"
		file = open(self.__filePath, 'w+')
		file.write(headers + '\n')
		file.close()

	#open the file
	def openFile(self):
		self.f = open(self.__filePath, 'a')

	#write the string to end of file
	def quickAppend(self, target):
		self.f.write(target + '\n')

	#close file
	def closeFile(self):
		self.f.close()

	#open file, read everything, close file, return result
	def quickRead(self):
		result = []
		self.f = open(self.__filePath, 'r')
		for line in self.f:
			editedLine = line.split('\n')
			result.append(editedLine[0])
		self.f.close()
		return result
		
