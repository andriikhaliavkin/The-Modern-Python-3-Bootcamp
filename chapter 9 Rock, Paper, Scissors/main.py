# print('init')
# from multiprocessing import RLock
import random
ai_choice = random.choice(['rock', 'paper', 'scissors'])
human_choice = input('Your choice?: ').lower()

if human_choice != 'rock' and human_choice != 'paper' and human_choice != 'scissors':
  print('You should choose only among rock / paper / scissors')
elif human_choice == ai_choice:
  print('Draw')
elif (human_choice == 'rock' and ai_choice == 'scissors') or (human_choice == 'scissors' and ai_choice == 'paper') or (human_choice == 'paper' and ai_choice == 'rock'):
  print("Human wins")
else:
  print("Ai wins")