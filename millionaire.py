import random


def game_start():
    print("This is the game of games..\nIn the arena..\nMr Steven Vágó is awating You!\nBecome the next Millionaire!")


def quiz():
    with open('questions.txt', "r") as file:
        question_lines = file.readlines()
        question_table = [element.replace("\n", "").split(";") for element in question_lines]
    with open('answers.txt', "r") as file:
        lines = file.readlines()
        answer_table = [element.replace("\n", "").split(",") for element in lines]
        for i in range(len(question_lines)):
            shuffled_list = random.shuffle(question_table[i])
            a = answer_table[i][0]
            b = answer_table[i][1]
            c = answer_table[i][2]
            d = answer_table[i][3]
            first_choice = "A: "+''.join(answer_table[i][0])
            second_choice = "B: "+''.join(answer_table[i][1])
            third_choice = "C: "+''.join(answer_table[i][2])
            fourth_choice = "D: "+''.join(answer_table[i][3])
            print(', '.join(question_table[i]))
            print(first_choice)
            print(second_choice)
            print(third_choice)
            print(fourth_choice)
            result = input("Select the correct answer: ")
            print(result)
            correct_result = ""
            for instance in [a, b, c, d]:
                if instance == answer_table[i][0]:
                    correct_result = i
                    if instance == correct_result:
                        print("well done")
                    else:
                        print("better luck next time")


def main():
    game_start()
    quiz()


if __name__ == "__main__":
    main()
