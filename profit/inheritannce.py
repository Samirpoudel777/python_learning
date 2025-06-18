#    write a python prgram to create student and teacher class in the student class there is the property of name address faculty and teacher class with property of name and address is inheritance from student class and other property are subject      
# write a program to enter  a 15 employee salary and find out the highest salary from them
# write a program tof enter a fifteen number and arrange in ascending order
class student:
    def __init__(self,name,address,faculty):
        self.name=name;
        self.address=address;
        self.faculty=faculty;
        
    def student_details(self):
        print(f"studentname:{self.name} studentaddress:{self.address} studentfaculty:{self.faculty}")
class teacher(student):
    def __init__(self,name,address,faculty,subject):
        super().__init__(name,address,faculty)
        self.subject=subject;
        
    def teacher_details(self):
            print(f"studentname:{self.name} studentaddress;{self.address} teachersubjec:{self.subject}")

student1=student("samir poudel","bhimnagar","english")
student1.student_details()  
teacher1 = teacher("nabin poudel", "bishalchowk", "Science", "Math")
teacher1.teacher_details()
            
        
     
    
   