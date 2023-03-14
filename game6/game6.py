class Win:
    """Additional class to count walks"""
    defeated = 0
win = Win()

class Rules:
    """Class Rules"""
    def rules(self):
        print("""Правила гри дуже прості, ти заблукав у Львові, знаходишся на вулиці Козельницькій і тобі потрібно пройтися вуличками та вбити усіх ворогів!
Для того щоб їх вбити на кожній з вулиць є предмет, який у цьому допоможе. Але не факт, що цим предметом ти зможеш вбити ворога. Тобто тобі потрібно буде
позбирати усі предмети і потім пробувати вбити, або ж ризикувати. Також у тебе є 100 hp - здоров'я, якщо ти раз використав не той предмет, то hp = 50.
Але на одній з вуличок тебе чекатиме добра людина, яка зможе тебе полікувати. Успіхів!
Всього у грі є шість команди:
    1. Вибрати напрямок(west abo east)
    2. talk - поговорити з ворогом
    3. take - взяти предмет
    4. fight - побитися з ворогом
    5. live - можливість полікуватися
    6. help - можливі команди
    """)

class Street:
    """Class Street"""
    def __init__(self, name):
        """Init args"""
        self.name = name
        self.description = ""
        self.links = {}
        self.character = None
        self.item = None
    
    def set_description(self, description):
        """Set description"""
        self.description = description
    

    def link_room(self, street_to_link, direction):
        """
        Link streets
        """
        self.links[direction] = street_to_link

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
    
    def move(self, ex_direction):
        """Move streets"""
        for direction, street in self.links.items():
            if ex_direction == direction:
                return street
            
    def get_details(self):
        """Get details"""
        print(self.name)
        print("""....(¯`°v°´¯)...........(¯`°v°´¯)\n
.....(_.^._).............(_.^._)""")
        print(self.description)
        print("Можливі команди - help")
        if self.links:
            for direction, street in self.links.items():
                print(f"{street.name} - {direction}")


class Character:
    """Class main"""
    def __init__(self, name, descr_of_enemy, enemy=None):
        """Init args"""
        self.name = name
        self.descr_of_enemy = descr_of_enemy
        self.sentence = ""
        if enemy is None:
            enemy = True
        self.enemy = enemy
    
    def set_conversation(self, sentence):
        """Set conversation"""
        self.sentence = sentence
    
    def talk(self):
        """To talk"""
        print(f"[{self.name} says]: {self.sentence}")

class Enemy(Character):
    """Class Enemy"""
    def __init__(self, name, descr_of_enemy, enemy=None):
        """Init args."""
        super().__init__(name, descr_of_enemy, enemy)
        self.conversation = None
        self.week = None
        self.health = 100
    
    def set_weakness(self, week):
        """Set weakness"""
        self.week = week
    
    def describe(self):
        """Describe"""
        print(f"{self.name} є тут!")
        print(self.descr_of_enemy)
    
    def fight(self, fight_with):
        """Fight"""
        if self.week == fight_with:
            win.defeated += 1
            print(f"{self.name} помер від {self.week}!")
            return True
        else:
            print("Ти використав не той предмет!")
            return False
        
    def reduce_health(self, health):
        """Reduce health"""
        return health - 50
    
    def get_defeated(self):
        """Count"""
        return win.defeated

class Friend(Character):
    """Class Friend"""
    def __init__(self, name, descr_of_enemy, enemy):
        """Init args"""
        super().__init__(name, descr_of_enemy, enemy)


    def describe(self):
        """Describe"""
        print(f"{self.name} є тут!")
        print(self.descr_of_enemy)
        return None
    
    def increase_health(self, healthy):
        """To increase health"""
        if healthy == 100:
            return healthy
        return healthy + 50

class Item:
    def __init__(self, name):
        """Init args"""
        self.name = name
        self.dess = ""
        self.week = ""
    
    def set_description(self, dess):
        """Set description."""
        self.dess = dess
    
    def describe(self):
        """Describe"""
        print(f"The [{self.name}] is here - {self.dess}")
    
    def get_name(self):
        """Get name"""
        return self.name