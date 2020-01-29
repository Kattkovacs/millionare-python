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
        print("Error! Only letters: " + ' '.join(allowed_list_of_letters) + " allowed!")
        answer = input("Select the correct answer!")
    return answer


def choose_random_from_list(list_):

    return random.choice(list_)

def audience_help(answers, current_line, question, table_line_length, choises, shuffled_line):
    
    play_sound("./msc/kozonseg.mp3", 0)
    for choise in [answers]:
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
            time.sleep(4)
            os.system('clear')
            for choise_ in [answers]:
                if choise == current_line[0]:
                    if choise_ == a:
                        fake_a_percent = random.randrange(40, 89)
                        fake_b_percent = random.randrange(0, (100 - fake_a_percent))
                        fake_c_percent = random.randrange(0, (100 - fake_a_percent-fake_b_percent))
                        fake_d_percent = 100-(fake_a_percent + fake_b_percent + fake_c_percent)
                    if choise_ == b:
                        fake_b_percent = random.randrange(40, 89)
                        fake_a_percent = random.randrange(0, (100 - fake_b_percent))
                        fake_c_percent = random.randrange(0, (100 - fake_b_percent-fake_a_percent))
                        fake_d_percent = 100 - (fake_a_percent+fake_b_percent + fake_c_percent)
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
                time.sleep(4)
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


def quiz_table(table_line_length, choises, question, shuffled_line):

    lengths = []
    choice_length = []
    for i in range(4):
        lengths.append((len(choises[i].letter)+len(choises[i].answer)+len(choises[i].mark)+len(choises[i].f_end)+len(choises[i].s_end)))
        choice_length.append(len(choises[i].letter)+len(choises[i].answer)+len(choises[i].mark)+len(choises[i].quote))
    spaces_ = table_line_length-(lengths[0]+lengths[1]+4)
    spaces__ = table_line_length-(lengths[2]+lengths[3]+4)
    answer_line_length = table_line_length-4
    print("   "+choises[0].slash+bg.black+answer_line_length*"‾"+bg.rs+choises[0].slash_)
    print("  "+choises[0].slash+bg.black+(table_line_length-2)*" "+bg.rs+choises[0].slash_)
    print(" -◀"+bg.black+choises[0].slash_+bg.black+''.join(question).center((answer_line_length), ' ')+choises[0].slash+bg.rs+"▶-")
    print("  "+choises[0].slash+bg.black+(table_line_length-3)*" "+choises[0].slash+bg.rs)
    print("   "+choises[0].slash+bg.black+answer_line_length*"_"+bg.rs+choises[0].slash_)
    print("    "+choice_length[0]*"_"+(spaces_+2)*" "+choice_length[1]*"_")
    print("  "+choises[0].line+choises[0].f_end+choises[0].firstpart+choises[0].mark+choises[0].additional+choises[0].quote+choises[0].letter+choises[0].secondpart+choises[0].answer+choises[0].thirdpart+choises[0].s_end+spaces_*"-"+choises[1].f_end+choises[1].firstpart+choises[1].mark+choises[1].additional+choises[1].quote+choises[1].letter+choises[1].secondpart+choises[1].answer+choises[1].thirdpart+choises[1].s_end+choises[2].line)
    print("    "+choice_length[0]*"‾"+(spaces_+2)*" "+choice_length[1]*"‾")
    print("    "+choice_length[2]*"_"+(spaces__+2)*" "+choice_length[3]*"_")
    print("  "+choises[2].line+choises[2].f_end+choises[2].firstpart+choises[2].mark+choises[2].additional+choises[2].quote+choises[2].letter+choises[2].secondpart+choises[2].answer+choises[2].thirdpart+choises[2].s_end+spaces__*"-"+choises[3].f_end+choises[3].firstpart+choises[3].mark+choises[3].additional+choises[3].quote+choises[3].letter+choises[3].secondpart+choises[3].answer+choises[3].thirdpart+choises[3].s_end+choises[3].line)
    print("    "+choice_length[2]*"‾"+(spaces__+2)*" "+choice_length[3]*"‾")


def print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter, head='vago.txt'):
   
    vago_feje_sorai = open_drawing(head, 'r')
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
    print((80*" ")+bg.black+(len(prices[-1])+2)*"-".rstrip() + bg.rs)
    print((80*" ")+bg.black+"|"+" "+Halv+"∥"+Tel+"∥"+Aud+(len(prices[-1])-(len(Halv)+len(Tel)+len(Aud)+4))*" "+bg.black+"|"+bg.rs)
    print((80*" ")+bg.black+(len(prices[-1])+2)*"-"+bg.rs)
    print((80*" ")+bg.black+(len(prices[-1])+2)*"-"+bg.rs)
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
    print(''.join(vago_feje_sorai[15]).rstrip()+31*" "+bg.black+(len(prices[:-1])+1)*"-"+bg.rs)
    for art in range(16, 20):
        print(''.join(vago_feje_sorai[art]).rstrip())


