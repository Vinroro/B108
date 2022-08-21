#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random


barrel_pocket = [i for i in range(1, 31)]
numbers_in_game = barrel_pocket.copy()


class GameCard:
    def __init__(self, whose_card):
        self.whose_card = f" Карточка {whose_card} "
        self.numbers_count = 15
        self.numbers_in_card = []

        while len(self.numbers_in_card) != 15:
            random_number = random.randint(0, len(numbers_in_game) - 1)
            self.numbers_in_card.append(numbers_in_game[random_number])
            numbers_in_game.remove(numbers_in_game[random_number])

        self.card_fields_values = []

        while len(self.card_fields_values) != 27:
            self.card_fields_values.append("  ")

        self.random_positions = []

        for i in range(3):
            while len(self.random_positions) != (5 + (i * 5)):
                random_pos = random.randint(0, 8) + (i * 9)
                if random_pos not in self.random_positions:
                    self.random_positions.append(random_pos)

        for i in self.random_positions:
            self.card_fields_values[i] = self.numbers_in_card[0]
            self.numbers_in_card.remove(self.numbers_in_card[0])

    def card_generation(self):
        result = ""
        card_len = 26

        for i in range(int((card_len - len(self.whose_card)) / 2)):
            result += "-"
        result += self.whose_card
        while len(result) != card_len:
            result += "-"
        result += "\n"

        for i in range(3):
            for j in range(9):
                if len(str(self.card_fields_values[(i * 9) + j])) == 2:
                    result += f"{str(self.card_fields_values[(i * 9) + j])} "
                else:
                    result += f" {str(self.card_fields_values[(i * 9) + j])} "
            result = result[:-1] + "\n"

        result += "-" * card_len

        return result

    def cross_the_number(self, number):
        if number in self.card_fields_values:
            self.card_fields_values[self.card_fields_values.index(number)] = " -"
            self.numbers_count -= 1
            return True
        return False

    def pass_the_number(self, number):
        return number not in self.card_fields_values

    def computer_choice(self, number):
        if number in self.card_fields_values:
            self.card_fields_values[self.card_fields_values.index(number)] = " -"
            self.numbers_count -= 1

    def numbers_in_card_check(self):
        return self.numbers_count != 0


game_card1 = GameCard("Игрока")
game_card2 = GameCard("Компьютера")


def gameplay(player_game_card, computer_game_card):
    correct_player_choice = True

    while correct_player_choice and player_game_card.numbers_in_card_check() \
            and computer_game_card.numbers_in_card_check():
        print(player_game_card.card_generation())
        print(computer_game_card.card_generation())

        barrel = barrel_pocket[random.randint(0, len(barrel_pocket) - 1)]
        barrel_pocket.remove(barrel)
        print(f"Бочонок с числом {barrel} в игре")

        player_choice = input("Зачеркнуть число? (y/n)\n")
        while player_choice != "y" and player_choice != "n":
            player_choice = input("Неверная команда. Зачеркнуть число? (y/n)\n")
        if player_choice == "y":
            correct_player_choice = player_game_card.cross_the_number(barrel)
        elif player_choice == "n":
            correct_player_choice = player_game_card.pass_the_number(barrel)

        computer_game_card.computer_choice(barrel)

    if player_game_card.numbers_in_card_check():
        print("Компьютер победил")
    else:
        print("Игрок победил")


gameplay(game_card1, game_card2)
