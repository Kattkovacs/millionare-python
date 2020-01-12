import random
import copy
import sys
import os
from sty import Style, RgbFg, fg, rs, bg
import time
from playsound import playsound
import pygame
""" from PIL import Image
 """


def game_start():
    fg.purple = Style(RgbFg(148, 0, 211))
    pygame.mixer.init()
    os.system('clear')
    play_sound("loim_intro.wav",0)
    time.sleep(2)
    print("This is the game of games..\nIn the arena..\nMr Steven Vágó is awaiting You!\n"+fg.purple+"Become the next Millionaire!\n"+fg.rs)
    milliomos_kép()
    time.sleep(5)

def milliomos_kép():
    width, height = 22, 22
    a, b = 10, 10
    r = 10
    EPSILON = 4.4
    bg.purple = bg(148, 0, 211)

    map_= [[' ' for x in range(width)]for y in range(height)]

    for y in range(height):
        for x in range(width):
            if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:
                map_[y][x] = bg.purple+" "+bg.rs                    
    for line in range(len(map_)):
        if line==2:
            for i in range(5,15):
                map_[line][i]==""
            map_[line].insert(5,"Who wants to be a")
            
        print("      " + ' '.join(map_[line]))
        

def play_sound(filename,starting_time):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0.07)
    pygame.mixer.music.play(0,starting_time)

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
""" 
def price_table(counter,prices,vago_feje_sorai,sor):
    for kor in range(len(prices)):
        print(prices[sor]) """

