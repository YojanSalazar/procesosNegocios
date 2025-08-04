import curses as cs
from game.logic import winner
from game.game import (versus, show_winner, names, start_game, show_winner_round)

def main(stdscr):
    games_score = [0, 0]
    player_names = names(stdscr)
    n_rounds = int(int(start_game(stdscr)) / 2 + 1)
    while True:
        

        round_winner = round(stdscr, player_names, n_rounds)

        if round_winner == "player1":
            games_score[0] += 1
        else:
            games_score[1] += 1


        show_winner_round(stdscr, games_score, winner=round_winner, names=player_names)


        stdscr.clear()
        stdscr.addstr(0, 0, "¿Quieres jugar otra vez? (s/n)")
        stdscr.refresh()
        if stdscr.getch() != ord('s'):
            break

    stdscr.clear()
    stdscr.addstr(0, 0, "¡Gracias por jugar!")
    stdscr.refresh()
    stdscr.getch()
    


def round(stdscr, player_names, n_rounds):
    players_score = [0, 0]
    while True:
        vs = versus(stdscr, player_names)

        result = winner(vs)

        if result == "player1":
            players_score[0] +=1
        elif result == "player2":
            players_score[1] += 1 
        
        show_winner(stdscr, players_score, winner=result, names=player_names)
        
        if players_score[0] == n_rounds or players_score[1] == n_rounds:
            if players_score[0] > players_score[1]:
                round_winner = "player1"
            else:
                round_winner = "player2"
            return round_winner

if __name__ == "__main__":
    cs.wrapper(main)


