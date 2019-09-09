def play():
    print("****************************")
    print("Welcome to the Hangaman Game")
    print("****************************")

    secret_word = "vitor"
    hanged = False
    hit = False

    while (not hanged and not hit):

        attempt = input("What's the letter? ")
        attempt = attempt.strip()

        word_index = 0

        for word in secret_word:
            if(attempt.upper() == word.upper()):
                print("You found the letter(s) {} in the position {}".format(word, word_index))
            word_index = word_index + 1
    print("Game Over")


if (__name__ == "__main__"):
    play()