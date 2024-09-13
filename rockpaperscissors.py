import random

count_rock=0
count_paper=0
count_scissors=0

def update_counts(user_input):#counts how many rock, paper, scissors have been played by the user
  turn=user_input
  global count_rock,count_paper,count_scissors 
  if turn==0:
    count_rock+=1
  if turn==1:
    count_paper+=1
  if turn==2:
    count_scissors+=1

def predict():#predicts good move based on basic human psychology using counts of rock paper scissor previously played
  global pred
  if count_rock > count_paper and count_rock > count_scissors:#user prefers rock
    pred = 0
  elif count_paper > count_rock and count_paper > count_scissors:#user prefers paper
    pred = 1
  elif count_scissors > count_rock and count_scissors > count_paper:#user prefers scissors
    pred = 2
  else:#user preference cannot be decided
    pred= random.randint(0,2)

player_score=0
comp_score=0

def update_scores(user_input):#score calculating function
  global player_score, comp_score
  predict()
  if user_input == 0:
    if pred == 0:
      print("\nYou played ROCK, computer played ROCK.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played ROCK, computer played PAPER.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played ROCK, computer played SCISSORS.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    
  elif user_input == 1:
    if pred == 0:
      print("\nYou played PAPER, computer played ROCK.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played PAPER, computer played PAPER.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played PAPER, computer played SCISSORS.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    
  else:
    if pred == 0:
      print("\nYou played SCISSORS, computer played ROCK.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif pred == 1:
      print("\nYou played SCISSORS, computer played PAPER.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    else:
      print("\nYou played SCISSORS, computer played SCISSORS.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
comp_score=0
player_score=0
count_rock=0
count_scissors=0
count_paper=0
valid_entries = ['0', '1', '2']
while True:
  user_input= input("Enter 0=ROCK, 1=PAPER, or 2=SCISSORS: ")
  while user_input not in valid_entries:#To manage errors when a wrong input is given
    print("Invalid input!!")
    user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")
  user_input= int(user_input)
  update_scores(user_input)
  update_counts(user_input)
  
  if comp_score == 10:
    print("Computer Won!")
    break  
  elif player_score == 10:
    print("You won!")  
    break