
print("**********     Hi! This is my Resume     ********** ")
print()

while True:
    proceed = input("Type OK to See my Information : ")
    if proceed == "OK" or proceed == "ok": pass
    else:
        print("Please Try Again : ")
        break
    print()


#PARENT CLASS
    class Person:
        def __init__(self,firstName,midName,lastName,course):
            self.firstName = firstName
            self.midName = midName
            self.lastName = lastName
            self.course = course

        def introduceOne(self):
            print("Hi! My Name is " + self.firstName + " " + self.midName + " " + self.lastName)
            print("I'am " + self.course)


#CHILD CLASS
    class Info(Person):
        def __init__(self, firstName,midName,lastName,course,email,address,phone):
            super().__init__(firstName, midName, lastName,course)
            self.email = email
            self.address = address
            self.phone = phone

        def introduceOne(self):
            super().introduceOne()
            print("You can Email me to : " + self.email)
            print("My Address : " + self.address)
            print("My Phone Number : " + self.phone)
                #print("Hi! My Name is  " + self.firstName + " " + self.midName + " " + self.lastName + " " + "" + "I 'am " + self.course)


    class Contact(Person):

        pOne = Person("Efren","G.","Marquez Jr.","BSIT Graduate")
        iOne = Info("Efren","G.","Marquez Jr.","BSIT Graduate","titanicsilver101@gmail.com","596-B C Bayani St. Brgy.11 Amadeo, Cavite","0910 193 5206")

        #pOne.introduceOne()
        iOne.introduceOne()


    print()
    me = input("Type OK to View About Me : ")
    if me == "OK" or me == "ok": pass
    else:
        print("Please Try Again : ")
        break

    print()
    print("ABOUT ME : ")
    print()


    print("   - To serve in the organization by sharing my information that I learned at school ")
    print("     in order to gain more knowledge and improve my skills in the real world of job.")
    

    print()
    exp = input("Type OK to View my Work Experienced : ")
    if exp == "OK" or exp == "ok": pass
    else:
        print("Please Try Again : ")
        break


    print()
    print("EXPERIENCE : ")
    print()

    exp = [
        ["OJT Technical Support in ICT Department",["Olivarez College Tagaytay","August - February","2016-2017"]],
        ["Data Encoder in DIY",["Wilcon Depot Silang","March to August 2023"]],
        ["Sales Associate",["Fora Tagaytay","January to October"]]
        ]

    for x in exp:
        print(x[0])
        for i in x[1]:
            print(" -" + " " +  i )
        print()



    print()
    skl = input("Type OK to View my Skills : ")
    if skl == "OK" or skl == "ok": pass
    else:
        print("Please Try Again : ")
        break


    print()
    print("SKILLS :")
    print()

    print("Knowledgable in : ")
    print("   - MS Word,","MS Excel,","MS Power Point")
    print("   - Adobe Photoshop,","Canva")
    print("   - Basic Hardware Trouble Shooting")
    print("   - Python Programming Language")



    print()
    edu = input("Type OK to View my Educational Background : ")
    if edu == "OK" or edu == "ok": pass
    else:
        print("Please Try Again : ")
        break


    print()
    print("EDUCATION :")
    print()

    edu = [
        ["City College of Tagaytay",["Bachelor of Science in Information Technology","Akle St.,Kaybagal South,Tagaytay City","2018-2022"]],
        ["Working Hands Discipleship And Vocational School",["Computer Technology","Second Mile Campus, Balubad II, Silang,Cavite","2015-2016"]],
        ]
    
    for x in edu:
        print(x[0])
        for i in x[1]:
            print(" -" + " " +  i )
        print()


    print()
    last = input("Type OK to View the Last Part : ")
    if last == "OK" or last == "ok": pass
    else:
        print("Please Try Again : ")
        break


    print()
    print("     __________Thank You For Viewing  Of  My Resume In All About Me, That's All For Me Thank You !!!__________     ")
    print()


    break