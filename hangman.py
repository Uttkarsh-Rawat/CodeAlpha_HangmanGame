import random

words = ["python", "coding", "computer", "program", "developer"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("===== WELCOME TO HANGMAN GAME =====")

while wrong_guesses < max_attempts:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You Won!")
        print("The word was:", word)
        break

else:
    print("\nGame Over!")
    print("The correct word was:", word)