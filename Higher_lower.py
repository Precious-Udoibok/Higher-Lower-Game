#Higher Lower game
#import random module and art, game data module
import random
from art import logo,vs,clear
from game_data import data

#create a function to display the random choices
def options(random_choice):
    '''This function displays the printed version of the accouts'''
    return f'{random_choice['name']}, a {random_choice['description']}, from {random_choice['country']}'
            #print(random_choice[keys1])

def score_checker(score):
    '''Function that check the scores'''
    if score == 0:
        print('Did we make this too hard for you?\nThe average score is 3\nWe are pretty embarrassed for you right now.')
    elif score > 0 and score < 3:
        print('The Average Score is 3, let\'s pretend that never happened.')
    elif score >=3 and score < 6:
        print('Oh dear!!! That\'s soooooo average.\ncome on. You can get a score of 6 can\'t you? ')
    elif score >= 6 and score <10:
        print('Not bad, Keep trying you are getting there.')
    else:
        print('Nice One. You are one of our Top PLayers now.')


#function that compare the score
def answer_check(follower,optionacount,optionbcount):
    '''function that compare the scores'''
    if optionacount > optionbcount:
        return follower == 'a' #this will return either true or false, just like comparism
    else: # if optionacount <optionbcount
        return follower == 'b' #this too will return either true or false

#A function to play the game
def higher_lower():
    '''Plays the higher lower game'''
    score = 0 #a variable to store the score
    random_choice1 = random.choice(data) #pick  a random account from the data in art.py
    optionA = options(random_choice1) #display the printed format of the random account
    optionA_count = random_choice1['follower_count'] #get the number of followers
    bigger = True #set a flag to continue the game
    while bigger:
        random_choice2 = random.choice(data) #pick another random account
        #display logo
        print(logo)
        if score > 0:
            print(f'You\'re Correct, Current score: {score}')
        else:
            pass
        print(f'Compare A: {optionA}')

        #print the vs logo from art.py
        print(vs)
        optionB = options(random_choice2)
        while optionA == optionB:
            optionB = options(random_choice2) #continue to look for another random account
        print(f'Against B: {optionB}')
        optionB_count = random_choice2['follower_count']
        # print(optionA_count,optionB_count)# use to check your code
        followers = input('Who has more followers? Type A or B: ').lower()
        #store the true or False in a varaiable
        is_check = answer_check(follower=followers,optionacount=optionA_count,optionbcount=optionB_count)
        #check is its true or fase
        if is_check: #if true is retuned
            optionA = optionB #set option a to option b
            optionA_count = optionB_count #set optiona followers to option b followers
            score += 1 #increment the score by 1
        else:
            bigger = False #end game
            print(logo) #display logo
            print(f'Your Final Score is {score}\n') #display the final score
            score_checker(score) #call the score checker function
            another_game= input('\nWill you like to play again (y/n): ').lower() #ask the user if they will play again
            if another_game == 'y':
                higher_lower() #call the higher lower game function
            elif another_game == 'n':
                print('\nGood Bye. Have a nice day.')
                bigger = False #end the game
            else:
                print('You did not enter the correct value')
                bigger = False #end the game
higher_lower() #call the higher lower game function