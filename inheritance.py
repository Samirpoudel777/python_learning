# class Person:
#     def __init__(self,name,age,address):
#         self.name=name;
#         self.age=age;
#         self.address=address;
#     def person_details(self):
#         print(f"Employee Name:{self.name} Employee age:{self.age} Emp address: {self.address}")

# class Employee(Person):
#     def __init__(self, name, age, address,emp_post, emp_salary):
#         super().__init__(name, age, address)
#         self.emp_post=emp_post
#         self.emp_salary=emp_salary
#     def emp_detail(self):
#      print(f"Employee Name:{self.name} Employee age:{self.age} Emp address: {self.address} Emp post: {self.emp_post} Emp Salary: {self.emp_salary}")

    


# emp2 = Employee("Nabin",22,"Bharatpur-20,chitwan","Web Developer",50000); 
# emp3 = Employee("Nabin",22,"Bharatpur-20,chitwan","Web Developer",50000); 

# emp4 = Employee("Nabin",22,"Bharatpur-20,chitwan","Web Developer",50000); 
# emp5 = Employee("Nabin",22,"Bharatpur-20,chitwan","Web Developer",50000); 
# emp6 = Employee("Nabin",22,"Bharatpur-20,chitwan","Web Developer",50000); 
# emp7 = Employee("Nabin",22,"Bharatpur-20,chitwan","Web Developer",50000); 
# emp8 = Employee("Nabin",22,"Bharatpur-20,chitwan","Web Developer",50000); 

# print(emp2.emp_detail()) 
# print(emp3.emp_detail())       
      
# print(emp4.emp_detail())       
# print(emp5.emp_detail())       
# print(emp6.emp_detail())       
# print(emp7.emp_detail())       
# print(emp8.emp_detail())       


# 
# class Person:
#     def __init__(self, person_name, person_age, person_salary, person_job):
#         self.person_name = person_name
#         self.person_age = person_age
#         self.person_salary = person_salary
#         self.person_job = person_job

#     def person_details(self):
#         print(self.person_name, self.person_age, self.person_salary, self.person_job)

# x = Person("Samir", 17, 5000000, "Software Engineer")
# x.person_details()

# class Employee(Person):
#     def __init__(self, person_name, person_age, person_salary, person_job, person_address):
#         super().__init__(person_name, person_age, person_salary, person_job)
#         self.person_address = person_address  # Corrected assignment

#     def employee_details(self):
#         print(self.person_name, self.person_age, self.person_salary, self.person_job, self.person_address)  # Fixed typo in 'self'

# y = Employee("samir", 25, 8000000, "hacrr", "chitwan")
# y.employee_details()
#animal name wild,types: subclass :dog ,property:sound=second class
class animal:
    def __init__(self,ainmal_name,)