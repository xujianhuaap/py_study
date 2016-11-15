#!/usr/bin/python
#coding=utf-8
import os
import os.path
import shutil
import traceback
import logging
#抛出异常
def createFile(fileName):
	if(os.path.exists(fileName)):
		raise Exception('file existed')
	currentWork=os.getcwd()
	filePath=os.path.join(currentWork,fileName)
	file=open(filePath,'w')
	file.write('jia qianwen')
	file.close()
	return file

#捕获异常
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s- %(message)s',filename='test.log')
try:	
	createFile('love')
except Exception as Error:
	currentWork=os.getcwd()
	errPath=os.path.join(currentWork,'error.log')
	errFile=open(errPath,'w')
	try:
		tr=traceback.format_exc()
		errFile.write(tr)
		errFile.close()
		logging.debug('file existed')
	except UnicodeDecodeError:
		logging.debug('decoding error')

stu=os.path.join(currentWork,'student');		
if os.path.exists(stu):
	shutil.rmtree(stu)
	
student=os.path.join(currentWork,'student.txt')
if(os.path.exists(student)):
	os.unlink(student)

	
		
	