def help_modules(answers, current_line, question, table_line_length, shuffled_line, choises, Help_available, prices, prices1, prices2, counter):
    
    help_ = safe_input(": ", ["a","t","h"])
    if help_.lower() == "a":
        if Help_available[0]:
            audience_help(answers, current_line, question, table_line_length, choises, shuffled_line)
            Help_available[0] = False
            print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
            quiz_table(table_line_length, choises, question, shuffled_line)
        else:
            print("You have already used the audience's help!")

    if help_.lower() == "t":
        if Help_available[1]:
            telephone_help(question, current_line)
            Help_available[1] = False
        else:
            print("You have already used the telephone help!")

    if help_.lower() == "h":
        if Help_available[2]:
            halving(table_line_length, question, shuffled_line, choises, current_line, answers)
            Help_available[2] = False
            print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter, 'vago_helping.txt')
            quiz_table(table_line_length, choises, question, shuffled_line)
        else:
            print("You have already used the halving help!")
    return Help_available


def give_audience_choises():
   
    percents = []
    percents.append(random.randrange(40, 89))
    percents.append(random.randrange(0, 100-percents[0]))
    percents.append(random.randrange(0, 100-percents[0]-percents[1]))
    percents.append(100-(percents[0]+percents[1]+percents[2]))
    if percents[0]+percents[1]+percents[2]+percents[3] != 100:
        print(" AUDIENCE HELP IS BROKEN!!!")
    return percents


def audience_help(answers, current_line, question, table_line_length, choises, shuffled_line):
    
    os.system('clear')
    betuk = ["A: ", "B: ", "C: ", "D: "]
    percents_list = give_audience_choises()
    for i in range(len(shuffled_line)):
        if shuffled_line[i] == current_line[0]:
            first_ = bg.black+betuk[i]+str(percents_list[0])+"%"+bg.rs
            del betuk[i]
    second_ = bg.black+betuk[0]+str(percents_list[1])+"%"+bg.rs
    third_ = bg.black+betuk[1]+str(percents_list[2])+"%"+bg.rs
    fourth_ = bg.black+betuk[2]+str(percents_list[3])+"%"+bg.rs
    for s in ["A", "B", "C", "D"]:
        for i in [first_, second_, third_, fourth_]:
            if s in i:
                print(i)


def print_phone_conversation(text, question, good_answer):
    
    play_sound("./msc/telhiv.mp3", 0)
    time.sleep(2)
    play_sound("./msc/telefon.mp3", 0)
    then = time.time() 
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    time.sleep(2)
    print(''.join(text[0]))
    print("\n"+''.join(question))
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    time.sleep(2)
    print(''.join(text[1]))
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    time.sleep(2)
    print(fg.red+''.join(text[2])+fg.rs)
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    time.sleep(2)
    print(''.join(text[3]))
    if text[2][0] == 'I call the Force for help!':
        print(''.join(text[4]))
        print(good_answer+"\n")
        print(''.join(text[5]))
    else:
        print(''.join(text[4]))
        print(good_answer+"\n")
    print(fg.orange+str(30-int(time.time()-then))+fg.rs)
    now = time.time()
    # play_sound('telefon.mp3', 54.0)
    time.sleep(1)
    print("Call Duration: ", int(now-then), " seconds\\ 30 a")


def telephone_help(question, current_line):
    phone = safe_input("Who'd you like to call?\nfor mum, press 'm'\nfor dad press 'd'\nfor old teacher from high school press 't'\nfor Maester Yoda press 'y': ", ["m", "d", "t", "y"])
    call_list = ['m', 'd', 't', 'y']
    call_files_directory = "./Database/Telephone_conversations/"
    call_text_files = ["mum.txt", "dad.txt", "teacher.txt", "yoda_master.txt"]
    for letter in range(len(call_list)):
        if phone.lower() == call_list[letter]:
            call_text_files[letter] = call_files_directory + call_text_files[letter]
            text = (open_file(call_text_files[letter], 'r'))
            print_phone_conversation(text, question, current_line[0])


