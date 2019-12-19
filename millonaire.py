import random
import copy
import sys
import os
from sty import Style, RgbFg, fg, rs
import time

def game_start():
    fg.purple = Style(RgbFg(148, 0, 211))
    print("This is the game of games..\nIn the arena..\nMr Steven Vágó is awating You!\n"+fg.purple+"Become the next Millionaire!"+fg.rs)

def quiz():
    with open('questions.txt', "r") as file:
        question_lines = file.readlines()
        question_table = [element.replace("\n", "").split(";") for element in question_lines]
    with open('answers.txt', "r") as file:
        list_of_answers = []
        for line in file:
            line = line.strip().split(',')
            list_of_answers.append(line)
        counter = 0
        copy_of_list_of_answers = copy.deepcopy(list_of_answers)
        for i in range(len(question_lines)):
            current_line = list_of_answers[i]
            shuffled_line = copy_of_list_of_answers[i]
            random.shuffle(shuffled_line)
            a = shuffled_line[0]
            b = shuffled_line[1]
            c = shuffled_line[2]
            d = shuffled_line[3]
            fg.orange = Style(RgbFg(255, 150, 50))
            first_choice = fg.orange + 'A: ' + fg.rs +''.join(shuffled_line[0])
            second_choice = fg.orange + 'B: ' + fg.rs+''.join(shuffled_line[1])
            third_choice = fg.orange + 'C: ' + fg.rs+''.join(shuffled_line[2])
            fourth_choice = fg.orange + 'D: ' + fg.rs+''.join(shuffled_line[3])
            print(', '.join(question_table[i]))
            print(first_choice)
            print(second_choice)
            print(third_choice)
            print(fourth_choice)
            answer = input("Select the correct answer: ")
            counter += 1
            if answer == 'a':
                answer=a
            if answer == 'b':
                answer=b
            if answer == 'c':
                answer=c
            if answer == 'd':
                answer=d
            if answer==current_line[0]:
                fg.green = Style(RgbFg(0, 255, 0))
                print(fg.green + "Well done!" + fg.rs)
                time.sleep(2)
                os.system('clear')
                
            else:
                print("Better luck next time!")
                sys.exit(0)
            if counter==5:
                print(fg.orange + "You have guaranteed 100.000 Ft" + fg.rs)
            if counter==10:
                print(fg.orange + "You have guaranteed 1.500.000 Ft" + fg.rs)
            if counter==15:
                print(fg.orange + "Congratulations!\nYou've just won the unbelivable 40.000.000 Ft\n"+fg.purple+"You became the new Millionaire!!!" + fg.rs)
                sys.exit(0)
def main():
    game_start()
    quiz()

if __name__ == "__main__":
    main()

