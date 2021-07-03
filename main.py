import os
import random
import sys


def clear_screen():
    """
    Clear screen on Windows
    For Linux or Mac use "cls" instead
    """
    os.system("clear")


def read(route):
    content = []
    base_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base_dir, route), 'r', encoding='UTF-8') as file:
        for line in file:
            content.append(str(line))
    return content


def read_answer():
    answer = ""
    error = False
    while len(answer) == 0:
        msg = "Insert a valid letter: " if error else "Insert a letter: "
        aux = input(msg)
        answer = aux if not aux.isnumeric() and len(aux) == 1 else ""
        if len(answer) > 0:
            answer = answer.lower() if 97 <= ord(answer.lower()) <= 122 else ""
        error = len(answer) == 0
    return answer


class Game:
    def __init__(self):
        self.answers = []
        self.HANGMANPICS = []

        self.answers = read("./archives/words.txt")
        self.HANGMANPICS = self.get_hangman_pics()
        self.new_game()

    def get_hangman_pics(self):
        response = read("./archives/hangmanpics.txt")
        result = []
        height = 7
        aux = ""
        for i in range(len(response)):
            if i % height == 0:
                result.append(aux)
                aux = ""
            aux += response[i]
        result.remove("")
        return result

    def get_random_answer(self):
        aux = random.randint(0, len(self.answers))
        return self.answers[aux].strip()

    def get_answer_len(self, answer):
        result = ["_" for _ in answer]
        return result

    def draw_state(self, mistake_number, answer_state):
        clear_screen()
        print(self.HANGMANPICS[mistake_number])
        for letter in answer_state:
            print(letter, end=" ")
        print()

    def verify_letter(self, letter, answer):
        try:
            answer.index(letter)
            return True
        except ValueError:
            return False

    def update_answer_state(self, letter, answer, answer_state):
        new_state = answer_state[:]
        for i in range(len(answer)):
            if letter == answer[i]:
                new_state[i] = letter
        return new_state

    def has_won(self, answer_state):
        try:
            answer_state.index("_")
            return False
        except ValueError:
            return True

    def menu(self):
        print("Do you want to start a new game?\n[Y]es\n[N]o")
        response = read_answer()
        if response == "y":
            self.new_game()
        else:
            sys.exit()

    def new_game(self):
        answer = self.get_random_answer()
        answer_state = self.get_answer_len(answer)
        mistakes = 0
        win = False
        states = len(self.HANGMANPICS)
        while mistakes < states and not win:
            self.draw_state(mistakes, answer_state)
            letter = read_answer()
            if self.verify_letter(letter, answer):
                answer_state = self.update_answer_state(letter, answer, answer_state)
            else:
                mistakes += 1
            win = self.has_won(answer_state)
        self.draw_state(mistakes if win else states - 1, answer_state)
        result = "CONGRATS\nYou won" if win else "Sorry, you lose"
        print(result)
        self.menu()


if __name__ == '__main__':
    game = Game()

