#coding:utf-8

#1、除数为零异常：
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero.")


#2、使用异常避免崩溃
print("Give me two numbers,and I will divide them.")
print("Enter 'q' to quit.")

while True:
	first_number=raw_input("\nFirst number:")
	if first_number=='q':
		break
	second_number=raw_input("Second number:")
	try:
		answer=int(first_number)/int(second_number)
	except ZeroDivisionError as e:
		print("You can't divide by 0!!!")
	else:
		print(answer)


#3、处理FileNotFoundError异常：
filename='alice'
try:
	with open(filename) as file_object:
		contents=file_object.read()
except FileNotFoundError:
	msg="Sorry,the file "+filename+" does not exist."
	print(msg)
else:
	words=contents.split()
	num_words=len(words)
	print("The file "+filename+" has about "+str(num_words)+" words.")
