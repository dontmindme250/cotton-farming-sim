import time
import os
import json
import random

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
				self.shop_items = {
						"1": {"name": "Fertilizer", "cost": 50, "effect": 2, "description": "Increases cotton per second by 2"},
						"2": {"name": "Scarecrow", "cost": 100, "effect": 5, "description": "Increases cotton per second by 5"},
						"3": {"name": "Harvester", "cost": 200, "effect": 0, "description": "Automatically harvests cotton"},
				}
				self.upgrades = {
						"1": {"name": "Advanced Tools", "cost": 500, "effect": 2, "description": "Increases cotton per click by 2"},
						"2": {"name": "Irrigation System", "cost": 1000, "effect": 5, "description": "Increases cotton per second by 5"},
						"3": {"name": "High-Yield Seeds", "cost": 2000, "effect": 10, "description": "Increases cotton per second by 10"},
				}
				self.objectives = {
						"1": {"name": "Harvest 1000 Cotton", "reward": 500, "completed": False},
						"2": {"name": "Reach 100 Total Clicks", "reward": 300, "completed": False},
						"3": {"name": "Earn 5000 Money", "reward": 800, "completed": False},
				}
				self.achievements = {
						"Harvest King": {"description": "Harvest 10000 cotton", "reward": 1000, "completed": False},
						"Click Master": {"description": "Reach 500 total clicks", "reward": 800, "completed": False},
						"Wealthy Farmer": {"description": "Earn 10000 money", "reward": 1200, "completed": False},
				}

		def harvest_cotton(self):
				self.cotton += self.cotton_per_click * self.click_multiplier
				self.total_clicks += 1
				os.system('cls' if os.name == 'nt' else 'clear')
				print("You harvested cotton!")

		def buy_click_multiplier(self):
				if self.cotton >= self.click_multiplier_cost:
						self.cotton -= self.click_multiplier_cost
						self.click_multiplier *= 2
						self.click_multiplier_cost *= 2
						os.system('cls' if os.name == 'nt' else 'clear')
						print("You bought a click multiplier!")

		def buy_auto_cotton_multiplier(self):
				if self.cotton >= self.auto_cotton_multiplier_cost:
						self.cotton -= self.auto_cotton_multiplier_cost
						self.auto_cotton_multiplier += 1
						self.auto_cotton_multiplier_cost *= 2
						os.system('cls' if os.name == 'nt' else 'clear')
						print("You bought an auto cotton multiplier!")

		def buy_shop_item(self, choice):
				if choice in self.shop_items:
						item = self.shop_items[choice]
						if self.money >= item["cost"]:
								self.money -= item["cost"]
								if choice == "1":
										self.cotton_per_second += item["effect"]
								elif choice == "2":
										self.cotton_per_second += item["effect"]
								elif choice == "3":
										self.auto_cotton_multiplier += 1
								os.system('cls' if os.name == 'nt' else 'clear')
								print(f"You bought {item['name']}!")
						else:
								print("Not enough money!")

		def buy_upgrade(self, choice):
				if choice in self.upgrades:
						upgrade = self.upgrades[choice]
						if self.money >= upgrade["cost"]:
								self.money -= upgrade["cost"]
								if choice == "1":
										self.cotton_per_click += upgrade["effect"]
								elif choice == "2":
										self.cotton_per_second += upgrade["effect"]
								elif choice == "3":
										self.cotton_per_second += upgrade["effect"]
								os.system('cls' if os.name == 'nt' else 'clear')
								print(f"You bought {upgrade['name']}!")
						else:
								print("Not enough money!")

		def auto_harvest(self):
				self.cotton += self.auto_cotton_multiplier * self.cotton_per_second

		def display_status(self):
				print(f"Current Cotton: {self.cotton}")
				print(f"Cotton per Click: {self.cotton_per_click * self.click_multiplier}")
				print(f"Cotton per Second: {self.cotton_per_second}")
				print(f"Click Multiplier Cost: {self.click_multiplier_cost}")
				print(f"Auto Cotton Multiplier: {self.auto_cotton_multiplier}")
				print(f"Auto Cotton Multiplier Cost: {self.auto_cotton_multiplier_cost}")
				print(f"Total Clicks: {self.total_clicks}")
				print(f"Money: {self.money}")
				print("Shop Items:")
				for key, item in self.shop_items.items():
						print(f"{key}: {item['name']} - Cost: {item['cost']} - Effect: {item['description']}")
				print("Upgrades:")
				for key, upgrade in self.upgrades.items():
						print(f"{key}: {upgrade['name']} - Cost: {upgrade['cost']} - Effect: {upgrade['description']}")
				print()

