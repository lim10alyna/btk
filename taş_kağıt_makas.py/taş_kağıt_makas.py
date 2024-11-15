import random

# Abstract Player sınıfı
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.moves = []

    def make_move(self):
        pass

    def add_score(self):
        self.score += 1

    def record_move(self, move):
        self.moves.append(move)

    def show_moves(self):
        print(f"{self.name}'in Hamleleri: {', '.join(self.moves)}")


# HumanPlayer sınıfı
class HumanPlayer(Player):
    def make_move(self):
        move = input(f"{self.name}, hamleni seç (taş, kağıt, makas): ").lower()
        while move not in ["taş", "kağıt", "makas"]:
            move = input("Geçersiz hamle! Lütfen tekrar seç (taş, kağıt, makas): ").lower()
        self.record_move(move)
        return move


# RandomComputerPlayer sınıfı
class RandomComputerPlayer(Player):
    def make_move(self):
        move = random.choice(["taş", "kağıt", "makas"])
        self.record_move(move)
        print(f"Bilgisayar {self.name} hamlesini yaptı: {move}")
        return move


# Oyun Sonucu Kontrolü
def determine_winner(move1, move2):
    if move1 == move2:
        return "Beraberlik"
    elif (move1 == "taş" and move2 == "makas") or (move1 == "kağıt" and move2 == "taş") or (move1 == "makas" and move2 == "kağıt"):
        return "Oyuncu"
    else:
        return "Bilgisayar"


# Oyun Döngüsü
def play_game():
    player_name = input("Oyuncu Adı: ")
    human = HumanPlayer(player_name)
    computer = RandomComputerPlayer("Bilgisayar")

    while True:
        print("\n--- Yeni Tur ---")
        human_move = human.make_move()
        computer_move = computer.make_move()

        result = determine_winner(human_move, computer_move)

        if result == "Oyuncu":
            print(f"{human.name} kazandı!")
            human.add_score()
        elif result == "Bilgisayar":
            print(f"Bilgisayar kazandı!")
            computer.add_score()
        else:
            print("Beraberlik!")

        print(f"Skor: {human.name} {human.score} - Bilgisayar {computer.score}")

        cont = input("Devam etmek ister misiniz? (evet/hayır): ").lower()
        if cont != "evet":
            break

    print("\nOyun Bitti!")
    print(f"Final Skor: {human.name} {human.score} - Bilgisayar {computer.score}")
    human.show_moves()
    computer.show_moves()


if __name__ == "__main__":
    play_game()
