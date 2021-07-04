#PROTOTYPE1

import time

#mh = 5        #ye sabse end me assign karna hai. kyunki decisions ke hisab se range badhani padegi. 0 to 10 me kaam ni chalega. LOS GEHTS!
#ph = 5      #assigning both mental and physical health mid points.      #in iteration 2, set lower end of one health as or something. as it will be unfair to have 10 ph and 0 mh and still win.

yes = ['Y','y']
no = ['N','n']

def win():    #THERE IS ONLY ONE WAY TO WIN, YOU SOCIALISE WELL, YOU FORGIVE PEOPLE, AND STAY PHYSICALLY FIT.
    print('{:*^100}'.format(''))
    print('*{:^98}*'.format(''))
    print('*{:^98}*'.format('Hey smart ape! You played your cards right!\nYou won!'))     #can add a message that if you socialise well, workout and learn forgiveness - you can win life.
    print('*{:^98}*'.format(''))
    print('{:*^100}'.format(''))

def lost():
    print('{:*^100}'.format(''))
    print('*{:^98}*'.format(''))
    print('*{:^98}*'.format('Life is hard sometimes. Sorry you lost.'))
    print('*{:^98}*'.format(''))
    print('{:*^100}'.format(''))

def destiny():
    print('This feature will be added in prototype2')
def start():
    print('{:*^80}'.format(''))      #printing the rules first.
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('Welcome to the Life. Here, you will be given 2 choices for every decision.'))
    print('*{:^78}*'.format('Each choice will have its own consequence. So be smart.'))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('Press Y for Yes and N for No. (case insensitive)'))
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('NOTE: If you type anything other than (above) choices-'))
    print('*{:^78}*'.format('      You will get a message from GOD.'))
    print('*{:^78}*'.format(''))
    #print('*{:^78}*'.format('Your mental health and physical health range from 0 to 10'))          #change this later
    #print('*{:^78}*'.format('Both are initially assigned as 5. '))
    #print('*{:^78}*'.format('If anyone of them reaches 0 you lose.'))
    #print('*{:^78}*'.format('If anyone of them reaches 10 you win.'))
    print('*{:^78}*'.format('FINDERS KEEPERS: there is a little device which can hack the simulation ;)') )     #ISSUE: if they go back in time, how will scores match. Or should I remove scores. soltion: lets just build.
    print('*{:^78}*'.format(''))
    print('*{:^78}*'.format('Enjoy'))
    print('*{:^78}*'.format(''))
    print('{:*^80}'.format(''))
    awake()

def god():
    print('\nHey mortal. This is GOD.')
    time.sleep(1)
    print('\nI caught you trying to sneak a new choice. Dont try to hack my craft son.')
    time.sleep(1)
    print('\nI am sending you back to sleep. This time, be a good boy and play by the rules.')
    awake()

def awake():
    #from here the game starts
    time.sleep(4)
    inp1= input('\n\nYou are now awake. Do you wish to leave the bed?:  ')
    if inp1 in yes:
        extro()
    elif inp1 in no:
        intro()
    else:
        god() 


def extro():  #this is if you leave the bed
    print('\nYour best friend is texting you to meet up for lunch at a nearby restraunt.')
    extro1 = input('\nDo you wish to hangout with him?  ')
    if extro1 in no:
        print('\nYou went out for a walk and had a great time with yourself.')
        time.sleep(2)
        print('\nYou return home tired and crash on the bed.')
        time.sleep(2)
        intro()
    elif extro1 in yes:
        print('\nYou decide to meet with your best friend at lunch.')
        time.sleep(1)
        print('\nYou meet him at the restaurant. He confesses that he is in a relationship with your ex - who broke up with you 4 days ago.')
        time.sleep(2)
        print('\nYou feel this rush in your veins.')
        extro2= input('\nPress N to beat up your best friend or Press Y to forgive him: ')
        if extro2 in no:
            time.sleep(1)
            print('\nYou engange in a hand to hand fight with your best friend. You accidentally push him harder than you wished to.' )
            time.sleep(2)
            print('He hits the corner of a table.')
            time.sleep(1)
            print('\nHe is bleeding to death.')
            extro3 = input('\nPress Y to try to help him or press N to run away: ')
            if extro3 in no:
                print('\nYou are now running away as fast as you can. Where do you wish to hide?')
                extro4 = input('\nPress Y to go home. Press N to hide in a nearby forest: ')
                if extro4 in yes:
                    print('\nYou run straight to your house. You are crying and breathing heavy.')
                    extro5 = input('\nPress Y to stay in bed and cry. Press N to commit suicide: ')
                    if extro5 in no:
                        suicide()
                    elif extro5 in yes:
                        print('\nParalysed with fear, you stayed in bed')
                        time.sleep(2)
                        arrest()
                    else:
                        god()
                elif extro4 in no:
                    timemachine()
                else:
                    god()
                   
            elif extro3 in yes:
                print('\nYou call for an ambulance. And try to stop his bleeding.')
                time.sleep(2)
                print('\nYour bestie dies before ambulance could reach. He takes his last breath in your arms.')
                time.sleep(2)
                arrest()
            else:
                god()
        elif extro2 in yes:
            print('\nYou chose to be a bigger man. You acted as you have moved on from your ex and you are cool with everything.\nYou finish your lunch and leave.')
            time.sleep(2)
            print('\nOn the way home - you realise, even after acting cool, this pain is still churning inside you and you need a vent for it.')
            extro6 = input('\nPress Y to join gym. Press N to go to a bar: ')
            if extro6 in yes:
                print('\nYou signed up at a gym.')
                time.sleep(1)
                print('\nYou made all the right choices. This proves you are a bigger man!')
                time.sleep(2)
                print('\nOr... you cheated with a time machine LOL. But, just like life, this game isnt fair.')
                time.sleep(2)
                win()
                restart()
            elif extro6 in no:
                print('\nYou reach a bar & order drinks until you are hammered.')
                time.sleep(1)
                print('\nA drunk stranger is trying to annoy you unnecessarily.')
                extro7 = input('Press Y to ignore him and focus on your drink. Press N to pick a fight with him: ')
                if extro7 in yes:
                    print('\nDrinking becomes your daily habit.\nAlong with being emotionally frustrated, you also ruined your physical health.')
                    time.sleep(2)
                    lost()
                    restart()
                elif extro7 in no:
                    print('\nYou break a bottle on his head.\nHe falls on the ground and starts to bleed heavily')
                    time.sleep(2)
                    print('\nYou run away from the bar as fast as you can')
                    extro8 = input('\nPress Y to run and hide in your house. Press N to hide in the nearby forest: ')
                    if extro8 in no:
                        timemachine()
                    elif extro8 in yes:
                        arrest()
                    else:
                        god()
                else:
                    god()
            else:
                god()
        else:
            god()
                

