import json
import os
import random
import time
from cryptography.fernet import Fernet



def generate_key():
    key_file_path = "encryption_key.key"
    if not os.path.exists(key_file_path):
        key = Fernet.generate_key()
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)
        print("New encryption key generated and saved.")
    else:
        print("Existing encryption key loaded.")

generate_key()

def load_key():
    """
    Loads the Fernet key from the file.
    """
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
    return key

key = load_key()
cipher_suite = Fernet(key)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Farm:
    def __init__(self):
        self.cotton = 0
        self.cotton_per_second = 1
        self.cotton_per_click = 1
        self.click_multiplier_cost = 10
        self.click_multiplier = 1
        self.auto_cotton_multiplier_cost = 100
        self.auto_cotton_multiplier = 0
        self.total_clicks = 0
        self.money = 0
        self.current_season = "Spring"
        self.season_effects = {
            "Spring": {
                "cotton_per_second": 1.2,
                "cotton_per_click": 1.1
            },
            "Summer": {
                "cotton_per_second": 1,
                "cotton_per_click": 1
            },
            "Autumn": {
                "cotton_per_second": 0.8,
                "cotton_per_click": 0.9
            },
            "Winter": {
                "cotton_per_second": 0.5,
                "cotton_per_click": 0.7
            }
        }
        self.season_change_time = time.time() + random.randint(600, 900)
        self.shop_items = {
            "1": {
                "name": "Fertilizer",
                "cost": 50,
                "effect": 2,
                "description": "Increases cotton per second by 2"
            },
            "2": {
                "name": "Scarecrow",
                "cost": 100,
                "effect": 5,
                "description": "Increases cotton per second by 5"
            },
            "3": {
                "name": "Harvester",
                "cost": 200,
                "effect": 0,
                "description": "Automatically harvests cotton"
            },
        }
        self.upgrades = {
            "1": {
                "name": "Advanced Tools",
                "cost": 500,
                "effect": 2,
                "description": "Increases cotton per click by 2"
            },
            "2": {
                "name": "Irrigation System",
                "cost": 1000,
                "effect": 5,
                "description": "Increases cotton per second by 5"
            },
            "3": {
                "name": "High-Yield Seeds",
                "cost": 2000,
                "effect": 10,
                "description": "Increases cotton per second by 10"
            },
        }
        self.objectives = {
            "1": {
                "name": "Harvest 1000 Cotton",
                "reward": 500,
                "completed": False
            },
            "2": {
                "name": "Reach 100 Total Clicks",
                "reward": 300,
                "completed": False
            },
            "3": {
                "name": "Earn 5000 Money",
                "reward": 800,
                "completed": False
            },
        }
        self.achievements = {
            "Harvest King": {
                "description": "Harvest 10000 cotton",
                "reward": 1000,
                "completed": False
            },
            "Click Master": {
                "description": "Reach 500 total clicks",
                "reward": 800,
                "completed": False
            },
            "Wealthy Farmer": {
                "description": "Earn 10000 money",
                "reward": 1200,
                "completed": False
            },
        }
        self.interactions_enabled = True

    def change_season(self):
        if time.time() >= self.season_change_time:
            seasons = ["Spring", "Summer", "Autumn", "Winter"]
            self.current_season = random.choice(seasons)
            self.season_change_time = time.time() + random.randint(600, 900)
            print(f"The season has changed to {self.current_season}.")

    def harvest_cotton(self):
        if self.interactions_enabled:
            season_effect = self.season_effects[self.current_season]["cotton_per_click"]
            self.cotton += int(self.cotton_per_click * self.click_multiplier * season_effect)
            self.total_clicks += 1

    def buy_click_multiplier(self):
        if self.interactions_enabled:
            if self.cotton >= self.click_multiplier_cost:
                self.cotton -= self.click_multiplier_cost
                self.click_multiplier *= 2
                self.click_multiplier_cost *= 2
                clear_screen()
                print("You bought a click multiplier!")
            else:
                print("Not enough cotton!")

    def buy_auto_cotton_multiplier(self):
        if self.interactions_enabled:
            if self.cotton >= self.auto_cotton_multiplier_cost:
                self.cotton -= self.auto_cotton_multiplier_cost
                self.auto_cotton_multiplier += 1
                self.auto_cotton_multiplier_cost *= 2
                clear_screen()
                print("You bought an auto cotton multiplier!")
            else:
                print("Not enough cotton!")

    def buy_shop_item(self, choice):
        if self.interactions_enabled:
            if choice in self.shop_items:
                item = self.shop_items[choice]
                if self.money >= item["cost"]:
                    self.money -= item["cost"]
                    if choice in ["1", "2"]:
                        self.cotton_per_second += item["effect"]
                    elif choice == "3":
                        self.auto_cotton_multiplier += 1
                    clear_screen()
                    print(f"You bought {item['name']}!")
                else:
                    print("Not enough money!")

    def buy_upgrade(self, choice):
        if self.interactions_enabled:
            if choice in self.upgrades:
                upgrade = self.upgrades[choice]
                if self.money >= upgrade["cost"]:
                    self.money -= upgrade["cost"]
                    if choice == "1":
                        self.cotton_per_click += upgrade["effect"]
                    elif choice in ["2", "3"]:
                        self.cotton_per_second += upgrade["effect"]
                    clear_screen()
                    print(f"You bought {upgrade['name']}!")
                else:
                    print("Not enough money!")

    def auto_harvest(self):
        if self.interactions_enabled:
            season_effect = self.season_effects[self.current_season]["cotton_per_second"]
            self.cotton += int(self.auto_cotton_multiplier * self.cotton_per_second * season_effect)

    def display_status(self):
        clear_screen()
        print(f"Money: {self.money}")
        print(f"Current Cotton: {self.cotton}")
        print(f"Total Clicks: {self.total_clicks}\n")
        print(f"Cotton per Click: {self.cotton_per_click * self.click_multiplier}")
        print(f"Cotton per Second: {self.cotton_per_second}")
        print(f"Auto Cotton Multiplier: {self.auto_cotton_multiplier}\n")
        print(f"Auto Cotton Multiplier Cost: {self.auto_cotton_multiplier_cost}")
        print(f"Click Multiplier Cost: {self.click_multiplier_cost}\n")
        print("Shop Items:")
        for key, item in self.shop_items.items():
            print(f"{key}: {item['name']} - Cost: {item['cost']} | Effect: {item['description']}")
        print("\nUpgrades:")
        for key, upgrade in self.upgrades.items():
            print(f"{key}: {upgrade['name']} - Cost: {upgrade['cost']} | Effect: {upgrade['description']}")
        print()

