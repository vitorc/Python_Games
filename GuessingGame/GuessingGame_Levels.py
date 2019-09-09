import random
r = random

print("*****************")
print("Guessing game")
print("*****************")

# secret_number_with_seed = random.seed(100) Seed define a entrada do valor
# secret_number_with_round = round(r.random() * 10) Nesse caso o valor inicial será zero e isso pode gerar algum erro no código.
secret_number = r.randrange(1, 101)
attempts_total = 0

print("What's the level?")
print("(1) Easy 2(Normal) 3(Hard)")
level = int(input("Choose your level: "))

if(level == 1):
    attempts_total = 20
elif(level == 2):
    attempts_total = 10
else:
    attempts_total = 2

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
        print("Wrong number! The Number is Lower than secret number")
    elif (bigger_result):
        print("Wrong number! The Number is bigger than secret number")
print(secret_number)
print("GAME OVER")