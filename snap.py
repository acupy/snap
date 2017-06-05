from models import Player, SnapException
from controllers import GameEngine, GameType


def main():
    player1 = Player('Jekyll')
    player2 = Player('Hyde')
    try:
        gameEngine = GameEngine(2, GameType.value_match)
        gameEngine.play((player1, player2))
    except SnapException as ex:
        print ex
    # A lot more exception handling ...

if __name__ == "__main__":
    main()
