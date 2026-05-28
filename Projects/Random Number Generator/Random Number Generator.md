# How the game works:
Line 2: Imports Python's random module so we can generate random numbers

Line 5: Shows a welcome message

Line 8: Asks for the maximum range (e.g., if you type 20, numbers will be 1-20)

Line 11: random.randint() picks a secret number between 1 and your max

Line 14: attempts = 0 starts the counter at zero

Line 17: guess = None creates an empty placeholder

Line 20: while guess != secret_number keeps looping until correct

Line 22-23: Gets the player's guess

Line 26: Adds 1 to attempts each guess

Line 29-35: Gives hints (too high, too low, or correct)

Line 38: Game over message

Example gameplay: