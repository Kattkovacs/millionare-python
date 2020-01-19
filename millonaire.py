import random
import copy
import sys
import os
from sty import Style, RgbFg, fg, rs, bg
import time
import pygame


def game_start():
    fg.purple = Style(RgbFg(148, 0, 211))
    pygame.mixer.init()
    os.system('clear')
    play_sound("loim_intro.wav", 0)
    time.sleep(2)
    print("This is the game of games..\nIn the arena..\nMr Steven Vágó is awaiting You!\n"+fg.purple+"Become the next Millionaire!\n"+fg.rs)
    time.sleep(5)

def play_sound(filename, starting_time):
    pygame.mixer.init()
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

def quiz_table(table_line_length,choises,question,shuffled_line):
    print("  "+bg.black+"/"+"‾"*(table_line_length-6)+"\\"+bg.rs)
    width = table_line_length
    print("-"+bg.black+"‹"+''.join(question).center((width-4),' ')+"›"+bg.rs+"-")
    print("  "+bg.black+"\\"+"_"*(table_line_length-6)+"/"+bg.rs)
    space_left=7
    upper_line_first_second_choise="  "+bg.black+"/"+(len(shuffled_line[0])+space_left)*"‾"+"\\"+bg.rs+(" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+22)))+bg.black+"/"+(len(shuffled_line[1])+space_left)*"‾"+"\\"+bg.rs
    under_line_first_second_choise="  "+bg.black+"\\"+(len(shuffled_line[0])+space_left)*"_"+"/"+bg.rs+(" "*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+22)))+bg.black+"\\"+(len(shuffled_line[1])+space_left)*"_"+"/"+bg.rs
    upper_line_third_fourth_choise="  "+bg.black+"/"+(len(shuffled_line[2])+space_left)*"‾"+"\\"+bg.rs+(" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+22)))+bg.black+"/"+(len(shuffled_line[3])+space_left)*"‾"+"\\"+bg.rs
    under_line_third_fourth_choise="  "+bg.black+"\\"+(len(shuffled_line[2])+space_left)*"_"+"/"+bg.rs+(" "*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+22)))+bg.black+"\\"+(len(shuffled_line[3])+space_left)*"_"+"/"+bg.rs
    print(upper_line_first_second_choise)
    print("-"+bg.black+"‹ "+ choises[0] +" ›"+bg.rs+ ("-"*(table_line_length-(len(shuffled_line[0])+len(shuffled_line[1])+24))) +bg.black+"‹ "+choises[1] + " ›"+bg.rs+"-")
    print(under_line_first_second_choise)
    print(upper_line_third_fourth_choise)
    print("-"+bg.black+"‹ "+ choises[2] +" ›"+bg.rs+ ("-"*(table_line_length-(len(shuffled_line[2])+len(shuffled_line[3])+24)))+bg.black+"‹ "+choises[3] + " ›"+bg.rs+"-")
    print(under_line_third_fourth_choise)