def timemachine():
    
     print('\nYou run straight to hide in the nearby forest. You keep running until you find yourself lost inside the jungle and cant figure a way out')
     time.sleep(2)
     print('\nTired, you sit down near a tree and realise there is a thing under you butt.')
     time.sleep(2)
     print('\nYou turn around to look - its a box. \nYou open it to find a device and a paper-note next to it, which says-')
     time.sleep(2)
     print('\nONCE HUMANITY WAS WRONG ABOUT SPACE - BUT NOW WE KNOW EARTH IS ROUND AND REVOLVES AROUND SUN.')
     time.sleep(2)
     print('\nCURRENTLY, HUMANITY IS WRONG ABOUT TIME - IT DOESNT FLOW IN ONE DIRECTION.')
     time.sleep(2)
     print('\nBUT YOU, A GREAT SEEKER, HAS FOUND A TIME MACHINE WHICH CAN HELP YOU GO BACK IN TIME AND MAKE DIFFERENT CHOICES.')
     time.sleep(3)
     print('\nYou can travel back to your previous choices by using following keywords: ')
     tm = input('\nPress Y to return back to your bed\n\nPress N to return to reply your besties text: ')
     
     if tm in yes:
         print('\nMachine initialising')
         time.sleep(1)
         print('\nSending you back to bed')
         time.sleep(1)
         print('\n3')
         time.sleep(1)
         print('2')
         time.sleep(1)
         print('1')
         time.sleep(1)
         print('\nWOOOOOOSH!!!')
         
         awake()
     elif tm in no:
         print('\nMachine initialising')
         time.sleep(1)
         print('\nSending you back in time')
         time.sleep(1)
         print('\n3')
         time.sleep(1)
         print('2')
         time.sleep(1)
         print('1')
         time.sleep(1)
         print('\nWOOOOOOSH!!!')
         time.sleep(1)
         extro()
     else:
        god()
         
         
                   
                       

def arrest(): #this is when you get arrested / police figures out that you did the crime.
    print('\nPolice investigates and finds that you did the crime.\nThey arrest you.')
    print('\nIn court. Judge sentences you to a DEATH PENALTY.')
    time.sleep(2)
    lost()
    restart()
    
    
def intro():
    intro1= input('\nPress Y to sleep. Press N to lie awake in bed:  ')
    if intro1 in yes:
        print('\nYou chose to sleep. See you again when you wake up :)')
        time.sleep(3)
        awake()
    elif intro1 in no:
        intro2 = input('\nPress Y to watch some youtube videos or N to stare at the ceiling fan and overthink: ')
        if intro2 in yes:
            time.sleep(2)
            print('\nYou slept while watching youtube. See you again when get up')
            time.sleep(3)
            awake()
        elif intro2 in no:
            
            print('\nDue to overthinking, depression is rising.')
            time.sleep(2)
            intro3 = input('\nDo you wish to call your therapist? ')
            if intro3 in yes:
                print('\nYour therapist told you to take medicines and rest.')
                time.sleep(1)
                intro4 = input('\nWould you obey her and take your meds? ')
                if intro4 in yes:
                    print('\nGood, you now feel better and relaxed. Sleep a little, we will meet again when you get up')
                    time.sleep(3)
                    awake()
                elif intro4 in no:
                    
                    print('\nThe burden of existence is getting heavy on you')
                    time.sleep(1)
                    suicide()
                    
                else:
                    god()
            elif intro3 in no:
                print('\nThe burden of existence is getting heavy on you')
                time.sleep(1)
                intro5 = input('\nPress Y to cry or press N to commit suicide:  ')
                if intro5 in yes:
                    print('\nThere are no tears left. You just feel numb and dead from inside.')
                    suicide()
                elif intro5 in no:
                    suicide()
                else:
                    god()
            else:
                god()
        else:
            god()
    else:
        god()

def suicide():
    print('\nYou couldnt take it anymore. Everything just feels heavy and you find death as the only escape.')
    time.sleep(2)
    print('\nYou ate rat poison and died.')
    time.sleep(2)
    restart()


def restart():
    re = input('\nSecond times the charm! Do you wish to play again? ')
    if re in yes:
        start()
    elif re in no:
        print('\nToo bad to see you leave. Anyways, make good choices in your real life ')
        time.sleep(2)
        print('\nAssuming it is real.')
        time.sleep(2)
        print('\nIs it?')
        time.sleep(2)
        print('\n\nHave a good life.\n\nBye')
        time.sleep(4)
        quit()
    else:
        god()


start()


