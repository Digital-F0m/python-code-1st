
# PARENT CLASS
class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def Introduce(self):
        print("Hi I'm " + self.firstName + " " + self.lastName)    

    def introdoceLastName(self):
        print("Hi I'm " + self.lastName)
        
#CHILD CLASS
class Student(Person):
    def __init__(self,firstName,lastName,sectionYear):
        super().__init__(firstName,lastName)
        self.sectionYear = sectionYear

    def Introduce(self):
        #print("From " + self.sectionYear)
        super().Introduce()
        print("From " + self.sectionYear)
    
    def saySection(self):
        print(self.sectionYear)



class Employee(Person):
    def __init__(self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        self.salary = salary

    def Introduce(self):
        super().Introduce()
        print("My salary is " + str(self.salary))

    def saySalary(self):
        print("Salary is " + str(self.salary))

pOne = Person("Efren","Marquez")
sOne = Student("Pauline","de Leon","1-B")
eOne = Employee("Janice","Marzan",7000)

pOne.introdoceLastName()
sOne.introdoceLastName()
eOne.introdoceLastName()




# # PARENT CLASS
# class Person:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def Introduce(self):
#         print("Hi I'm " + self.firstName + " " + self.lastName)    
        
# #CHILD CLASS
# class Student(Person):
#     def __init__(self,firstName,lastName,sectionYear):
#         super().__init__(firstName,lastName)
#         self.sectionYear = sectionYear

#     def Introduce(self):
#         #print("From " + self.sectionYear)
#         super().Introduce()
#         print("From " + self.sectionYear)



# class Employee(Person):
#     def __init__(self, firstName, lastName, salary):
#         super().__init__(firstName, lastName)
#         self.salary = salary

#     def Introduce(self):
#         super().Introduce()
#         print("My Salary is " + str(self.salary))

# pOne = Person("Efren","Marquez")
# sOne = Student("Pauline","de Leon","1-B")
# eOne = Employee("Janice","Marzan",7000)

# pOne.Introduce()
# sOne.Introduce()
# eOne.Introduce()




# # PARENT CLASS
# class Person:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def Introduce(self):
#         print("Hi I'm " + self.firstName + " " + self.lastName)    
        
# #CHILD CLASS
# class Student(Person):
#     def __init__(self,firstName,lastName,sectionYear):
#         super().__init__(firstName,lastName)
#         self.sectionYear = sectionYear

#     def Introduce(self):
#         # print("From " + self.sectionYear)
#         super().Introduce()
#         print("From " + self.sectionYear)

# pOne = Person("Efren","Marquez")
# sOne = Student("Pauline","de Leon","1-B")
# pOne.Introduce()
# sOne.Introduce()




# #PARENT CLASS
# class Person:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def Introduce(self):
#         print("Hi I'm " + self.firstName + " " + self.lastName)    
        
# #CHILD CLASS
# class Student(Person):
#     def __init__(self,firstName,lastName,sectionYear):
#         super().__init__(firstName,lastName)
#         self.sectionYear = sectionYear

#     def Introduce(self):
#         print("Hi I'm " + self.firstName + " " + self.lastName + " " + "From" + " " + self.sectionYear)

# pOne = Person("Efren","Marquez")
# sOne = Student("Pauline","de Leon","1-B")
# pOne.Introduce()
# sOne.Introduce()




# #PARENT CLASS
# class Person:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def Introduce(self):
#         print("Hi I'm " + self.firstName + " " + self.lastName)    
        
# #CHILD CLASS
# class Student(Person):
#     def __init__(self,firstName,lastName,sectionYear):
#         super().__init__(firstName,lastName)
#         self.sectionYear = sectionYear


# pOne = Person("Efren","Marquez")
# sOne = Student("Pauline","de Leon","1-B")
# pOne.Introduce()
# sOne.Introduce()




# #PARENT CLASS
# class Person:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def Introduce(self):
#         print("Hi I'm " + self.firstName + " " + self.lastName)    
        
# #CHILD CLASS
# class Student(Person):
#     def __init__(self,firstName,lastName,sectionYear):
#         super().__init__(firstName,lastName)
#         self.sectionYear = sectionYear

# pOne = Person("Efren","Marquez")
# sOne = Student("Pauline","de Leon","1-B")




# # PARENT CLASS
# class Person:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def Introduce(self):
#         print("Hi I'm " + self.firstName + " " + self.lastName)    
        
# # CHILD CLASS
# class Student(Person):
#     pass
    
# pOne = Person("Efren","Marquez")
# pOne.Introduce()

# sOne = Student("Pauline","de Leon")
# sOne.Introduce()




