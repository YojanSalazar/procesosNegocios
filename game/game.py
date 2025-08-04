import curses  

opciones = ['Piedra', 'Papel', 'Tijera']

def seleccionar_opcion(stdscr, jugador):  
    curses.curs_set(0)  
    current_row = 0     

    while True:         
        stdscr.clear()  
        stdscr.addstr(0, 0, f"{jugador}, elige tu jugada:") 

        for i, opcion in enumerate(opciones):               
            if i == current_row:
                stdscr.attron(curses.A_REVERSE)            
                stdscr.addstr(i + 2, 0, opcion)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 0, opcion)

        key = stdscr.getch() 

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(opciones) - 1:
            current_row += 1
        elif key == ord('\n'): 
            return opciones[current_row]  


def show_winner(stdscr, current_score, winner, names):
    if winner == "empate":
        stdscr.clear()
        stdscr.addstr(0, 0, "¡Es un empate!")
        stdscr.refresh()
        stdscr.getch()
    else:
        curses.curs_set(0)
        stdscr.clear()
        stdscr.addstr(0,0, f"{names[winner]} gana")
        stdscr.addstr(1, 0, f"{names["player1"]}: {current_score[0]}")
        stdscr.refresh()
        stdscr.addstr(2, 0, f"{names["player2"]}: {current_score[1]}")
        stdscr.refresh()
        stdscr.getch()

def names(stdscr):
    curses.curs_set(0)
    
    curses.echo()
    
    stdscr.clear()
    stdscr.addstr(0, 0, "Ingrese el nombre del jugador 1:")
    stdscr.refresh()
    nombre1 = stdscr.getstr(1, 0, 20).decode('utf-8')

    stdscr.clear()
    stdscr.addstr(0, 0, "Ingrese el nombre del jugador 2:")
    stdscr.refresh()
    nombre2 = stdscr.getstr(1, 0, 20).decode('utf-8')

    curses.noecho()
    
    return {"player1": nombre1, "player2": nombre2}
    


def versus(stdscr, names):
    player1 = seleccionar_opcion(stdscr, f"{names['player1']}") 
    stdscr.clear()  
    stdscr.addstr(0, 0, f"¡Turno del {names['player2']}! Presiona una tecla...")
    stdscr.refresh()  
    stdscr.getch()    

    player2 = seleccionar_opcion(stdscr, f"{names['player2']}") 
    stdscr.clear()
    stdscr.addstr(0, 0, f"{names['player1']} eligió: {player1}")
    stdscr.addstr(1, 0, f"{names['player2']} eligió: {player2}")
    stdscr.refresh()
    stdscr.getch()

    return {
        "player1": player1,
        "player2": player2
    }

