import random
first_value = 0
second_value = 0
result = 0
user_answer = 0
number_of_problems = 0

number_of_problems = int(input("How many problems would you like to tackle?"))
print("WELCOME TO MATHMANIA")
print("LET'S BEGIN")
for i in range(number_of_problems):
    first_value = random.randint(1,100)
    second_value = random.randint(1,100)
    format = random.randint(0,3) 

    if format == 0:
        print("The sum is " + str(first_value) + " + " + str(second_value)) 
        user_answer = int(input("Enter your answer: "))
        result = first_value + second_value
        print("The result is: " + str(result))
        if user_answer == result:
            print("Great job! That's the right answer!")
        else:
            print("That is the wrong answer. The right one is "+ str(result))

    if format == 1:
        print("The sum is " + str(first_value) + " - " + str(second_value)) 
        user_answer = int(input("Enter your answer: "))
        result = first_value - second_value
        print("The result is: " + str(result))
        if user_answer == result:
            print("Great job! That's the right answer!")
        else:
            print("That is the wrong answer. The right one is "+ str(result))

    if format == 2:
        print("The sum is " + str(first_value) + " / " + str(second_value)) 
        user_answer = float(input("Enter your answer: "))
        result = first_value / second_value
        result = round(result, 2)
        print("The result is: " + str(result))
        if user_answer == result:
            print("Great job! That's the right answer!")
        else:
            print("That is the wrong answer. The right one is "+ str(result))

    if format == 3:
        print("The sum is " + str(first_value) + " * " + str(second_value)) 
        user_answer = int(input("Enter your answer: "))
        result = first_value * second_value
        print("The result is: " + str(result))
        if user_answer == result:
            print("Great job! That's the right answer!")
        else:
            print("That is the wrong answer. The right one is "+ str(result))
