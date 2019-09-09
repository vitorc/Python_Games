print("*****************")
print("Guessing game")
print("*****************")

secret_number = 43
attempts_total = 3


for attempt in range(1, attempts_total + 1):
    print("Attempt {} by {}".format(attempt, attempts_total))
    user_number_str = input("Fill the number: ")
    print("Your number was: " + user_number_str)
    user_number = int(user_number_str)

    if(user_number < 1 or user_number > 100):
        print("Please fill number between 1 and 100!")
        continue  #Sai do IF e executa o for de novo

    right_result = secret_number == user_number
    lower_result = user_number < secret_number
    bigger_result = user_number > secret_number

    if (right_result):
        print("You discovery the secret number")
        print("WINNER!")
        break

    elif(lower_result):
        print("Wrong number! The Number is Lower than real number")
    elif (bigger_result):
        print("Wrong number! The Number is bigger than real number")
print("GAME OVER")