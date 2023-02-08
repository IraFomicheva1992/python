# Создайте программу для игры в ""Крестики-нолики"".

def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print ('-------------')

def move_player(sign, board):
    check = False
    while not check:
        move = input('номер ячейки, куда поставить ' + sign + ': ')
        try:
            move = int(move)
        except:
            print('ввод числа')
        if move >= 1 and move <= 9:
            if str(board[move - 1]) not in 'XO':
                board[move - 1] = sign
                check = True
            else:
                print('ячейка занята')
        else:
            print('ввод числа от 1 до 9')

def control_win(board):
    coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in coordinates:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False