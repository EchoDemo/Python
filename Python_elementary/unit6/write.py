#coding:utf-8


#1、写入空文件：第二个参数可指定读取模式('r')、写入模式('w')、附加模式('a')或让你能够读取和写入文件的模式('r+')。python将默认为只读模式打开。如果写入的文件不存在，将自动创建。如果存在时以写入模式打开，则清空该文件。
filename='programming.txt'
with open(filename,'w') as file_object:
	file_object.write("I love programming.\n") #写入多行文本需指定换行符。
	file_object.write("I love create new games.\n")


#2、如果需要给文件添加内容，而不是覆盖原有的内容，可以以附加模式打开文件。
filename='programming.txt'
with open(filename,'a') as file_object:
	file_object.write("I also love find something.")