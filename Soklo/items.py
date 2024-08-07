class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class HealthPotion(Item):
    def __init__(self):
        super().__init__('Health Potion', 50)
        self.heal_amount = 200

class ManaPotion(Item):
    def __init__(self):
        super().__init__('Mana Potion', 50)
        self.mana_restore = 200
