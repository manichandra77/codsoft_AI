import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board represented as a list
        self.current_winner = None  # Track the winner

    def print_board(self):
        # This prints the board to the console
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # This prints the board with numbers indicating the positions (for player's reference)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(state, depth, alpha, beta, maximizing_player):
    max_player = 'X'  # The AI player
    other_player = 'O' if max_player == 'X' else 'X'

    # Check if the previous move is a winner
    if state.current_winner == other_player:
        return {'position': None, 'score': 1 * (depth + 1) if other_player == max_player else -1 * (depth + 1)}

    # Check if there are no empty squares
    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if maximizing_player:
        best = {'position': None, 'score': -float('inf')}
        for possible_move in state.available_moves():
            state.make_move(possible_move, max_player)
            sim_score = minimax(state, depth + 1, alpha, beta, False)  # Recursive call

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if sim_score['score'] > best['score']:
                best = sim_score

            alpha = max(alpha, sim_score['score'])
            if beta <= alpha:
                break
        return best

    else:
        best = {'position': None, 'score': float('inf')}
        for possible_move in state.available_moves():
            state.make_move(possible_move, other_player)
            sim_score = minimax(state, depth + 1, alpha, beta, True)  # Recursive call

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if sim_score['score'] < best['score']:
                best = sim_score

            beta = min(beta, sim_score['score'])
            if beta <= alpha:
                break
        return best

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter
    while game.empty_squares():
        if game.num_empty_squares() == 9:
            square = x_player.get_move(game)
        else:
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'  # Switch player

    if print_game:
        print('It\'s a tie!')

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # Random move if board is empty
        else:
            minimax_result = minimax(game, 0, -float('inf'), float('inf'), True)
            square = minimax_result['position']
        return square

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = AIPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
