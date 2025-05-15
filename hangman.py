import random
word_list = ["apple","ball","cat"]
lives = 6
chosen_word = random.choice(word_list)
display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)  
game = False
while not game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game = True
            print("You lose!!")
        elif '_' not in display:
            game = True
            print("You Win!!")