def print_quizmaster_with_prices_table(Help_available,table_line_length,prices,prices1,prices2,counter):
    vago_feje_sorai = open_drawing('vago.txt', 'r')
    Aud="👥 "
    Tel=bg.black+"📞 "
    Halv="50:50"
    for helps in Help_available:
        if helps == False:
            if helps==Help_available[0]:
                Aud=bg.red+"👥 "+bg.rs
            if helps==Help_available[1]:
                Tel=bg.red+"📞 "+bg.rs
            if helps==Help_available[2]:
                Halv=bg.red+"50:50"+bg.rs
    n=0
    print(((table_line_length+2)*" ")+bg.black+(len(prices[-1])+2)*"-".rstrip()+bg.rs)
    
    print(((table_line_length+2)*" ")+bg.black+"|"+" "+Halv+"∥"+Tel+" "+"∥"+Aud+(len(prices[-1])-(len(Halv)+len(Tel)+len(Aud)+4))*" "+bg.black+"|"+bg.rs)
    print(((table_line_length+2)*" ")+bg.black+(len(prices[-1])+2)*"-"+bg.rs)
    print(((table_line_length+2)*" ")+bg.black+(len(prices[-1])+2)*"-"+bg.rs)
    for head_lines in range(15):
        """ spaces=14
        szám=len(vago_feje_sorai[head_lines][0].strip())
        if szám>10:
                if szám ==11:
                    spaces=12
                if szám ==12:
                    spaces=18
                if szám ==13:
                    spaces=17
                if szám ==14:
                    spaces=12
                if szám ==15:
                    spaces=12
                if szám==16:
                    spaces=10
                if szám==17:
                    spaces=10
                if szám==18:
                    spaces=10
                if szám==19:
                    spaces=8
                if szám==20:
                    spaces=10
                if szám==21:
                    spaces=7
                if szám==22:
                    spaces=7
                if szám==23:
                    spaces=7
                if szám==24:
                    spaces=6
                if szám==25:
                    spaces=5
                if szám==26:
                    spaces=5
                if szám==27:
                    spaces=7
                if szám==28:
                    spaces=5
                if szám==29:
                    spaces=7  
                if szám==30:
                    spaces=5
                if szám==31:
                    spaces=5
                if szám==32:
                    spaces=5 """
        bg.orange = bg(255, 150, 50)
        spaces_=(len(prices1[0])-len(prices1[head_lines]))*" "
        if prices2[head_lines]==prices2[0]:
            prices2[0]=bg.black+fg.white+prices1[0]
        if counter==14:
            prices2[0]=bg.orange+fg.black+prices1[0]
        if prices2[head_lines]==prices2[counter]:
            prices2[14-counter]=bg.orange+fg.black+prices1[14-counter]
            
            if counter >= 1:
                prices2[14-counter+1]=bg.black+fg.orange+prices1[14-counter+1]
            for n in range(counter+1,15):
                if n in [5,10,14]:
                    prices2[n]=bg.black+fg.white+prices2[n]
                prices2[n]=bg.black+fg.orange+prices2[n]
        print(''.join(vago_feje_sorai[head_lines]).strip('\n')+" "*spaces+bg.black+"|"+fg.rs+bg.rs+prices2[head_lines]+spaces_+fg.white+bg.black+"|"+bg.rs+fg.rs)
    
    print(''.join(vago_feje_sorai[15]).rstrip()+13*" "+bg.black+(len(prices[:-1])+1)*"-"+bg.rs)
    for art in range(16,20):
        print(''.join(vago_feje_sorai[art]).rstrip())

def help_modules(a,b,c,d,current_line,question,vago_feje_sorai,table_line_length,shuffled_line,choises,Audience,Telephone,Halving,Help_available,prices,prices1,prices2,counter):
    help_=input("For Audience's help, type 'a'\nFor Telephone help type 't'\nFor halving type 'h': ")        
    if help_.lower()=="a":
        if Audience==False:
            print("You have already used the audience help!")
        else:    
            audience_help(a,b,c,d,current_line,question,table_line_length,choises,shuffled_line)
            Audience=False
            print_quizmaster_with_prices_table(Help_available,table_line_length,prices,prices1,prices2,counter)
            quiz_table(table_line_length,choises,question,shuffled_line)

            
    if help_.lower()=="t":
        if Telephone==False:
            print("You have already used the telephone help!")
        else:
            telephone_help(question,current_line)
            Telephone=False
    if help_.lower()=="h":
        if Halving==False:
            print("You have already used the halving help!")
        else:
            halving(vago_feje_sorai,table_line_length,question,shuffled_line,choises,current_line,a,b,c,d)
            Halving=False
            print_quizmaster_with_prices_table(Help_available,table_line_length,prices,prices1,prices2,counter)
            quiz_table(table_line_length,choises,question,shuffled_line)

    answer = input("Select the correct answer(a,b,c,d): \n(In case you need help type 'h')")
    return Audience, Telephone, Halving, answer
    