def halving(table_line_length, question, shuffled_line, choises, current_line, answers):
    os.system('clear')
    time.sleep(2)
    play_sound("./msc/felezo.mp3", 0)
    possibilities = []
    for shuffled_element in shuffled_line:
        if shuffled_element == current_line[0]:
            possibilities.append(shuffled_element)
            for index in range(1):
                if shuffled_element == answers[0]:
                    possibilities.append(random.choice([answers[1], answers[2], answers[3]]))
                elif shuffled_element == answers[1]:
                    possibilities.append(random.choice([answers[0], answers[2], answers[3]]))
                elif shuffled_element == answers[2]:
                    possibilities.append(random.choice([answers[0], answers[1], answers[3]]))
                elif shuffled_element == answers[3]:
                    possibilities.append(random.choice([answers[0], answers[1], answers[2]]))
    if answers[0] not in possibilities:
        choises[0].answer =" "*(len(choises[0].answer)-1)+"▕"
    if answers[1] not in possibilities:
        choises[1].answer = " "*(len(choises[1].answer)-1)+"▕"
    if answers[2] not in possibilities:
        choises[2].answer = " "*(len(choises[2].answer)-1)+"▕"
    if answers[3] not in possibilities:
        choises[3].answer = " "*(len(choises[3].answer)-1)+"▕"


def marking(Choise, answer, current_line, answers, choises, table_line_length, shuffled_line, question, Help_available, prices, prices1, prices2, counter):
    letterses = ['a', 'b', 'c', 'd']
    abcd = [' A: ', ' B: ', ' C: ', ' D: ']
    for letters_ in range(len(letterses)):
        if answer.lower() == letterses[letters_]:
            answer = answers[letters_]
            choises[letters_] = Choise(abcd[letters_], shuffled_line[letters_], '\x1b[48;2;255;150;50m', '\x1b[39m', '\x1b[49m', '\x1b[30m')

    return choises, answer


def check_answer(answer, Choise, current_line, answers, choises, table_line_length, shuffled_line, question):
    betuk = [' A: ', ' B: ', ' C: ', ' D: ']
    for pos in range(len(answers)):
        if shuffled_line[pos] == current_line[0]:
            index = shuffled_line.index(shuffled_line[pos])
    if answer == current_line[0]:
        choises[index] = Choise(betuk[index], shuffled_line[index], '\x1b[42m', '\x1b[39m', '\x1b[49m', '\x1b[30m')
        fg.green = Style(RgbFg(0, 255, 0))
        time.sleep(2)
        os.system('clear')
        play_sound("./msc/jo valasz.mp3", 0)
        print(fg.green + "Well done!" + fg.rs)
    else:
        play_sound("./msc/rossz valasz.mp3", 0)
        time.sleep(2)
        fg.red = Style(RgbFg(255, 0, 0))
        print(fg.red+answer+"\nBetter luck next time!"+fg.rs)
        ask = safe_input("Would you like to play again? ('y'/'n')", ['y'])
        if ask == 'y':
            game_start()
            quiz()
        else:
            sys.exit(0)

    return choises


def calculate_quiz_table_size(question_lines, list_of_answers):
    max_question_length = 0
    answer_lengths = []
    for question_ in range(len(question_lines)):
        if len(question_lines[question_][0]) > max_question_length:
            max_question_length = len(question_lines[question_][0])
    for answer in list_of_answers:
        for element in answer:
            if element != answer[0]:
                answer_lengths.append(len(element))
                answer_lengths.sort()
    if answer_lengths[-1]*2 > max_question_length:
        table_line_length = answer_lengths[-1]*2
    else:
        table_line_length = max_question_length

    return table_line_length


def stop_game_and_guess_out_of_game(answer, Help_available, table_line_length, prices, prices1, prices2, counter, current_line, answers, choises, shuffled_line, question):
    if answer.lower() == "s":
        os.system('clear')
        play_sound("./msc/zene_le.mp3", 0)
        print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
        quiz_table(table_line_length, choises, question, shuffled_line)
        answer = safe_input("\nSelect the correct answer (a,b,c,d)! ", ["a", "b", "c", "d"])
        marking(Choise,answer, current_line, answers, choises, table_line_length, shuffled_line, question, Help_available, prices, prices1, prices2, counter)
        os.system('clear')
        print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
        print("  "+bg.black+"/"+"‾"*(table_line_length-6)+"\\"+bg.rs)
        width = table_line_length
        if counter == 0:
            won_prize = "0 Ft."
            len_table = len("‾"*(table_line_length-6-len(won_prize)))
        else:
            won_prize = prices[counter-1]
            len_table = len("‾"*(table_line_length-len(prices2[counter-1])))
        print("-"+bg.black+"‹"+fg.orange+''.join(won_prize.center((width-4), ' '))+fg.rs+"›"+bg.rs+"-")
        print("  "+bg.black+"\\"+"_"*(table_line_length-6)+"/"+bg.rs)
        time.sleep(3)
        sys.exit(0)


