import sys
from game_data import Player, Location, Item

class World:
    """A class to store all map, location and item data for game world."""

    def __init__(self, mapfile, locfile, itemfile):
        """
        (World, str filename, str filename, str filename) -> None

        Initialize a World using data from given filenames.
        """

        self.map = []
        self.locations = {}
        self.items = {}

        self.load_map(mapfile)
        self.load_locations(locfile)
        self.load_items(itemfile)

    def load_map(self, filename):
        '''
        (World, str filename) -> None
        Store map from filename in self.map as a nested list
        of strings like so:
            1 2 5
            3 -1 4
        becomes [['1','2','5'], ['3','-1','4']]
        The given 'filename' is a string that gives name of text file
        in which map data is located.
        '''

        map = open(filename,'r')
        for line in map:
            line=line.strip()
            self.map.append(line.split())  

    def load_locations(self, filename):
        '''
        (World, str filename) -> None
        Store all locations from filename in self.locations
        as a dictionary where integer location numbers are the keys,
        and Location objects are the values:
        {integer location number: Location object}.

        The given 'filename' is a string that gives name of text file
        in which location data is located.
        '''

        # TODO:
        # Open and read given filename
        # For each location, create a new Location object with data from file.
        #   e.g. new_location = Location(location id, short desc, long desc, ...)
        # Add this location to self.locations dict with key as integer
        # of location id and value as this new_location object

    def load_items(self, filename):
        '''
        (World, str filename) -> None
        Store all items from filename in self.items
        with item name as the key, and an Item object as the value.
        Each item should also be added into self.locations as
        based on the item's starting location as given in text file.

        The given 'filename' is a string that gives name of text file
        in which item data is located.
        '''

        # TODO:
        # Open and read given filename
        # For each item, create a new Item object with data from file.
        # Then, two things must be done:
        # 1. Using item's starting location, append Item object
        #    to that starting location's ".items" list
        #    i.e. (add Item to self.locations[starting_location_id].items)
        # 2. Store item in self.items dict with key as str item name
        #    and value as Item object

    def get_room(self, x, y):
        '''
        (World, int, int) -> Location
        Return the Location object associated with x, y values given.
        '''

        # TODO:
        # 1. Get location id at given x, y coordinates in self.map list
        # 2. Return Location object associated with this location number in self.locations dictionary

        pass

    def get_moves(self, x, y):
        '''
        (World, int, int) -> lst of str
        The given x and y represent the player's current position.
        Using x, y coordinates, check self.map list for what directions the player can currently move in.
        Return list of possible moves based on map data and boundaries.
        e.g. The returned list should look something like: ["go north", "go south"]
        '''

        pass

# --- END of World class --- #


# --- Functions to handle player's actions in the game ---

def view_inventory():
    '''
    Suggested helper function.
    You may use or remove this as you see fit.
    TODO: Update this docstring based on how you use this method.
    '''

    pass

def use_item(current_item, current_location):
    '''
    Suggested helper function.
    You may use or remove this as you see fit.
    TODO: Update this docstring based on how you use this method.
    '''

    pass

def get_actions(current_location):
    '''
    (Location) -> lst of strs
    Return a list of strings where each string represents
    a possible action the user can take from the given current_location.
    e.g. The returned list should look something like:
         ["go north", "go south", "take t-card"]
    '''

    actions = []

    # TODO:
    # Use WORLD.get_moves to append all possible moves to actions.
    # Append any other possible actions (e.g. 'take item' option for
    # each available item from current room), etc.

    return actions

def do_action(choice, current_loc):
    '''
    (str, Location) -> None
    This function takes str choice and Location current_loc and
    carries out consequences of making the given choice.
    You may update this docstring based on how you choose to code this function.
    '''

    # TODO:
    # Carry out consequences of making the given choice
    # e.g.
    if choice == "go north":
        PLAYER.move_north()
    # ... handle any other possible choices ...


if __name__ == "__main__":

    # Variables to store world info and player info
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(0, 0) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit"]

    while not PLAYER.victory:

        # Variable to keep track of player's current location
        # Get current location based on player's x and y coordinates
        current_loc = WORLD.get_room(PLAYER.x, PLAYER.y)

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)

        print("\nWhat to do? \n")
        available_actions = get_actions(current_loc)
        for action in available_actions:
            print(action)

        print("===")
        print("Menu Options: \n")
        for option in menu:
            print(option)

        choice = input("\nChoose action: ")

        # Check that choice is valid in this situation
        # If it is, call do_action(choice, current_loc),
        # If not, print appropriate error message
