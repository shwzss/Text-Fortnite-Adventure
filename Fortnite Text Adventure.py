import random
import time
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.shield = 0
        self.weapon = None
        self.shield_potions = 0
        self.kills = 0

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Location:
    def __init__(self, name, opponents):
        self.name = name
        self.opponents = opponents

def start_game():
    print("Welcome to Fortnite Text Adventure!")
    player_name = input("Enter your player name: ")
    player = Player(player_name)
    weapons = [Weapon("Pistol", 15), Weapon("Shotgun", 25), Weapon("Assault Rifle", 20)]
    locations = [
        Location("Tilted Towers", 16),
        Location("Pleasant Park", 16),
        Location("Retail Row", 16),
        Location("Runny Races", 16),
        Location("Dusty Depot", 16),
        Location("Shabby Shores", 16)
    ]

    storm_circles = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Final"]

    print(f"Welcome, {player.name}! Your mission is to survive and be the last one standing!")

    while True:
        print(f"\nKills: {player.kills}")
        print("Select your action:")
        for i, location in enumerate(locations, start=1):
            print(f"{i}. Land in {location.name}")
        print(f"{len(locations) + 1}. Quit")

        choice = input("Enter your choice: ")

        if choice.isdigit() and 1 <= int(choice) <= len(locations):
            location_index = int(choice) - 1
            print(f"\nYou land in {locations[location_index].name}.")
            encounter_location(player, locations[location_index], weapons, storm_circles)
        elif choice == str(len(locations) + 1):
            print("\nThanks for playing Fortnite Text Adventure. See you next time!")
            sys.exit()
        else:
            print("\nInvalid choice. Please choose again.")

def encounter_location(player, location, weapons, storm_circles):
    print(f"\nYou arrived at {location.name}. Prepare for potential encounters!")
    time.sleep(1)

    while location.opponents > 0:
        opponent_health = random.randint(50, 100)
        print("\nYou encounter an opponent!")
        time.sleep(1)
        try:
            outcome = fight_opponent(player, location, opponent_health, weapons)
            if outcome == "win":
                location.opponents -= 1
                player.kills += 1
                print("You defeated the opponent!")
                if location.opponents == 0:
                    print("You cleared all opponents in this location!")
                    break
            elif outcome == "lose":
                print("You were defeated by the opponent. Game over!")
                time.sleep(5)  # Wait for 5 seconds
                sys.exit()
        except Exception as e:
            print(f"An error occurred during the battle: {e}")

    if player.kills == 96:
        print("\nCongratulations! You cleared all opponents in all locations and won the game!")
        print("Thank you for playing Fortnite Text Adventure!")
        sys.exit()

    if random.randint(1, 10) == 1:
        collect_shield(player)

    if random.randint(1, 5) == 1:
        print(f"\nAttention {player.name}: You are in the {random.choice(storm_circles)} Storm Circle!")

def collect_shield(player):
    shield_amount = random.randint(25, 50)
    player.shield += shield_amount
    player.shield_potions += 1
    print(f"\nYou found a shield potion and gained {shield_amount} shields! You now have {player.shield} shields.")

def fight_opponent(player, location, opponent_health, weapons):
    while opponent_health > 0 and player.health > 0:
        print(f"\nYour Health: {player.health}")
        print(f"Opponent's Health: {opponent_health}")
        print(f"Opponents Remaining: {location.opponents}")
        print("\nSelect your action:")
        print("1. Attack")
        print("2. Use Shield")
        print("3. Change Weapon")

        choice = input("Enter your choice: ")

        if choice == '1':
            if player.weapon:
                opponent_health -= player.weapon.damage
                print(f"You attacked the opponent with {player.weapon.name}.")
            else:
                print("You don't have a weapon to attack!")
        elif choice == '2':
            if player.shield > 0:
                player.shield -= 1
                print("You used a shield and protected yourself!")
            else:
                print("You don't have any shield potions left!")
        elif choice == '3':
            player.weapon = random.choice(weapons)
            print(f"You switched to {player.weapon.name}.")
        else:
            print("Invalid choice. Please choose again.")

        if opponent_health > 0:
            player.health -= random.randint(5, 15)
            print("The opponent attacked you!")
        if player.health <= 0:
            return "lose"
        time.sleep(1)

    return "win"

start_game()
