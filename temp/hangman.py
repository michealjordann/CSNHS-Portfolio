import random
words = ["python", "computer", "ascii", "school", "chatgpt", "coding"]

hangmen = [
    """
      +---+
      |   |
          |
          |
          |
          |
    ---------""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    ---------""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    ---------""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ---------""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    ---------""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    ---------""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ---------"""
]

def hangman():
    word = random.choice(words)
    guessed = ["_"] * len(word)
    used = []
    wrong = 0

    while wrong < 6 and "_" in guessed:
        #Display word count and used letters
        print(hangmen[wrong])
        print("Word:", " ".join(guessed))
        print("Used letters:", " ".join(used))
        #User input and check if its one letter
        guess = input("\nGuess a letter ").lower()

        if len(guess) != 1 or (guess.isalpha() == False):
            print("Enter a letter")
            continue

        #Check if letters are already used, and add to list of used letters
        already_used = False
        for letter in used:
            if letter == guess:
                already_used = True
                break

        if already_used:
            print("Already used")
            continue

        used.append(guess)

        #Check if letter is in the word
        correct = False
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
                correct = True

        if correct:
            print("That is in the word!")
        else:
            print("Not in the word")
            wrong += 1



    #Win or lose
    print(hangmen[wrong])
    if "_" not in guessed:
        print("You Win! The word was", word)
    else:
        print("You Lose! The word was", word)

hangman()
