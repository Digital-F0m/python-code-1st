#CHALLENGE FOR OBJECT_FUNCTIONS  ADDITIONAL !!!

class User:
    def __init__(self,firstName,lastName,likesCount,friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName
        print("User Created Name : " + self.firstName)

    def Introduce(self):
        print("Hi I am " + self.firstName + " " + self.lastName)

    def fullProfile(self):
        print("Full Name : " + self.firstName + " " + self.lastName)  
        print("Likes : " + str(self.likesCount))
        print("Friends : ")
        for friends in self.friendsName:
            print(" " + " - " + friends )     

#userOne = User("Efren","Marquez",30,["Jonathan Toledo","Joel Barrientos","Justine Hernadez","Jas Bautista"])
userTwo = User("Pauline","Deleon",69,["Janice Marzan","Ericka Panganiban","Elmira Lunar","Elaine Luna"])
#userTwo.Introduce()
userTwo.fullProfile()




# CHALLENGE FOR OBJECT_FUNCTIONS !!!

# class User:
#     def __init__(self,firstName,lastName,likesCount,friendsName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendsName = friendsName
#         print("User Created Name : " + self.firstName)

#     def Introduce(self):
#         print("Hi I am " + self.firstName + " " + self.lastName)

#     def fullProfile(self):
#         print("Full Name : " + self.firstName + " " + self.lastName)  
#         print("Likes : " + str(self.likesCount))
#         print("Friends : ")
#         for friends in self.friendsName:
#             print(" " + " - " + friends)     

# userOne = User("Efren","Marquez",30,["Jonathan Toledo","Joel Barrientos","Justine Hernandez","Jas Bautista"])
# #userOne.Introduce()
# userOne.fullProfile()




# STEPS IN CHALLENGE :

# class User:
#     def __init__(self,firstName,lastName,likesCount,friendsName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendsName = friendsName
#         print("User Created Name : " + self.firstName)

#     def Introduce(self):
#          print("Hi I am " + self.firstName + " " + self.lastName)

#     def fullProfile(self):
#         print("Full Name : " + self.firstName + " " + self.lastName)  
#         print("Likes : " + str(self.likesCount))
#         for friend in self.friendsName:
#             print(friend)

# userOne = User("Efren","Marquez",30,["Jonathan Toledo","Joel Barrientos","Justine Hernandez","Jas Bautista"])
# userOne.fullProfile()




# class User:
#     def __init__(self,firstName,lastName,likesCount,friendsName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendsName = friendsName
#         print("User Created Name : " + self.firstName)

#     def Introduce(self):
#          print("Hi I am " + self.firstName + " " + self.lastName)

#     def fullProfile(self):
#         print("Full Name : " + self.firstName + " " + self.lastName)  
#         print("Likes : " + str(self.likesCount))

# userOne = User("Efren","Marquez",30,["Jonathan Toledo","Joel Barrientos","Justine Hernandez","Jas Bautista"])
# userOne.fullProfile()




# class User:
#     def __init__(self,firstName,lastName,likesCount,friendsName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendsName = friendsName
#         print("User Created Name : " + self.firstName)

#     def Introduce(self):
#         print("Hi I am " + self.firstName + " " + self.lastName)

# userOne = User("Efren","Marquez",30,["Jonathan Toledo","Joel Barrientos","Justine Hernandez","Jas Bautista"])
# userOne.Introduce()




# class User:
#     def __init__(self,firstName,lastName,likesCount,friendsName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.likesCount = likesCount
#         self.friendsName = friendsName
#         print("User Created Name : " + self.firstName)

# userOne = User("Efren","Marquez",30,["Jonathan Toledo","Joel Barrientos","Justine Hernandez","Jas Bautista"])




# class Animal:
#     def __init__(self,type,voice):
#         self.type = type
#         self.voice = voice
#     def speak(self):
#         print(self.voice)    

#     def introduceSelf(self):
#         print("I am a " + self.type)

# # aOne = Animal("Dog","Arf")
# # aOne.introduceSelf()
# # aOne.speak()
# atwo = Animal("Cat","Meow")
# atwo.introduceSelf()
# atwo.speak()




# class Animal:
#     def __init__(self,type,voice):
#         self.type = type
#         self.voice = voice
#     def speak(self):
#         print(self.voice)    

#     def introduceSelf(self):
#         print("I am a " + self.type)

# aOne = Animal("Dog","Arf")
# aOne.introduceSelf()




# class Animal:
#     def __init__(self,type,voice):
#         self.type = type
#         self.voice = voice

#     def speak(self):
#         print(self.voice)    

# aOne = Animal("Dog","Arf")
# aOne.speak()
    



# class Animal:
#     def __init__(self,type,voice):
#         self.type = type
#         self.voice = voice

# aOne = Animal("Dog","Arf")
# print(aOne.voice)
        