def quiz_table(table_line_length,first_choice,second_choice,third_choice,fourth_choice,shuffled_line,question_lines,i):
    print(bg.black+" "+"-"*(table_line_length)+bg.rs)
    width = table_line_length
    print(bg.black+" "+', '.join(question_lines[i]).center(width,'-')+bg.rs)
    print(bg.black+" |"+ first_choice + (" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+13))) + second_choice + " |"+bg.rs)
    print(bg.black+" |"+ third_choice + (" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+13)))+fourth_choice + " |"+bg.rs)
    print(bg.black+" "+"-"*table_line_length+bg.rs)

def help_modules(a,b,c,d,current_line,question_lines,i,vago_feje_sorai,table_line_length,shuffled_line,first_choice,second_choice,third_choice,fourth_choice,Audience,Telephone,Halving):
    help_=input("For Audience's help, type 'a'\nFor Telephone help type 't'\nFor halving type 'h': ")        
    if help_.lower()=="a":
        if Audience==False:
            print("You have already used the audience help!")
        else:    
            audience_help(a,b,c,d,current_line,question_lines)
            Audience=False
    if help_.lower()=="t":
        if Telephone==False:
            print("You have already used the telephone help!")
        else:
            telephone_help(question_lines,current_line,i)
            Telephone=False
    if help_.lower()=="h":
        if Halving==False:
            print("You have already used the halving help!")
        else:
            halving(vago_feje_sorai,table_line_length,question_lines,i,shuffled_line,first_choice,second_choice,third_choice,fourth_choice,current_line,a,b,c,d)
            Halving=False

    answer = input("Select the correct answer(a,b,c,d): \n(In case you need help type 'h')")
    return Audience, Telephone, Halving
    


def audience_help(a,b,c,d,current_line,question_lines):
    play_sound("kozonseg.mp3",0)
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
def telephone_help(question_lines,current_line,i):
    phone=input("Who'd you like to call?\nfor mum, press 'm'\nfor dad press 'd'\nfor old teacher from high school press 't'\nfor Maester Yoda press 'y': ")
    if phone.lower()=='m':
        play_sound("telhiv.mp3",0)
        time.sleep(2)
        play_sound("telefon.mp3",0)
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
        play_sound('telefon.mp3',54.0)
        time.sleep(1)
        print("Call Duration: ", int(now-then), " seconds\ 30 a")
    if phone.lower()=='d':
        play_sound("telhiv.mp3",0)
        time.sleep(2)
        play_sound("telefon.mp3",0)
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
        pygame.mixer.music.stop()
        play_sound('telefon.mp3',54.0)
        time.sleep(1)
        print("Call Duration: ", int(now-then), " seconds\ 30 seconds")
    if phone.lower()=='t':
        play_sound("telhiv.mp3",0)
        time.sleep(2)
        play_sound("telefon.mp3",0)
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
        pygame.mixer.music.stop()
        play_sound('telefon.mp3',54.0)
        time.sleep(1)       
        print("Call Duration: ", int(now-then), " seconds\ 30 seconds")
    if phone.lower()=='y':
        play_sound("telhiv.mp3",0)
        time.sleep(2)
        play_sound("telefon.mp3",0)
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
        pygame.mixer.music.stop() 
        play_sound('telefon.mp3',54.0)
        time.sleep(1)
        print("Call Duration: ", int(now-then), " seconds\ 30 seconds max.")
def halving(vago_feje_sorai,table_line_length,question_lines,i,shuffled_line,first_choice,second_choice,third_choice,fourth_choice,current_line,a,b,c,d):
    os.system('clear')
    time.sleep(2)
    play_sound("felezo.mp3",0)
    vago_feje_sorai = open_drawing('vago.txt', 'r')
    for head_lines in vago_feje_sorai:
        print(''.join(head_lines).rstrip())
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
        first_choice=fg.orange + '◆ A: ' +" "*len(a)+ fg.rs
    if b not in possibilities:
        second_choice=fg.orange + '◆ B: ' +" "*len(b)+ fg.rs
    if c not in possibilities:
        third_choice=fg.orange + '◆ C: '+" "*len(c) + fg.rs
    if d not in possibilities:       
        fourth_choice=fg.orange + '◆ D: ' +" "*len(d)+ fg.rs


    quiz_table(table_line_length,first_choice,second_choice,third_choice,fourth_choice,shuffled_line,question_lines,i)
         
    
def marking(answer,current_line,a,b,c,d,first_choice,second_choice,third_choice,fourth_choice,table_line_length,shuffled_line,question_lines,i):
    bg.white = bg(255, 255, 255)
    if answer.lower()=='a':
        answer = a
        first_choice=bg.white + first_choice +bg.black
    if answer.lower()=='b':
        answer = b
        second_choice=bg.white + second_choice +bg.black
    if answer.lower()== 'c':
        answer = c
        third_choice=bg.white + third_choice +bg.black
    if answer.lower()== 'd':
        answer = d
        fourth_choice=bg.white + fourth_choice +bg.black
    os.system('clear')
    quiz_table(table_line_length,first_choice,second_choice,third_choice,fourth_choice,shuffled_line,question_lines,i)
    play_sound("marked.wav",0)
    time.sleep(4)
    if answer==a:
        if a == current_line[0]:
            first_choice=bg.green + fg.orange + '◆ A: ' + fg.rs + ''.join(a) +bg.black
        else:
            first_choice=bg.red + fg.orange + '◆ A: ' + fg.rs + ''.join(a) +bg.black
    if answer==b:
        if b == current_line[0]:
            second_choice=bg.green + fg.orange + '◆ B: ' + fg.rs + ''.join(b) +bg.black
        else: 
            second_choice=bg.red + fg.orange + '◆ B: ' + fg.rs + ''.join(b) +bg.black
    if answer==c:
        if c == current_line[0]:
            third_choice=bg.green + fg.orange + '◆ C: ' + fg.rs + ''.join(c) +bg.black
        else:
            third_choice=bg.red + fg.orange + '◆ C: ' + fg.rs + ''.join(c) +bg.black
    if answer==d:
        if d == current_line[0]:
            fourth_choice=bg.green + fg.orange + '◆ D: ' + fg.rs + ''.join(d) +bg.black
        else:
            fourth_choice=bg.red + fg.orange + '◆ D: ' + fg.rs + ''.join(d) +bg.black
    if answer != current_line[0]:
        for pos in [a,b,c,d]:
            if pos==current_line[0]:
                if pos==a:
                    first_choice=bg.green + first_choice + bg.black
                if pos==b:
                    second_choice=bg.green + second_choice + bg.black
                if pos==c:
                    third_choice=bg.green + third_choice + bg.black
                if pos==d:
                    fourth_choice=bg.green + fourth_choice + bg.black
    time.sleep(1)
    os.system('clear')
    quiz_table(table_line_length,first_choice,second_choice,third_choice,fourth_choice,shuffled_line,question_lines,i)
    check_answer(answer,current_line,a,b,c,d,first_choice,second_choice,third_choice,fourth_choice,table_line_length,shuffled_line,question_lines,i)

    



def check_answer(answer,current_line,a,b,c,d,first_choice,second_choice,third_choice,fourth_choice,table_line_length,shuffled_line,question_lines,i):
    if answer == current_line[0]:
        play_sound("jo valasz.mp3",0)
        fg.green = Style(RgbFg(0, 255, 0))
        print(fg.green + "Well done!" + fg.rs)
        time.sleep(2)
        os.system('clear')
    else:
        play_sound("rossz valasz.mp3",0)
        time.sleep(2)
        fg.red = Style(RgbFg(255, 0, 0))
        print(fg.red+answer+"\nBetter luck next time!"+fg.rs)
        sys.exit(0)

def quiz():
    Help_available=[]
    Audience=True
    Telephone=True
    Halving=True
    counter = 0
    prices=["5.000 Ft ","10.000 Ft", "25.000 Ft","50.000 Ft","100.000 Ft","200.000 Ft","300.000 Ft","500.000 Ft","800.000Ft","1.500.000Ft","3.000.000 Ft","5.000.000 Ft","10.000.000 Ft","20.000.000 Ft","40.000.000 Ft"]
    question_lines=open_file('questions.txt', "r")
    list_of_answers=open_file('answers.txt', "r")
    copy_of_list_of_answers = copy.deepcopy(list_of_answers)
    for i in range(len(question_lines)):
        os.system('clear')
        current_line = list_of_answers[i]
        shuffled_line = copy_of_list_of_answers[i]
        random.shuffle(shuffled_line)
        a = shuffled_line[0]
        b = shuffled_line[1]
        c = shuffled_line[2]
        d = shuffled_line[3]
        fg.orange = Style(RgbFg(255, 150, 50))
        first_choice =fg.orange + '◆ A: ' + fg.rs + ''.join(shuffled_line[0])
        second_choice =fg.orange + '◆ B: ' + fg.rs + ''.join(shuffled_line[1])
        third_choice =fg.orange + '◆ C: ' + fg.rs + ''.join(shuffled_line[2])
        fourth_choice = fg.orange + '◆ D: ' + fg.rs + ''.join(shuffled_line[3])
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
       
        Aud="👥 "
        Tel=bg.black+"📞 "
        Halv="50:50"
        for i in Help_available:
            if i == False:
                if i==Help_available[0]:
                    Aud=bg.red+"👥 "+bg.rs
                if i==Help_available[1]:
                    Tel=bg.red+"📞 "+bg.rs
                if i==Help_available[2]:
                    Halv=bg.red+"50:50"+bg.rs
        n=0
        for head_lines in range(len(prices)):
            first_length=len(''.join(vago_feje_sorai[head_lines]))
            """ print(len(vago_feje_sorai[1][0]))
            print(table_line_length)
            print(first_length)
            print(table_line_length-first_length) """
            spaces=12
            szám=len(vago_feje_sorai[head_lines][0].strip())
            if szám>10:
                    if szám ==11:
                       spaces=10
                    if szám ==12:
                       spaces=16
                    if szám ==13:
                       spaces=15
                    if szám ==14:
                       spaces=10
                    if szám ==15:
                       spaces=10
                    if szám==16:
                        spaces=8
                    if szám==17:
                        spaces=8
                    if szám==18:
                        spaces=8
                    if szám==19:
                        spaces=6
                    if szám==20:
                        spaces=8
                    if szám==21:
                        spaces=5
                    if szám==22:
                        spaces=5
                    if szám==23:
                        spaces=5
                    if szám==24:
                        spaces=4
                    if szám==25:
                        spaces=3
                    if szám==26:
                        spaces=3
                    if szám==27:
                        spaces=5
                    if szám==28:
                        spaces=3
                    if szám==29:
                        spaces=5  
                    if szám==30:
                        spaces=3
                    if szám==31:
                        spaces=3
                    if szám==32:
                        spaces=3


            if head_lines==0:
                prices[0]="5.000 Ft" 
            if head_lines==4:
                prices[4]=bg.black+fg.white+prices[4]+"   "+fg.rs+bg.rs
            if head_lines==9:
                prices[9]=bg.black+fg.white+prices[9]+fg.rs+"  "+bg.rs
            if head_lines==14:
                prices[14]=fg.white+prices[14]+fg.rs 
            if head_lines==counter:
                if head_lines==4 or 9 or 14:
                    prices[head_lines]=fg.white+fg.black+prices[head_lines]+bg.rs+fg.rs+(len(prices[-1])-len(prices[head_lines]))*" "
                else:
                    prices[head_lines]=bg.white+fg.black+prices[head_lines]+bg.rs+fg.rs+(len(prices[-1])-len(prices[head_lines]))*" "

            print(''.join(vago_feje_sorai[head_lines]).rstrip()+" ".rstrip()*spaces+" "*spaces+fg.orange+prices[head_lines].rstrip()+fg.rs+(len(prices[-1])-len(prices[head_lines]))*" ".rstrip())
            #print(''.join(vago_feje_sorai[head_lines]).strip('\n')+7*" "+prices[head_lines].strip('\n'))
            
        for art in range(15,20):
            print(''.join(vago_feje_sorai[art]).rstrip())
        quiz_table(table_line_length,first_choice,second_choice,third_choice,fourth_choice,shuffled_line,question_lines,i)        
        counter += 1
        answer = input("Select the correct answer(a,b,c,d): \n(In case you need help type 'h')")
        if answer.lower()=='h':
            vago_feje_sorai = open_drawing('vago.txt', 'r')
            #help_modules(a,b,c,d,current_line,question_lines,i,vago_feje_sorai,table_line_length,shuffled_line,first_choice,second_choice,third_choice,fourth_choice,Audience,Telephone,Halving)
            Help_available=help_modules(a,b,c,d,current_line,question_lines,i,vago_feje_sorai,table_line_length,shuffled_line,first_choice,second_choice,third_choice,fourth_choice,Audience,Telephone,Halving)
            Audience=Help_available[0]
            Telephone=Help_available[1]
            Halving=Help_available[2]
        answer = input("Are you sure?")
        marking(answer,current_line,a,b,c,d,first_choice,second_choice,third_choice,fourth_choice,table_line_length,shuffled_line,question_lines,i)
        for round_ in range(len(prices)+1):
            if counter==round_:
                print(fg.orange +prices[counter]+fg.rs)
                time.sleep(1)
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