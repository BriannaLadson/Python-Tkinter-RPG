import random
import numpy as np

import helpfunctions as helpf

class Game:
	def __init__(self, save_path):
		self.save_path = save_path + "/game_data"
		
		self.directions = {
			"north": [0, -1],
			"northwest": [-1, -1],
			"northeast": [1, -1],
			"south": [0, 1],
			"southwest": [-1, 1],
			"southeast": [1, 1],
			"west": [-1, 0],
			"east": [1, 0],
		}
		
		self.location_map = []
		
		self.civilizations = []
		self.settlements = []
		
	def get_location(self, entity):
		if entity.lx == None or entity.ly == None or entity.lz == None:
			if self.location_map[entity.gy][entity.gx]:
				location = self.location_map[entity.gy][entity.gx]
				
				return f"{location.name} {entity.gx},{entity.gy}"
				
			else:
				return f"{entity.gx},{entity.gy}"
				
		else:
			return f"{entity.lx},{entity.ly},{entity.lz}"
		
	def random_region_placement(self, entity):
		map_size = self.world_size
		
		entity.gx = random.randint(0, map_size - 1)
		entity.gy = random.randint(0, map_size - 1)
		
	def move_entity(self, entity, dir):
		if entity.lx == None and entity.ly == None:
			self.move_entity_region(entity, dir)
			
		else:
			self.move_entity_tile(entity, dir)
			
	def move_entity_region(self, entity, dir):
		map_size = self.world_size
		
		try:
			cx, cy = self.directions[dir]
			
			tx = (entity.gx + cx) % map_size
			ty = (entity.gy + cy) % map_size
				
			entity.gx = tx
			entity.gy = ty
			
			#if isinstance(entity, Player):
			#	self.turns = 60
		
		except KeyError:
			if dir == "in":
				entity.lx = self.local_map_size // 2 - 1
				entity.ly = entity.lx
				entity.lz = 0
				
				#if isinstance(entity, Player):
				#	self.turns = 1
				
	def move_entity_tile(self, entity, dir):
		map_size = self.local_map_size
		
		try:
			cx, cy = self.directions[dir]
			
			tx = entity.lx + cx
			ty = entity.ly + cy
			
			if not (0 <= tx < map_size) or not (0 <= ty < map_size):
				entity.lx = None
				entity.ly = None
				entity.lz = None
				
				raise KeyError
				
			entity.lx = tx
			entity.ly = ty
			
			#if isinstance(entity, Player):
			#	self.turns = 1
			
		except KeyError:
			pass
			
	def generate_civilization(self, race):
		civilization_name_system_id = race.get_name_system_id("civilization")
		civilization_name = self.name_system_objs[civilization_name_system_id].get_name()
		
		civilization = Civilization(race, civilization_name)
		
		self.civilizations.append(civilization)
			
	def generate_settlement(self, race):
		map_size = self.world_size
	
		gx = random.randint(0, map_size - 1)
		gy = random.randint(0, map_size - 1)
		
		if self.location_map[gy][gx] is not None:
			return None
		
		biome = self.overworld_generator.get_biome(gx, gy)
		
		if not biome["id"] in race.settlement_biomes:
			return None
			
		settlement_char = race.settlement_char
		settlement_char_color = race.settlement_char_color
		
		settlement_name_system_id = race.get_name_system_id("settlement")
		settlement_name = self.name_system_objs[settlement_name_system_id].get_name()
		
		settlement = Settlement(
			gx, gy, 
			settlement_char, 
			settlement_char_color,
			settlement_name,
		)
			
		self.settlements.append(settlement)
		
		self.location_map[gy][gx] = settlement
		
		return settlement
		
class Entity:
	def __init__(self):
		self.gx = 0
		self.gy = 0
		
		self.lx = None
		self.ly = None
		self.lz = None
			
	def is_location_local(self):
		if self.lx == None or self.ly == None or self.lz == None:
			return False
			
		else:
			return True

#Creatures		
class Creature(Entity):
	def __init__(self):
		super().__init__()
		
class Player(Creature):
	def __init__(self):
		super().__init__()
		
		self.char = '@'

#Map		
class LocalMapGenerator:
	def __init__(self, biome, seed, map_size):
		self.biome = biome
		
		self.main_color = biome.color
		
		self.seed = seed
		
		self.wraparound = False
		
		self.map_size = map_size
		
		self.generate_map()
		
	def generate_map(self):
		self.map_array = np.full((self.map_size, self.map_size), self.main_color, dtype=object)
		
	def tile_color(self, x, y):
		return self.map_array[y][x]
		
class Settlement:
	def __init__(self, gx, gy, char, char_color, name="Settlement"):
		self.gx = gx
		self.gy = gy
		
		self.char = char
		
		self.char_color = char_color
		
		self.is_capital = False
		
		self.name = name
		
#Factions
class Civilization:
	def __init__(self, culture, name):
		self.culture = culture
		
		self.capital = None
		
		self.settlements = []
		
		self.name = name

#Json Objects		
class Biome:
	def __init__(self, *args):
		self.id = args[0]
		
		self.name = args[1]
		
		self.color = args[2]
		
class NameSystem:
	def __init__(self, *args):
		self.id = args[0]
		
		self.name = args[1]
		
		self.parts = args[2]
		
	def get_name(self):
		name = ""
		
		for part in self.parts:
			name_part = random.choice(part)
			
			name += name_part
			
		return name
		
class Race:
	def __init__(self, *args):
		self.id = args[0]
		
		self.name = args[1]
		
		self.civilization_number = args[2]
		
		self.civilization_name_systems = args[3]
		
		self.settlement_number = args[4]
		
		self.settlement_biomes = args[5]
		
		self.settlement_char = args[6]
		
		self.settlement_char_color = args[7]
		
		self.settlement_name_systems = args[8]
		
	def get_name_system_id(self, name_system_type):
		name_systems = getattr(self, f"{name_system_type}_name_systems")
		
		if len(name_systems) > 0:
			return random.choice(name_systems)
			
		else:
			return None