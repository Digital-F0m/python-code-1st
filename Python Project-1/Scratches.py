
# import random
# import string


# def  crack_password(password):
#     attempts = 0
#     while True:
#         guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))
#         attempts += 1
#         if guess == password:
#             return attempts
        
# password = input("Enter the password to crack: ")

# print("Cracking password....")

# attempts = crack_password(password)

# print(f"The password was cracked in {attempts} attempts.")








# x = 5

# while x > 0:
#     print(x)
#     x-=1




# numbers = [1,2,3,4,5]

# for number in numbers:
#     print(number)




# def say_Hello(name):
#     print("Hello," + name + "!")

# say_Hello("Efren")
# say_Hello("Jasha")
    



# def Squared(x):
#     return x * x

# result = Squared(5)
# print(result)




# name = input("What is Your Name? ")
# print("Hello," + name + "!")




# name = "Efren"
# age = 18

# print("My name is " + name + " " + "AND my age is" +" " + str(age))




#BACK AGAIN !

# file = open("Scratch_Code_Text.txt","r")
# content = file.read()
# file.close()
# print(content)




#BACK AGAIN !

# file = open("Example.text","W")
# file.write("Hello World !")
# file.close()




# numbers = [1,2,3,4,5]

# numbers.append(6)
# numbers.remove(4)

# numbers[2] = 10

# print(numbers)




# person = {"Name":"John","Age":30}

# person ["Gender"] = "Male"
# person.pop("Age")
# person["Name"] = "Jane"

# print(person)





# numbers = {1,2,3,4,5}
# number2 = set([1,2,3,4,5])

# numbers.add(6)
# numbers.remove(4)

# print(numbers)




# number1 = {1,2,3,4,5}
# number2 = {4,5,6,7,8}

# print(number1.union(number2))




# name = "JOHN"
# greeting = "Hello," + name + "!"

# multiplied_greeting = greeting * 3

# print(multiplied_greeting)




#BACK AGAIN

# example_string = "HELLO, WORLD!"

# #print(example_string.find("WORLD"))

# new_string = example_string.replace("WORLD", "PYTHON")

# print(new_string)




#BACK AGAIN

# file = open("example.txt","r")
# content = file.read()
# file.close()


# with open("example.text","r") as file:
#     content =  file.read()




#BACK AGAIN

# file = open("example.text","w")
# file.write("Hello,World!")
# file.close()


# with open("example.text","w"):
#     content = file.write()




#BASIC !!!

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def Me(self):
#         print(self.name)

#     def Birthday(self):
#         #self.age = self.age + 1
#         self.age += 1
#         print("My Age is : " + str(self.age))

# p1 = Person("John",30)
# p2 = Person("Mary",25)


# print(p1.name)
# p1.Birthday()


# p1.Me()
# p1.Birthday()
# p2.Me()
# p2.Birthday()




#BACK AGAIN

# try:
#     result = x/y
# except ZeroDivisionError:
#     print("Cannot Divide By Zero")




#BACK AGAIN

# try:
#     result = x/y
# except ZeroDivisionError:
#     print("Cannot Divide By Zero")
# finally:
#     print("Execution Complete")




#BACK AGAIN

# if y == 0:
#     raise ValueError("Cannot Divide By Zero")




#BACK AGAIN

# import Re

# text = "ABCDEF"
# x = Re.search("ABD",text)




#BACK AGAIN

# import Re

# text = "The Cat is Black"
# new_text = Re.sub("Cat","Dog",text)




#BACK AGAIN

# import Threading 

# def my_function():

#     #Code to be executed in the new thread

# thread = Threading.thread(target=my_function)




# x = 6

# print(x)


# y = x * 7

# print(y)




#BACK AGAIN

# name = input('Enter file : ')
# handle = open(name, 'r')
# counts = dict()

# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word , count in list (counts.items()):
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)




#BACK AGAIN

# 5
# x = 5
# x + 1

# print(x)




#BACK AGAIN

# prompt = "What is the airspeed velocity of an unladen swallow?\n"
# speed =  input(prompt)
# int(speed)
# int(speed) + 5


# speed = input(prompt)




# name = input("Enter your name : ")
# print("Hello, " + name)



# hour = input("Enter Hours : ")
# rate = input("Enter Rate : ")

# pay = int(hour) * float(rate)

# print(pay)




# width = 17
# height = 12.0

# print("The qoutient is : " + str(width // 2))
# print("The qoutient is : " + str(width / 2.0))
# print("The qoutient is : " + str(height / 3))
# print(1 + 2 * 5)



#BACK AGAIN

# Exercise: Write the program  which prompts the user  for a
#Celsius temperature, convert the temperature to Fahrenheit,
#and print out the converted temperature



#BACK AGAIN

# x = 3  
# if x < 10:
#     print("Small")
# print("Done")     print("DOne")




# x = 0
# y = 4

# if x == y:
#     print("x and y are equal")
# else:
#     if x < y:
#         print("x is less than y ")
#     else:
#         print("x is greater than y")




# x = -1
# x = 11

# if 0 < x:
#     if x < 10:
#         print("x is a positive single-digit number.")





# x = -2

# if 0 < x and x < 10:
#     print("x is a positive single-digit number: ")




#BACK AGAIN

