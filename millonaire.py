import random
import copy
import sys
import os
from sty import Style, RgbFg, fg, bg
import time
import pygame
import circle


def game_start():
    fg.purple = Style(RgbFg(148, 0, 211))
    pygame.mixer.init()
    os.system('clear')
    play_sound("./msc/loim_intro.wav", 0)
    time.sleep(2)
    print("This is the game of games..\nIn the arena..\nMr Steven Vágó is awaiting You!\n"+fg.purple+"Become the next Millionaire!\n"+fg.rs)
    circle.who_wants_to_be_a_millionaire_circle()
    time.sleep(5)


def play_sound(filename, starting_time):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    # pygame.mixer.music.set_volume(0.07)
    pygame.mixer.music.play(0, starting_time)


def open_file(filename, mode):
    with open(filename, mode) as file:
        list_of_file = []
        for line in file:
            line = line.strip().split(',')
            list_of_file.append(line)
    return list_of_file


def open_drawing(filename, mode):
    with open(filename, mode) as file:
        list_of_file = []
        for line in file:
            line = line.split(',')
            list_of_file.append(line)
    return list_of_file


def safe_input(input_text, allowed_list_of_letters):
    answer = input(input_text)
    while answer not in allowed_list_of_letters:
        print("Error! Only letters: " + ' '.join(allowed_list_of_letters) +" allowed!")
        answer = input("Select the correct answer!")
    return answer


def choose_random_from_list(list_):
    return random.choice(list_)


def quiz_table(table_line_length, choises, question, shuffled_line):
    print("  "+bg.black+"/"+"‾"*(table_line_length-6)+"\\"+bg.rs)
    width = table_line_length
    print("-"+bg.black+"‹"+''.join(question).center((width-4), ' ')+"›"+bg.rs+"-")
    print("  "+bg.black+"\\"+"_"*(table_line_length-6)+"/"+bg.rs)
    space_left = 7
    upper_line_first_second_choise = "  "+bg.black+"/"+(len(shuffled_line[0])+space_left)*"‾"+"\\"+bg.rs+(" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+22)))+bg.black+"/"+(len(shuffled_line[1])+space_left)*"‾"+"\\"+bg.rs
    under_line_first_second_choise = "  "+bg.black+"\\"+(len(shuffled_line[0])+space_left)*"_"+"/"+bg.rs+(" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+22)))+bg.black+"\\"+(len(shuffled_line[1])+space_left)*"_"+"/"+bg.rs
    upper_line_third_fourth_choise = "  "+bg.black+"/"+(len(shuffled_line[2])+space_left)*"‾"+"\\"+bg.rs+(" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+22)))+bg.black+"/"+(len(shuffled_line[3])+space_left)*"‾"+"\\"+bg.rs
    under_line_third_fourth_choise = "  "+bg.black+"\\"+(len(shuffled_line[2])+space_left)*"_"+"/"+bg.rs+(" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+22)))+bg.black+"\\"+(len(shuffled_line[3])+space_left)*"_"+"/"+bg.rs
    print(upper_line_first_second_choise)
    print("-"+bg.black+"‹ " + choises[0] + " ›" + bg.rs + ("-"*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+24))) + bg.black+"‹ "+choises[1] + " ›"+bg.rs+"-")
    print(under_line_first_second_choise)
    print(upper_line_third_fourth_choise)
    print("-"+bg.black+"‹ " + choises[2] + " ›" + bg.rs + ("-"*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+24)))+bg.black+"‹ "+choises[3] + " ›"+bg.rs+"-")
    print(under_line_third_fourth_choise)


