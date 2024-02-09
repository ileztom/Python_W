def choose_word():
    words = "олень"
    return words
def play_game():
    word_to_guess = choose_word()
    guessed_word = "_" * len(word_to_guess)
    lives = 3
    while guessed_word != word_to_guess and lives > 0:
        print("У вас {} жизн{}".format(lives, "ь" if lives == 1 else "и"))
        print("Слово:", " ".join(guessed_word))
        guess = input("Введите букву или угадайте слово целиком: ").lower()
        if len(guess) == 1:
            if guess in word_to_guess:
                print("Правильно!")
                guessed_word = "".join([c if c == guess or guessed_word[i] != "_" else "_" for i, c in enumerate(word_to_guess)])
            else:
                print("Неправильно")
                lives -= 1
        elif len(guess) == len(word_to_guess) and guess.isalpha():
            if guess == word_to_guess:
                guessed_word = word_to_guess
                print("Вы угадали слово!")
            else:
                print("Неправильно")
                lives -= 1
        else:
            print("Неверный ввод")
    if guessed_word == word_to_guess:
        print("Вы угадали слово: {}".format(word_to_guess))
    else:
        print("Вы проиграли, загаданное слово было: {}".format(word_to_guess))
play_game()