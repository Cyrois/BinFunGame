import time
import os.path
from Signal import Signal

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

	#opens the file, write the string to end of file, closes file
	def quickAppend(self, target):
		self.f = open(self.__filePath, 'a')
		self.f.write(target + '\n')
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

