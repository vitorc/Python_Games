import random

def print_star_game_message():
    print("****************************")
    print("Welcome to the Hangaman Game")
    print("****************************")
def load_secret_words():
    words = []

    with open("secret_words.txt", "r") as file:
        for line in file:
            line = line.strip()
            words.append(line)

    random_number = random.randrange(0, len(words))
    secret_word = words[random_number].upper()
    return  secret_word
def start_ok_words(secret_word):
    return ["_" for word in secret_word]
def user_attempt():
    attempt = input("What's the word? ")
    attempt = attempt.strip().upper()
    return attempt
def correct_attempt(secret_word, attempt, ok_words):
    word_index = 0
    for word in secret_word:
        if (attempt == word):
            ok_words[word_index] = word
        word_index = word_index + 1
def print_winner_message():
    print("Congrats!!! YOU WIN!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def print_loser_message(secret_word):
    print("Damn it, You was Hanged!")
    print("The correct word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def print_Hangman_Game(error):
    print("  _______     ")
    print(" |/      |    ")

    if(error == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(error == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(error == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(error == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(error == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(error == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (error == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def play():
    print_star_game_message()
    secret_word = load_secret_words()
    ok_words = start_ok_words(secret_word)

    hanged = False
    hit = False
    error = 0
    while (not hanged and not hit):
        attempt = user_attempt()
        if(attempt in secret_word):
            correct_attempt(secret_word, attempt, ok_words)
        else:
            error += 1
            print_Hangman_Game(error)
        hanged = error == 7
        hit = "_" not in ok_words
        print(ok_words)

    if(hit):
        print_winner_message()
    else:
        print_loser_message(secret_word)

if (__name__ == "__main__"):
    play()