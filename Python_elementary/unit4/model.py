#1、首先创建一个模块，其扩展名是.py的文件，包含要导入到程序中的代码。下面的模块中只包含一个函数。

#model.py

def make_pizza(size,*toppings):
	print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
	for topping in toppings:
		print("-"+topping)
    

#2、导入创建的模块：module_name.function_name()就可以调用模块中的函数了。

#test.py

import model

model.make_pizza(16,'pepperoni')
model.make_pizza(12,'mushroom','green peppers','extra cheese')


#3、导入特定的函数：导入函数之后就可以直接调用函数了：function_name()

#from module_name import function_name #导入特定函数

#from module_name import function_1,function_2,function_3 #导入任意数量的函数。


#4、使用as给函数指定别名：

#from module_name import function_name as another_name


#5、使用as给模块指定别名：

#import module_name as another_name


#6、导入模块中的所有函数：

#from module_name import*
