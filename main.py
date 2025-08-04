import curses as cs
from game.logic import winner
from game.game import (versus, show_winner, names)

def main(stdscr):
    player_names = names(stdscr)
    players_score = [0, 0]
    count_games = 0
    while True:
        vs = versus(stdscr, player_names)

        result = winner(vs)

        if result == "player1":
            count_games +=1
            players_score[0] +=1
        elif result == "player2":
            count_games +=1
            players_score[1] += 1 
        
        show_winner(stdscr, players_score, winner=result, names=player_names)
        
        if players_score[0] == 2:
            break
        elif players_score[1] == 2:
            break
    
        
if __name__ == "__main__":
    cs.wrapper(main)       
        

