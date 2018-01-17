#coding:utf-8

#1、调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个
#参数。如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是
#错误的参数类型。
help(abs)
abs(100)
abs(-20)
abs(12.34)
#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数。str()函数把其他类型转换成str。
int('123')
int(12.34)
str(123)
str(1.23)
#sum()函数接受一个list作为参数，并返回list所有元素之和。请计算1*1 + 2*2 + 3*3 + ... + 100*100
L=[]
x=1
while 1:
	if x==101:
		break
	else:
		L.append(x*x)
		x=x+1
print sum(L)


#2、在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写
#函数体，函数的返回值用 return 语句返回。函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将
#结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。如果没有return语句，函数执行完毕后也会返回
#结果，只是结果为 None。return None可以简写为return。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print my_abs(-1)


#3、math包提供了sin()和 cos()函数，我们先用import引用它：import math
#函数可以返回多个值,但其实这只是一种假象，Python函数返回的仍然是单一值。实际上，其返回值是一个tuple！在语法上，
#返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实
#就是返回一个tuple，但写起来更方便。
import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y
r = move(100, 100, 60, math.pi / 6)
print r


#4、使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数
#调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
#汉诺塔的移动
def move(n,a,b,c):
	if n==1:
		print a,'-->',c
		return
	move(n-1,a,c,b)
	print a,'-->',c
	move(n-1,b,a,c)
move(3,'A','B','C')


#5、Python自带的 int() 函数，其实就有两个参数，我们既可以传一个参数，又可以传两个参数：
#int()函数的第二个参数是转换进制，如果不传，默认是十进制 (base=10)，如果传了，就用传入的参数。
#可见，函数的默认参数的作用是简化调用，你只需要把必须的参数传进去。但是在需要的时候，又可以传入额外的参数来覆盖默认参数值。
#由于函数的参数按从左到右的顺序匹配(即：第一个实参将关联到函数定义中的第一个形参，第二个实参将关联到函数定义中的第二个形参，以此类推。)
#所以默认参数只能定义在必需参数的后面。
def greet(x='world'):
	print 'hello,',x,'.'
greet()
greet('EchoDemo')


#6、如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数。可变参数的名字前面有个 * 号，我们可以传入
#0个、1个或多个参数给可变参数。Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，
#直接把变量 args 看成一个 tuple 就好了。
def average(*args):
	if len(args)==0:
		return 0.0
	else:
		return sum(args)*1.0/len(args)
print average()
print average(1,2)
print average(1,2,2,3,4)
#如果要让函数接受不同类型的实参，必须把在函数中接受任意数量实参的形参放在最后。

#7、传递列表：
def greet_users(names):
	for name in names:
		message='Hello,'+name.title()+"!"
		print(message)

usernames=['hannah','ty','margot']
greet_users(usernames)


#8、在函数中修改列表：
def print_model(unprinted_designs,completed_models):
	while unprinted_designs:
		current_design=unprinted_designs.pop()
		print("Printing model:"+current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nFollowing models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs=['iphone case','robor pendant','dodecahefron']
completed_models=[]

print_model(unprinted_designs,completed_models)
show_completed_models(completed_models)


#9、通过传递列表的副本(切片法)而不是原件来达到不修改列表：
#function_name(list_name[:])


#10、当预先不知道传递给函数的会是什么样的信息，可将函数编写成能够接受任意数量的键值对。
def build_profile(first,last,**user_info):
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile

user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
