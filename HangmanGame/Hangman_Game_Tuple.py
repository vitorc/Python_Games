def play():
    print("****************************")
    print("Welcome to the Hangaman Game")
    print("****************************")

    secret_word = "vitor"
    ok_words = ["_", "_", "_", "_", "_"]
    hanged = False
    hit = False


    while (not hanged and not hit):

        attempt = input("What's the letter? ")
        attempt = attempt.strip()

        word_index = 0

        for word in secret_word:
            if(attempt.upper() == word.upper()):
                ok_words[word_index] = word
            word_index = word_index + 1

        else:
            print("WRONG! TRY AGAIN!")
        print(ok_words)
    print("Game Over")

if (__name__ == "__main__"):
    play()