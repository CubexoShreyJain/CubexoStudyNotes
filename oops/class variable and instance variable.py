class Employee():
    salary =  10000               # Class variable, every instance will SHARE this variable

rohan = Employee()
rohan.name  = "Rohan"             # Instance variables 
rohan.skill = "sql"

print(rohan.name,rohan.salary)    #Rohan 10000

shrey = Employee()

print(shrey.salary)               # 10000

shrey.salary = 1000000000         # Now instances created a new variable salary

print(shrey.salary, Employee.salary , rohan.salary) #1000000000 10000 10000

Employee.salary  = 100000          #Changes variable of class

print(shrey.salary, Employee.salary , rohan.salary) #1000000000 100000 100000

print(shrey.__dict__,"\n",rohan.__dict__,"\n",Employee.__dict__)


