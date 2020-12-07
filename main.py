game_is_on = True
current_player = 'x'
winner = None


def restart():
    print("\n")
    print("***********Let's play our game**********")
    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']

    def display_board():

        print('\n')
        print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' + '   | 1 | 2 | 3 |')
        print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ' + '   | 4 | 5 | 6 |')
        print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' + '   | 7 | 8 | 9 |')
        print('\n')

    display_board()

    def play_game():
        while game_is_on:
            handle_turn(current_player)
            cheak_if_game_over()
            flip_player()

        if winner == 'x' or winner == 'o':
            print(winner + ' won the match' + ' try next time ' + current_player)
            '''restart = 'yes'
            while True:

                if restart == 'yes':
                    restart = input("Do you want to play again:")
                    continue
                elif restart == 'no':
                    print("player don't want to play")
                    break'''

        else:
            print("Match Draw")

    def handle_turn(player):
        print(current_player + "'s turn..")
        postion = input("Enter a number form 1-9:")
        valid = False
        while not valid:
            while postion not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                postion = input("Please insert a number from 1-9:")
            postion = int(postion) - 1
            if board[postion] == '-':
                valid = True
            else:
                print("You have already insert this number...")
            board[postion] = player

            display_board()

    def cheak_if_game_over():
        cheak_for_winner()
        cheak_if_tie()

    def cheak_for_winner():
        global winner
        row_winner = cheak_row()
        column_winner = cheak_column()
        diagonal_winner = cheak_diagonal()

        if row_winner:
            winner = row_winner
        elif column_winner:
            winner = column_winner
        elif diagonal_winner:
            winner = diagonal_winner
        else:
            winner = None

    def cheak_row():
        global game_is_on
        row_1 = board[0] == board[1] == board[2] != '-'
        row_2 = board[3] == board[4] == board[5] != '-'
        row_3 = board[6] == board[7] == board[8] != '-'

        if row_1 or row_2 or row_3:
            game_is_on = False
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        return

    def cheak_column():
        global game_is_on
        column_1 = board[0] == board[3] == board[6] != '-'
        column_2 = board[1] == board[4] == board[7] != '-'
        column_3 = board[2] == board[5] == board[8] != '-'

        if column_1 or column_2 or column_3:
            game_is_on = False
            if column_1:
                return board[0]
            elif column_2:
                return board[1]
            elif column_3:
                return board[2]
            return

    def cheak_diagonal():
        global game_is_on
        diagonal_1 = board[0] == board[4] == board[8] != '-'
        diagonal_2 = board[6] == board[4] == board[2] != '-'

        if diagonal_1 or diagonal_2:
            game_is_on = False
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[6]
        return

    def cheak_if_tie():
        global game_is_on
        if '-' not in board:
            game_is_on = False
        else:
            return

    def flip_player():
        global current_player

        if current_player == 'x':
            current_player = 'o'
        elif current_player == 'o':
            current_player = 'x'
        else:
            return

    play_game()

    run_again = input("Do you want to restart it:")
    if run_again == 'yes'.lower():
        restart()
    elif run_again == 'no'.lower():
        print("player don't want to play")
    else:
        print("Invalid")


restart()


