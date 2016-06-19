class Location:
    '''Class to represent each location in game world.'''

    def __init__(self):
        '''Creates a new location.

        Data that should be associated with each Location object:
        an integer location ID,
        a brief description,
        a long description,
        items that are available in the location,
        and whether or not the location has been visited before.

        You may change/add parameters and the data available for each
        Location class as you see fit.
        e.g. You may want to add special actions that could be available for
             some locations.

        All locations in your game MUST be represented as an instance of this class.
        '''

        # TODO: Add new attributes for this class here to store location data.
        # e.g. a list to store items available in location (store as Item objects)
        self.items = []

    def get_brief_description (self, locations_dict, location_id):
        '''
        (Location) -> str
        Return str brief description of location.'''
        x=" "

        for location_id in locations_dict:
            x = locations_dict[locations_id].get_brief_decription
        return x

    def get_full_description (self, locations_dict, location_id):
        '''
        (Location) -> str
        Return str long description of location.'''
        for location_id in locations_dict:
            return location_dict[location_id]



    # TODO: Add other 'getter' methods as above for other location data as needed

class Item:
    '''Class to represent each item in game world.'''

    def __init__ (self, name, start, target, target_points):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points being the number of points player gets
        if item is deposited in target location.

        You may change these parameters and the data available for each
        Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
        -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance of this class.
        '''

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location (self):
        '''
        (Item) -> int
        Return location (the integer id) of where item is first found.'''

        self.x = 4
        self.y = 3

    def get_name(self):
        '''
        (Item) -> str
        Return the str name of the item.'''

        pass

    def get_target_location (self):
        '''
        (Item) -> int
        Return item's target location (the integer id) of where it should be deposited.'''

        pass

    def get_target_points (self):
        '''
        (Item) -> int
        Return integer points awarded for depositing the item in its target location.'''

        pass

class Player:
    '''Class to represent the player in game world.'''

    def __init__(self, x, y):
        '''
        (Player, int, int) -> None
        Creates a new Player at given x and y coordinates.

        You may add new parameters / attributes / methods to this class as you see fit.
        '''
        self.x = x
        self.y = y
        self.victory = False # set to True once player has won game
        self.score = 0
        self.inventory = [] # store list of item names that are in player's inventory

    def move(self, dx, dy):
        '''
        (Player, int, int) -> None
        Given integers dx and dy, move player to new location (self.x + dx, self.y + dy)
        '''
        self.x += dx
        self.y += dy

    def move_north(self):
        '''
        (Player) -> None
        Helper function to move Player one position north on map.
        These integer directions are based on how the map must be stored
        in our nested list self.map.
        '''
        self.move(0,-1)

    def move_south(self):
        '''
        (Player) -> None
        Helper function to move Player one position south on map.
        These integer directions are based on how the map must be stored
        in our nested list self.map.
        '''
        self.move(0,1)

    def move_east(self):
        '''
        (Player) -> None
        Helper function to move Player one position east on map.
        These integer directions are based on how the map must be stored
        in our nested list self.map.
        '''

        # TODO: use self.move to move one east

        self.move(1,0)

    def move_west(self):
        '''
        (Player) -> None
        Helper function to move Player one position west on map.
        These integer directions are based on how the map must be stored
        in our nested list self.map.
        '''

        self.move(-1,0)


    def add_item(self, item):
        '''
        (Player, str item name) -> None
        Add given item name to player's inventory.
        :param item:
        :return:
        '''

         if item not in self.inventory:
            self.inventory.append(item)
        return True

    def remove_item(self, item):
        '''
        (Player, str item name) -> None
        Remove given item name from player's inventory.
        '''

         if item in self.inventory:
            self.inventory.remove(item)
        return True

    def get_inventory(self):
        '''
        (Player) -> lst
        Return player's inventory.
        '''

        return self.inventory
