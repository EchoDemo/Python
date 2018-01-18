#coding:utf-8

#from car import Car,ElectricCar #导入多个类
#from car import* #导入模块中所有的类，不推荐使用这种方式；
import car #导入整个模块，此时需要有前缀car.来调用具体的类；

my_new_car=car.Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()

my_tesla=car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())