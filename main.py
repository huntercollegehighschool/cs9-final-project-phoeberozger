"""
Name(s): Phoebe Rozger
Name of Project: Hangman
"""
import random

words = ["algorithm", "cylinder", "bergamot", "discovery", "campfire", "paisley", "hexagon", "flourish", "fragment", "hydraulic", "porcelain", "carousel", "awestruck", "wistful", "birdcage", "tarnished", "locksmith"]

tries = 7
word = random.choice(words)
previously_guessed = []
obscured_word = "_" * len(word)
obscured_word_list = list(obscured_word)
letters_in_word = list(word)
correct = False
word_length = len(word)

print("Welcome to Hangman!")
print("Your word is:",obscured_word)

player_guess = input("Guess a letter or a word! You have seven tries to guess the correct word. ")

while tries > 0 and correct == False:
  if player_guess.isalpha() and len(player_guess) == 1:
    if player_guess in previously_guessed:
      print("You already guessed that.")
      print("You have",tries,"tries left.")
      player_guess = input("Guess another word or letter: ")
    elif player_guess not in letters_in_word:
      print("The letter",player_guess,"is not in the word." )
      tries = tries - 1
      previously_guessed.append(player_guess)
      print("The word is:",''.join(obscured_word_list))
      print("You have guessed:", previously_guessed)
      print("You have",tries,"tries left.")
      player_guess = input("Guess another word or letter: ")
    elif player_guess in letters_in_word:
      previously_guessed.append(player_guess)
      guess_index = letters_in_word.index(player_guess)
      obscured_word_list.pop(guess_index)
      obscured_word_list.insert(guess_index, player_guess)
      if obscured_word_list == letters_in_word:
        print("Congratulations,",word,"was the word!")
        correct = True
      elif obscured_word_list != letters_in_word: 
        print(player_guess,"is in the word!")
        print("The word is:",''.join(obscured_word_list))
        print("You have guessed:", previously_guessed)
        print("You have",tries,"tries left.")
        player_guess = input("Guess another word or letter: ")
  elif len(player_guess) == len(word) and player_guess.isalpha() and player_guess != word:
    tries = tries - 1
    print(player_guess,"is not the word.")
    previously_guessed.append(player_guess)
    print("You have guessed:", previously_guessed)
    print("You have",tries,"tries left.")
    player_guess = input("Guess another word or letter: ")
  elif player_guess == word:
    print("Congratulations,",player_guess,"was the word!")
    correct = True
  else: player_guess = input("Please enter a valid word or letter: ")

if tries == 0 and correct == False:
  print("You lost! The word was \"",word,"\".")