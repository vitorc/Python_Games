import random
r = random

print("*****************")
print("Guessing game")
print("*****************")

# secret_number_with_seed = random.seed(100) Seed define a entrada do valor
# secret_number_with_round = round(r.random() * 10) Nesse caso o valor inicial será zero e isso pode gerar algum erro no código.
secret_number = r.randrange(1, 11)
attempts_total = 3


for attempt in range(1, attempts_total + 1):
    print("Attempt {} by {}".format(attempt, attempts_total))
    user_number_str = input("Fill the number: ")
    print("Your number was: " + user_number_str)
    user_number = int(user_number_str)

    if(user_number < 1 or user_number > 10):
        print("Please fill number between 1 and 10!")
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
print(secret_number)
print("GAME OVER")