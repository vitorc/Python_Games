print("*****************")
print("Guess game")
print("*****************")

secretnumber = 43
attempts_total = 3
attempt = 1

while (attempt <= attempts_total):
    print("Attempt {} by {}".format(attempt, attempts_total))
    usernumber_str = input("Fill the number: ")
    print("Your number was: " + usernumber_str)
    usernumber = int(usernumber_str)

    right_result = secretnumber == usernumber
    lower_result = usernumber < secretnumber
    bigger_result = usernumber > secretnumber

    if (right_result):
        print("You discovery the secret number")
    elif(lower_result):
        print ("Wrong number lower than real number")
    elif (bigger_result):
        print("Wrong number bigger than real number")
    attempt = attempt + 1
