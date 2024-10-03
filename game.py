import random

# Define the suits and ranks
categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():
    # Create and shuffle the deck of cards
    deck = [f'{value} of {category}' for category in categories for value in values]
    random.shuffle(deck)
    return deck

def card_value(card):
    return values.index(card.split(' ')[0])

def play_game():
    deck = create_deck()
    player1_hand = deck[:7]
    player2_hand = deck[7:14]

    print("Player 1's hand:", player1_hand)
    print("Player 2's hand:", player2_hand)

    while player1_hand and player2_hand:
        # Player 1's turn
        action = input("Player 1, choose a card to play or type 'quit': ").strip()
        if action.lower() == 'quit':
            break
        if action in player1_hand:
            player1_hand.remove(action)
        else:
            print("Invalid card, please choose a card from your hand.")
            continue

        # Player 2's turn
        action = input("Player 2, choose a card to play or type 'quit': ").strip()
        if action.lower() == 'quit':
            break
        if action in player2_hand:
            player2_hand.remove(action)
        else:
            print("Invalid card, please choose a card from your hand.")
            continue

    # Check who quit
    if player1_hand and not player2_hand:
        print("Player 2 has no cards left. Player 1 wins!")
    elif player2_hand and not player1_hand:
        print("Player 1 has no cards left. Player 2 wins!")
    else:
        print("Player 1's remaining cards:", player1_hand)
        print("Player 2's remaining cards:", player2_hand)

        player1_score = sum(card_value(card) for card in player1_hand)
        player2_score = sum(card_value(card) for card in player2_hand)

        print(f"Total value of Player 1's cards: {player1_score}")
        print(f"Total value of Player 2's cards: {player2_score}")

        if player1_score > player2_score:
            print("Player 1 loses because their cards are greater.")
        else:
            print("Player 1 wins because their cards are lower.")

# Start the game
play_game()