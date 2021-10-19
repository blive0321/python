# if else with number
score = int(input("Please input the number: "))
if score >= 10:
    print ("The number is bigger and equal than 10.")
else:
    print ("The number is smaller than 10.")


# if elif else
score2 = int(input("Please the English score: "))
if score2 >= 90:
    print ("Grade is : A")
elif score2 >= 80:
    print ("Grade is : B")
elif score2 >= 70:
    print ("Grade is : C")
elif score2 >= 60:
    print ("Grade is : D")
else:
    print ("Failed the exam.")


# if else with text
answer = str(input("Please input [Y/N]: "))
if answer == "Y":
    print ("Yes")
else:
    print ("No")
