import json
import random
import Colors
import logging
logging.basicConfig(level=logging.DEBUG, filename='Location-debug.log')


class Location:
    def __init__(self):
        self.player = Colors.BLUE + " @ " + Colors.END
        self.empty_space = " "
        self.enemy = Colors.RED + "E" + Colors.END
        self.tree = Colors.GREEN + "T" + Colors.END
        self.entrance = Colors.WHITE + "[E]" + Colors.END
        self.out_of_vision = Colors.WHITE + "[ ]" + Colors.END
        self.grid = []
        self.color_grid = []
        self.content_grid = []
        self.location_data = ""
        self.altitude = 0
        self.move_count = 9
        self.visibility = 5
        self.update_temp_var = self.empty_space
        self.moves_UPDOWN = 0
        self.moves_RIGHTLEFT = 0
        self.curr_pos = [20, 20]
        self.boarder_distance = 0
        self.campaign_name = ''
        self.distance_to_boarder_UPOWN = self.boarder_distance
        self.distance_to_boarder_RIGHTLEFT = self.boarder_distance
        self.approach_grid_movement_UPDOWN = False
        self.approach_grid_movement_RIGHTLEFT = False
        self.set_location_runs = 0
        self.quadrant_list = random.sample(range(4), 4)
        self.biome_pos = [0, 0, 0, 0]
        logging.debug('__init__ accessed')

    def assign_campaign_name(self, var, val):
        """
        Takes the campaign name from Game Control and applies it here so when you save or load campaigns on Game Control
        it loads it here as well
        """
        logging.debug('Assign_campaign_name called')
        logging.debug('Assigned campaign name')
        logging.debug('Called from Game_control')
        setattr(self, var, val)

    def set_location(self):
        """

        """
        logging.debug('Set_location called')
        logging.debug(f'Set location to {self.curr_pos[0]}, {self.curr_pos[1]}')
        logging.debug('Called from self.player_movement()')
        if self.set_location_runs == 0:
            self.update_temp_var = self.grid[self.curr_pos[0]][self.curr_pos[1]]
        self.grid[self.curr_pos[0]][self.curr_pos[1]] = self.player
        self.set_location_runs += 1

    def check_location(self):
        """

        """
        logging.debug('Unfinished function')
        return self.altitude

    def change_altitude(self, direction):
        """

        :param direction:
        """
        if direction == "up":
            self.altitude += 1
        if direction == "down":
            self.altitude -= 1
        self.save_grid()

    def get_data(self):
        """
        Takes data from the Location_info.json document and applies it all to self.location_data
        """
        logging.debug('Get_data called')
        logging.debug('Taking data for Location descriptions and assigning it to self.location_data')
        logging.debug('Called at the beginning of Location run')
        f = open('JSON files/Location_info.json')
        location_info_raw = f.read()
        location_info = json.loads(location_info_raw)
        self.location_data = location_info

    def create_location_grids(self, s):
        """
        Creates a w by h grid using for loops and appends self.empty_space ([ ]) to each grid space
        :param s: The size of the grid
        """
        logging.debug('create_location_grid called')
        logging.debug('Creating a grid with specified s <size>')
        logging.debug('Called at the beginning of Location run')
        for i in range(s):
            row = []
            for j in range(s):
                row.append(self.empty_space)
            self.grid.append(row)
        for i in range(s):
            row = []
            for j in range(s):
                row.append(self.empty_space)
            self.color_grid.append(row)
        for i in range(s):
            row = []
            for j in range(s):
                row.append(self.empty_space)
            self.content_grid.append(row)

    def print_location_grid(self, grid):
        """
        Prints out the grid created bby self.create_location_grid with any changes applied by later functions
        """
        logging.debug('print_location_grid called')
        logging.debug('Printing out the grid')
        logging.debug('Called at the beginning of Location run and end of every loop')
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j], end=' ')
            print()

    def print_player_grid(self):
        for i in range(self.curr_pos[0] - self.visibility//2, self.curr_pos[0] + self.visibility//2 + 1):
            for j in range(self.curr_pos[1] - self.visibility//2, self.curr_pos[1] + self.visibility//2 + 1):
                print(self.grid[i][j], end=' ')
            print()

    def increase_visibility(self):
        """
        Increases the size of the grid by 2 spaces in order to keep the existence of a perfect center (equal grid spaces
        on all sides)
        """
        logging.debug('Increase_visibility called')
        logging.debug('Increasing visibility by 2 grid spaces')
        self.visibility += 2

    def decrease_visibility(self):
        """
        Decreases the size of the grid by 2 spaces in order to keep the existence of a perfect center (equal grid spaces
        on all sides)
        """
        logging.debug('Decrease_visibility called')
        logging.debug('Decreasing visibility by 2 grid spaces')
        self.visibility -= 2

    def randomize_grid(self, direction):
        """
        Assigns random predefined variables to random grid spaces from the grid created in self.create_location_grid
        """
        logging.debug('Randomize_grid called')
        logging.debug('Randomizes the grid after creation')
        logging.debug('Called at the beginning of Location run')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                random_gen = random.randint(0, 100)
                if random_gen <= 1:
                    random_gen = self.enemy
                elif random_gen <= 8:
                    random_gen = self.tree
                elif random_gen <= 100:
                    random_gen = self.empty_space
                if direction == "All":
                    self.content_grid[i][j] = random_gen
                elif direction == "North":
                    self.grid[0][j] = random_gen
                elif direction == "East":
                    self.grid[i][0] = random_gen
                elif direction == "South":
                    self.grid[len(self.grid) - 1][j] = random_gen
                elif direction == "West":
                    self.grid[i][len(self.grid) - 1] = random_gen

    def update_grid(self, direction):
        for i in reversed(range(len(self.grid))):
            for j in reversed(range(len(self.grid[i]))):
                if direction == "North":
                    # print("moved north")
                    if i != 0:
                        if self.grid[i - 1][j] == self.player:
                            self.grid[
                                self.curr_pos[0] + 1][
                                self.curr_pos[1]] = self.update_temp_var
                            self.update_temp_var = self.grid[
                                self.curr_pos[0] - 1][
                                self.curr_pos[1]]
                        else:
                            self.grid[i][j] = self.grid[i - 1][j]
                        # self.grid[(len(self.grid) - 1) - self.approach_moves_north][j] = self.out_of_vision
                if direction == "South":
                    # print("moved south")
                    if i != len(self.grid) - 1:
                        if self.grid[i + 1][j] == self.player:
                            self.grid[
                                self.curr_pos[0]][
                                self.curr_pos[1] - 1] = self.update_temp_var
                            self.update_temp_var = self.grid[
                                self.curr_pos[0]][
                                self.curr_pos[1] + 1]
                        else:
                            self.grid[i][j] = self.grid[i + 1][j]
                        # self.grid[(len(self.grid) - 1) - ((len(self.grid) - 1) - self.approach_moves_south)][
                            # j] = self.out_of_vision
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if direction == "East":
                    # print("moved east")
                    if j != len(self.grid) - 1:
                        if self.grid[i][j + 1] == self.player:
                            self.grid[
                                self.curr_pos[0]][
                                self.curr_pos[1] - 1] = self.update_temp_var
                            self.update_temp_var = self.grid[
                                self.curr_pos[0]][
                                self.curr_pos[1] + 1]
                        else:
                            self.grid[i][j] = self.grid[i][j + 1]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if direction == "West":
                    # print("moved west")
                    if self.grid[i][j] == self.player:
                        self.grid[
                            self.curr_pos[0] - 1][
                            self.curr_pos[1]] = self.update_temp_var
                        self.update_temp_var = self.grid[
                            self.curr_pos[0] + 1][
                            self.curr_pos[1]]
                    else:
                        self.grid[i][j] = self.grid[i][j - 1]
                    # self.grid[i][(len(self.grid) - 1) - (
                    #             (len(self.grid) - 1) - self.approach_moves_west)] = self.out_of_vision

    def location_boarders(self, boarder_distance):
        """
        Sets a distance after which the player encounters a 'boarder' that they cant cross, it also prints out this
        boarder whenever the player gets close to it.
        :param boarder_distance: How far a player can move before reaching the boarder
        """
        logging.debug('Location_boarders called')
        logging.debug('Assigns border distance, assigns it to self.boarder distance, and creates boarders where needed')
        logging.debug('Called in Location loop after self.revert_grid')
        self.boarder_distance = boarder_distance
        self.distance_to_boarder_UPOWN = (boarder_distance - abs(self.moves_UPDOWN))
        self.distance_to_boarder_RIGHTLEFT = (boarder_distance - abs(self.moves_RIGHTLEFT))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.distance_to_boarder_UPOWN < -abs(self.visibility//2):
                    self.approach_grid_movement_UPDOWN = True
                elif self.distance_to_boarder_UPOWN < (self.visibility//2):
                    self.approach_grid_movement_UPDOWN = True
                else:
                    self.approach_grid_movement_UPDOWN = False
                if self.distance_to_boarder_RIGHTLEFT < -abs(self.visibility//2):
                    self.approach_grid_movement_RIGHTLEFT = True
                elif self.distance_to_boarder_RIGHTLEFT < self.visibility//2:
                    self.approach_grid_movement_RIGHTLEFT = True
                else:
                    self.approach_grid_movement_RIGHTLEFT = False

    def check_empty_file(self):
        """
        Checks the SavedGridData.Json for content and if it contains any it replaces it with a '0' in order to make it
        easy to delete and clear the documents data
        """
        logging.debug('Check_empty_file called')
        logging.debug('Checks file for characters, if the file is empty it creates a new save, otherwise it runs '
                      'self.save_grid')
        logging.debug('Called only for the purpose of clearing SavedGridData.json')
        with open("JSON files/SavedGridData.json", 'r') as f:
            one_char = f.read(1)
            if not one_char or one_char == '0':
                data = [
                    {self.campaign_name: {self.altitude: self.grid}}
                    ]
                sf = json.dumps(data, indent=4, separators=(',', ': '))
                with open('JSON files/SavedGridData.json', "w") as outfile:
                    outfile.write(sf)
                print("Created save 0")
            else:
                print("Passed grid save")
                self.save_grid()

    def save_grid(self):
        """
        Saves the grid and its content to the campaign name and coordinates and loads the same grid if the campaign name
        and coordinates match
        """
        logging.debug('Save_grid called')
        logging.debug('Saves grid under campaign name and coordinates if grid is saved loads saved grid')
        logging.debug('Called in Location loop')
        with open('JSON files/SavedGridData.json') as outfile:
            data = json.load(outfile)
            times_checked = len(data)
            times_run = 1
        for d in data:
            for key, value in d.items():
                for k, v in value.items():
                    if key == self.campaign_name:
                        # print(f"k:{k}, grid_name:{grid_name}")
                        if k == self.altitude:
                            self.grid = v
                            print(f"loaded current altitude: {self.altitude}")
                        else:
                            new_grid = times_checked - times_run
                            if new_grid == 0:
                                print("New altitude grid saved\n")
                                data.append({self.campaign_name: {self.altitude: self.grid}})
                                with open('JSON files/SavedGridData.json', 'w') as json_file:
                                    json.dump(data, json_file,
                                              indent=4,
                                              separators=(',', ': '))
                                return
                            else:
                                times_run += 1
                                pass

    def combine_grids(self):
        """
        Saves the grid and its content to the campaign name and coordinates and loads the same grid if the campaign name
        and coordinates match
        """
        logging.debug('Save_grid called')
        logging.debug('Saves grid under campaign name and coordinates if grid is saved loads saved grid')
        logging.debug('Called in Location loop')
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.content_grid[i][j] == " ":
                    self.grid[i][j] = self.color_grid[i][j]
                else:
                    self.color_code_grid()

    def color_code_grid(self):
        biome_colors = []
        for n in range(0, 4):
            for i in self.quadrant_list:
                biome = self.quadrant_list.index(self.quadrant_list[i])
                if biome == 0:
                    biome_colors.append(Colors.RED2)
                if biome == 1:
                    biome_colors.append(Colors.YELLOW2)
                if biome == 2:
                    biome_colors.append(Colors.GREEN)
                if biome == 3:
                    biome_colors.append(Colors.GREY)
        content = [self.tree, self.enemy, self.player]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid.index(self.grid[i]) in range(0, 21):
                    if self.grid.index(self.grid[j]) in range(0, 21):
                        if self.content_grid[i][j] in content:
                            self.grid[i][
                                j] = biome_colors[0] + "[" + Colors.END + self.content_grid[i][j] + biome_colors[0] + "]" + Colors.END
                    else:
                        if self.content_grid[i][j] in content:
                            self.grid[
                                i][
                                j] = biome_colors[1] + "[" + Colors.END + self.content_grid[i][j] + biome_colors[1] + "]" + Colors.END
                else:
                    if self.grid.index(self.grid[j]) in range(0, 21):
                        if self.content_grid[i][j] in content:
                            self.grid[i][
                                j] = biome_colors[2] + "[" + Colors.END + self.content_grid[i][j] + biome_colors[2] + "]" + Colors.END
                    else:
                        if self.content_grid[i][j] in content:
                            self.grid[i][j] = biome_colors[3] + "[" + Colors.END + self.content_grid[i][
                                j] + biome_colors[3] + "]" + Colors.END

    # def color_code_player(self):


    def move_north(self):
        """
        Triggers either the self.update and self.randomize _grid_north() and moves
        """
        logging.debug('Move_north called')
        logging.debug("ran player movement")
        self.update_grid("North")
        self.randomize_grid("North")
        self.moves_UPDOWN += 1

    def move_east(self):
        logging.debug('Move_east called')
        logging.debug("ran player movement")
        self.update_grid("East")
        self.randomize_grid("East")
        self.moves_RIGHTLEFT += 1

    def move_south(self):
        logging.debug('Move_south called')
        logging.debug("ran player movement")
        self.update_grid("South")
        self.randomize_grid("South")
        self.moves_UPDOWN -= 1

    def move_west(self):
        logging.debug('Move_west called')
        logging.debug("ran player movement")
        self.update_grid("West")
        self.randomize_grid("West")
        self.moves_RIGHTLEFT -= 1

    def player_movement(self):
        logging.debug('Player_movement called')
        if self.move_count == 5:
            self.move_count = 0
            print("Quick tip! You can save time by just imputing the initials of the direction you want to go in"
                  "\nfor example: n for north, ne for north east, etc...")
        move = input("What direction would you like to move in?\n(Options: west, north-west, north, north-east, "
                     "east, south-east, south, south-west)\n")
        self.move_count += 1
        while True:
            if move in ["west", "north-west", "north", "north-east", "east", "south-east", "south", "south-west",
                        "north west", "north east", "south east", "south west", "n", "ne", "e", "se", "s", "sw", "w",
                        "nw", "dev-7-8-22"]:
                break
            else:
                move = input("Input invalid, please input a valid direction to move in.\nWhat direction would you like"
                             " to move in?\n(Options: west, north-west, north, north-east, east, south-east, south, "
                             "south-west)\n")
        if move == "west" or move == "w":
            self.move_west()
        elif move == "north-west" or move == "north west" or move == "nw":
            self.move_north()
            self.move_west()
        elif move == "north" or move == "n":
            self.move_north()
        elif move == "north-east" or move == "north east" or move == "ne":
            self.move_north()
            self.move_east()
        elif move == "east" or move == "e":
            self.move_east()
        elif move == "south-east" or move == "south east" or move == "se":
            self.move_south()
            self.move_east()
        elif move == "south" or move == "s":
            self.move_south()
        elif move == "south-west" or move == "south west" or move == "sw":
            self.move_south()
            self.move_west()
        else:
            while True:
                dev_funct = input("You are now in dev testing mode, what do you want to run: ")
                if dev_funct == "end":
                    break

    def clear_save_file(self):
        """
        Changes content of grid file to 0 to make it easier to delete its contents
        ONLY RUN TO CLEAR SAVED DATA IF YOU RUN THE PROGRAM WITH AN EMPTY FOLDER IT BREAKS
        """
        logging.debug('Clear_save_file called')
        data = 0
        sf = json.dumps(data, indent=4, separators=(',', ': '))
        with open('JSON files/SavedGridData.json', "w") as outfile:
            outfile.write(sf)

    def generate_biomes(self, biome, size):
        biome_center = []
        if biome == "wasteland":
            biome = Colors.RED2 + "[ ]" + Colors.END
            quadrant = self.quadrant_list[0]
        if biome == "desert":
            biome = Colors.YELLOW2 + "[ ]" + Colors.END
            quadrant = self.quadrant_list[1]
        if biome == "forest":
            biome = Colors.GREEN + "[ ]" + Colors.END
            quadrant = self.quadrant_list[2]
        if biome == "mountains":
            biome = Colors.GREY + "[ ]" + Colors.END
            quadrant = self.quadrant_list[3]
        if quadrant == 0:
            biome_center = [random.randint(0 + size, 20 - size), random.randint(0 + size, 20 - size)]
        elif quadrant == 1:
            biome_center = [random.randint(0 + size, 20 - size), random.randint(20 + size, 40 - size)]
        elif quadrant == 2:
            biome_center = [random.randint(20 + size, 40 - size), random.randint(0 + size, 20 - size)]
        elif quadrant == 3:
            biome_center = [random.randint(20 + size, 40 - size), random.randint(20 + size, 40 - size)]
        for row in range(biome_center[0] - size // 2, biome_center[0] + size // 2):
            for col in range(biome_center[1] - size // 2, biome_center[1] + size // 2):
                if quadrant == self.quadrant_list[0]:
                    self.color_grid[row][col] = biome
                elif quadrant == self.quadrant_list[1]:
                    self.color_grid[row][col] = biome
                elif quadrant == self.quadrant_list[2]:
                    self.color_grid[row][col] = biome
                elif quadrant == self.quadrant_list[3]:
                    self.color_grid[row][col] = biome

    def generate_world(self):
        for lists in self.color_grid:
            while ' ' in lists:
                self.generate_biome()
                for i in range(len(self.color_grid)):
                    for j in range(len(self.color_grid[i])):
                        while self.color_grid[i][j] == ' ':
                            self.color_grid[i][j] = self.color_grid[random.randint(0, len(self.color_grid) - 1)][random.randint(0, len(self.color_grid) - 1)]


    def generate_biome(self):
        for i in range(0, len(self.color_grid)//2):
            for j in range(0, len(self.color_grid)//2):
                self.generate_biomes("desert", random.randint(0, 10))
                self.generate_biomes("forest", random.randint(0, 10))
                self.generate_biomes("mountains", random.randint(0, 10))
                self.generate_biomes("wasteland", random.randint(0, 10))


#
loc = Location()
loc.clear_save_file()
loc.get_data()
loc.create_location_grids(41)
loc.randomize_grid("All")
loc.generate_world()
loc.combine_grids()
loc.print_location_grid(loc.grid)
print("\n")
loc.check_empty_file()
loc.set_location()
loc.print_player_grid()
loc.location_boarders(200)
while True:
    print(f"Currently at: ({loc.moves_RIGHTLEFT}, {loc.moves_UPDOWN})")
    loc.player_movement()
    loc.location_boarders(200)
    loc.set_location()
    loc.print_player_grid()
