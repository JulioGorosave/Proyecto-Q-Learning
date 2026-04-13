# q_learning.py

import random
import pickle
from game_logic import *

alpha = 0.1
gamma = 0.9
epsilon = 0.3

Q = {}

def board_to_string(board):
    return str(board.reshape(ROWS * COLS))

def choose_action(state, valid_actions):
    if random.uniform(0,1) < epsilon:
        return random.choice(valid_actions)
    
    q_values = [Q.get((state, a), 0) for a in valid_actions]
    return valid_actions[q_values.index(max(q_values))]

def save_q():
    with open("q_table.pkl", "wb") as f:
        pickle.dump(Q, f)

def load_q():
    global Q
    try:
        with open("q_table.pkl", "rb") as f:
            Q = pickle.load(f)
    except:
        Q = {}

def train(episodes=20000):
    global epsilon

    for ep in range(episodes):
        board = create_board()
        state = board_to_string(board)
        done = False

        while not done:
            valid = get_valid_locations(board)
            action = choose_action(state, valid)

            drop_piece(board, action, 1)

            if check_win(board, 1):
                reward = 1
                done = True
                new_state = board_to_string(board)

            else:
                valid = get_valid_locations(board)
                if valid:
                    opponent_move = random.choice(valid)
                    drop_piece(board, opponent_move, 2)

                    if check_win(board, 2):
                        reward = -1
                        done = True
                    else:
                        reward = -0.01
                else:
                    reward = 0
                    done = True

                new_state = board_to_string(board)

            old_q = Q.get((state, action), 0)
            future_q = max([Q.get((new_state, a), 0) for a in get_valid_locations(board)] or [0])

            Q[(state, action)] = old_q + alpha * (reward + gamma * future_q - old_q)

            state = new_state

        epsilon = max(0.01, epsilon * 0.995)

        if ep % 2000 == 0:
            print(f"Episodio {ep}")

    save_q()