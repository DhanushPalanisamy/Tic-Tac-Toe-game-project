# tic tac toe
# tic tac toe

[x]: draw a board
[x]: input player Name
[x]: put sign to each player
[x]: if they do not input between (1,9), direct them to previous state
[x]: if they do not input between (1,9), direct them to previous state 
[X]: put sign to exact spot
[X]: print board after each input
[x]: calculate and show result


import sys

instructions = 
This will be our tic tac toe board
@@ -26,82 +23,74 @@
3. Player 1 will go first.

sign_dict = [[], [], [], [], [], [], [], [], []]
sign_dict = []

for i in range(9):
    sign_dict[i].append(' ')
    sign_dict.append(' ')


def print_board():
    board = f
def print_board(sign_dict):
  board = f
{sign_dict[0][0]} | {sign_dict[1][0]} | {sign_dict[2][0]}
{sign_dict[0]} | {sign_dict[1]} | {sign_dict[2]}
---|---|---
{sign_dict[3][0]} | {sign_dict[4][0]} | {sign_dict[5][0]}
{sign_dict[3]} | {sign_dict[4]} | {sign_dict[5]}
---|---|---
{sign_dict[6][0]} | {sign_dict[7][0]} | {sign_dict[8][0]}
{sign_dict[6]} | {sign_dict[7]} | {sign_dict[8]}
""
print(board)
print(board)


index_list = []


def take_input(player_name):
    while True:
        x = int(input(f'{player_name}: '))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print('This spot is blocked.')
                continue
            index_list.append(x)
            return x
        print('Please Enter number between 1-9')


def result_calculation(player_one, player_two):
    if sign_dict[0][0] == sign_dict[1][0] == sign_dict[2][0] == 'X' or sign_dict[1][0] == sign_dict[4][0] == \
            sign_dict[7][0] == 'X' or sign_dict[0][0] == sign_dict[4][0] == sign_dict[8][0] == 'X' or sign_dict[2][0] == \
            sign_dict[5][0] == sign_dict[8][0] == 'X' or sign_dict[3][0] == sign_dict[4][0] == sign_dict[5][0] == 'X' or \
            sign_dict[2][0] == sign_dict[4][0] == sign_dict[6][0] == 'X' or sign_dict[6][0] == sign_dict[7][0] == \
            sign_dict[8][0] == 'X' or sign_dict[0][0] == sign_dict[3][0] == sign_dict[6][0] == 'X':
        print(f 'Congratulations {player_one}. You WON.!!'')
        sys.exit("Thank you both for joining")
    elif sign_dict[0][0] == sign_dict[1][0] == sign_dict[2][0] == 'O' or sign_dict[1][0] == sign_dict[4][0] == \
            sign_dict[7][0] == 'O' or sign_dict[0][0] == sign_dict[4][0] == sign_dict[8][0] == 'O' or sign_dict[2][0] == \
            sign_dict[5][0] == sign_dict[8][0] == 'O' or sign_dict[3][0] == sign_dict[4][0] == sign_dict[5][0] == 'O' or \
            sign_dict[2][0] == sign_dict[4][0] == sign_dict[6][0] == 'O' or sign_dict[6][0] == sign_dict[7][0] == \
            sign_dict[8][0] == 'O' or sign_dict[0][0] == sign_dict[3][0] == sign_dict[6][0] == 'O':
        print(f'Congratulations {player_two}. You WON.!!')
        sys.exit("Thank you both for joining")
    else:
        return
  while True:
    x = int(input(f'{player_name}: '))
    x -= 1
    if 0 <= x < 10:
      if x in index_list:
        print('This spot is blocked.')
        continue
      index_list.append(x)  
      return x
    print('Please Enter number between 1-9')


def result_calculation(sign_dict, player_one, player_two):
  if sign_dict[0] == sign_dict[1] == sign_dict[2] == 'X' or sign_dict[1] == sign_dict[4] == sign_dict[7] == 'X' or sign_dict[0] == sign_dict[4] == sign_dict[8] == 'X' or sign_dict[2] == sign_dict[5] == sign_dict[8] == 'X' or sign_dict[3] == sign_dict[4] == sign_dict[5] == 'X' or sign_dict[2] == sign_dict[4] == sign_dict[6] == 'X' or sign_dict[6] == sign_dict[7] == sign_dict[8] == 'X' or sign_dict[0] == sign_dict[3] == sign_dict[6] == 'X' :
    print(f'Congratulations {player_one}. You WON.!!')
    quit('Thank you both for joining')
  elif sign_dict[0] == sign_dict[1] == sign_dict[2] == 'O' or sign_dict[1] == sign_dict[4] == sign_dict[7] == 'O' or sign_dict[0] == sign_dict[4] == sign_dict[8] == 'O' or sign_dict[2] == sign_dict[5] == sign_dict[8] == 'O' or sign_dict[3] == sign_dict[4] == sign_dict[5] == 'O' or sign_dict[2] == sign_dict[4] == sign_dict[6] == 'O' or sign_dict[6] == sign_dict[7] == sign_dict[8] == 'O' or sign_dict[0] == sign_dict[3] == sign_dict[6] == 'O' :
    print(f'Congratulations {player_two}. You WON.!!')
    quit('Thank you both for joining')
  else:
    return


def main():
    print("Welcome to sunny's tic tac toe game.!!")
    player_one = input("Enter player 1 name: ")
    player_two = input("Enter player 2 name: ")
    print(f"Thank you for joining Mr./Mrs. {player_one} and Mr./Mrs. {player_two}")
    print(instructions)
    print(f"Mr. {player_one}'s sign is - X")
    print(f"Mr. {player_two}'s sign is - O")
    input("Enter any key to start the game: ")
    print_board()
    for i in range(0, 9):
        if i % 2 == 0:
            index = take_input(player_one)
            sign_dict[index][0] = 'X'
        else:
            index = take_input(player_two)
            sign_dict[index][0] = 'O'

        print_board()
        result_calculation(player_one, player_two)

    print("This is a tie..!! Nobody won. Play Again.")


  print("Welcome to sunny's tic tac toe game.!!")
  player_one = input("Enter player 1 name: ")
  player_two = input("Enter player 2 name: ")
  print(f"Thank you for joining Mr./Mrs. {player_one} and Mr./Mrs. {player_two}")
  print(instructions)
  print(f"Mr. {player_one}'s sign is - X")
  print(f"Mr. {player_two}'s sign is - O")
  input("Enter any key to start the game: ")
  print_board(sign_dict)
  for i in range(0,9):
    if i%2 == 0:
      index = take_input(player_one)
      sign_dict[index] = 'X'
    else:
      index = take_input(player_two)
      sign_dict[index] = 'O'

    print_board(sign_dict)
    result_calculation(sign_dict, player_one, player_two)


  print("This is a tie..!! Nobody won. Play Again.")



main()