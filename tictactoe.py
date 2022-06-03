board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
global filled
filled = False
def display(board):
  print(board[0] + '|' + board[1] + '|' + board[2])
  print(board[3] + '|' + board[4] + '|' + board[5])
  print(board[6] + '|' + board[7] + '|' + board[8])

player1 = ' '
player2 = ' '
while player1 != 'X' or player1 != '0':
  player1 = input('Player1 please pick a marker "X" or "0" ')
  if player1 == '0':
    player2 = 'X'
    break
  elif player1 == 'X':
    player2 ='0'
    break
  else :
    player1 = input("choose either 'X' or '0'")
    continue

while not filled:
  try:
    position = int(input('player1 Please enter an index: '))    
  except ValueError:
    print("Not an integer!")
    continue
  else:  
    board[position] = player1
    display(board)
    if board[0] == '0' and board[3] == '0' and board[6] == '0' or board[1] == '0' and board[4] == '0' and board[7] == '0' or board[2] == '0' and board[5] == '0' and board[8] == '0' or board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
      filled = True
      print('You won!!')
      break
    elif board[1] == '0' and board[2] == '0' and board[0] =='0' or board[3] == '0' and board[4] == '0' and board[5] =='0' or board[6] == '0' and board[7] == '0' and board[8] =='0' or board[1] == 'X' and board[2] == 'X' and board[0] =='X' or board[3] == 'X' and board[4] == 'X' and board[5] =='X' or board[6] == 'X' and board[7] == 'X' and board[8] =='X':
      filled = True
      print('You won!!')
      break
    elif board[0] =='0' and board[4] ==  '0' and board[8]=='0' or board[6] == '0' and board[4] == '0' and board[2] == '0' or board[0] =='X' and board[4] ==  'X' and board[8]=='X' or board[6] == 'X' and board[4] == 'X' and board[2] == 'X':
      filled = True
      print('You won!!')
      break
  
  finally:
    if filled != True:
      try:
        position2 = int(input('player2 Please enter an index: '))
      except ValueError:
        print("Not an integer!")
      else:  
        board[position2] = player2
        display(board)
  if board[0] == '0' and board[3] == '0' and board[6] == '0' or board[1] == '0' and board[4] == '0' and board[7] == '0' or board[2] == '0' and board[5] == '0' and board[8] == '0' or board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
    filled = True
    print('You won!!')
    break
  elif board[1] == '0' and board[2] == '0' and board[0] =='0' or board[3] == '0' and board[4] == '0' and board[5] =='0' or board[6] == '0' and board[7] == '0' and board[8] =='0' or board[1] == 'X' and board[2] == 'X' and board[0] =='X' or board[3] == 'X' and board[4] == 'X' and board[5] =='X' or board[6] == 'X' and board[7] == 'X' and board[8] =='X':
    filled = True
    print('You won!!')
    break
  elif board[0] =='0' and board[4] ==  '0' and board[8]=='0' or board[6] == '0' and board[4] == '0' and board[2] == '0' or board[0] =='X' and board[4] ==  'X' and board[8]=='X' or board[6] == 'X' and board[4] == 'X' and board[2] == 'X':
    filled = True
    print('You won!!')
    break