def audience_help(a,b,c,d,current_line,question,table_line_length,choises,shuffled_line):
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
            os.system('clear')
            for choise_ in [a,b,c,d]:
                if choise ==current_line[0]:
                    if choise_==a:
                        fake_a_percent=random.randrange(40,89)
                        fake_b_percent=random.randrange(0,(100-fake_a_percent))
                        fake_c_percent=random.randrange(0,(100-fake_a_percent-fake_b_percent))
                        fake_d_percent=100-(fake_a_percent+fake_b_percent+fake_c_percent)
                    if choise_==b:
                        fake_b_percent=random.randrange(40,89)
                        fake_a_percent=random.randrange(0,(100-fake_b_percent))
                        fake_c_percent=random.randrange(0,(100-fake_b_percent-fake_a_percent))
                        fake_d_percent=100-(fake_a_percent+fake_b_percent+fake_c_percent)
                    if choise_==c:
                        fake_c_percent=random.randrange(40,89)
                        fake_b_percent=random.randrange(0,(100-fake_c_percent))
                        fake_a_percent=random.randrange(0,(100-fake_c_percent-fake_b_percent))
                        fake_d_percent=100-(fake_a_percent+fake_b_percent+fake_c_percent)
                    if choise_==d:
                        fake_d_percent=random.randrange(40,89)
                        fake_b_percent=random.randrange(0,(100-fake_d_percent))
                        fake_c_percent=random.randrange(0,(100-fake_d_percent-fake_b_percent))
                        fake_a_percent=100-(fake_d_percent+fake_b_percent+fake_c_percent)
                    if fake_a_percent+fake_b_percent+fake_c_percent+fake_d_percent != 100:
                        print("Sheibe")
                print("A:"+bg.blue+fake_a_percent*" "+" "+str(fake_a_percent)+"%"+"\n"+bg.rs+"B:"+bg.blue+fake_b_percent*" "+" "+str(fake_b_percent)+"%"+"\n"+bg.rs+"C:"+bg.blue+fake_c_percent*" "+" "+str(fake_c_percent)+"%"+"\n"+bg.rs+"D:"+bg.blue+fake_d_percent*" "+" "+str(fake_d_percent)+"%"+"\n"+bg.rs)
                time.sleep(1)
                os.system('clear')
                sys.stdout.write("\033[F")
            elems=[a_percent,b_percent,c_percent,d_percent]
            max_element=max(elems[0],elems[1],elems[2],elems[3])
            a__=(f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  A: {bg.rs+bg.blue+a_percent*" "+bg.black+fg.rs+str(a_percent)}%')
            b__=(f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  B: {bg.rs+bg.blue+b_percent*" "+bg.black+fg.rs+str(b_percent)}%')
            c__=(f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  C: {bg.rs+bg.blue+c_percent*" "+bg.black+fg.rs+str(c_percent)}%')
            d__=(f'{(table_line_length+1)*" "+bg.black+"|"+fg.orange}  D: {bg.rs+bg.blue+d_percent*" "+bg.black+fg.rs+str(d_percent)}%')
            print((table_line_length+1)*" "+bg.black+(max_element+11)*"-"+bg.rs)
            print(a__+(((max_element)-a_percent)+3)*" "+"|"+bg.rs)
            time.sleep(1)
            print(b__+(((max_element)-b_percent)+2)*" "+"|"+bg.rs)
            time.sleep(1)
            print(c__+(((max_element)-c_percent)+2)*" "+"|"+bg.rs)
            time.sleep(1)
            print(d__+(((max_element)-d_percent)+3)*" "+"|"+bg.rs)
            print((table_line_length+1)*" "+bg.black+(max_element+11)*"-"+bg.rs)
        
def telephone_help(question,current_line):
    phone=input("Who'd you like to call?\nfor mum, press 'm'\nfor dad press 'd'\nfor old teacher from high school press 't'\nfor Maester Yoda press 'y': ")
    if phone.lower()=='m':
        play_sound("telhiv.mp3",0)
        time.sleep(2)
        play_sound("telefon.mp3",0)
        then = time.time()
        print(fg.orange+str(30-int(time.time()-then))+fg.rs)
        print("Hi mummy, I'm playing the Millionaire..Here's the question.. \n"+', '.join(question))
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
        print("Hi dad, I'm playing the Millionaire..Here's the question.. \n"', '.join(question))
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
        print("Great day Mr Teacher I am your former student, and I'm playing the Millionaire..Here's the question..\n"', '.join(question))
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
        print("Hi Yoda, I need your force of knowledge because I'm playing the Millionaire..Here's the question..\n"', '.join(question))
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
def halving(vago_feje_sorai,table_line_length,question,shuffled_line,choises,current_line,a,b,c,d):
    os.system('clear')
    time.sleep(2)
    play_sound("felezo.mp3",0)
    vago_feje_sorai = open_drawing('vago.txt', 'r')
    for head_lines in vago_feje_sorai:
        print(''.join(head_lines).rstrip())
    possibilities=[]
    for shuffled_element in shuffled_line:
            if shuffled_element==a:
                possibilities.append(random.choice([b,c,d]))
            elif shuffled_element==b:
                possibilities.append(random.choice([a,c,d]))
            elif shuffled_element==c:
                possibilities.append(random.choice([a,b,d]))
            elif shuffled_element==d:
                possibilities.append(random.choice([a,c,b]))
    if a not in possibilities:
        choises[0]=fg.orange + '◆ A: ' +" "*len(a)+ fg.rs
    if b not in possibilities:
        choises[1]=fg.orange + '◆ B: ' +" "*len(b)+ fg.rs
    if c not in possibilities:
        choises[2]=fg.orange + '◆ C: '+" "*len(c) + fg.rs
    if d not in possibilities:       
        choises[3]=fg.orange + '◆ D: ' +" "*len(d)+ fg.rs

def marking(answer,current_line,a,b,c,d,choises,table_line_length,shuffled_line,question,Help_available,prices,prices1,prices2,counter):
    bg.white = bg(255, 255, 255)
    if answer.lower()=='a':
        answer = a
        choises[0]=bg.white + fg.blue + choises[0] + fg.rs + bg.black
    if answer.lower()=='b':
        answer = b
        choises[1]=bg.white + fg.blue +  choises[1] + fg.rs +bg.black
    if answer.lower()== 'c':
        answer = c
        choises[2]=bg.white + fg.blue +  choises[2] + fg.rs +bg.black
    if answer.lower()== 'd':
        answer = d
        choises[3]=bg.white + fg.blue +  choises[3] + fg.rs +bg.black
    os.system('clear')
    print_quizmaster_with_prices_table(Help_available,table_line_length,prices,prices1,prices2,counter)
    quiz_table(table_line_length,choises,question,shuffled_line)

    play_sound("marked.wav",0)
    time.sleep(4)
    if answer==a:
        if a == current_line[0]:
            choises[0]=bg.green + fg.orange + '◆ A: ' + fg.rs + ''.join(a) +"  "+bg.black
        else:
            choises[0]=bg.red + fg.orange + '◆ A: ' + fg.rs + ''.join(a) +"  "+bg.black
    if answer==b:
        if b == current_line[0]:
            choises[1]=bg.green + fg.orange + '◆ B: ' + fg.rs + ''.join(b) +"  "+bg.black
        else: 
            choises[1]=bg.red + fg.orange + '◆ B: ' + fg.rs + ''.join(b) +"  "+bg.black
    if answer==c:
        if c == current_line[0]:
            choises[2]=bg.green + fg.orange + '◆ C: ' + fg.rs + ''.join(c) +"  "+bg.black
        else:
            choises[2]=bg.red + fg.orange + '◆ C: ' + fg.rs + ''.join(c) +"  "+bg.black
    if answer==d:
        if d == current_line[0]:
            choises[3]=bg.green + fg.orange + '◆ D: ' + fg.rs + ''.join(d) +"  "+bg.black
        else:
            choises[3]=bg.red + fg.orange + '◆ D: ' + fg.rs + ''.join(d) +"  "+bg.black
    if answer != current_line[0]:
        for pos in [a,b,c,d]:
            if pos==current_line[0]:
                if pos==a:
                    choises[0]=bg.green + choises[0] +"  "+ bg.black
                if pos==b:
                    choises[1]=bg.green + choises[1] +"  "+ bg.black
                if pos==c:
                    choises[2]=bg.green + choises[2] +"  "+ bg.black
                if pos==d:
                    choises[3]=bg.green + choises[3] +"  "+ bg.black
    time.sleep(1)
    os.system('clear')
    print_quizmaster_with_prices_table(Help_available,table_line_length,prices,prices1,prices2,counter)
    quiz_table(table_line_length,choises,question,shuffled_line)
    check_answer(answer,current_line,a,b,c,d,choises,table_line_length,shuffled_line,question)

    



def check_answer(answer,current_line,a,b,c,d,choises,table_line_length,shuffled_line,question):
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
    prices=["5.000 Ft","10.000 Ft", "25.000 Ft","50.000 Ft","100.000 Ft","200.000 Ft","300.000 Ft","500.000 Ft","800.000 Ft","1.500.000 Ft","3.000.000 Ft","5.000.000 Ft","10.000.000 Ft","20.000.000 Ft","40.000.000 Ft"]
    prices1=['40.000.000 Ft', '20.000.000 Ft', '10.000.000 Ft', '5.000.000 Ft', '3.000.000 Ft', '1.500.000 Ft', '800.000 Ft', '500.000 Ft', '300.000 Ft', '200.000 Ft', '100.000 Ft', '50.000 Ft', '25.000 Ft', '10.000 Ft', '5.000 Ft']
    prices2=['40.000.000 Ft', '20.000.000 Ft', '10.000.000 Ft', '5.000.000 Ft', '3.000.000 Ft', '1.500.000 Ft', '800.000 Ft', '500.000 Ft', '300.000 Ft', '200.000 Ft', '100.000 Ft', '50.000 Ft', '25.000 Ft', '10.000 Ft', '5.000 Ft']
    question_lines=open_file('questions.txt', "r")
    list_of_answers=open_file('answers.txt', "r")
    copy_of_list_of_answers = copy.deepcopy(list_of_answers)
    for i in range(len(question_lines)):
        counter = i
        question=question_lines[i]
        time.sleep(2)
        os.system('clear')
        current_line = list_of_answers[i]
        shuffled_line = copy_of_list_of_answers[i]
        random.shuffle(shuffled_line)
        a = shuffled_line[0]
        b = shuffled_line[1]
        c = shuffled_line[2]
        d = shuffled_line[3]
        fg.orange = Style(RgbFg(255, 150, 50))
        first_choice =fg.orange + '◆ A: ' + fg.rs + ''.join(shuffled_line[0])+"  "
        second_choice =fg.orange + '◆ B: ' + fg.rs + ''.join(shuffled_line[1])+"  "
        third_choice =fg.orange + '◆ C: ' + fg.rs + ''.join(shuffled_line[2])+"  "
        fourth_choice = fg.orange + '◆ D: ' + fg.rs + ''.join(shuffled_line[3])+"  "
        choises=[first_choice,second_choice,third_choice,fourth_choice]
        max_question_length=0
        answer_lengths=[]
        for question_ in question_lines:
            if len(question_)>max_question_length:
                max_question_length=len(question_)
        for answer in list_of_answers:
            for element in answer:
                answer_lengths.append(len(element))
                answer_lengths.sort()
        if answer_lengths[-1]*2>max_question_length:
            table_line_length=answer_lengths[-1]*2
        else: 
            table_line_length=max_question_length
        print_quizmaster_with_prices_table(Help_available,table_line_length,prices,prices1,prices2,counter)
        quiz_table(table_line_length,choises,question,shuffled_line)    
        answer = input("Select the correct answer(a,b,c,d): \n(In case you need help type 'h')")
        if answer.lower()=='h':
            vago_feje_sorai = open_drawing('vago.txt', 'r')
            Help_available=help_modules(a,b,c,d,current_line,question,vago_feje_sorai,table_line_length,shuffled_line,choises,Audience,Telephone,Halving,Help_available,prices,prices1,prices2,counter)
            Audience=Help_available[0]
            Telephone=Help_available[1]
            Halving=Help_available[2]
        answer = input("Are you sure?")
        marking(answer,current_line,a,b,c,d,choises,table_line_length,shuffled_line,question,Help_available,prices,prices1,prices2,counter)
        won_prize=fg.orange+prices[i]+fg.rs
        if i == 4:
            won_prize=fg.orange + "You have guaranteed 100.000 Ft" + fg.rs
            time.sleep(1)
        elif i == 9:
            won_prize=fg.orange + "You have guaranteed 1.500.000 Ft" + fg.rs
            time.sleep(1)
        elif i == 14:
            won_prize=fg.orange + "Congratulations!\nYou've just won the unbelivable 40.000.000 Ft\n"+fg.purple+"You became the new Millionaire!!!" + fg.rs
            time.sleep(3)
            sys.exit(0)
        print_quizmaster_with_prices_table(Help_available,table_line_length,prices,prices1,prices2,counter)
        print("  "+bg.black+"/"+"‾"*(table_line_length-6)+"\\"+bg.rs)
        width = table_line_length
        len_table=len("‾"*(table_line_length-6-len(won_prize)))
        print("-"+bg.black+"‹"+int(len_table/2)*" "+''.join(won_prize).center((width-4),' ')+(int(len_table/2)+1)*" "+"›"+bg.rs+"-")
        print("  "+bg.black+"\\"+"_"*(table_line_length-6)+"/"+bg.rs)   
        time.sleep(1)


def main():
    #game_start()
    quiz()


if __name__ == "__main__":
    main()