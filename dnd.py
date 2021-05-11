import requests

site_url = 'https://www.dnd5eapi.co/api/'


class Spell:
    def __init__(self, name):
        spell_name = name.replace(' ', '-')
        site_drl = 'spells/{}/'.format(spell_name)
        spell_json = requests.get(site_url + site_drl)
        if spell_json.status_code == 404:
            raise ValueError("Spell is bogus.  Try a real one next time.")
        spelldex = spell_json.json()
        self.name = spelldex['name']
        self.desc = spelldex['desc']

        self.range = spelldex['range']
        self.cast = spelldex['casting_time']
        self.damage_type = spelldex['damage']['damage_type']['index']
        self.damage = spelldex['damage']['damage_at_slot_level']
        self.url = site_url + spelldex['url']


class Monster:
    def __init__(self, name):
        monster_name = name.replace(' ', '-')
        site_drl = 'monsters/{}/'.format(monster_name)
        spell_json = requests.get(site_url + site_drl)
        if spell_json.status_code == 404:
            raise ValueError("Monster is bogus.  Try a real one next time.")
        monsterdex = spell_json.json()
        self.name = monsterdex['name']
        self.armor_class = monsterdex['armor_class']
        self.size = monsterdex["size"]
        self.type = monsterdex["type"]
        self.alignment = monsterdex["alignment"]
        self.hit_points = monsterdex["hit_points"]
        self.hit_dice = monsterdex["hit_dice"]
        self.speed = monsterdex["speed"]
        self.strength = monsterdex["strength"]
        self.dexterity = monsterdex["dexterity"]
        self.constitution = monsterdex["constitution"]
        self.intelligence = monsterdex["intelligence"]
        self.wisdom = monsterdex["wisdom"]
        self.charisma = monsterdex["charisma"]
        self.rating = monsterdex["challenge_rating"]


class Races:
    def __init__(self, name):
        race_name = name.replace(' ', '-')
        site_drl = 'races/{}/'.format(race_name)
        spell_json = requests.get(site_url + site_drl)
        if spell_json.status_code == 404:
            raise ValueError("Race is bogus.  Try a real one next time.")
        racedex = spell_json.json()
        self.name = racedex['name']
        self.speed = racedex['speed']
        self.ability_bonuses_1 = racedex['ability_bonuses'][0]['ability_score']['name']
        self.ability_bonus_1 = racedex['ability_bonuses'][0]['bonus']
        self.ability_bonuses_2 = racedex['ability_bonuses'][1]['ability_score']['name']
        self.ability_bonus_2 = racedex['ability_bonuses'][1]['bonus']
        self.alignment = racedex['alignment']
        self.size = racedex['size_description']
        self.lang = racedex['language_desc']


class Class:
    def __init__(self, name):
        class_name = name.replace(' ', '-')
        site_drl = 'classes/{}/'.format(class_name)
        spell_json = requests.get(site_url + site_drl)
        if spell_json.status_code == 404:
            raise ValueError("Class is bogus.  Try a real one next time.")
        classdex = spell_json.json()
        self.name = classdex['name']
        self.hit = classdex['hit_die']
        self.proficiency_choices = classdex['proficiency_choices']
        self.proficiencies = classdex['proficiencies']
        self.saving_throws = classdex['saving_throws']
        self.starting_equipment = classdex['starting_equipment']


class Equipment:
    def __init__(self, name):
        equip_name = name.replace(' ', '-')
        site_drl = 'equipment/{}/'.format(equip_name)
        spell_json = requests.get(site_url + site_drl)
        if spell_json.status_code == 404:
            raise ValueError("Equipment is bogus.  Try a real one next time.")
        equipmentdex = spell_json.json()
        self.name = equipmentdex['name']
        self.equipment_category = equipmentdex['equipment_category']['name']
        self.cost = equipmentdex['cost']
        if self.equipment_category == 'Armor':
            self.armor_category = equipmentdex['armor_category']
            self.armor_class = equipmentdex['armor_class']
            self.str_minimum = equipmentdex['str_minimum']
            self.stealth_disadvantage = equipmentdex['stealth_disadvantage']
            self.weight = equipmentdex['weight']
        if self.equipment_category == 'Weapon':
            self.weapon_range = equipmentdex['weapon_range']
            self.damage = equipmentdex['damage']['damage_dice']
            self.damage_type = equipmentdex['damage']['damage_type']['name']


class Magic_Item:
    def __init__(self, name):
        magic_name = name.replace(' ', '-')
        site_drl = 'magic-items/{}/'.format(magic_name)
        spell_json = requests.get(site_url + site_drl)
        if spell_json.status_code == 404:
            raise ValueError("Magic item is bogus.  Try a real one next time.")
        magicdex = spell_json.json()
        self.name = magicdex['name']
        self.category = magicdex['equipment_category']['name']
        self.desc = magicdex['desc']


class Ammo:
    def __init__(self, name):
        ammo_name = name.replace(' ', '-')
        site_drl = 'weapon-properties/{}/'.format(ammo_name)
        spell_json = requests.get(site_url + site_drl)
        if spell_json.status_code == 404:
            raise ValueError("Equipment is bogus.  Try a real one next time.")
        ammodex = spell_json.json()
        self.name = ammodex['name']
        self.desc = ammodex['desc']
        print(self.desc)


# Spell(name='acid splash')
# Monster(name='aboleth')
# Races(name='dragonborn')
# Class(name='rogue')
# Equipment(name='burglars pack')
# Equipment(name='padded')
# Equipment(name='abacus')
# Armor(name='burglars pack')
# Magic_Item(name='adamantine armor')
# Ammo(name='ammunition')

#Spell(name='acid splash')
#Monster(name='aboleth')
#Races(name='dragonborn')
#Class(name='rogue')
#Equipment(name='burglars pack')
#Equipment(name='padded')
#Equipment(name='abacus')
#Armor(name='burglars pack')
#Magic_Item(name='adamantine armor')
#Ammo(name='ammunition')