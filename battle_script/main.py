import sys

from battle_script.classes.game import Person

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 60},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(60, 65, 60, 34, magic)

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())