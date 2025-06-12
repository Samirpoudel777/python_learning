# class person:
#     def __init__(self,stdname,stdage,stdgrade):
#         self.stdname =stdname
#         self.stdage = stdage
#         self.stdgrade = stdgrade
# p1=person("nabin",17,"see")
# print(p1.stdname)
# print(p1.stdage)
# print(p1.stdgrade)
 
 
class person:
    def __init__(self,name, age,nationality):
        self.name=name
        self.age=age
        self.nationality=nationality
    def __str__(self):
        return f"{self.name}{self.age}{self.nationality}"
p1=person("ASMIT",17,"AFRICANE")
print(p1)

        