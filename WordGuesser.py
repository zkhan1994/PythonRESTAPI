def guessLetter():

    letters = ["f", "o", "x"]
    guessedLetters = []

    while len(guessedLetters) < len(letters):
        lets = input("Enter letter: ")

        if lets in letters and lets not in guessedLetters:
            guessedLetters.append(lets)
            print(f"Congrats! You've found a new letter: {lets}")
        else:
            print("Incorrect or already guessed letter.")

        print(f"Current guessed letters: {guessedLetters}")

    print("Congrats! You won.")


guessLetter()
