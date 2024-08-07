class Hero:
    def __init__(self, name, strength, agility, intelligence, strength_growth, agility_growth, intelligence_growth):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.strength_growth = strength_growth
        self.agility_growth = agility_growth
        self.intelligence_growth = intelligence_growth
        self.level = 1
        self.exp = 0
        self.health = strength * 100
        self.mana = intelligence * 100
        self.attack_damage = strength * 10
        self.armor = agility * 0.75
        self.magic_resistance = intelligence * 1.0
        self.health_regen = strength * 1.0
        self.mana_regen = intelligence * 1.0
        self.attack_speed = agility * 0.25
        self.active_ability = None
        self.passive_ability = None

    def level_up(self):
        self.level += 1
        self.strength += self.strength_growth
        self.agility += self.agility_growth
        self.intelligence += self.intelligence_growth
        self.health += self.strength_growth * 100
        self.mana += self.intelligence_growth * 100
        self.attack_damage += self.strength_growth * 10
        self.armor += self.agility_growth * 0.75
        self.magic_resistance += self.intelligence_growth * 1.0
        self.health_regen += self.strength_growth * 1.0
        self.mana_regen += self.intelligence_growth * 1.0
        self.attack_speed += self.agility_growth * 0.25

    def apply_item(self, item):
        # Logic to apply item effects to the hero
        pass

class Aaron(Hero):
    def __init__(self):
        super().__init__('Aaron', 5, 3, 2, 2, 1, 1)
        self.active_ability = self.KnightStrike()
        self.passive_ability = self.SteelArmor()

    class KnightStrike:
        def __init__(self):
            self.damage = [100, 110, 125, 145, 175, 200, 250, 300, 375, 500]
            self.mana_cost = [50, 55, 60, 65, 70, 75, 85, 100, 125, 150]
            self.cooldown = [6, 5.75, 5.50, 5.25, 5, 4.75, 4.50, 4.25, 4, 3.75]
            self.target = 'all_enemies'

    class SteelArmor:
        def __init__(self):
            self.armor_bonus = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.target = 'all_allies'

class Bromy(Hero):
    def __init__(self):
        super().__init__('Healer', 3, 2, 5, 1, 1, 2)
        self.active_ability = self.Heal()
        self.passive_ability = self.RegenAura()

    class Heal:
        def __init__(self):
            self.heal_amount = [100, 120, 140, 160, 180, 200, 250, 300, 400, 500]
            self.mana_cost = [50, 55, 60, 65, 70, 75, 80, 90, 100, 110]
            self.cooldown = [8, 7.75, 7.50, 7.25, 7, 6.75, 6.50, 6.25, 6, 5.75]
            self.target = 'self_allies'

    class RegenAura:
        def __init__(self):
            self.health_regen_bonus = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.target = 'all_allies'
