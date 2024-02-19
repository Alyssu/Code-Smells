from flask import Blueprint, jsonify
from observer import battle_subject, PlayerObserver

app_bp = Blueprint('app', __name__)

@app_bp.route('/battle/<result>', methods=['GET'])
def finish_battle(result):
    valid_results = ['win', 'lose', 'draw']  # Defina os resultados válidos
    if result not in valid_results:
        return jsonify({"error": "Resultado inválido"}), 400
    battle_subject.finish_battle(result)
    return jsonify({"message": "Batalha finalizada. Observadores notificados."})

@app_bp.route('/register/<player_name>', methods=['GET'])
def register_observer(player_name):
    observer = PlayerObserver(player_name)
    battle_subject.add_observer(observer)
    return jsonify({"message": f"Jogador {player_name} registrado como observador."})

@app_bp.route('/info', methods=['GET'])
def get_info():
    battle_result = battle_subject.get_last_battle_result()
    observers = [observer.name for observer in battle_subject.get_observers()]
    return jsonify({"battle_result": battle_result, "observers": observers})

@app_bp.route('/place_armies/<player_name>/<territory_name>/<int:armies>', methods=['GET'])
def place_armies(player_name, territory_name, armies):
    player_observer = next((observer for observer in battle_subject.get_observers() if observer.name == player_name), None)
    if player_observer:
        territory = next((territory for territory in player_observer.territories if territory.name == territory_name), None)
        if territory:
            player_observer.place_armies(territory, armies)
            return jsonify({"message": f"Exércitos colocados em {territory_name}."})
        else:
            return jsonify({"error": "Território não encontrado"}), 404
    else:
        return jsonify({"error": "Jogador não encontrado"}), 404
    
@app_bp.route('/add_player/<player_name>', methods=['GET'])
def add_player(player_name):
    player = PlayerObserver(player_name)
    battle_subject.add_player(player)
    return jsonify({"message": f"Jogador {player_name} adicionado à batalha."})
