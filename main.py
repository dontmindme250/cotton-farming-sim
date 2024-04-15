import json
import os
import random
import time

def ClearScreen():
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
						"Spring": {"cotton_per_second": 1.2, "cotton_per_click": 1.1},
						"Summer": {"cotton_per_second": 1, "cotton_per_click": 1},
						"Autumn": {"cotton_per_second": 0.8, "cotton_per_click": 0.9},
						"Winter": {"cotton_per_second": 0.5, "cotton_per_click": 0.7}
				}
				self.season_change_time = time.time() + random.randint(600, 900)
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
						self.cotton += round(self.cotton_per_click * self.click_multiplier * season_effect)
						self.total_clicks += 1

		def buy_click_multiplier(self):
				if self.interactions_enabled:
						if self.cotton >= self.click_multiplier_cost:
								self.cotton -= self.click_multiplier_cost
								self.click_multiplier *= 2
								self.click_multiplier_cost *= 2
								ClearScreen()
								print("You bought a click multiplier!")
						else:
								print("Not enough cotton!")
				else:
						print("You cannot buy a click multiplier during this event.")

		def buy_auto_cotton_multiplier(self):
				if self.interactions_enabled:
						if self.cotton >= self.auto_cotton_multiplier_cost:
								self.cotton -= self.auto_cotton_multiplier_cost
								self.auto_cotton_multiplier += 1
								self.auto_cotton_multiplier_cost *= 2
								ClearScreen()
								print("You bought an auto cotton multiplier!")
						else:
								print("Not enough cotton!")
				else:
						print("You cannot buy an auto cotton multiplier during this event.")

		def buy_shop_item(self, choice):
				if self.interactions_enabled:
						if choice in self.shop_items:
								item = self.shop_items[choice]
								if self.money >= item["cost"]:
										self.money -= item["cost"]
										if choice == "1" or choice == "2":
												self.cotton_per_second += item["effect"]
										elif choice == "3":
												self.auto_cotton_multiplier += 1
										ClearScreen()
										print(f"You bought {item['name']}!")
								else:
										print("Not enough money!")
				else:
						print("You cannot buy items during this event.")

		def buy_upgrade(self, choice):
				if self.interactions_enabled:
						if choice in self.upgrades:
								upgrade = self.upgrades[choice]
								if self.money >= upgrade["cost"]:
										self.money -= upgrade["cost"]
										if choice == "1":
												self.cotton_per_click += upgrade["effect"]
										elif choice == "2" or choice == "3":
												self.cotton_per_second += upgrade["effect"]
										ClearScreen()
										print(f"You bought {upgrade['name']}!")
								else:
										print("Not enough money!")
				else:
						print("You cannot buy upgrades during this event.")

		def auto_harvest(self):
				if self.interactions_enabled:
						season_effect = self.season_effects[self.current_season]["cotton_per_second"]
						self.cotton += self.auto_cotton_multiplier * self.cotton_per_second * season_effect

		def display_status(self):
				print(f"Money : {self.money}")
				print(f"Current Cotton : {self.cotton}")
				print(f"Total Clicks : {self.total_clicks}")
				print()
				print(f"Cotton per Click : {self.cotton_per_click * self.click_multiplier}")
				print(f"Cotton per Second : {self.cotton_per_second}")
				print(f"Auto Cotton Multiplier : {self.auto_cotton_multiplier}")
				print()
				print(f"Auto Cotton Multiplier Cost : {self.auto_cotton_multiplier_cost}")
				print(f"Click Multiplier Cost : {self.click_multiplier_cost}")
				print()

				print("Shop Items:")
				for key, item in self.shop_items.items():
						print(f"{key}: {item['name']} - Cost : {item['cost']} | Effect : {item['description']}")
				print()

				print("Upgrades:")
				for key, upgrade in self.upgrades.items():
						print(f"{key}: {upgrade['name']} - Cost : {upgrade['cost']} | Effect : {upgrade['description']}")
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
						"achievements": farm.achievements,
						"interactions_enabled": farm.interactions_enabled, # Save the state of interactions
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
				farm.interactions_enabled = data.get("interactions_enabled", True) # Load interactions state
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
		ClearScreen()
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

def check_objectives(farm):
		for key, objective in farm.objectives.items():
				if not objective["completed"]:
						if key == "1" and farm.cotton >= 1000 or key == "2" and farm.total_clicks >= 100 or key == "3" and farm.money >= 5000:
								print(f"Objective Completed: {objective['name']}")
								farm.money += objective["reward"]
								farm.objectives[key]["completed"] = True

def check_achievements(farm):
		for key, achievement in farm.achievements.items():
				if not achievement["completed"]:
						if key == "Harvest King" and farm.cotton >= 10000 or key == "Click Master" and farm.total_clicks >= 500 or key == "Wealthy Farmer" and farm.money >= 10000:
								print(f"Achievement Unlocked: {achievement['description']}")
								farm.money += achievement["reward"]
								farm.achievements[key]["completed"] = True

def main():
		farm = main_menu()
		FarmVars = Farm()
		while True:
				check_objectives(farm)
				check_achievements(farm)
				farm.auto_harvest()
				farm.display_status()
				farm.change_season()
				action = input("Press 'h' to harvest cotton, 'b' to buy click multiplier, 'a' to buy auto cotton multiplier, 's' to open shop, 'u' to buy upgrade, 'save' to save game, or 'q' to quit.\n").lower()
				ClearScreen()
				if action == "save":
						save_game(farm)
				elif action == "q":
						print("Thanks for playing!")
						break
				elif farm.interactions_enabled:
						if action == "h":
								farm.harvest_cotton()
						elif action == "b":
								farm.buy_click_multiplier()
						elif action == "a":
								farm.buy_auto_cotton_multiplier()
						elif action == "s":
								print("Shop Items:")
								for key, item in FarmVars.shop_items.items:
									print(f"{key}: {item['name']} - Cost : {item['cost']} | Effect : {item['description']}")
								print()
								choice = input("Enter the number of the item you want to buy or 'q' to go back.\n")
								if choice != 'q':
										farm.buy_shop_item(choice)
								ClearScreen()
						elif action == "u":
								print("Upgrades:")
								for key, upgrade in FarmVars.upgrades.items():
									print(f"{key}: {upgrade['name']} - Cost : {upgrade['cost']} | Effect : {upgrade['description']}")
								print()
								choice = input("Enter the number of the upgrade you want to buy or 'q' to go back.\n")
								if choice != 'q':
										farm.buy_upgrade(choice)
								ClearScreen()
				else:
						print("Interactions are temporarily disabled due to an event.")
				time.sleep(0.1)  # update speed

if __name__ == "__main__":
		main()
