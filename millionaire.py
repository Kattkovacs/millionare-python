import random
def game_start():
    print("This is the game of games..\nIn the arena..\nMr Steven Vágó is awating You!\nBecome the next Millionaire!")

def quiz():
    with open('questions.txt', "r") as file:
        lines = file.readlines()
        table = [element.replace("\n", "").split(";") for element in lines]
        print(', '.join(table[0]))
    with open('answers.txt', "r") as file:
        lines = file.readlines()
        table = [element.replace("\n", "").split(",") for element in lines]
        shuffled_list=random.shuffle(table[0])
        a="A: "+''.join(table[0][0])
        b="B: "+''.join(table[0][1])
        c="C: "+''.join(table[0][2])
        d="D: "+''.join(table[0][3])
        print(a)
        print(b)
        print(c)
        print(d)

def main():
    game_start()
    quiz()

if __name__ == "__main__":
    main()





