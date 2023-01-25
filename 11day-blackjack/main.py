from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pick_card():
    card_random = random.randint(0, len(cards) - 1)
    return cards[card_random]


def cal_sum(deck):
    return int(sum(deck))


def play():
    print(logo)
    i = 1
    human_deck = []
    computer_deck = []
    for i in range(2):
        human_deck.append(pick_card())
    print(f"   Your card: {human_deck}, current score: {cal_sum(human_deck)}")
    computer_deck.append(pick_card())
    print(f"   Computer first card: {computer_deck}")
    while cal_sum(computer_deck) < 17:
        computer_deck.append(pick_card())

    if cal_sum(human_deck) < 21:
      keep_play = input("Type 'y' to get another card, type 'n' to pass: ")
      while keep_play == "y":
        human_deck.append(pick_card())
        print(f"   Your card: {human_deck}, current score: {cal_sum(human_deck)}")
        if cal_sum(human_deck) < 21:
          keep_play = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
          keep_play = "n"
      print(f"   Your final hand: {human_deck}, final score: {cal_sum(human_deck)}")
      print(f"   Computer's final hand: {computer_deck}, final score: {cal_sum(computer_deck)}")

    if cal_sum(human_deck) == cal_sum(computer_deck):
      print("## We have a draw. Play again ##")
    elif cal_sum(human_deck) > 21:
      print("## You went over. You lose ##")
    elif cal_sum(computer_deck) > 21:
      print("## Computer went over. You win ##")
    elif cal_sum(computer_deck) <= 21 and cal_sum(human_deck) < cal_sum(computer_deck) :
        print("## The computer won. You lose ##")
    else:
        print("## You win")


should_continue = True

while should_continue == True:
    if input("Do you want to play blackjack game, answer 'y' or 'n': ") == "y":
        play()
    else:
        should_continue = False
