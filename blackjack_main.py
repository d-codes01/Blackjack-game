import random
import os
from blackjack_art import logo
def random_card():
    '''Returns a random card'''
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def game_score(cards):
    '''Calculates the score'''
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(player_score,computer_score):
    '''Declares the decision by comparing the scores'''
    if player_score==computer_score:
        return "Draw!"
    elif player_score==0:
        return "Win with a blackjack!"
    elif computer_score==0:
        return "Lose! Opponent won with a blackjack"
    elif player_score>21:
        return "Lose! you went over."
    elif computer_score>21:
        return "Won! opponent went over."
    elif player_score>computer_score:
        return "You win!"
    else:
        return "You lose!"
def play():
    '''Plays the game'''
    player_cards=[]
    computer_cards=[]
    game_over=False
    for _ in range(2):
        player_cards.append(random_card())
        computer_cards.append(random_card())


    while not game_over==True:
        player_score=game_score(player_cards)
        computer_score=game_score(computer_cards)
        print(f"Your cards are {player_cards} and your score is {player_score}")
        print(f"Computer's cards are {computer_cards} and score is {computer_score}")

        if player_score==0 or computer_score==0 or player_score>21:
            game_over=True
        else:
            player_deal=input("Type 'y' to get another card and type 'n' to pass: ")
            if player_deal=='y':
                player_cards.append(random_card())
            else:
                game_over=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(random_card())
        computer_score=game_score(computer_cards)

    print(f"Your final cards are {player_cards} and final score is {player_score}")
    print(f"Computer's final cards are {computer_cards} and final score is {computer_score}")

    print(compare(player_score,computer_score))
while input("Do you want to play the game? Type 'y' or 'n'")=='y':
    os.system("cls")
    print(logo)
    play()
    