def save_game(farm):
    with open("savegame.json", "wb") as file:
        data = {
            "cotton": farm.cotton,
            "cotton_per_second": farm.cotton_per_second,
            "cotton_per_click": farm.cotton_per_click,
            "click_multiplier_cost": farm.click_multiplier_cost,
            "click_multiplier": farm.click_multiplier,
            "auto_cotton_multiplier_cost": farm.auto_cotton_multiplier_cost,
            "auto_cotton_multiplier": farm.auto_cotton_multiplier,
            "total_clicks": farm.total_clicks,
            "money": farm.money,
            "current_season": farm.current_season,
            "season_effects": farm.season_effects,
            "shop_items": farm.shop_items,
            "upgrades": farm.upgrades,
            "objectives": farm.objectives,
            "achievements": farm.achievements,
            "interactions_enabled": farm.interactions_enabled,
        }
        data_json = json.dumps(data).encode('utf-8')
        encrypted_data = cipher_suite.encrypt(data_json)
        file.write(encrypted_data)
        print("Game saved.")

def load_game():
    if os.path.exists("savegame.json"):
        with open("savegame.json", "rb") as file:
            encrypted_data = file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            data = json.loads(decrypted_data.decode('utf-8')) 
        farm = Farm()
        farm.cotton = data["cotton"]
        farm.cotton_per_second = data["cotton_per_second"]
        farm.cotton_per_click = data["cotton_per_click"]
        farm.click_multiplier_cost = data["click_multiplier_cost"]
        farm.click_multiplier = data["click_multiplier"]
        farm.auto_cotton_multiplier_cost = data["auto_cotton_multiplier_cost"]
        farm.auto_cotton_multiplier = data["auto_cotton_multiplier"]
        farm.total_clicks = data["total_clicks"]
        farm.money = data["money"]
        farm.current_season = data["current_season"]
        farm.season_effects = data.get("season_effects", farm.season_effects)
        farm.shop_items = data.get("shop_items", farm.shop_items)
        farm.upgrades = data.get("upgrades", farm.upgrades)
        farm.objectives = data["objectives"]
        farm.achievements = data["achievements"]
        farm.interactions_enabled = data.get("interactions_enabled", True)
        print("Game loaded.")
        return farm
    else:
        print("No saved game found.")
        return Farm()

def main_menu():
    print("Welcome to Cotton Farming Simulator!")
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")
    choice = input("Enter your choice: ")
    clear_screen()
    if choice == "1":
        return Farm()
    elif choice == "2":
        return load_game()
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        return main_menu()

def main():
    farm = main_menu()
    while True:
        farm.display_status()
        action = input("Press 'h' to harvest cotton, 'b' to buy click multiplier, 'a' to buy auto cotton multiplier, 's' to open shop, 'u' to buy upgrade, 'save' to save game, or 'q' to quit.\n").lower()
        if action == "save":
            save_game(farm)
        elif action == "q":
            clear_screen()
            print("Thanks for playing!")
            break
        elif action == "h":
            farm.harvest_cotton()
        elif action == "b":
            farm.buy_click_multiplier()
        elif action == "a":
            farm.buy_auto_cotton_multiplier()
        elif action == "s":
            print("Shop Items:")
            for key, item in farm.shop_items.items():
                print(f"{key}: {item['name']} - Cost: {item['cost']} | Effect: {item['description']}")
            print()
            choice = input("Enter the number of the item you want to buy or 'q' to go back.\n")
            if choice != 'q':
                farm.buy_shop_item(choice)
        elif action == "u":
            print("Upgrades:")
            for key, upgrade in farm.upgrades.items():
                print(f"{key}: {upgrade['name']} - Cost: {upgrade['cost']} | Effect: {upgrade['description']}")
            print()
            choice = input("Enter the number of the upgrade you want to buy or 'q' to go back.\n")
            if choice != 'q':
                farm.buy_upgrade(choice)
        time.sleep(0)  # update speed

if __name__ == "__main__":
    main()