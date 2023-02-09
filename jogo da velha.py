board = [' ' for x in range(9)]
players = ('X', 'O')

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print("Sua vez player {} ({}):".format(number, icon))
    choice = int(input("Selecione um espaço (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("Esse espaço já está preenchido!")

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

def select_mode():
    print("Jogo da Velha Game Modes:")
    print("1. Player vs Player")
    print("2. Player vs Computer (Coming soon)")
    print("3. Quit")
    mode = int(input("Digite sua escolha: ").strip())
    return mode

def play_game():
    print(" Jogo da velha\n")
    print_board()
    while True:
        for player in players:
            player_move(player)
            print_board()
            if is_victory(player):
                print("{} wins! Congratulations!".format(player))
                return
            elif is_draw():
                print("Deu empate!")
                return

while True:
    mode = select_mode()
    if mode == 1:
        play_game()
    elif mode == 2:
        print("Esse modo de jogo estará disponível em breve!")
    elif mode == 3:
        print("Obrigado por jogar o jogo da velha!")
        break
    else:
        print("Opção inválida! Digite uma opção válida.")

while True:
    answer = input("Quer jogar novamente! (Y/N): ").strip().upper()
    if answer == 'Y':
        board = [' ' for x in range(9)]
        play_game()
    elif answer == 'N':
        print("Obrigado por jogar o jogo da velha!")
        break
    else:
        print("Opção inválida! Digite uma opção válida")

