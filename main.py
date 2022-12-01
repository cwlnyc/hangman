import requests
import json
import sys
import getpass


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
hangman_pieces = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg', 'left foot', 'right foot']

def get_word():
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': 'UOp+98qkiurM2wI15MlOQA==YMcU4CJ2u7uYQhRB'})
    if response.status_code == requests.codes.ok:
        response_json = json.loads(response.text)
        word = response_json['word'].lower()
        return word
    else:
        print("Error:", response.status_code, response.text)


def check_if_in_word(letter, word):
    letter_positions = [pos for pos, char in enumerate(word) if char == letter]
    return letter_positions


def print_current_state_of_word(revealed_letters, word):
    display_word = ''
    i = 0
    for letter in word:
        if i in revealed_letters:
            display_word = f'{display_word}{letter}'
        else:
            display_word = f'{display_word}_'
        i += 1
    print(display_word)


def get_letter_from_user(used_letters):
    invalid_response = True
    while invalid_response:
        print("Please enter a letter:")
        user_input = sys.stdin.readline().strip()
        if user_input in used_letters:
            print(f"You have already used {user_input}. Please guess another letter:")
        elif len(user_input) == 1:
            return user_input

def game_start():
    word = getpass.getpass('Input a word for your partner: ').strip()

    while (len(used_hangman_pieces) < len(hangman_pieces)) and (len(revealed_letters) < len(word)):
        print_current_state_of_word(revealed_letters, word)
        user_letter = get_letter_from_user(used_letters)
        used_letters.append(user_letter)
        letter_positions = check_if_in_word(user_letter, word)
        if not letter_positions:
            used_hangman_pieces.append(hangman_pieces[len(used_hangman_pieces)])
            print(f"Wrong letter! Your hangman now is: {used_hangman_pieces}")
        else:
            for pos in letter_positions:
                revealed_letters.append(pos)
        unused_letters = list(set(alphabet).difference(used_letters))
        print(f"Your unused letters are: {sorted(unused_letters)}")


    if len(revealed_letters) == len(word):
        print(f"Excellent! You guessed the word: {word}!")
    else:
        print(f"You're a loser. Try again another day. The word you couldn't seem to figure out was {word}.")


if __name__ == '__main__':
    repeat_play = 'y'
    while repeat_play.lower() == 'y' or repeat_play.lower() == 'yes':
        used_hangman_pieces = []
        revealed_letters = []
        used_letters = []
    #   word = get_word()
        game_start()
        print("Play again?")
        repeat_play = sys.stdin.readline().strip()
