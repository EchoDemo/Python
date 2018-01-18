#coding:utf-8

#1、函数input的工作原理：input()和raw_input()这两个函数均能接收字符串，但raw_input()
#直接读取控制台的输入（任何类型的输入它都可以接收）。而对于input()，它希望能够读取一个合法的
#python表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
#除非对input()有特别需要，否则一般情况下我们都是推荐使用raw_input()来与用户交互。
#python3里input()默认接收到的是str类型。
message=input("input: ")
print(message)
information=raw_input("raw_input: ")
print(information)


#2、创建多行字符串：
prompt="If you tell us who you are,we can personalize the messages you see."
prompt+="\nWhat is your name?\n"

name=raw_input(prompt)
print("\nHello,"+name+"!")


#3、使用int来获取数值输入：
age=raw_input("How old are you?\n")
age=int(age)
print(age>=18);
