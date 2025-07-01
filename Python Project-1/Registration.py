
print("__________Registration Form__________")

print()


while True:
    proceed = input("Press OK to Continue for Fill-up : ")
    if proceed == "OK" or proceed == "ok": pass
    else: 
        print("Please try Again : ")
        break

    class Members():
        def __init__(self,firstName,lastName,age,gender,birthday,citizenship):
            self.firstName = firstName
            self.lastName = lastName
            self.age = age
            self.gender = gender
            self.birthday = birthday
            self.citizenship = citizenship
            
        def introduce(self):
            print("     First Name : " + self.firstName)
            print("     Last Name : " + self.lastName)
            print("     Age : " + str(self.age))
            print("     Gender : " + self.gender)
            print("     Birthday :  " + self.birthday)
            print("     Citizenship  : " + self.citizenship)


    listOfMembers = []


    print()
    firstName = input("First Name : ")
    lastName = input("LastName : ")
    age = int(input("Age : "))
    gender = input("Gender : ")
    birthday = input("Birthday : ")
    citizenship = input("Citizenship : ")

    m = Members(firstName,lastName,age,gender,birthday,citizenship)
    listOfMembers.append(m)

    print()
    choice = input("Press OK to Proceed : ")
    if choice == "OK" or choice == "ok":
        print("Successfully ! ")
    else:
        print("Unsuccessfull ! " )   
        break

    for member in listOfMembers:
        print()
        print("Member : ")
        member.introduce()
    break


    
    
    

        