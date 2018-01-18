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


class Battery(object):
	"""docstring for Battery"""
	def __init__(self, battery_volume=70):
		self.battery_volume = battery_volume

	def describe_battery(self):
		print("This car has a "+str(self.battery_volume)+"-kwh battery.")

	def get_range(self):
		if self.battery_volume==70:
			range=240
		elif self.battery_volume==85:
			range=270

		message="This car can go approximately "+str(range)
		message+=" miles on a full charge."
		print(message)


class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make,model,year):
		super(ElectricCar, self).__init__(make,model,year)		