# prompt = "What is the air velocity of an unladen swallow?\n"
# speed = input(prompt)
# int(speed)




#BACK AGAIN

# inp = input("Enter Fahrentheit Temperature : ")
# fahr = float(inp)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)




# inp = input("Enter Fahrentheit  Temperature : ")
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 /  9.0
#     print(cel)
# except:
#     print("Please Enter a Number")




# x = 6
# y = 2
# x >= 2 and (x/y) > 2
    #True

# x = 1
# y = 0
# x >= 2 and (x/y) > 2
    #False

# x = 6
# y = 0
# x >= 2 and (x/y) < 2
    #ZeroDivisionError



# x = 1 
# y = 0
# x >= 2 and y != 0 and (x/y) > 2
#     #False

# x = 6 
# y = 0
# x >= 2 and y != 0 and (x/y) > 2
#     #False

# x >= 2 and (x/y) > 2 and y!= 0
#     #ZeroDivisionError




#EXERCISES

hour = int(input("Enter your Hours :"))
rate = int(input("Enter your Rate :"))
pay =  1.5

print("Your day is Rate in 40 Hours is :" + hour)


#TO BE CONTINUED IN PAGE 52.....






# print("CARINDERIA NI FOM !!!")

# ulam  = {
#     "  -  Menudo":40,
#     "  -  Sinigang":45,
#     "  -  Lumpia":20,
#     "  -  Eggplant":30,
#     "  -  Ampalaya":45,
#     "  -  Chicken Carrie":50,
#     "  -  Adobo":50,
#     "  -  Munggo":35
# }

# kanin = {
#     "Fried Rice":15,
#     "Regular Rice":10,
#     "Adobo Rice":20
# }

# inumin = {
#     "Coke":15,
#     "Royal":15,
#     "MountainDew":14,
#     "Sprite":13
# }


# order = []

# print()
# print("---------- MENU ---------- ")
# print()

# while True:
#     ulam = input("Type Your Menu : ")
#     order.append(ulam)



# for key, value in ulam.items():
#     print(f"{key}: {value: .2f}")

# print()
# print("---------- RiCE ---------- ")
# print()

# for key, value in kanin.items():
#     print(f"{key}: {value: .2f}")

# print()
# print("---------- DRINKS ---------- ")
# print()

# for key, value in inumin.items():
#     print(f"{key}: {value: .2f}")






















# class carinderia:
#     def __init__(self,menudo,sinigang,lumpia,torta,ampalaya,carrie,munggo,rice,coke,royal,mountaindew,sprite):
#         self.menudo = menudo
#         self.sinigang = sinigang
#         self.lumpia = lumpia
#         self.torta = torta
#         self.ampalaya = ampalaya
#         self.carrie = carrie
#         self.munggo = munggo
#         self.rice = rice
#         self.coke = coke
#         self.royal = royal
#         self.mountainDew = mountaindew
#         self.sprite = sprite

#     def introduceMenu(self):
#         print("MENU : ")
#         print("  -   Menudo = 40 " )
#         print("  -   Sinigang = 50 " )
#         print("  -   Lumpia = 10 " )
#         print("  -   Torta = 30 " )
#         print("  -   Ampalaya = 35 " )
#         print("  -   Carrie = 50 " )
#         print("  -   Munggo = 35 " )
#         print()
#         print("RICE :")
#         print("   -  1 Rice = 10 " )
#         print()
#         print("DRINKS :")
#         print("   -  Coke = 12 ")
#         print("   -  Royal  = 13 ")
#         print("   -  Mountain Dew = 13 ")
#         print("   -  Sprite = 14 ")

# cOne = carinderia(40,50,10,30,35,50,35,10,12,13,13,14)

# cOne.introduceMenu()

# order = []


# print()
# ulam = input("Type Your 'MENU' If Any Or Type Any KEY to Passed : ")

# print(" ----- Succesful Order ----- ")

# cOne = carinderia(ulam)
# order.append(cOne)

# if ulam == "Menudo": pass
# elif ulam == "Sinigang": pass
# elif ulam == "Lumpia": pass
# elif ulam == "Torta": pass
# elif ulam == "Ampalaya": pass
# elif ulam == "Carrie": pass
# elif ulam == "Munggo": pass
# else:
#     print("OK")


# kanin  = int(input("How Many Rice ? : "))

# # if kanin == "RICE": pass



# inumin = input("Type Your Drinks : ")

# order = ulam +  kanin + inumin

# order = carinderia()

# addRice = input("Add Rice ? : ")

# 

# 

# addDrinks = input("Add Drinks ? " )


# if order == "Menudo":
#     print("Succesfull Order")
# elif order == "Sinigang":
#     print("Succesfull Order")
# elif order == "Lumpia":
#     print("Succesfull Order")
# elif order == "Torta":
#     print("Succesfull Order")
# elif order == "Ampalaya":
#     print("Succesfull Order")
# elif order == "Carrie":
#     print("Succesfull Order")
# elif order == "Munngo":
#     print("Succesfull Order")
# else:
#     print("Invalid Order")

# bill = int(input("CHECK YOUR BILL: [Type OK] "))


# choice = input("Check MENU ? [Yes/Any Char] : ")
# if choice == "Yes" or choice == "yes": pass
# else: 




