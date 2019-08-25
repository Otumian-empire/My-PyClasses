# importing fies
from Employee import Employee as App

print("hello")

me = App("John Doe", "Python Devrloper", 1200)
print(f"My name is {me.name} and i am a {me.job}.\nMy salary is {me.salary}.\nWhen i work overtime, My salary for the month is {me.return_gross_pay(7)}")

