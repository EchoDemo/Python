#coding:utf-8

#1、创建父类：
class Car(object):
	"""docstring for Car"""
	def __init__(self, make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading=0
#		self.gas_tank=True
	
	def get_descriptive_name(self):
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")

	def update_odometer(self,mileage):
		if mileage>self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer.")

	def increment_odometer(self,miles):
		self.odometer_reading+=miles;

	def full_gas_tank(self):
		print("Whether or not this Car's gas tank is full:"+self.gas_tank)


#2、创建一个battery类用作ElectricCar类的一个属性
class Battery():
	"""docstring for Battery"""
	def __init__(self, battery_volume=70):
		self.battery_volume = battery_volume

	def describe_battery(self):
		print("This car has a "+str(self.battery_volume)+"-kwh battery")
		

#2、创建子类：
class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make,model,year):
		super(ElectricCar, self).__init__(make,model,year)
#		self.battery_volume=70 #子类的独特属性；

#子类独特方法
#	def describe_battery(self):
#		print("This car has a "+str(self.battery_volume)+"-kwh battery.")

#子类重写父类的方法
	def full_gas_tank(self):
		print("This car doesn't need a gas tank!")


my_tesla=ElectricCar('tesla','models',2016)
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.full_gas_tank()