def save_game(farm):
		with open("savegame.json", "w") as file:
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
						"objectives": farm.objectives,
						"achievements": farm.achievements
				}
				json.dump(data, file)
		print("Game saved.")

def load_game():
	if os.path.exists("savegame.json"):
			with open("savegame.json", "r") as file:
					data = json.load(file)
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
			farm.objectives = data["objectives"]
			farm.achievements = data["achievements"]
			print("Game loaded.")
			return farm
	else:
			print("No saved game found.")

def main_menu():
	print("Welcome to Cotton Farming Simulator!")
	print("1. New Game")
	print("2. Load Game")
	print("3. Quit")
	choice = input("Enter your choice: ")
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

def check_events(farm):
	# Random event: Drought reduces cotton production for a period of time
	if random.random() < 0.05:  # 5% chance of drought event
			print("Drought! Cotton production reduced.")
			farm.cotton_per_second -= 3
			time.sleep(5)  # Duration of the event
			farm.cotton_per_second += 3
			os.system('cls' if os.name == 'nt' else 'clear')

def check_objectives(farm):
	for key, objective in farm.objectives.items():
			if not objective["completed"]:
					if key == "1" and farm.cotton >= 1000:
							print(f"Objective Completed: {objective['name']}")
							farm.money += objective["reward"]
							farm.objectives[key]["completed"] = True
					elif key == "2" and farm.total_clicks >= 100:
							print(f"Objective Completed: {objective['name']}")
							farm.money += objective["reward"]
							farm.objectives[key]["completed"] = True
					elif key == "3" and farm.money >= 5000:
							print(f"Objective Completed: {objective['name']}")
							farm.money += objective["reward"]
							farm.objectives[key]["completed"] = True

def check_achievements(farm):
	for key, achievement in farm.achievements.items():
			if not achievement["completed"]:
					if key == "Harvest King" and farm.cotton >= 10000:
							print(f"Achievement Unlocked: {achievement['description']}")
							farm.money += achievement["reward"]
							farm.achievements[key]["completed"] = True
					elif key == "Click Master" and farm.total_clicks >= 500:
							print(f"Achievement Unlocked: {achievement['description']}")
							farm.money += achievement["reward"]
							farm.achievements[key]["completed"] = True
					elif key == "Wealthy Farmer" and farm.money >= 10000:
							print(f"Achievement Unlocked: {achievement['description']}")
							farm.money += achievement["reward"]
							farm.achievements[key]["completed"] = True

def main():
	farm = main_menu()
	while True:
			check_events(farm)
			check_objectives(farm)
			check_achievements(farm)
			farm.auto_harvest()
			farm.display_status()
			action = input("Press 'h' to harvest cotton, 'b' to buy click multiplier, 'a' to buy auto cotton multiplier, 's' to open shop, 'u' to buy upgrade, 'save' to save game, or 'q' to quit.\n").lower()
			os.system('cls' if os.name == 'nt' else 'clear')
			if action == "h":
					farm.harvest_cotton()
			elif action == "b":
					farm.buy_click_multiplier()
			elif action == "a":
					farm.buy_auto_cotton_multiplier()
			elif action == "s":
					choice = input("Enter the number of the item you want to buy or 'q' to go back.\n")
					if choice != 'q':
							farm.buy_shop_item(choice)
			elif action == "u":
					choice = input("Enter the number of the upgrade you want to buy or 'q' to go back.\n")
					if choice != 'q':
							farm.buy_upgrade(choice)
			elif action == "save":
					save_game(farm)
			elif action == "q":
					print("Thanks for playing!")
					break
			else:
					print("Invalid input. Please try again.")

			time.sleep(0.1) # update speed

if __name__ == "__main__":
	main()
