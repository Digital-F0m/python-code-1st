#CHALLENGE FOR ARGUMENTS 1.0 !!!

def summationOf(*numbers):
    sum = 0
    for number in numbers:
        # sum = sum + number
        sum += number
    return sum

#print(summationOf(1,2,3))
print(summationOf(1,2,3,434,535,34343,545,32,321))




# def summationOf(*numbers):
#     sum = 0
#     for number in numbers:
#         # sum = sum + number
#         sum += number
#     return sum

# #print(summationOf(1,2,3,4,5,6,7,8,9,10))
# print("SummationOf(1,2,3,4,5,6,7,8,9,10) ")
# print(summationOf(1,2,3,4,5,6,7,8,9,10))




# def printStudent(**student):
#     print(student["name"])
#     print(student["course"])
#     print(student["age"])
#     print(student["average"])
#     print(student["coursecode"])

# printStudent(name="Efren", age=18, course="BSIT", average=90, coursecode=101)




# def printStudent(name, course, age):
#     print(name)
#     print(course)
#     print(age)

# printStudent("Efren", "BSIT", 18)




# def printFamily(*firstNames, lastName):
#     for name in firstNames:
#         print(name + " " + lastName)

# printFamily("Jonathan", "Raymart", "Joel", "Justine", "Jonjon", "Jericho", lastName="jBros")




# def sayHello(firstName,lastName):
#     print(firstName + " " + lastName)


# sayHello(lastName="Marquez",firstName="Efren")




# def sayHello(firstName,lastName):
#     print(firstName + " "  + lastName)

# sayHello("Efren","Marquez")




# def sayHello(*names):
#     for name in names:
#         #print(name)
#         print("Hello, " + name)

# sayHello("Efren","Janice","Ericka","Rhufa","Pauline","Elaine","Jessica")




# def sayHello(*names):
#     print(names)

# sayHello("Efren","Janice","Ericka","Rhufa","Pauline","Elaine","Jessica")




# def sayHello(name, nameOne, nameTwo, nameThree):
#     print("Hello, " + name)
#     print("Hello, " + nameOne)
#     print("Hello, " + nameTwo)
#     print("Hello, " + nameThree)

# sayHello("Efren","Janice","Ericka","Rhufa")




# def sayHello(name):
#     print("Hello, " + name)

# sayHello(input("Enter Name : "))
