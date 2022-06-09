import filecmp as fc #filecmp module for comparison operation
file1 '/Text1.txt' #main file path
file2 = '/Text2.txt' #path of file for compare
result = fc.cmp(file1,file2) #its a simple method for compare files in python
if result == True:
	print("File is Same")
else:
	print("File is Different")
