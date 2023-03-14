class Room:
    def __init__(self, name):
        """
        Init arguments.
        >>> room = Room("Kitchen")
        >>> room.name
        'Kitchen'
        """
        self.name = name
        self.description = ""
        self.links = {}
        self.character = None
        self.item = None
    def set_description(self, description):
        """
        >>> dining_hall = Room("Dining Hall")
        >>> dining_hall.set_description("A large room with ornate golden decorations on each wall.")
        'A large room with ornate golden decorations on each wall.'
        """
        self.description = description
        return description
    def link_room(self, room_to_link, direction):
        """
        >>> kitchen = Room("Kitchen")
        >>> dining_hall = Room("Dining Hall")
        >>> kitchen.link_room(dining_hall, "south")
        """
        self.links[direction] = room_to_link
    
    def move(self, ex_direction):
        """Move rooms"""
        for direction, room in self.links.items():
            if ex_direction == direction:
                return room
    
    def set_character(self, character):
        """Set character"""
        self.character = character

    def get_character(self):
        """Get character"""
        return self.character if self.character else None
    
    def set_item(self, item):
        """Set item"""
        self.item = item
    
    def get_item(self):
        """Get item"""
        return self.item if self.item else None
    
    def get_details(self):
        """Get details"""
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, room in self.links.items():
            print(f"The {room.name} is {direction}")

class Win:
    """Additional class to count walks"""
    defeated = 0
win = Win() 

class Enemy:
    def __init__(self, name, descr_of_enemy):
        """
        >>> enemy = Enemy("Dave", "A smelly zombie")
        >>> enemy.name
        'Dave'
        """
        self.name = name
        self.descr_of_enemy = descr_of_enemy
        self.sentence = ""
        self.week = ""

    def set_conversation(self, sentence):
        """
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        """
        self.sentence = sentence
    
    def set_weakness(self, week):
        """Set weakness"""
        self.week = week
    
    def describe(self):
        """Describe enemy."""
        print(f"{self.name} is here!")
        print(self.descr_of_enemy)

    def talk(self):
        """Talk with enemy"""
        print(f"[{self.name} says]: {self.sentence}")
    
    def fight(self, fight_with):
        """Fight with enemy"""
        if self.week == fight_with:
            win.defeated += 1
            print(f"You fend {self.name} off with the {self.week}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False
    def get_defeated(self):
        """To count walks"""
        return win.defeated
    
class Item:
    def __init__(self, name):
        """
        >>> cheese = Item("cheese")
        >>> cheese.name
        'cheese'
        """
        self.name = name
        self.dess = ""
        self.week = ""
    def set_description(self, dess):
        """
        >>> cheese = Item("cheese")
        >>> cheese.set_description("A large and smelly block of cheese")
        """
        self.dess = dess
    def describe(self):
        """Describe item"""
        print(f"The [{self.name}] is here - {self.dess}")
    def get_name(self):
        """Get name."""
        return self.name