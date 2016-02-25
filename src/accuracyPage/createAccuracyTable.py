#!/usr/bin/python
import MySQLdb
import time
import os.path
import sys
sys.path.insert(0,'/home/chris/BinFunGame/src')
from Signal import Signal
from Database import Database

db = Database("54.218.32.132", "bfguser", "bfg123", "bfg")
db.createAccuracyTable()