def print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter):
    vago_feje_sorai = open_drawing('vago.txt', 'r')
    Aud = "👥 "
    Tel = bg.black+"📞 "
    Halv = "50:50 "
    for helps in Help_available:
        if not helps:
            if helps == Help_available[0]:
                Aud = bg.red+"👥 "+bg.rs
            if helps == Help_available[1]:
                Tel = bg.red+"📞 "+bg.rs
            if helps == Help_available[2]:
                Halv = bg.red+"50:50 "+bg.rs
    n = 0
    print((62*" ")+bg.black+(len(prices[-1])+2)*"-".rstrip() + bg.rs)
    print((62*" ")+bg.black+"|"+" "+Halv+"∥"+Tel+"∥"+Aud+(len(prices[-1])-(len(Halv)+len(Tel)+len(Aud)+4))*" "+bg.black+"|"+bg.rs)
    print((62*" ")+bg.black+(len(prices[-1])+2)*"-"+bg.rs)
    print((62*" ")+bg.black+(len(prices[-1])+2)*"-"+bg.rs)
    for head_lines in range(15):
        bg.orange = bg(255, 150, 50)
        spaces_ = (len(prices1[0])-len(prices1[head_lines]))*" "
        if prices2[head_lines] == prices2[0]:
            prices2[0] = bg.black+fg.white+prices1[0]
        if counter == 14:
            prices2[0] = bg.orange+fg.black+prices1[0]
        if prices2[head_lines] == prices2[counter]:
            prices2[14-counter] = bg.orange+fg.black+prices1[14-counter]
            if counter >= 1:
                prices2[14-counter+1] = bg.black+fg.orange+prices1[14-counter+1]
            for n in range(counter+1, 15):
                if n in [5, 10, 14]:
                    prices2[n] = bg.black+fg.white+prices2[n]
                prices2[n] = bg.black+fg.orange+prices2[n]                
        print(''.join(vago_feje_sorai[head_lines]).strip('\n')+bg.black+"|"+fg.rs+bg.rs+prices2[head_lines]+spaces_+fg.white+bg.black+"|"+bg.rs+fg.rs)
    print(''.join(vago_feje_sorai[15]).rstrip()+13*" "+bg.black+(len(prices[:-1])+1)*"-"+bg.rs)
    for art in range(16, 20):
        print(''.join(vago_feje_sorai[art]).rstrip())


def help_modules(a, b, c, d, current_line, question, vago_feje_sorai, table_line_length, shuffled_line, choises, Audience, Telephone, Halving, Help_available, prices, prices1, prices2, counter):
    help_ = safe_input("For Audience's help, type 'a'\nFor Telephone help type 't'\nFor halving type 'h': ", ["a","t","h"])
    if help_.lower() == "a":
        if Audience:
            audience_help(a, b, c, d, current_line, question, table_line_length, choises, shuffled_line)
            Audience = False
            print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
            quiz_table(table_line_length, choises, question, shuffled_line)
        else:
            print("You have already used the audience's help!")

    if help_.lower() == "t":
        if Telephone:
            telephone_help(question, current_line)
            Telephone = False
        else:
            print("You have already used the telephone help!")

    if help_.lower() == "h":
        if Halving:
            halving(vago_feje_sorai, table_line_length, question, shuffled_line, choises, current_line, a, b, c, d)
            Halving = False
            print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
            quiz_table(table_line_length, choises, question, shuffled_line)
        else:
            print("You have already used the halving help!")
    answer = safe_input("Select the correct answer(a,b,c,d):", ["a", "b", "c", "d"])
    return Audience, Telephone, Halving, answer


