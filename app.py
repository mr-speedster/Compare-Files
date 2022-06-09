import filecmp as fc #filecmp module for comparison operation
f1 = '/storage/emulated/0/Download/Text1.txt' #main file path
f2 = '/storage/emulated/0/Download/Text2.txt' #path of file for compare
result = fc.cmp(f1,f2) #its a simple method for compare files in python
print(result) 