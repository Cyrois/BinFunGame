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
	self.__filePathBlack = ''
	self.__filePathGreen = ''
	self.__filePathBlue = ''
	self.__filePathGrey = ''

	#constructor that will create a csv file for each of the bins for each new date
	def __init__(self, relativePath, location):
		self.relfilePath = relativePath
		self.setCurrentDate(time.strftime("%d_%m_%Y"))
		self.__locationID = location

		#create file according to date, location and bin color
		self.__filePathBlack = self.relfilePath + self.__currentDate + "_" + self.__locationID + "_" + "black" + self.__fileExtension
		self.__filePathGreen = self.relfilePath + self.__currentDate + "_" + self.__locationID + "_" + "green" + self.__fileExtension
		self.__filePathBlue = self.relfilePath + self.__currentDate + "_" + self.__locationID + "_" + "blue" + self.__fileExtension
		self.__filePathGrey = self.relfilePath + self.__currentDate + "_" + self.__locationID + "_" + "grey" + self.__fileExtension
		
		#CREATE and initialize the file with headers
		self.quickInit(filePathBlack)
		self.quickInit(filePathGreen)
		self.quickInit(filePathBlue)
		self.quickInit(filePathGrey)
		
	#get the current date
	def getCurrentDate(self):
		return self.__currentDate

	#return true if the current date is the same as the latest file being written to
	#a false value would indicate that a new file should be created to write the data to
	def isCurrentDate(self, date):
		return self.__currentDate == date
	
	#set the current date
	def setCurrentDate(self, date):
		self.__currentDate = date
		
	#CREATE and initialize the file with headers
	def quickInit(self, filePath):
		headers = "ID,Location,Date,Time"
		file = open(filePath, 'w+')
		file.write(headers + '\n')
		file.close()

	#opens the file, writes each string in the buffer to the file, closes file
    #TODO need to edit the filePath to include the bin color, not the signal
	def quickAppendBuffer(self, data):
		date = time.strftime("%d_%m_%Y") #get current date
		if not self.isCurrentDate(date): #check if the date has changed
			self.setCurrentDate(date);

			#create file according to date, location and bin color
			self.__filePathBlack = self.relfilePath + self.__currentDate + "_" + self.__locationID + "_" + "black" + self.__fileExtension;
			self.__filePathGreen = self.relfilePath + self.__currentDate + "_" + self.__locationID + "_" + "green" + self.__fileExtension
			self.__filePathBlue = self.relfilePath + self.__currentDate + "_" + self.__locationID + "_" + "blue" + self.__fileExtension
			self.__filePathGrey = self.relfilePath + self.__currentDate + "_" + self.__locationID + "_" + "grey" + self.__fileExtension

			#create a new file if new date
			if not os.path.isfile(self.__filePathBlack): 
				self.quickInit(self.__filePathBlack);
			if not os.path.isfile(self.__filePathGreen):
				self.quickInit(self.__filePathGreen);
			if not os.path.isfile(self.__filePathBlue): 
				self.quickInit(self.__filePathBlue);
			if not os.path.isfile(self.__filePathGrey): 
				self.quickInit(self.__filePathGrey);
		
		#open all of the current date's files
		currentFileBlack = open(self.__filePathBlack, 'a');
		currentFileGreen = open(self.__filePathGreen, 'a');
		currentFileBlue = open(self.__filePathBlue, 'a');
		currentFileGrey = open(self.__filePathGrey, 'a');

		#write all the signal data to their respective files
		for line in data:
			color = Signal.parseSignal(line)[0];
			if not color:
				return;
			if color == "black":
				currentFileBlack.write(line + '\n');
			if color == "green":
				currentFileGreen.write(line + '\n');
			if color == "blue":
				currentFileGreen.write(line + '\n');
			if color == "grey":
				currentFileGreen.write(line + '\n');
		
		#close all of the current date's files	
		currentFileBlack.close();
		currentFileGreen.close();
		currentFileBlue.close();
		currentFileGrey.close();

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
		
