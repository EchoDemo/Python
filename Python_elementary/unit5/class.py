#coding:utf-8

#1、创建dog类：
class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name,age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
		self.master_numbers=0 #为属性指定默认值

	def sit(self):
		print(self.name.title()+" is now sitting.")

	def roll_over(self):
		print(self.name.title()+" rolled over.")
		
	def update_master_numbers(self,master_numbers):
		if master_numbers>self.master_numbers:
		    self.master_numbers=master_numbers;
		else:
			print("You can't change the master_numbers!")


#2、根据类创建实例：
my_dog=Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()


#3、修改属性的值:直接修改，通过方法修改，
print(my_dog.master_numbers)
my_dog.master_numbers=2
print(my_dog.master_numbers)

my_dog.update_master_numbers(3)
print(my_dog.master_numbers)

