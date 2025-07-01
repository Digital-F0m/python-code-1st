#CHALLENGE FOR CONDITIONAL STATEMENTS !!!

math = float(input("Grade for Math: "))
english = float(input("Grade for English: "))
filipino = float(input("Grade for Filipino :"))

average = (math + english + filipino) / 3

print("AVERAGE " + str(average))

if average  > 100 or average <= 50:
    print("Invalid Grade")
elif average >= 98:
    print("With Highest Honors")
elif average >= 95:
    print("With High Honors")
elif average >= 90:
    print("With Honors")
elif average >= 75:
    print("PASSED")
else:
    print("FAILED")




# bag = ("lipstick")

# if "wallet" in bag:
#     print("Wala namang laman Yan")
# else:
#     print("Sige pasok ka")




# bag = ["wallet","lipstick"]

# if "gun" in bag or "laptop" in bag or "computer" in bag:
#     print("Huli Ka!")
# else:
#     print("Sige Pasok Ka")




# bag = ["wallet","gun","lipstick","cellphone","knife"]

# if "gun" in bag:
#     print("Huli Ka!")
# else:
#     print("Sige Pasok Ka")




# hasMeterStick = False
# hasRuler = False
# hasBallpen = True


# if hasMeterStick and hasRuler or hasBallpen:
#     print("Pasok Ka")
# else:
#     print("Pwede kana lumabas")




# hasMeterStick = False
# hasRuler = True

# if hasMeterStick or hasRuler:
#     print("Pasok Ka")
# else:
#     print("Pwede kana lumabas")




# hasMeterStick = True
# hasRuler = True

# if hasMeterStick and hasRuler:
#     print("Pasok Ka")
# else:
#     print("Pwede kana lumabas")




# userName = input("Enter Your UserName : ")
# password = input("Enter Your Password : ")

# if userName == "Efren" and password == "Admin":
#     print("Yes Boss!")
# elif userName == "Fom" and password == "Admin123":
#     print("Welcome Boss!")
# else:
#     print("Invalid User")




# age = int(input("Enter your Age : "))
# height = int(input("Enter your Height : "))

# if age >= 18 and height >= 176:
#     print("Tall and Legal Age")
# elif age >= 18 and height >= 150:
#         print("Average and Legal Age")
# elif age >= 18:
#         print("Short and Legal Age")
# else:
#     print("Too Young")




# age = int(input("Enter your Age : "))

# # if age >= 18:
# #     print("Too Young")

# if not age >= 18:
#     print("Too Young")
# else:
#     print("Legal Age")




# age = int(input("Enter your Age : "))
# height = int(input("Enter your Height : "))

# if age >= 18:
#     if height >= 176:
#         print("Tall and Legal Age")
#     elif height >= 150:
#         print("Average and Legal Age")
#     else:
#         print("Short and Legal Age")
# else:
#     print("Too Young")




# age = int(input("Enter your Age : "))

# if age >= 18:
#     print("Legal Age")
# elif age >= 13:
#     print("Teenager")
# elif age >= 5:
#     print("Child")
# else:
#     print("Too Young")




# age = int(input("Enter your Age : "))

# if age >= 18:
#     print("Legal Age")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Too Young")




# password = input("Enter Password : ")

# if password == "123abc":
#     print("Access Granted")
# else:
#     print("Access Denied")




# age = int(input("Enter your Age : "))

# if age >= 18:
#     print("Legal Age")
# else:
#     print("Too Young")




# age = int(input("Enter Your Age: "))

# if age >= 18:
#     print("Legal Age")
#     #print("Thank you for using the Program")
# print("Thank you for using the Program")


