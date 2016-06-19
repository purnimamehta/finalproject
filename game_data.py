class Location:
    '''Class to represent each location in game world.'''

    def __init__(self, location_id, brief_description, long_description, items, location_visited, points):
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
        self.location_id = location_id
        self.items = []
        self.brief_description = brief_description
        self.long_description = long_description
        self.location_visited = location_visited
        self.points = points

    def get_location_id(self):
        '''
        (Location) -> chr
        Return chr of location id.
        '''
        return self.location_id

    def get_items(self):
        '''
        (Items) -> lst
        Return a list of items that are available at each location
        '''
        return self.items

    def get_brief_description(self):
        '''
        (Location) -> str
        Return str brief description of location.
        '''
        return self.brief_description

    def get_full_description(self):
        '''
        (Location) -> str
        Return str long description of location.
        '''
        return self.long_description

    def get_location_visited(self):
        '''
        (Location) -> str
        Return str long description of location.
        '''
        return self.location_visited

    def get_points(self):
        '''
        (Location) -> chr
        Return chr points for visiting each location
        '''
        return self.points

class Item:
    '''Class to represent each item in game world.'''

    def __init__ (self, name, start, target, target_points, ):
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
        Return location (the integer id) of where item is first found.
        '''
        return self.start


    def get_name(self):
        '''
        (Item) -> str
        Return the str name of the item.
        '''
        return self.name


    def get_target_location (self):
        '''
        (Item) -> int
        Return item's target location (the integer id) of where it should be deposited.
        '''
        return self.target


    def get_target_points (self):
        '''
        (Item) -> int
        Return integer points awarded for depositing the item in its target location.
        '''
        return self.target_points


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
        self.x = self.x + dx
        self.y = self.y + dy

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
        '''
        if item not in self.inventory:
            self.inventory.append(item)
        return self.inventory


    def remove_item(self, item):
        '''
        (Player, str item name) -> None
        Remove given item name from player's inventory.
        '''
        if item in self.inventory:
            self.inventory.remove(item)
        return self.inventory


    def get_inventory(self):
        '''
        (Player) -> lst
        Return player's inventory.
        '''
        return self.inventory
