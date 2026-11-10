print("~" * 40)
print()
print("   Welcome to Jargon Jumble!")
print("   A Tech-Themed Word Scramble Game")
print()
print("~" * 40)

import random
word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
]

ROUNDS = 5
round_num = 1
score = 0
used = []

while round_num <= ROUNDS:
    print(f"ROUND NUMBER - {round_num}")
    print()
    pick_a_word, hint = random.choice(word_bank)

    while (pick_a_word,hint) in used:
        pick_a_word, hint = random.choice(word_bank)

    used.append((pick_a_word,hint))

    list_a_word = list(pick_a_word)
    random.shuffle(list_a_word)
    print(f'Shuffle word is: {"".join(list_a_word)}')
    print()
    guess = input("Guess the Word or Type 'hint' to get a hint for the word or Type 'skip' to skip the word or Type 'quit' to quit the game: ").strip().lower()
    print()
        
    if guess == "hint":
        print(f"Hint: {hint}")
        print()
        guess = input("Guess the Word Now or Type 'skip' to skip the word or Type 'quit' to quit the game: ").strip().lower()
        print()

    if guess == "quit":
        print("Thanks for playing! Have a Great Day!")
        break
    elif guess == "skip":
        print(f"Skipped! The word was '{pick_a_word}'.")
    elif guess == pick_a_word:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Sorry, the word was '{pick_a_word}'.")

    print()
    round_num += 1

print(f"Final Score: {score}/{ROUNDS}")
print()
if score == 5:
    print("Flawless! All tests passing, zero bugs.")
elif score == 4:
    print("Near perfect, only one failing test!")
elif score == 3:
    print("Good effort! The code runs, and that's what counts.")
elif score < 3:
    print("Have you tried turning it off and on again?")