def winner(versus):
    rules = {
        "Piedra": "Tijera",
        "Tijera": "Papel",
        "Papel": "Piedra"
    }

    if versus["player1"] == versus["player2"]:
        print("Empate")
        return "empate"
        
    elif rules[versus["player1"]] == versus["player2"]:
        print("Jugador 1 gana")
        return "player1"
    else:
        print("Jugador 2 gana")
        return "player2"
    