#coding:utf-8

"""1、函数open()用于打开文件，接受一个要打开文件的名称的参数(这里是在同一个目录之下)，这里的open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象，存储于file_object当中，关键字with不需要访问文件后将其关闭。当文件不在同一个目录之下，使用相对路径open：with open('text_files\filename.txt') as file_object:或者使用绝对路径open：由于绝对路径比较长，所以先将绝对路径传递给一个变量，再把变量作为open的参数。"""

with open('pi_digits.txt') as file_object:
	contents=file_object.read() #使用read()读取这个文件的全部内容，并将其作为字符串存储在变量contens当中。
	print(contents.strip()) #打印contents的值，并且删除末尾的空行。


"""2、逐行读取："""
filename='pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.strip())



"""3、open返回的文件对象只在with代码块内可用,创建一个包含文件各行内容的列表"""
filename='pi_digits.txt'

with open(filename) as file_object:
	lines=file_object.readlines()

for line in lines:
	print(line.strip())

pi_string=''
for line in lines:
	pi_string+=line.strip()

print(pi_string)
print(len(pi_string))





