import json;

data = {
    "player1": {
        "name": "Tonyn",
        "energy": 6,
        "movimientos": {
            "DSDP": {
                "energy": 3,
                "name": "Taladoken",
                "text": " usa un Taladoken"
            },
            "SDK": {
                "energy": 2,
                "name": "Remuyuken",
                "text": " conecta un Remuyuken"
            },
            "P": {
                "energy": 1,
                "name": "Puño",
                "text": " da un puñetazo"
            },
            "K": {
                "energy": 1,
                "name": "Patada",
                "text": " da una patada"
            },
        }
    },
    "player2": {
        "name": "Arnaldor",
        "energy": 6,
        "movimientos": {
            "SAK": {
                "energy": 3,
                "name": "Remuyuken",
                "text": " conecta un Remuyuken"
            },
            "ASAP": {
                "energy": 2,
                "name": "Taladoken",
                "text": " usa un Taladoken"
            },
            "P": {
                "energy": 1,
                "name": "Puño",
                "text": " da un puñetazo"
            },
            "K": {
                "energy": 1,
                "name": "Patada",
                "text": " da una patada"
            },
        }
    },
}

def get_order_player(player1, player2, fight_json, player1_moves, player2_moves, cont):
    cont += 1
    tmp = ["movimientos", "golpes"]
    order_player = []

    if cont == 2:
        order_player = [player1, player2]
        return order_player

    if player1_moves > player2_moves:
        order_player = [player2, player1]
    elif player2_moves > player1_moves:
        order_player = [player1, player2]
    else:
        player1_moves = len(fight_json[player1][tmp[cont]])
        player2_moves = len(fight_json[player2][tmp[cont]])
        order_player = get_order_player(player1, player2, fight_json, player1_moves, player2_moves, cont)

    return order_player

def main(fight_string):
    fight_json = json.loads(fight_string)

    player1 = list(fight_json.keys())[0]
    player2 = list(fight_json.keys())[1]
    
    player1_moves = len(fight_json[player1]["movimientos"]) + len(fight_json[player1]["golpes"])
    player2_moves = len(fight_json[player2]["movimientos"]) + len(fight_json[player2]["golpes"])
    order_player = get_order_player(player1, player2, fight_json, player1_moves, player2_moves, -1)

    for i in range(5):
        for player in order_player:
            action = ''
            try:
                action = fight_json[player]["movimientos"][i]
            except:
                pass
            try:
                action += fight_json[player]["golpes"][i]
            except:
                pass
            
            player_lost = [x for x in list(fight_json.keys()) if x != player][0]
            kick = False

            for move in list(data[player]['movimientos']):
                if move in action:
                    kick = True
                    player_move = "" if len(move) == len(action) else " se mueve y"
                    data[player_lost]["energy"] += (data[player]["movimientos"][move]["energy"] * -1)
                    print(f"{data[player]['name']}{player_move}{data[player]['movimientos'][move]['text']}")
                    break

            if not kick and action != '':
                print(f"{data[player]['name']} se mueve")
            
            if data[player_lost]["energy"] <= 0:
                print(f"{data[player]['name']} gana la pelea y aun le queda {data[player]['energy']} de energia")
                exit()

    if data[player1]['energy'] == data[player2]['energy']:
        print("Empate")
    elif data[player1]['energy'] > data[player2]['energy']:
        print(f"{data[player1]['name']} gana")
    else:
        print(f"{data[player2]['name']} gana")

if __name__=="__main__":
    main('{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}')
    #main('{"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"],"golpes":["K", "P", "K", "P"]},"player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "k"]}}')
    #main('{"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}} ')
