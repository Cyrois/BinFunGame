#!/usr/bin/env python

from SDfile import SDfile

#Constants
SDfileRootPath = "/home/chris/BinFunGame/src/TempFiles/"
headers = "ID,Location,Date,Time"

def main():
	#a = append, r+ = read/write, w = write, r = read

	#Test using a class
	sensor2 = SDfile(SDfileRootPath, "Nest")
	#sensor2.quickInit(headers)
	#sensor2.quickAppend("3,nest,sept12,5:30pm" + '\n')
	#sensor2.quickAppend("4,nest,sept12,5:30pm" + '\n')
	#sensor2.quickAppend("4,nest,sept12,10:30pm" + '\n')
	sensor2.quickAppendBuffer(["black,panago,sept12,10:30pm", "green,pizzahut,sept12,10:30pm", "black,freshSlice,sept12,10:30pm"])
	#print "quickRead: " + str(sensor2.quickRead())

if __name__ == "__main__":
	main()
