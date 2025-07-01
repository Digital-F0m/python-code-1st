
print(" ------- WELCOME ------- ")
print("      JBros Members")
print()



while True:

    proceed = input("Type OK to CONTINUE or Type Any KEY to PASSED : ") 
    if proceed == "ok" or proceed == "OK": pass
    else:
        print("Please Try Again : ")
        break
    
            
    while True:

        userName = ["JBROS"]
        password = ["sorbj"]

        currUsername = input("Enter Username : ")
        currPassword = input("Enter Password : ")


        for x in range(len(userName)):
            if currUsername == userName[x] and currPassword == password[x]:
                print("Welcome, " + userName[x])
                break
        else:
            print("Unsuccessful! ")           
            break


        print()
        class Members:
            def __init__(self,programmer,friendsName):
                self.programmer = programmer
                self.friendsName = friendsName
                print(" ----- JBROS MEMBERS ----- ")
                print("Programmer : " + self.programmer)
                for friends in self.friendsName:
                    print("  - " + friends)

        mOne = Members("Efren Marquez II",["Jonathan Toledo","Joel Barrientos","Justine Hernandez","Jas Bautista","Jericho Senar","Raymart Panganiban"])
        break
    break





# for x in range(len(userName)):
#             if currUsername == userName[x] and currPassword == password[x]:
#                 print("Welcome, " + userName[x])
#                 break
#             else:
#                 print("Unsuccessful ! ")           
#         break
            









    # while True:
    #     print()
    #     continued = input("You want to Continue : ? [Type YES to Continue / Any Key to PASS] ")

    #     if continued == "YES" or continued == "yes": pass
    #     else:
    #         print("Please Try Again : ")
    #         break 










# m = Members(currUsername,currPassword)
#     ListofMembers.append(m)



# print(ListofMembers)






# class Members:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def introduce(self):
#         print("First Name : " + self.firstName)
#         print("Last Name : " + self.lastName)







# def printStudent(**student):
#     print(student["name"])
#     print(student["course"])
#     print(student["age"])
#     print(student["average"])
#     print(student["coursecode"])

# printStudent(name="Efren", age=18, course="BSIT", average=90, coursecode=101)



# def sayHello(*names):
#      print(names)
#      print("Hello, " + str(names))

# sayHello("Efren","Janice","Ericka","Rhufa","Pauline","Elaine","Jessica")






# age = int(input("Enter your Age : "))

# # if age >= 18:
# #     print("Too Young")

# if not age >= 18:
#     print("Too Young")
# else:
#     print("Legal Age")