def pressed_h_key(answer, answers, current_line, question, table_line_length, shuffled_line, choises, Help_available, prices, prices1, prices2, counter):
    if answer.lower() == 'h':
            os.system('clear')
            print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter, head='vago_helping.txt')
            quiz_table(table_line_length, choises, question, shuffled_line)
            Help_available = help_modules(answers, current_line, question, table_line_length, shuffled_line, choises, Help_available, prices, prices1, prices2, counter)
            Audience = Help_available[0]
            Telephone = Help_available[1]
            Halving = Help_available[2]


def quiz():
    Help_available = [True, True, True]
    prices = ["5.000 Ft", "10.000 Ft", "25.000 Ft", "50.000 Ft", "100.000 Ft", "200.000 Ft", "300.000 Ft", "500.000 Ft", "800.000 Ft", "1.500.000 Ft", "3.000.000 Ft", "5.000.000 Ft", "10.000.000 Ft", "20.000.000 Ft", "40.000.000 Ft"]
    prices1 = ['40.000.000 Ft', '20.000.000 Ft', '10.000.000 Ft', '5.000.000 Ft', '3.000.000 Ft', '1.500.000 Ft', '800.000 Ft', '500.000 Ft', '300.000 Ft', '200.000 Ft', '100.000 Ft', '50.000 Ft', '25.000 Ft', '10.000 Ft', '5.000 Ft']
    prices2 = ['40.000.000 Ft', '20.000.000 Ft', '10.000.000 Ft', '5.000.000 Ft', '3.000.000 Ft', '1.500.000 Ft', '800.000 Ft', '500.000 Ft', '300.000 Ft', '200.000 Ft', '100.000 Ft', '50.000 Ft', '25.000 Ft', '10.000 Ft', '5.000 Ft']
    question_lines = open_file('questions.txt', "r")
    list_of_answers = open_file('questions.txt', "r")
    starting_range = 0
    ending_range = 4

    class Choise():
        def __init__(self, letter, answer, firstpart, secondpart, thirdpart, additional):
            self.additional = additional
            self.mark = "▏"
            self.quote = "◆"
            self.letter = letter
            self.answer = answer + "     " + "▕"
            self.firstpart = firstpart
            self.secondpart = secondpart
            self.thirdpart = thirdpart
            self.f_end = "◀"
            self.s_end = "▶"
            self.line = "-"
            self.slash = "▕"
            self.slash_ = "▏"

    letters_ = [" A: ", " B: ", " C: ", " D: "]
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
        choises = [' ', ' ', ' ', ' ']
        for letter_ in range(len(letters_)):

            choises[letter_] = Choise(letters_[letter_],shuffled_line[letter_],'\x1b[40m','\x1b[39m','\x1b[49m','\x1b[38;2;255;150;50m')
        answers = [a, b, c, d]
        fg.orange = Style(RgbFg(255, 150, 50))
        table_line_length = calculate_quiz_table_size(question_lines,list_of_answers)
        print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
        quiz_table(table_line_length, choises, question, shuffled_line)
        answer = safe_input("\nSelect the correct answer (a,b,c,d) or 'h' for help! ", ["a", "b", "c", "d", "h", "s"])
        pressed_h_key(answer,answers, current_line, question, table_line_length, shuffled_line, choises, Help_available, prices, prices1, prices2, counter)
        list_of_are_you_sure_sound_files = ["./msc/vegleges.mp3", "./msc/vegleges2.mp3", "./msc/vegleges3.mp3", "./msc/vegleges4.mp3", "./msc/vegyem_veglegesnek.mp3"]
        are_you_sure_sound = choose_random_from_list(list_of_are_you_sure_sound_files)
        play_sound(are_you_sure_sound, 0)
        time.sleep(1)
        answer = safe_input("Are you sure? ", ["a", "b", "c", "d", "s"])
        stop_game_and_guess_out_of_game(answer, Help_available, table_line_length, prices, prices1, prices2, counter,current_line, answers, choises, shuffled_line, question)
        answer=marking(Choise,answer, current_line, answers, choises, table_line_length, shuffled_line, question, Help_available, prices, prices1, prices2, counter)[1]
        os.system('clear')
        print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
        quiz_table(table_line_length, choises, question, shuffled_line)
        play_sound("./msc/marked.mp3", 0)
        time.sleep(4)
        #check_answer(answer, Choise, current_line, answers, choises, table_line_length, shuffled_line, question)
        choises=check_answer(answer, Choise, current_line, answers, choises, table_line_length, shuffled_line, question)
        print_quizmaster_with_prices_table(Help_available, table_line_length, prices, prices1, prices2, counter)
        quiz_table(table_line_length, choises, question, shuffled_line)
        time.sleep(2)
        os.system('clear')
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
    #game_start()
    quiz()


if __name__ == "__main__":
    main()
