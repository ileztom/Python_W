import getters


def isSingleLetter(string):
    if len(string) == 1 and string.isalpha():
        return True
    else:
        return False


def checkLetter(word, letter):
    return letter in word


def isStatr(statr):
    if statr.lower() == 'y':
        return True
    elif statr.lower() == 'n':
        return False
    else:
        return None


def AskStart():
    isStr = None
    while isStr is None:
        isStr = isStatr(input())
        if isStr is None:
            print(getters.mesg['statrWrongInput'])
        elif isStr:
            print(getters.mesg['statrMessage'])
        else:
            print(getters.mesg['exitGame'])
            return False
    return True


def GameLoop(word, guessed_letters, HP):
    isEnd = False
    while not isEnd:
        gl = inputLetter(guessed_letters)
        if checkLetter(word.lower(), gl.lower()):
            print(getters.mesg['isLetterCorrect'])
        else:
            print(getters.mesg['isLetterWrong'])
            HP -= 1
            print(getters.Gallows[str(HP)] + "\n")
        if HP == 0:
            print(getters.mesg['isEndLose'])
            isEnd = True
        else:
            print(getters.mesg['gesWord'] + getters.ShowWord(word, guessed_letters))
            if getters.ShowWord(word, guessed_letters) == word:
                print(getters.mesg['isEndWin'])
                isEnd = True


def inputLetter(guessed_letters):
    while True:
        gl = input()
        if not isSingleLetter(gl):
            print(getters.mesg['inputWrong'])
        elif gl in guessed_letters:
            print(getters.mesg['isLetterAlready'])
        else:
            guessed_letters.append(gl.lower())
            return gl


def GameProcess():
    print(getters.mesg['statr'])
    if not AskStart():
        return

    while True:

        word, description = getters.GetRandomWord()
        print(getters.mesg['newWord'] + description)
        print(getters.mesg['input'])

        guessed_letters = []
        HP = 5

        GameLoop(word, guessed_letters, HP)

        if not AskStart():
            return


def main():
    getters.GetWords()
    getters.GetGallows()
    GameProcess()


if __name__ == "__main__":
    main()