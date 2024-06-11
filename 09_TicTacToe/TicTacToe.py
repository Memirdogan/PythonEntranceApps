board = [" " for _ in range(9)]


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def get_move(board, player):
    while True:
        try:
            move = int(input(f"Oyuncu {player}, Hamlenizi girin (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                return move
            else:
                print("geçersiz hamle, tekrar deneyiniz!")
        except ValueError:
            print("lütfen (1-9) arasında sayı giriniz")


def make_move(board, move, player):
    board[move] = player


def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_draw(board):
    return " " not in board


def main():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        move = get_move(board, current_player)
        make_move(board, move, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"oyuncu {current_player}, Kazandı!")
            break

        if check_draw(board):
            print_board(board)
            print("Beraberlik!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == '__main__':
    main()
