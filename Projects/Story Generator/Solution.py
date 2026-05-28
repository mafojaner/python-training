# MAD LIBS STORY GENERATOR
# This program asks for words and creates a funny story

# STEP 1: Greet the user and explain the game
print("=" * 50)
print("Welcome to Mad Libs Story Generator!")
print("=" * 50)
print("I'll ask you for different types of words.")
print("Then I'll create a silly story using your words!")
print("-" * 50)

# STEP 2: Collect words from the user
# input() gets text from user
# .strip() removes any extra spaces before/after the word

# Ask for a person's name
name = input("Enter a name: ").strip()

# Ask for a place (like park, school, beach)
place = input("Enter a place (e.g., park, school, beach): ").strip()

# Ask for an adjective (describing word like happy, giant, purple)
adjective1 = input("Enter an adjective (describing word): ").strip()

# Ask for a noun (person, place, or thing)
noun1 = input("Enter a noun (e.g., dog, pizza, book): ").strip()

# Ask for a verb (action word like run, jump, sing)
verb1 = input("Enter a verb (action word): ").strip()

# Ask for another adjective
adjective2 = input("Enter another adjective: ").strip()

# Ask for a plural noun (more than one, like cats or trees)
plural_noun = input("Enter a plural noun (e.g., cats, cars, cookies): ").strip()

# Ask for an emotion (happy, sad, excited, scared)
emotion = input("Enter an emotion (e.g., happy, scared, excited): ").strip()

# Ask for a number (can be any whole number)
number = input("Enter a number: ").strip()

# Ask for another noun
noun2 = input("Enter one more noun: ").strip()

# STEP 3: Create the story by inserting the words
# Using f-string (format string) to put variables inside text
# The {} brackets show where each word goes

story = f"""
{'=' * 50}
📖 YOUR MAD LIBS STORY 📖
{'=' * 50}

One {adjective1} morning, {name} decided to go to {place}. 
As soon as {name} arrived, they saw a giant {noun1} that started to {verb1}!
"I can't believe my eyes!" shouted {name}, feeling very {emotion}.

Suddenly, {number} {adjective2} {plural_noun} appeared from behind the {noun1}.
They all wanted to join the {verb1} party! 
"I guess this is my life now," {name} laughed, picking up a {noun2} to join the fun.

Everyone danced together until sunset. It was the most {adjective1} day at {place}!
What a {adjective2} adventure!

{'=' * 50}
THE END
{'=' * 50}
"""

# STEP 4: Display the finished story
print("\n" + story)

# STEP 5: Optional - ask if user wants to play again
# This adds a loop to make the game repeatable
print("\nThanks for playing Mad Libs!")
print(f"Your words were: {name}, {place}, {adjective1}, {noun1}, {verb1}, {adjective2}, {plural_noun}, {emotion}, {number}, {noun2}")