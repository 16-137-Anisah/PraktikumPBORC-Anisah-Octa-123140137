class Character:
    def __init__(self, name, anime, power, health):
        self.name = name
        self.anime = anime
        self.power = power
        self.health = health
        self.defense_mode = False
        self.bonus_active = False
        self.bonus_used = False
    
    def attack(self, opponent):
        attack_power = self.power * 2 if self.bonus_active else self.power
        print(f"{self.name} menyerang {opponent.name} dengan kekuatan {attack_power}!")
        
        damage = attack_power
        if opponent.defense_mode:
            damage //= 2
            opponent.defense_mode = False
        
        opponent.health -= damage
        if opponent.health <= 0:
            print(f"{opponent.name} kalahhhh!")
        else:
            print(f"{opponent.name} sekarang memiliki {opponent.health} HP.")
        
        if self.bonus_active:
            self.bonus_active = False
            print(f"{self.name} sudah memakai bonus!")
        
    def heal(self, amount):
        heal_amount = amount * 3 if self.bonus_active else amount
        self.health += heal_amount
        print(f"{self.name} memulihkan {heal_amount} HP! Sekarang memiliki {self.health} HP.")
        
        if self.bonus_active:
            self.bonus_active = False
            print(f"{self.name} sudah memakai bonus!")
    
    def defend(self):
        self.defense_mode = True
        print(f"{self.name} bersiap bertahan, serangan berikutnya akan lebih lemah!")
    
    def activate_bonus(self):
        if not self.bonus_used:
            self.bonus_active = True
            self.bonus_used = True
            print(f"{self.name} mengaktifkan mode bonus!")
        else:
            print(f"{self.name} penggunaan mode bonus maksimal 1 kali!")
    
    def show_status(self):
        print(f"Nama: {self.name}, Anime: {self.anime}, Power: {self.power}, Health: {self.health}")

class Game:
    def __init__(self, chara1, chara2):
        self.chara1 = chara1
        self.chara2 = chara2
        self.round = 1
    
    def start_battle(self):
        print("\n=== PERTARUNGAN DIMULAI! ===")
        
        while self.chara1.health > 0 and self.chara2.health > 0:
            print(f"\nRound-{self.round} ==========================================================")
            self.chara1.show_status()
            self.chara2.show_status()
            
            for chara, opponent in [(self.chara1, self.chara2), (self.chara2, self.chara1)]:
                print("\n1. Attack     2. Heal     3. Defend     4. Activate Bonus     5. Giveup")
                action = input(f"{chara.name}, pilih aksi: ")
                
                if action == "1":
                    chara.attack(opponent)
                elif action == "2":
                    chara.heal(20)
                elif action == "3":
                    chara.defend()
                elif action == "4":
                    chara.activate_bonus()
                elif action == "5":
                    print(f"{opponent.name} menang!")
                    return
            
            self.round += 1
        
        winner = self.chara1 if self.chara1.health > 0 else self.chara2
        print(f"{winner.name} menang!")

def main():
    char1 = Character("Lelouch", "Code Geass", 50, 300)
    char2 = Character("Light Yagami", "Death Note", 50, 300)
    
    game = Game(char1, char2)
    game.start_battle()

if __name__ == "__main__":
    main()
