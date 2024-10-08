import time
import threading

# Class karakter robot
class Character:
    def __init__(self, name: str, health: int, damage: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage

    def attack(self, target) -> None:
        target.health -= self.damage
        target.health = max(target.health, 0)  


# Pilih robot
def pilih_robot():
    print("Pilih robot yang akan kamu gunakan:")
    print("1. Robot Thunder (Health: 120, Damage: 7)")
    print("2. Robot Blaze (Health: 100, Damage: 10)")
    print("3. Robot Frost (Health: 80, Damage: 12)")

    pilihan = int(input("Masukkan pilihanmu (1/2/3): "))

    if pilihan == 1:
        return Character(name="Thunder", health=120, damage=7)
    elif pilihan == 2:
        return Character(name="Blaze", health=100, damage=10)
    elif pilihan == 3:
        return Character(name="Frost", health=80, damage=12)
    else:
        print("Pilihan tidak valid. Pilih lagi.")
        return pilih_robot()


# Uroboros menyerang player setiap 1 detik
def serang_terus(enemy, player):
    while enemy.health > 0 and player.health > 0:
        enemy.attack(player)
        print(f"{enemy.name} menyerang {player.name}! Health {player.name}: {player.health}")
        if player.health <= 0:
            print(f"{player.name} telah dikalahkan!")
            break
        time.sleep(1)  # Nyerang setiap 1 detik


# Fungsi utama permainan
def game():
    robot = pilih_robot()  # Pemain memilih robot
    enemy = Character(name="Uroboros", health=1000, damage=3)

    # Mulai thread untuk serangan musuh setiap 1 detik
    thread_enemy = threading.Thread(target=serang_terus, args=(enemy, robot))
    thread_enemy.start()

    # Player menyerang musuh dengan menekan tombol Enter
    while robot.health > 0 and enemy.health > 0:
        input(f"Tekan Enter untuk menyerang {enemy.name}!")
        robot.attack(enemy)
        print(f"{robot.name} menyerang {enemy.name}! Health {enemy.name}: {enemy.health}")

        if enemy.health <= 0:
            print(f"{enemy.name} telah dikalahkan!")
            break


if __name__ == "__main__":
    game()
