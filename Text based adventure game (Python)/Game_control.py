from Location import Location
from Character import User
import random
import json
import logging
logging.basicConfig(level=logging.DEBUG, filename='Game_control-debug.log')


class GameControl:
    def __init__(self):
        self.rolls = 0
        self.MAX_ROLL = 3
        self.player = User()
        self.location = Location()
        # need instance variables for the player & location & timer (if needed)

# class Dice:
    def roll_die(self, amount, sides):
        rolls = []
        for i in range(amount):
            rolls.append(random.randint(1, sides))
        return rolls

    def assign_attributes(self, dice_values):
        self.player.change__init__("health", dice_values[0] + dice_values[1])
        self.player.change__init__("strength", dice_values[2] + dice_values[3])
        self.player.change__init__("speed", dice_values[4] + dice_values[5])

    def ask_roll_again(self):
        print(f"It is very nice to meet you once more {self.player.name}\nRoll for you attributes, your attributes "
              "consist of health, strength and speed:\nHealth is how many times you can get hit and keep fighting\n"
              "Strength is how hard you hit whoever you attack\nSpeed helps when you're dodging, attacking, or running "
              "away from enemies")
        print(f"Your current attributes are:\nHealth {self.player.health} of 12, Strength {self.player.health} of 12,"
              f" Speed {self.player.speed} of 12")
        while self.rolls < self.MAX_ROLL:
            userinput = input("Would you like to roll for new attributes? (yes/no)\n")
            while True:
                if userinput == "yes" or userinput == "no":
                    break
                else:
                    userinput = input("Please enter a valid answer\nWould you like to roll for new attributes? "
                                      "(yes/no)\n")
            if userinput == "yes":
                new_rolls = self.roll_die(6, 6)
                self.assign_attributes(new_rolls)
                print(f'\nYour health is {self.player.health} of 12, strength is {self.player.strength} of 12, speed is'
                      f' {self.player.speed} of 12')
                self.rolls += 1
                print(f"You have rolled {self.rolls}/3 times, you have {(3 - self.rolls)} rolls left")
            else:
                self.start_location()

    def ask_name(self):
        new_name = input("Do you have a name?\n")
        self.player.change__init__("name", new_name)
        current_rolls = self.roll_die(6, 6)
        self.assign_attributes(current_rolls)
        if new_name == "yes":
            new_name = input("What is your name:\n")
            self.player.change__init__("name", new_name)
            current_rolls = self.roll_die(6, 6)
            self.assign_attributes(current_rolls)
        elif new_name == "no":
            new_name = input("What shall you be called:\n")
            self.player.change__init__("name", new_name)
            current_rolls = self.roll_die(6, 6)
            self.assign_attributes(current_rolls)

    def check_empty_file(self):
        with open("JSON files/SavedCharacterData.json", 'r') as read_obj:
            one_char = read_obj.read(1)
            if one_char == '0' or not one_char:
                data = [{"blank_beginner_save": self.player.__dict__}]
                sf = json.dumps(data, indent=4, separators=(',', ': '))
                with open('JSON files/SavedCharacterData.json', "w") as outfile:
                    outfile.write(sf)

    def save_data(self):
        save_name = input("Save name (Data will be saved under this name):\n")
        self.location.assign_campaign_name("campaign_name", save_name)
        with open('JSON files/SavedCharacterData.json') as outfile:
            data = json.load(outfile)
            times_checked = len(data)
            times_run = 1
        for d in data:
            for k in d:
                if save_name == k:
                    print("Save name found in previously saved campaigns")
                    save_replace = input("There is a previous save with this name, would you like to replace it? "
                                         "(yes/no)\n")
                    while True:
                        if save_replace == "yes" or save_replace == "no":
                            break
                        else:
                            save_replace = input("Please input a valid response\n"
                                                 "Would you like to override the existing save?\n")
                    if save_replace == "yes":
                        for key in d:
                            if save_name == key:
                                with open('JSON files/SavedCharacterData.json', 'w') as json_file:
                                    json.dump(data, json_file,
                                              indent=4,
                                              separators=(',', ': '))
                                print("Campaign successfully overridden\n")
                                self.ask_name()
                                return
                    else:
                        self.save_data()
                else:
                    new_file = times_checked - times_run
                    if new_file == 0:
                        print("New save created\n")
                        data.append({save_name: self.player.__dict__})
                        with open('JSON files/SavedCharacterData.json', 'w') as json_file:
                            json.dump(data, json_file,
                                      indent=4,
                                      separators=(',', ': '))
                        self.ask_name()
                        return
                    else:
                        times_run += 1
                        pass

    def load_data(self):
        load_name = input("Save name (Data saved to this name will be loaded):\n")
        with open('JSON files/SavedCharacterData.json') as f:
            f = json.load(f)
            times_checked = len(f)
            times_run = 1
        for d in f:
            for key, value in d.items():
                if key == load_name:
                    for k, v in value.items():
                        self.player.change__init__(k, v)
                    print(f"Successfully loaded {load_name}\nWelcome back {self.player.name}")
                    self.start_location()
                elif load_name == "create new save":
                    self.save_data()
                elif load_name == "show previous saves":
                    print()
                    self.show_saves()
                else:
                    new_file = times_checked - times_run
                    if new_file == 0:
                        print("No save with that name found\nIf you have a previously created save, please enter the "
                              "correct save name\nIf you do not have a previously created save, please enter, create "
                              "new save\nIf you want to see a list of previously created saves, please enter, show "
                              "previous saves")
                        self.load_data()
                    else:
                        times_run += 1

    def show_saves(self):
        with open('JSON files/SavedCharacterData.json') as f:
            f = json.load(f)
        print("Current saved Campaigns:")
        for d in f:
            for sn in d:
                print(sn)
        print()

    def start_location(self):
        self.location.clear_save_file()
        self.location.get_data()
        self.location.create_location_grids(41)
        self.location.randomize_grid("All")
        self.location.generate_world()
        self.location.combine_grids()
        self.location.print_location_grid(self.location.grid)
        print("\n")
        self.location.check_empty_file()
        self.location.set_location()
        self.location.print_player_grid()
        self.location.location_boarders(200)

    def run_location(self):
        # Dev room entry code is dev-7-8-22
        print(f"Currently at: ({self.location.moves_RIGHTLEFT}, {self.location.moves_UPDOWN})")
        self.location.player_movement()
        self.location.location_boarders(200)
        self.location.set_location()
        self.location.print_player_grid()

    def start_game(self):
        self.check_empty_file()
        print("Welcome to: \"GAME NAME\"")
        self.show_saves()
        load_ask = input("To start - Have you saved a campaign before? (yes/no)\n")
        while True:
            if load_ask == "yes" or load_ask == "no":
                break
            else:
                load_ask = input("Please input a valid response\nDo you have a previous saved campaign? (yes/no)\n")
        if load_ask == "yes":
            self.load_data()
        else:
            print("Please create a new save!")
            self.save_data()
            self.ask_roll_again()
        print("Remember saves aren't automatic, if you want to save do it manually!")
        print("\n\n\n")
        self.location.print_location_grid(self.location.grid)


gc = GameControl()
gc.start_game()
while True:
    gc.run_location()
