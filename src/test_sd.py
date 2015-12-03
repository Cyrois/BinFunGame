from SDfile import SDfile
import os
import time

def test_isCurrentDateTest(tmpdir):
	p = tmpdir.mkdir("sub")
	print p
	sd = SDfile(str(p), "location")
	curTime = time.strftime("%d_%m_%Y")
	print sd.isCurrentDate(curTime)
	assert sd.isCurrentDate(curTime) == True
