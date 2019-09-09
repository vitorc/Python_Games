import random
r = random

def play():
    print("*****************")
    print("Guessing game")
    print("*****************")

    # O operador ( // ) Integer division é utilizado para exibir o valor inteiro do resultado da divisão sem arredondar
    # secret_number_with_seed = random.seed(100) Seed define a entrada do valor
    # secret_number_with_round = round(r.random() * 10) Nesse caso o valor inicial será zero e isso pode gerar algum erro no código.
    secret_number = r.randrange(1, 101)
    attempts_total = 0
    player_score = 1000

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
            print("Your Score was {}".format(player_score))
            break
        else:
            if(lower_result):
                print("Wrong number! The Number is Lower than secret number")

            elif (bigger_result):
                print("Wrong number! The Number is bigger than secret number")
            score_loss = abs(secret_number - user_number)
            player_score = player_score - score_loss
    print("The secret_number was {}".format(secret_number))
    print("GAME OVER")

if(__name__ == "__main__"):
    play()