#file read 
import os
import shutil
import fileinput
import shelve

#创建文件
def writeFile(dirName):
	try:
		studentFile=os.path.join(dirName,'student.txt')
		student=open(studentFile,'w')
		student.write('jia qian wen ,i love you')
		student.close()
		return student
	except OSError:
		print('can not open file')
		
#查询当前文件夹
def showCurrentDir():
	currentDir=os.getcwd()
	print(currentDir)
	return currentDir
	
#创建文件目录	
def createDir(currentDir):	
	dirName=os.path.join(currentDir,'student')
	print(dirName)
	if os.path.exists(dirName):
		print('existed')
	else:
		os.makedirs(dirName)
		print(os.listdir(currentDir))
		print('file size'+str(os.path.getsize(dirName)))
	return dirName
		
#path 的baseanme
def listChild(dirName):
	print('baseName:\t'+str(os.path.basename(dirName)))
	print('dirName:\t'+str(os.path.dirname(dirName)))

#path 的 split
def splitPath(dirName):
	head,tail=os.path.split(dirName)
	print('head:\t'+str(head)+'\t tail:\t'+str(tail))

#读取文件的内容
def readFile(fileName):
	try:
		if os.path.exists(fileName) and os.path.isfile(fileName):
			file=open(fileName)
			str=file.read()
			print(str)
			file.close()
		else:
			print('file not exists')
	except OSError:
		print('file not exists')

# 结构化数据持久（文件）保存
def saveStructureData():
	try:
		strucFile=shelve.open('student.data')
		strucFile['student']=['xu','li','zhang','song']
		strucFile['room']=['room_1','room_2','room_3','room_4']
		strucFile.close()
	except OSError:
		print("saveStructureData error")

def listStructureData():
	try:
		structFile=shelve.open('student.data')
		arr=list(structFile.keys())
		for k in arr:
			for v in structFile[k]:
				print('key:\t'+k+'\t values \t'+v)
		structFile.close()
	except OSError:
		print("listStructureDataa error")
#path abs path replace rel path
#print(dirName+'\t path replace \t'+os.path.relpath(dirName,'D:\\'))		
		
#shutil 主要用于file 的copy rename delete remove 
def copyFiles(res,destination):
	if not os.path.isfile(res):
		return
	if not os.path.isdir(destination):
		return
	shutil.copy(res,destination)
	print('copy sucess')
	
def copyTreeFiles(res,destination):
	if not os.path.isdir(res):
		return
	print('copy sucess \t'+shutil.copytree(res,destination))
	
	
def deletFile(path):
	if(os.path.isdir(path)):
		shutil.rmtree(path)
		
		
currentDir=showCurrentDir()
dirName=createDir(currentDir)
listChild(dirName)
#student=writeFile(dirName)
#readFile(os.path.join(dirName,'student.txt'))
#saveStructureData()	
#listStructureData()	
#copyFiles('D:\\py_code\\student\\student.txt',currentDir)
tempdir=os.path.join(currentDir,'student\\temp')
print(tempdir)
#copyTreeFiles('C:\\Users\\xujianhua\\Pictures','D:\\pic')
#deletFile('D:\\test')

	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
#









