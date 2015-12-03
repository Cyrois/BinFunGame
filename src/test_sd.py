from SDfile import SDfile
import os
import time

def test_isCurrentDate(tmpdir):
	p = tmpdir.mkdir("sub")
	sd = SDfile(str(p), "location")
	curDate = time.strftime("%d_%m_%Y")
	assert sd.isCurrentDate(curDate) == True

def test_getCurrentDate(tmpdir):
	p = tmpdir.mkdir("sub")
	sd = SDfile(str(p), "location")
	curDate = time.strftime("%d_%m_%Y")
	assert sd.getCurrentDate() == curDate

def test_setCurrentDate(tmpdir):
	p = tmpdir.mkdir("sub")
	sd = SDfile(str(p), "location")
	curDate = time.strftime("12_12_12")
	sd.setCurrentDate(curDate)
	assert sd.getCurrentDate() == curDate

def test_quickInit(tmpdir):
	p = tmpdir.mkdir("sub").join("blue.csv")
	curDate = time.strftime("%d_%m_%Y")
	filePathBlue = str(p) + curDate + "_" + "location_blue.csv"
	sd = SDfile(str(p), "location")
	sd.quickInit(filePathBlue)
	read = sd.quickRead(filePathBlue)
	expected = "ID,Location,Date,Time"
	assert read[0] == expected
