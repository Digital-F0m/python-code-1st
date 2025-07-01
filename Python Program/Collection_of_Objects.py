#CHALLENGE FOR COLLECTION OF OBJECTS !!!

class Student:
    def __init__(self,name,course,year,section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print("     Name    : " + self.name)
        print("     Course  : " + self.course)
        print("     Year    : " + self.year)
        print("     Section : " + self.section)
        

listOfStudents = []

while True:
    print()
    name = input("Name : ")
    course = input("Course : ")
    year = input("Year : ")
    section = input("Section : ")
    s = Student(name,course,year,section)
    listOfStudents.append(s)

    print()
    choice = input("Create Another Student? [Yes/Any Char] : ")
    if choice == "Yes" or choice == "yes": pass
    else: break

i = 1
for student in listOfStudents:
    print()
    print("Student # " + str(i))
    student.introduce()
    i = i + 1






#STEPS IN CHALLENGE :

# class Student:
#     def __init__(self,name,course,year,section):
#         self.name = name
#         self.course = course
#         self.year = year
#         self.section = section

#     def introduce(self):
#         print("     Name    : " + self.name)
#         print("     Course  : " + self.course)
#         print("     Year    : " + self.year)
#         print("     Section : " + self.section)        


# listOfStudents = []

# while True:
#     print()
#     name = input("Name : ")
#     course = input("Course : ")
#     year = input("Year : ")
#     section = input("Section : ")
#     s = Student(name,course,year,section)
#     listOfStudents.append(s)

#     print()
#     choice = input("Create Another Student? [Yes/Any Char] : ")
#     if choice == 'Y' or choice == 'y': pass
#     else: break

# for student in listOfStudents:
#     student.introduce()




# class Student:
#     def __init__(self,name,course,year,section):
#         self.name = name
#         self.course = course
#         self.year = year
#         self.section = section

#     def introduce(self):
#         print("     Name    : " + self.name)
#         print("     Course  : " + self.course)
#         print("     Year    : " + self.year)
#         print("     Section : " + self.section)        


# listOfStudents = []

# while True:
#     print()
#     name = input("Name : ")
#     course = input("Course : ")
#     year = input("Year : ")
#     section = input("Section : ")
#     s = Student(name,course,year,section)
#     listOfStudents.append(s)

#     print()
#     choice = input("Create Another Student? [Yes/Any Char] : ")
#     if choice == 'Y' or choice == 'y': pass
#     else: break

# print(listOfStudents)




# class Student:
#     def __init__(self,name,course,year,section):
#         self.name = name
#         self.course = course
#         self.year = year
#         self.section = section

#     def introduce(self):
#         print("     Name    : " + self.name)
#         print("     Course  : " + self.course)
#         print("     Year    : " + self.year)
#         print("     Section : " + self.section)
        
# while True:
#     print("\n")
#     name = input("Name : ")
#     course = input("Course : ")
#     year = input("Year : ")
#     section = input("Section : ")
#     print("\n")
#     choice = input("Create Another Student? [Yes/Any Char] : ")
#     if choice == 'Y' or choice == 'y': pass
#     else: break




# class Student:
#     def __init__(self,name,course,year,section):
#         self.name = name
#         self.course = course
#         self.year = year
#         self.section = section

#     def introduce(self):
#         print("     Name    : " + self.name)
#         print("     Course  : " + self.course)
#         print("     Year    : " + self.year)
#         print("     Section : " + self.section)
        
# while True:
#     name = input("Name : ")
#     course = input("Course : ")
#     year = input("Year : ")
#     section = input("Section : ")




# class Student:
#     def __init__(self,name,course,year,section):
#         self.name = name
#         self.course = course
#         self.year = year
#         self.section = section

#     def introduce(self):
#         print("     Name    : " + self.name)
#         print("     Course  : " + self.course)
#         print("     Year    : " + self.year)
#         print("     Section : " + self.section)
        
# while True:
#     print("Hello")      #Never Ending without Break Keyword.....
#     break
          



# class Person:
#     def __init__(self,name):
#         self.name = name
        
#     def introduce(self):
#         print("I am " + self.name)

# listOfPeople = []

# for i in range(5):
#     name = input("Enter a Name : ")
#     p = Person(name)
#     listOfPeople.append(p)

# for person in listOfPeople:
#     person.introduce()




# class Person:
#     def __init__(self,name):
#         self.name = name
        
#     def introduce(self):
#         print("I am " + self.name)

# listOfPeople = []

# for i in range(3):
#     name = input("Enter a Name : ")
#     p = Person(name)
#     listOfPeople.append(p)

# print(listOfPeople)




# class Person:
#     def __init__(self,name):
#         self.name = name
        
#     def introduce(self):
#         print("I am " + self.name)
        
# pOne = Person("Efren")
# pTwo = Person("Pauline")
# pThree = Person("Janice")
# pFour = Person("Elaine")

# listOfPeople = [pOne,pTwo,pThree,pFour]

# for person in listOfPeople:
#     print(person.name)




# class Person:
#     def __init__(self,name):
#         self.name = name
        
#     def introduce(self):
#         print("I am " + self.name)
        
# pOne = Person("Efren")
# pTwo = Person("Pauline")
# pThree = Person("Janice")

# listOfPeople = [pOne,pTwo,pThree]

# listOfPeople[3].introduce()




# class Person:
#     def __init__(self,name):
#         self.name = name
        
        
# pOne = Person("Efren")
# pTwo = Person("Pauline")
# pThree = Person("Janice")

# listOfPeople = [pOne,pTwo,pThree]

# print(listOfPeople[1].name)




# class Person:
#     def __init__(self,name):
#         self.name = name
#         print(self.name + " Created")
        
# pOne = Person("Efren")
# pTwo = Person("Pauline")
# pThree = Person("Janice")

# listOfPeople = [pOne,pTwo,pThree]




# class Person:
#     def __init__(self,name):
#         self.name = name
#         print(self.name + " Created")
        
# name =  input("Enter a Name : ")
# pOne = Person(name)



