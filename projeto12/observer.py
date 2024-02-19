class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.notify(message)

class BattleSubject(Subject):
    def __init__(self):
        super().__init__()
        self.last_battle_result = None

    def finish_battle(self, result):
        self.last_battle_result = result
        self.notify_observers(result)

    def get_last_battle_result(self):
        return self.last_battle_result
    
    def get_observers(self):
        return self._observers

    def get_last_battle_result(self):
        return self.last_battle_result
    
    def add_player(self, player):
        self.players.append(player)
        self.notify_observers(f"Jogador {player.name} foi adicionado à batalha.")

class Observer:
    def notify(self, message):
        pass

class Territory:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner  # Proprietário do território


class PlayerObserver(Observer):
    def __init__(self, name):
        self.name = name
        self.territories = {}  # Armazena territórios do jogador

    def notify(self, message):
        print(f"Jogador {self.name}: {message}")

    def place_armies(self, territory, armies):
        if territory.owner == self.name:
            # Adicione lógica para colocar exércitos no território
            if territory in self.territories:
                self.territories[territory] += armies
            else:
                self.territories[territory] = armies
            print(f"Jogador {self.name}: Coloquei {armies} exércitos em {territory}.")
        else:
            print("Operação negada: Território pertence a outro jogador.")

battle_subject = BattleSubject()
