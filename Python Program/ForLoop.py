# CHALLENGE FOR FOR LOOP!!!

# #INDEX       0         1        2         
userName = ["Efren", "Pauline","Rhufa"]
password = ["abc123", "admin123", "123admin"]

currUsername = input("Enter UserName : " )
currPassword = input("Enter Password : ")

for x in range(len(userName)):
    if currUsername == userName[x] and currPassword == password[x]:
        print("Welcome, " + userName[x])
        break
else:
    print("Account Not Found")




# for x in range(5):
#     print("Hello World!!!")




# for x in range(10):
#     print(x)




#EVEN NUMBER DIVISIBLE BY 2 = REMAINDER = 0
#ODD NUMBER IS NOT DIVISIBLE BY 2 REMAINDER !=0
#MODULO %

# print(3%2) # 1
# print(12%2) # 0


## numbers = [1,2,3,4,5,6,7,8,9,10]
# numbers = [1,3,5,7,8,9,10]


# for number in numbers:
#     if number % 2 == 0:
#         print("Even Number :" + str(number))
#     else:
#         print("Odd Number : " + str(number))




# fruits = ["Apple","Banana","Orange","Grapes","Avocado"]

# #For every x in fruits
# for x in fruits:
#     print(x)
#     if x == "Apple":
#         print("An Apple a Day Keeps the Doctor Away")
#     elif x == "Orange":
#         print("ORAGES!!!")




# fruits = ["Apple","Banana","Orange","Grapes","Avocado"]

# #For every x in fruits
# for x in fruits:
#     print(x)
#     if x == "Banana":
#         break




# fruits = ["Apple","Banana","Orange","Grapes","Avocado"]

# #For every x in fruits
# for x in fruits:
#     print(x)
#     break




# fruits = ["Apple","Banana","Orange","Grapes","Avocado"]

# #For every x in fruits
# for x in fruits:
#     print(x)
# else:
#     print("No More Fruits")




# fruits = ["Apple","Banana","Orange","Grapes","Avocado"]

# #For every x in fruits
# for x in fruits:
#     print(x)



