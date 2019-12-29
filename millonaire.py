import random
import copy
import sys
import os
from sty import Style, RgbFg, fg, rs
import time
from playsound import playsound
import pygame



def game_start():
    fg.purple = Style(RgbFg(148, 0, 211))
    pygame.mixer.init()
    play_sound("loim_intro.wav")
    os.system('clear')
    print(pygame.mixer.Sound("loim_intro.wav").get_volume())
    time.sleep(2)
    sound=pygame.mixer.Sound("loim_intro.wav")
    time.sleep(2)
    print(pygame.mixer.Sound("loim_intro.wav").get_volume())
    print("This is the game of games..\nIn the arena..\nMr Steven Vágó is awating You!\n"+fg.purple+"Become the next Millionaire!\n"+fg.rs)

def play_sound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0.07)
    pygame.mixer.music.play()

def open_file(filename, mode):
    with open(filename, mode) as file:
        list_of_file=[]
        for line in file:
            line = line.strip().split(',')
            list_of_file.append(line)
    return list_of_file

def open_drawing(filename, mode):
    with open(filename, mode) as file:
        list_of_file=[]
        for line in file:
            line = line.split(',')
            list_of_file.append(line)
    return list_of_file

def quiz_table(table_line_length,first_choice,second_choice,third_choice,fourth_choice,shuffled_line,question_lines,i):
    print(" "+"-"*(table_line_length))
    width = table_line_length
    print(" "+', '.join(question_lines[i]).center(width,'-'))
    print(" |"+ first_choice + (" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+9))) + second_choice + " |")
    print(" |"+ third_choice + (" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+9)))+fourth_choice + " |")
    print(" "+"-"*table_line_length)

def help_modules(a,b,c,d,current_line,question_lines,i,vago_feje_sorai,table_line_length,shuffled_line,first_choice,second_choice,third_choice,fourth_choice):
    help_=input("For Audience's help, type 'a'\nFor Telephone help type 't'\nFor halving type 'h': ")
    if help_.lower()=="a":
        audience_help(a,b,c,d,current_line,question_lines)
    if help_.lower()=="t":
        telephone_help(question_lines,current_line,i)
    if help_.lower()=="h":
        halving(vago_feje_sorai,table_line_length,question_lines,i,shuffled_line,first_choice,second_choice,third_choice,fourth_choice,current_line,a,b,c,d)
    answer = input("Select the correct answer(a,b,c,d): \n(In case you need help type 'h')")


def audience_help(a,b,c,d,current_line,question_lines):
    play_sound("kozonseg.wav")
    for choise in [a,b,c,d]:
        if choise ==current_line[0]:
            if choise==a:
                a_percent=random.randrange(40,89)
                b_percent=random.randrange(0,(100-a_percent))
                c_percent=random.randrange(0,(100-a_percent-b_percent))
                d_percent=100-(a_percent+b_percent+c_percent)
            if choise==b:
                b_percent=random.randrange(40,89)
                a_percent=random.randrange(0,(100-b_percent))
                c_percent=random.randrange(0,(100-b_percent-a_percent))
                d_percent=100-(a_percent+b_percent+c_percent)
            if choise==c:
                c_percent=random.randrange(40,89)
                b_percent=random.randrange(0,(100-c_percent))
                a_percent=random.randrange(0,(100-c_percent-b_percent))
                d_percent=100-(a_percent+b_percent+c_percent)
            if choise==d:
                d_percent=random.randrange(40,89)
                b_percent=random.randrange(0,(100-d_percent))
                c_percent=random.randrange(0,(100-d_percent-b_percent))
                a_percent=100-(d_percent+b_percent+c_percent)
            if a_percent+b_percent+c_percent+d_percent != 100:
                print(" AUDIENCE HELP IS BROKEN!!!")
                break
            print(f'A: {a_percent}%')
            time.sleep(1)
            print(f'B: {b_percent}%')
            time.sleep(1)
            print(f'C: {c_percent}%')
            time.sleep(1)
            print(f'D: {d_percent}%')
            pygame.mixer.fadeout(2)    
def telephone_help(question_lines,current_line,i):
    phone=input("Who'd you like to call?\nfor mum, press 'm'\nfor dad press 'd'\nfor old teacher from high school press 't'\nfor Maester Yoda press 'y': ")
    if phone.lower()=='m':
        play_sound("telhiv.wav")
        play_sound("telefon.wav")
        then = time.time()
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        print("Hi mummy, I'm playing the Millionaire..Here's the question.. \n"+', '.join(question_lines[i]))
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("Hi Honey.. I don't know the answer i'll ask your dad")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("..Dad!..Daddy!..Our son is in the Millionaire Show!! Can you believe??")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print(fg.red+"Mum please my time is almost up!!"+fg.rs)
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("Okay honey, it is D.. No, no wait, it is " + current_line[0])
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        now = time.time()
        pygame.mixer.fadeout(2)
        print("Call Duration: ", int(now-then), " seconds\ 30 seconds")
    if phone.lower()=='d':
        play_sound("telhiv.wav")
        play_sound("telefon.wav")
        then = time.time()
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        print("Hi dad, I'm playing the Millionaire..Here's the question.. \n"', '.join(question_lines[i]))
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("Hi Son.. I don't know the answer i'll ask your grandfather")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("..Dad!..Daddy!..Your grandson is in the Millionaire Show!! Can you believe??")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print(fg.red+"Dad please my time is almost up!!"+fg.rs)
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("Okay Son, he says it is A.. No, no wait, it is " + current_line[0])
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        now = time.time()
        pygame.mixer.fadeout(2)
        print("Call Duration: ", int(now-then), " seconds\ 30 seconds")
    if phone.lower()=='t':
        play_sound("telhiv.wav")
        play_sound("telefon.wav")
        then = time.time()
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        print("Great day Mr Teacher I am your former student, and I'm playing the Millionaire..Here's the question..\n"', '.join(question_lines[i]))
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("Welcome.. I'd never thought after so many years you'd call me!")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("I have to tell the principle..Mr!..Mr Principle!..One of your former student is in the Millionaire Show!! Can you believe??")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print(fg.red+"Sir please my time is almost up!!"+fg.rs)
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("Okay boy, he says it is A.. No, no wait, it is " + current_line[0])
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        now = time.time()
        pygame.mixer.fadeout(2)
        print("Call Duration: ", int(now-then), " seconds\ 30 seconds")
    if phone.lower()=='y':
        play_sound("telhiv.wav")
        play_sound("telefon.wav")
        then = time.time()
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        #Time after it finished
        print("May the force be with you, my son. How can I help u?")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("Hi Yoda, I need your force of knowledge because I'm playing the Millionaire..Here's the question..\n"', '.join(question_lines[i]))
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("I call the Force for help")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("*background* Hi Leila I'm Yoda please help this is the question..")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        time.sleep(2)
        print("The Force says "+ current_line[0] +"\nNever forget, do or don't but never try!")
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        now = time.time()
        pygame.mixer.fadeout(2)
        print("Call Duration: ", int(now-then), " seconds\ 30 seconds max.")
def halving(vago_feje_sorai,table_line_length,question_lines,i,shuffled_line,first_choice,second_choice,third_choice,fourth_choice,current_line,a,b,c,d):
    os.system('clear')
    time.sleep(2)
    play_sound("felezo.wav")
    vago_feje_sorai = open_drawing('vago.txt', 'r')
    for head_lines in vago_feje_sorai:
        print(''.join(head_lines).rstrip())
    print(" "+"-"*(table_line_length))
    width = table_line_length
    print(" "+', '.join(question_lines[i]).center(width,'-'))
    possibilities=[]
    for shuffled_element in shuffled_line:
        if shuffled_element == current_line[0]:
            possibilities.append(shuffled_element)
            for index in range(1):
                if shuffled_element==a:
                    possibilities.append(random.choice([b,c,d]))
                elif shuffled_element==b:
                    possibilities.append(random.choice([a,c,d]))
                elif shuffled_element==c:
                    possibilities.append(random.choice([a,b,d]))
                elif shuffled_element==d:
                    possibilities.append(random.choice([a,c,b]))
    if a not in possibilities:
        first_choice=fg.orange + 'A: ' +" "*len(a)+ fg.rs
    if b not in possibilities:
        second_choice=fg.orange + 'B: ' +" "*len(b)+ fg.rs
    if c not in possibilities:
        third_choice=fg.orange + 'C: '+" "*len(c) + fg.rs
    if d not in possibilities:       
        fourth_choice=fg.orange + 'D: ' +" "*len(d)+ fg.rs
    print(" |"+ first_choice + (" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+9))) + second_choice + " |")
    print(" |"+ third_choice + (" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+9)))+fourth_choice + " |")
    print(" "+"-"*table_line_length)          
    
def check_answer(answer,current_line,a,b,c,d):
    if answer.lower()=='a':
        answer = a
    if answer.lower()=='b':
        answer = b
    if answer.lower()== 'c':
        answer = c
    if answer.lower()== 'd':
        answer = d
    if answer == current_line[0]:
        play_sound("jo valasz.wav")
        fg.green = Style(RgbFg(0, 255, 0))
        print(fg.green + "Well done!" + fg.rs)
        time.sleep(2)
        os.system('clear')
    else:
        play_sound("rossz valasz.wav")
        time.sleep(2)
        fg.red = Style(RgbFg(255, 0, 0))
        print(fg.red+answer+"\nBetter luck next time!"+fg.rs)
        sys.exit(0)

def quiz():
    counter = 0
    question_lines=open_file('questions.txt', "r")
    list_of_answers=open_file('answers.txt', "r")
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
        first_choice =fg.orange + 'A: ' + fg.rs + ''.join(shuffled_line[0])
        second_choice =fg.orange + 'B: ' + fg.rs + ''.join(shuffled_line[1])
        third_choice =fg.orange + 'C: ' + fg.rs + ''.join(shuffled_line[2])
        fourth_choice = fg.orange + 'D: ' + fg.rs + ''.join(shuffled_line[3])
        max_question_length=0
        answer_lengths=[]
        for question in question_lines:
            if len(question)>max_question_length:
                max_question_length=len(question)
        for answer in list_of_answers:
            for element in answer:
                answer_lengths.append(len(element))
                answer_lengths.sort()
        if answer_lengths[-1]*2>max_question_length:
            table_line_length=answer_lengths[-1]*2
        else: 
            table_line_length=max_question_length
        vago_feje_sorai = open_drawing('vago.txt', 'r')
        for head_lines in vago_feje_sorai:
            print(''.join(head_lines).rstrip())
        quiz_table(table_line_length,first_choice,second_choice,third_choice,fourth_choice,shuffled_line,question_lines,i)        
        counter += 1
        answer = input("Select the correct answer(a,b,c,d): \n(In case you need help type 'h')")
        if answer.lower()=='h':
            vago_feje_sorai = open_drawing('vago.txt', 'r')
            help_modules(a,b,c,d,current_line,question_lines,i,vago_feje_sorai,table_line_length,shuffled_line,first_choice,second_choice,third_choice,fourth_choice)
        answer = input("Are you sure?")
        check_answer(answer,current_line,a,b,c,d)
        if counter == 5:
            print(fg.orange + "You have guaranteed 100.000 Ft" + fg.rs)
        if counter == 10:
            print(fg.orange + "You have guaranteed 1.500.000 Ft" + fg.rs)
        if counter == 15:
            print(fg.orange + "Congratulations!\nYou've just won the unbelivable 40.000.000 Ft\n"+fg.purple+"You became the new Millionaire!!!" + fg.rs)
            sys.exit(0) 


def main():
    game_start()
    quiz()


if __name__ == "__main__":
    main()