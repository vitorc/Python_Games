def play():
    print("****************************")
    print("Welcome to the Hangaman Game")
    print("****************************")
    secret_words_list = "vitor".upper()
    secret_word = "vitor".upper()
    ok_words = ["_" for word in secret_word]
    hanged = False
    hit = False
    error = 5
    while (not hanged and not hit):
        attempt = input("What's the letter? ")
        attempt = attempt.strip().upper()
        word_index = 0
        for word in secret_word:
            if(attempt == word):
                ok_words[word_index] = word
            word_index = word_index + 1
        else:
            error -= 1
        hanged = error == 0
        hit = "_" not in ok_words
        print(ok_words)
        print("Do you have more {} attempts".format(error - 1))


    if(hit):
        print("YOU WIN")
    else:
        print("YOU LOSE")
    print("Game Over")

if (__name__ == "__main__"):
    play()