import random

UNCHAR = '■'


mesg = {
    'statr': 'Вы готовы начать игру y/n? ',
    'statrWrongInput': 'Неправильный ввод! Введите только y или n! ',
    'statrMessage': 'Игра началась!',
    'exitGame': 'Очень жаль что вы от нас уходите, приходите ещё!',
    'newWord': 'Итак, я загадал слово! Вот его описание - ',
    'isEndWin': 'Вы выиграли! Хотите сыграть еще раз? y/n ',
    'isEndLose': 'Вы проиграли! Хотите сыграть еще раз? y/n ',
    'input': 'Введите букву: ',
    'isLetterCorrect': 'Эта буква есть в слове!',
    'isLetterWrong': 'Этой буквы нет в слове!',
    'isLetterAlready': 'Эта буква уже была!',
    'inputWrong': 'Неравильный ввод! Введите только одну букву!',
    'gesWord': 'Сейчас ваше слово выглядит так - ',

}

WORDS = {}

Gallows = {

}


def GetGallows():
    for i in range(5):
        Gallows[str(i)] = GetTextFromFile(f'{5-i}')


def GetTextFromFile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def GetWords():
    with open('words.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                title, description = line.split(':', 1)
                WORDS[title.strip()] = description.strip()


def GetRandomWord():
    if not WORDS:
        return None, None
    else:
        title, description = random.choice(list(WORDS.items()))
        return title, description


def ShowWord(word, guessed_letters):
    revealed_word = ""
    for ch in word:
        if ch.lower() in guessed_letters:
            revealed_word += ch
        else:
            revealed_word += UNCHAR
    return revealed_word
