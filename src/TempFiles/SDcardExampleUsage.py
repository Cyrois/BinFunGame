#!/usr/bin/env python

from classes.SDfile import SDfile

#Constants
SDfileRootPath = "/home/chris/capstone/SDcard/"
headers = "ID,Location,Date,Time"

def main():
	#a = append, r+ = read/write, w = write, r = read

	#Test without using the class
	sensor1 = open(SDfileRootPath+"sensor1.csv", 'w')
	sensor1.write(headers + '\n')
	sensor1.close()
	sensor1 = open(SDfileRootPath+"sensor1.csv", 'a')
	sensor1.write("3,nest,sept12,5:30pm" + '\n')
	sensor1.close()
	sensor1 = open(SDfileRootPath+"sensor1.csv", 'r+')
	print "Junk: " + str(sensor1.readlines())

	#Test using a class
	sensor2 = SDfile(SDfileRootPath+"sensor2.csv")
	sensor2.quickInit(headers)
	sensor2.quickAppend("3,nest,sept12,5:30pm" + '\n')
	sensor2.quickAppend("4,nest,sept12,5:30pm" + '\n')
	sensor2.quickAppend("4,nest,sept12,10:30pm" + '\n')
	sensor2.quickAppendBuffer(["4,panago,sept12,10:30pm", "5,pizzahut,sept12,10:30pm", "6,freshSlice,sept12,10:30pm"])
	print "quickRead: " + str(sensor2.quickRead())
	print "readLine: " + str(sensor2.readLine(2))

if __name__ == "__main__":
	main()
