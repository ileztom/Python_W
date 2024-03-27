import random

class HangmanGame:
    UNCHAR = '■'

    def __init__(self):
        self.messages = {
            'start': 'Ready to play? (y/n) ',
            'wrong_input': 'Invalid input! Enter only y or n! ',
            'start_message': 'The game has started!',
            'exit_game': 'Thanks for playing!',
            'new_word': 'I have chosen a word! Here is its description - ',
            'win': 'You won! Play again? (y/n) ',
            'lose': 'You lost! Play again? (y/n) ',
            'input': 'Enter a letter: ',
            'correct_letter': 'This letter is in the word!',
            'wrong_letter': 'This letter is not in the word!',
            'already_guessed': 'You have already guessed this letter!',
            'input_wrong': 'Invalid input! Enter only one letter!',
            'current_word': 'Current word: ',
        }
        self.words = {}
        self.gallows = {}

    def get_gallows(self):
        for i in range(5):
            self.gallows[str(i)] = self.get_text_from_file(f'{5-i}')

    def get_text_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    def get_words(self):
        with open('words.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if ':' in line:
                    title, description = line.split(':', 1)
                    self.words[title.strip()] = description.strip()

    def get_random_word(self):
        if not self.words:
            return None, None
        else:
            title, description = random.choice(list(self.words.items()))
            return title, description

    def show_word(self, word, guessed_letters):
        revealed_word = ""
        for ch in word:
            if ch.lower() in guessed_letters:
                revealed_word += ch
            else:
                revealed_word += self.UNCHAR
        return revealed_word

    def is_single_letter(self, string):
        return len(string) == 1 and string.isalpha()

    def check_letter(self, word, letter):
        return letter in word

    def is_start(self, start):
        return start.lower() == 'y' if start.lower() in ('y', 'n') else None

    def ask_start(self):
        is_start = None
        while is_start is None:
            is_start = self.is_start(input())
            if is_start is None:
                print(self.messages['wrong_input'])
            elif is_start:
                print(self.messages['start_message'])
            else:
                print(self.messages['exit_game'])
                return False
        return True

    def input_letter(self, guessed_letters):
        while True:
            letter = input()
            if not self.is_single_letter(letter):
                print(self.messages['input_wrong'])
            elif letter in guessed_letters:
                print(self.messages['already_guessed'])
            else:
                guessed_letters.append(letter.lower())
                return letter

    def game_loop(self, word, guessed_letters, hp):
        is_end = False
        while not is_end:
            letter = self.input_letter(guessed_letters)
            if self.check_letter(word.lower(), letter.lower()):
                print(self.messages['correct_letter'])
            else:
                print(self.messages['wrong_letter'])
                hp -= 1
                print(self.gallows[str(hp)] + "\n")
            if hp == 0:
                print(self.messages['lose'])
                is_end = True
            else:
                print(self.messages['current_word'] + self.show_word(word, guessed_letters))
                if self.show_word(word, guessed_letters) == word:
                    print(self.messages['win'])
                    is_end = True

    def game_process(self):
        print(self.messages['start'])
        if not self.ask_start():
            return

        while True:
            self.get_words()
            self.get_gallows()

            word, description = self.get_random_word()
            print(self.messages['new_word'] + description)
            print(self.messages['input'])

            guessed_letters = []
            hp = 5

            self.game_loop(word, guessed_letters, hp)

            if not self.ask_start():
                return

def main():
    hangman_game = HangmanGame()
    hangman_game.game_process()

if __name__ == "__main__":
    main()