def audience_help(a, b, c, d, current_line, question, table_line_length, choises, shuffled_line):
    play_sound("./msc/kozonseg.mp3", 0)
    for choise in [a, b, c, d]:
        if choise == current_line[0]:
            if choise == a:
                a_percent = random.randrange(40, 89)
                b_percent = random.randrange(0, (100-a_percent))
                c_percent = random.randrange(0, (100-a_percent-b_percent))
                d_percent = 100-(a_percent+b_percent+c_percent)
            if choise == b:
                b_percent = random.randrange(40, 89)
                a_percent = random.randrange(0, (100-b_percent))
                c_percent = random.randrange(0, (100-b_percent-a_percent))
                d_percent = 100-(a_percent+b_percent+c_percent)
            if choise == c:
                c_percent = random.randrange(40, 89)
                b_percent = random.randrange(0, (100-c_percent))
                a_percent = random.randrange(0, (100-c_percent-b_percent))
                d_percent = 100-(a_percent+b_percent+c_percent)
            if choise == d:
                d_percent = random.randrange(40, 89)
                b_percent = random.randrange(0, (100-d_percent))
                c_percent = random.randrange(0, (100-d_percent-b_percent))
                a_percent = 100-(d_percent+b_percent+c_percent)
            if a_percent+b_percent+c_percent+d_percent != 100:
                print(" AUDIENCE HELP IS BROKEN!!!")
                break
            os.system('clear')
            for choise_ in [a, b, c, d]:
                if choise == current_line[0]:
                    if choise_ == a:
                        fake_a_percent = random.randrange(40, 89)
                        fake_b_percent = random.randrange(0, (100-fake_a_percent))
                        fake_c_percent = random.randrange(0, (100-fake_a_percent-fake_b_percent))
                        fake_d_percent = 100-(fake_a_percent + fake_b_percent + fake_c_percent)
                    if choise_ == b:
                        fake_b_percent = random.randrange(40, 89)
                        fake_a_percent = random.randrange(0, (100-fake_b_percent))
                        fake_c_percent = random.randrange(0, (100-fake_b_percent-fake_a_percent))
                        fake_d_percent = 100-(fake_a_percent+fake_b_percent+fake_c_percent)
                    if choise_ == c:
                        fake_c_percent = random.randrange(40, 89)
                        fake_b_percent = random.randrange(0, (100-fake_c_percent))
                        fake_a_percent = random.randrange(0, (100-fake_c_percent-fake_b_percent))
                        fake_d_percent = 100-(fake_a_percent+fake_b_percent+fake_c_percent)
                    if choise_ == d:
                        fake_d_percent = random.randrange(40, 89)
                        fake_b_percent = random.randrange(0, (100-fake_d_percent))
                        fake_c_percent = random.randrange(0, (100-fake_d_percent-fake_b_percent))
                        fake_a_percent = 100-(fake_d_percent+fake_b_percent+fake_c_percent)
                    if fake_a_percent+fake_b_percent+fake_c_percent+fake_d_percent != 100:
                        print("Sheibe")
                print("A:"+bg.blue+fake_a_percent*" "+" "+str(fake_a_percent)+"%"+"\n"+bg.rs+"B:"+bg.blue+fake_b_percent*" "+" "+str(fake_b_percent)+"%"+"\n"+bg.rs+"C:"+bg.blue+fake_c_percent*" "+" "+str(fake_c_percent)+"%"+"\n"+bg.rs+"D:"+bg.blue+fake_d_percent*" "+" "+str(fake_d_percent)+"%"+"\n"+bg.rs)
                time.sleep(1)
                os.system('clear')
                sys.stdout.write("\033[F")
            elems = [a_percent, b_percent, c_percent, d_percent]
            max_element = max(elems[0], elems[1], elems[2], elems[3])
            a__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  A: {bg.rs+bg.blue+a_percent*" "+bg.black+fg.rs+str(a_percent)}%')
            b__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  B: {bg.rs+bg.blue+b_percent*" "+bg.black+fg.rs+str(b_percent)}%')
            c__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  C: {bg.rs+bg.blue+c_percent*" "+bg.black+fg.rs+str(c_percent)}%')
            d__ = (f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  D: {bg.rs+bg.blue+d_percent*" "+bg.black+fg.rs+str(d_percent)}%')
            print((table_line_length+1)*" " + bg.black + (max_element+11)*"-" + bg.rs)
            print(a__+(((max_element)-a_percent)+3)*" "+"|"+bg.rs)
            time.sleep(1)
            print(b__+(((max_element)-b_percent)+2)*" "+"|"+bg.rs)
            time.sleep(1)
            print(c__+(((max_element)-c_percent)+2)*" "+"|"+bg.rs)
            time.sleep(1)
            print(d__+(((max_element)-d_percent)+3)*" "+"|"+bg.rs)
            print((table_line_length+1)*" "+bg.black+(max_element+11)*"-" + bg.rs)


def telefonálgatós_függvény(text, question, good_answer):
    play_sound("./msc/telhiv.mp3", 0)
    time.sleep(2)
    play_sound("./msc/telefon.mp3", 0)
    then = time.time() 
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    time.sleep(2)
    print(text[0])
    print("\n"+''.join(question))
    print(text[1])
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    time.sleep(2)
    print(text[2])
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    time.sleep(2)
    print(fg.red+text[3]+fg.rs)
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    time.sleep(2)
    print(text[4] + good_answer+"\n")
    if text[4] == "The Force says ":
        print(text[5])
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    now = time.time()
    #play_sound('telefon.mp3', 54.0)
    time.sleep(1)
    print("Call Duration: ", int(now-then), " seconds\\ 30 a")

def telephone_help(question, current_line):

    phone = safe_input("Who'd you like to call?\nfor mum, press 'm'\nfor dad press 'd'\nfor old teacher from high school press 't'\nfor Maester Yoda press 'y': ", ["m","d","t","y"])
    if phone.lower() == 'm':
        text=["Hi mummy, I'm playing the Millionaire..\nHere's the question.. ",
        "Hi Honey.. I don't know the answer i'll ask your dad",
        "..Dad!..Daddy!..Our son is in the Millionaire Show!! Can you believe??",
        "Mum please my time is almost up!!",
        "Okay honey, it is D.. No, no wait, it is "]
        telefonálgatós_függvény(text, question, current_line[0])
    
    if phone.lower() == 'd':
        text=["Hi dad, I'm playing the Millionaire..\nHere's the question..  ",
        "Hi Son.. I don't know the answer i'll ask your grandfather",
        "..Dad!..Daddy!..Your grandson is in the Millionaire Show!! Can you believe??",
        "Dad please my time is almost up!!",
        "Okay Son, he says it is A.. No, no wait, it is "]
        telefonálgatós_függvény(text, question, current_line[0])
    
    if phone.lower() == 't':
        text=["Great day Mr Teacher I am your former student, and I'm playing the Millionaire..\nHere's the question.. ",
        "Welcome.. I'd never thought after so many years you'd call me!",
        "I have to tell the principle..Mr!..Mr Principle!..One of your former student is in the Millionaire Show!! Can you believe??",
        "Sir please my time is almost up!!",
        "Okay boy, he says it is A.. No, no wait, it is "]
        telefonálgatós_függvény(text, question, current_line[0])
    
    if phone.lower() == 'y':
        text=["Hi Maester Yoda! I'm the young padavan You have raised many years ago..\nI need your force of knowledge because I'm playing the Millionaire..Here's the question..",
        "May the force be with you, my son.",
        "I call the Force for help!",
        "*background* Hi Leila I'm Yoda please help this is the question..",
        "The Force says ",
        "And never forget: Do or don't but never try!"]
        telefonálgatós_függvény(text, question, current_line[0])
       

def halving(vago_feje_sorai, table_line_length, question, shuffled_line, choises, current_line, a, b, c, d):
    os.system('clear')
    time.sleep(2)
    play_sound("./msc/felezo.mp3", 0)
    vago_feje_sorai = open_drawing('vago.txt', 'r')
    possibilities = []
    for shuffled_element in shuffled_line:
        if shuffled_element == current_line[0]:
            possibilities.append(shuffled_element)
            for index in range(1):
                if shuffled_element == a:
                    possibilities.append(random.choice([b, c, d]))
                elif shuffled_element == b:
                    possibilities.append(random.choice([a, c, d]))
                elif shuffled_element == c:
                    possibilities.append(random.choice([a, b, d]))
                elif shuffled_element == d:
                    possibilities.append(random.choice([a, c, b]))
    if a not in possibilities:
        choises[0] = fg.orange + '◆ A: ' + " "*len(a) + fg.rs
    if b not in possibilities:
        choises[1] = fg.orange + '◆ B: ' + " "*len(b) + fg.rs
    if c not in possibilities:
        choises[2] = fg.orange + '◆ C: ' + " "*len(c) + fg.rs
    if d not in possibilities:
        choises[3] = fg.orange + '◆ D: ' + " "*len(d) + fg.rs


def marking(answer, current_line, a, b, c, d, choises, table_line_length, shuffled_line, question, Help_available, prices, prices1, prices2, counter):
    bg.white = bg(255, 255, 255)
    if answer.lower() == 'a':
        answer = a
        choises[0] = bg.white + fg.blue + choises[0] + fg.rs + bg.black
    if answer.lower() == 'b':
        answer = b
        choises[1] = bg.white + fg.blue + choises[1] + fg.rs + bg.black
    if answer.lower() == 'c':
        answer = c
        choises[2] = bg.white + fg.blue + choises[2] + fg.rs + bg.black
    if answer.lower() == 'd':
        answer = d
        choises[3] = bg.white + fg.blue + choises[3] + fg.rs + bg.black
    os.system('clear')
    print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
    quiz_table(table_line_length, choises, question, shuffled_line)

    play_sound("./msc/marked.mp3", 0)
    time.sleep(4)
    if answer == a:
        if a == current_line[0]:
            choises[0] = bg.green + fg.orange + '◆ A: ' + fg.rs + ''.join(a) + "  " + bg.black
        else:
            choises[0] = bg.red + fg.orange + '◆ A: ' + fg.rs + ''.join(a) + "  " + bg.black
    if answer == b:
        if b == current_line[0]:
            choises[1] = bg.green + fg.orange + '◆ B: ' + fg.rs + ''.join(b) + "  " + bg.black
        else:
            choises[1] = bg.red + fg.orange + '◆ B: ' + fg.rs + ''.join(b) + "  " + bg.black
    if answer == c:
        if c == current_line[0]:
            choises[2] = bg.green + fg.orange + '◆ C: ' + fg.rs + ''.join(c) + "  " + bg.black
        else:
            choises[2] = bg.red + fg.orange + '◆ C: ' + fg.rs + ''.join(c) + "  " + bg.black
    if answer == d:
        if d == current_line[0]:
            choises[3] = bg.green + fg.orange + '◆ D: ' + fg.rs + ''.join(d) + "  " + bg.black
        else:
            choises[3] = bg.red + fg.orange + '◆ D: ' + fg.rs + ''.join(d) + "  " + bg.black
    if answer != current_line[0]:
        for pos in [a, b, c, d]:
            if pos == current_line[0]:
                if pos == a:
                    choises[0] = bg.green + choises[0] + "  " + bg.black
                if pos == b:
                    choises[1] = bg.green + choises[1] + "  " + bg.black
                if pos == c:
                    choises[2] = bg.green + choises[2] + "  " + bg.black
                if pos == d:
                    choises[3] = bg.green + choises[3] + "  " + bg.black
    time.sleep(1)
    os.system('clear')
    print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
    quiz_table(table_line_length, choises, question, shuffled_line)
    check_answer(answer, current_line, a, b, c, d, choises, table_line_length, shuffled_line, question)


def check_answer(answer, current_line, a, b, c, d, choises, table_line_length, shuffled_line, question):
    if answer == current_line[0]:
        play_sound("./msc/jo valasz.mp3", 0)
        fg.green = Style(RgbFg(0, 255, 0))
        print(fg.green + "Well done!" + fg.rs)
        time.sleep(2)
        os.system('clear')
    else:
        play_sound("./msc/rossz valasz.mp3", 0)
        time.sleep(2)
        fg.red = Style(RgbFg(255, 0, 0))
        print(fg.red+answer+"\nBetter luck next time!"+fg.rs)
        sys.exit(0)


def quiz():
    Help_available = []
    Audience = True
    Telephone = True
    Halving = True
    prices = ["5.000 Ft", "10.000 Ft", "25.000 Ft", "50.000 Ft", "100.000 Ft", "200.000 Ft", "300.000 Ft", "500.000 Ft", "800.000 Ft", "1.500.000 Ft", "3.000.000 Ft", "5.000.000 Ft", "10.000.000 Ft", "20.000.000 Ft", "40.000.000 Ft"]
    prices1 = ['40.000.000 Ft', '20.000.000 Ft', '10.000.000 Ft', '5.000.000 Ft', '3.000.000 Ft', '1.500.000 Ft', '800.000 Ft', '500.000 Ft', '300.000 Ft', '200.000 Ft', '100.000 Ft', '50.000 Ft', '25.000 Ft', '10.000 Ft', '5.000 Ft']
    prices2 = ['40.000.000 Ft', '20.000.000 Ft', '10.000.000 Ft', '5.000.000 Ft', '3.000.000 Ft', '1.500.000 Ft', '800.000 Ft', '500.000 Ft', '300.000 Ft', '200.000 Ft', '100.000 Ft', '50.000 Ft', '25.000 Ft', '10.000 Ft', '5.000 Ft']
    question_lines = open_file('questions.txt', "r")
    list_of_answers = open_file('questions.txt', "r")
    # copy_of_list_of_answers  =  copy.deepcopy(list_of_answers)
    starting_range = 0
    ending_range = 4
    # play_sound("lom.mp3",0)
    for i in range(15):
        counter = i
        random_question = []
        random_question = random.choice(list_of_answers[starting_range:ending_range])
        question = random_question[0]
        time.sleep(2)
        os.system('clear')
        current_line = random_question[1:5]
        copy_of_list_of_answers = copy.deepcopy(random_question)
        shuffled_line = copy_of_list_of_answers[1:5]
        random.shuffle(shuffled_line)
        a = shuffled_line[0]
        b = shuffled_line[1]
        c = shuffled_line[2]
        d = shuffled_line[3]
        fg.orange = Style(RgbFg(255, 150, 50))
        first_choice = fg.orange + '◆ A: ' + fg.rs + ''.join(shuffled_line[0]) + "  "
        second_choice = fg.orange + '◆ B: ' + fg.rs + ''.join(shuffled_line[1]) + "  "
        third_choice = fg.orange + '◆ C: ' + fg.rs + ''.join(shuffled_line[2]) + "  "
        fourth_choice = fg.orange + '◆ D: ' + fg.rs + ''.join(shuffled_line[3]) + "  "
        choises = [first_choice, second_choice, third_choice, fourth_choice]
        max_question_length = 0
        answer_lengths = []
        for question_ in question_lines:
            if len(question_) > max_question_length:
                max_question_length = len(question_)
        for answer in list_of_answers:
            for element in answer:
                answer_lengths.append(len(element))
                answer_lengths.sort()
        if answer_lengths[-1]*2 > max_question_length:
            table_line_length = answer_lengths[-1]*2
        else:
            table_line_length = max_question_length
        print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
        quiz_table(table_line_length, choises, question, shuffled_line)
        answer = safe_input("\nSelect the correct answer (a,b,c,d) or 'h' for help! ", ["a", "b", "c", "d", "h", "s"])
        if answer.lower() == 'h':
            vago_feje_sorai = open_drawing('vago.txt', 'r')
            Help_available = help_modules(a, b, c, d, current_line, question, vago_feje_sorai, table_line_length, shuffled_line, choises, Audience, Telephone, Halving, Help_available, prices, prices1, prices2, counter)
            Audience = Help_available[0]
            Telephone = Help_available[1]
            Halving = Help_available[2]
        list_of_are_you_sure_sound_files = ["./msc/vegleges.mp3", "./msc/vegleges2.mp3", "./msc/vegleges3.mp3", "./msc/vegleges4.mp3", "./msc/vegyem_veglegesnek.mp3"]
        are_you_sure_sound = choose_random_from_list(list_of_are_you_sure_sound_files)
        play_sound(are_you_sure_sound, 0)
        time.sleep(1)
        answer = safe_input("Are you sure? ", ["a", "b", "c", "d", "s"])
        if answer.lower() == "s":
            os.system('clear')
            play_sound("./msc/zene_le.mp3", 0)
            print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
            quiz_table(table_line_length, choises, question, shuffled_line)
            answer = safe_input("\nSelect the correct answer (a,b,c,d)! ", ["a", "b", "c", "d"])
            marking(answer, current_line, a, b, c, d, choises, table_line_length, shuffled_line, question, Help_available, prices, prices1, prices2, counter)
            os.system('clear')
            print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
            print("  "+bg.black+"/"+"‾"*(table_line_length-6)+"\\"+bg.rs)
            width = table_line_length
            if i == 0:
                won_prize = "0 Ft."
                len_table = len("‾"*(table_line_length-6-len(won_prize)))
            else:
                won_prize = prices[i-1]
                len_table = len("‾"*(table_line_length-len(prices2[i-1])))
            print("-"+bg.black+"‹"+fg.orange+''.join(won_prize.center((width-4), ' '))+fg.rs+"›"+bg.rs+"-")
            print("  "+bg.black+"\\"+"_"*(table_line_length-6)+"/"+bg.rs)
            time.sleep(3)
            sys.exit(0)
        marking(answer, current_line, a, b, c, d, choises, table_line_length, shuffled_line, question, Help_available, prices, prices1, prices2, counter)
        won_prize = prices[i]
        if i == 4:
            won_prize = "You have guaranteed 100.000 Ft"
            time.sleep(1)
        elif i == 9:
            won_prize = "You have guaranteed 1.500.000 Ft"
            time.sleep(1)
        elif i == 14:
            won_prize = fg.orange + "Congratulations!\nYou've just won the unbelivable 40.000.000 Ft\n"+fg.purple+"You became the new Millionaire!!!" + fg.rs
            print(won_prize)
            time.sleep(3)
            sys.exit(0)
        print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
        print("  "+bg.black+"/"+"‾"*(table_line_length-6)+"\\"+bg.rs)
        width = table_line_length
        len_table = len("‾"*(table_line_length-6-len(won_prize)))
        print("-" + bg.black+"‹" + fg.orange + ''.join(won_prize).center((width-4), ' ') + fg.rs + "›" + bg.rs + "-")
        print("  "+bg.black+"\\"+"_"*(table_line_length-6)+"/"+bg.rs)
        starting_range = ending_range + 1
        ending_range = starting_range + 4
        time.sleep(1)


def main():
    game_start()
    quiz()


if __name__ == "__main__":
    main()
