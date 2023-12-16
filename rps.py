
import random



action_list = ['rock', 'paper', 'scissors']


player1_score = 0 
player2_score = 0

round_counter = 0


total_round = input("How many rounds do you want to play? ") 



while True:

  
  round_counter +=1
  print("Round number:", round_counter)

  
  player1_choice = random.choice(action_list)
  player2_choice = action_list[random.randint(0,2)]

  
  print("Player1:", player1_choice)
  print("Player2:", player2_choice)

  
  if player1_choice == player2_choice:
    print("Tie! Both player chose same action.")

  
  elif player1_choice == 'paper':
    if player2_choice == 'rock':
      print("Winner is: Player 1")
      player1_score +=1
    else:
      print("Winner is: Player 2")
      player2_score +=1

  elif player1_choice == 'rock':
    if player2_choice == 'paper':
      print("Winner is: Player 2")
      player2_score +=1
    else:
      print("Winner is: Player 1")
      player1_score +=1

  elif player1_choice == 'scissors':
    if player2_choice == 'paper':
      print("Winner is: Player 1")
      player1_score +=1
    else:
      print("Winner is: Player 2")
      player2_score +=1

  
  print("Score:", "Player1 =",player1_score, "Player2 =",player2_score)

  
  
  if player1_score == int(int(total_round)/2)+1 or player2_score == int(int(total_round)/2)+1:
    
    break
 


if player1_score == player2_score:
  print("There is no winner, tie.")
elif player1_score > player2_score:
  print("Player 1 wins with score", player1_score, ":", player2_score)
elif player1_score < player2_score:
  print("Player 2 wins with score", player1_score, ":", player2_score)
