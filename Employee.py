# OOP in python is basically creation of classes and inheritance.

class Employee:

	# private properties
	__hours_for_over_time = 6
	__hours_in_a_day = 24
	__number_working_days_in_month = 30
	
	# constructor
	def __init__(this, name, job, salary):
		this.name = name
		this.job = job
		this.salary = salary
		
	# calculate the gross pay based on the time employee did
	def return_gross_pay(this, hours_worked):
		gross_pay = 0
		
		if hours_worked >= this.__hours_for_over_time:
			over_time = hours_worked - this.__hours_for_over_time
			over_time_rate = over_time * this.salary
			
			rate_per_day = over_time_rate / this.__hours_in_a_day
			
			gross_pay = this.salary + (rate_per_day *  this.__number_working_days_in_month)
		else:
			gross_pay = this.salary
			
		return gross_pay
		
