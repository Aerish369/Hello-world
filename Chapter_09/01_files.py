# #Use open function to read the content of the file.
# f = open('D:\Python\Chapter_09', 'r')
f = open('sample.txt') #by default mode is read. 
# data = f.read()
data = f.read(5) #Read first 5 chars of sample.txt 
print(data)
f.close()
