"""
Chapitre 11.1

Classes pour représenter un personnage.
"""
import random as rd
from utils import clamp



class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(clas):
		return clas("Unarmed", clas.UNARMED_POWER, 1)




class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp

	@property
	def name(self):
		return self.__name

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, val):
		if val == None: 
			self.__weapon = Weapon.make_unarmed()
		else: self.__weapon = val
		
	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, hp):
		self.__hp = clamp(hp, 0, self.max_hp)



	def compute_damage(self, defender: "Character"):
		rand = rd.uniform(0.85, 1)
		critical = rd.randint(1, 16) == 1
		if critical: crit = 2
		else: crit = 1
		modifier = crit * rand
		dmg =  (((((2* self.level / 5)+ 2) * self.weapon.power * (self.attack / defender.defense)) / 50) + 2) * modifier

		return int(dmg), critical



def deal_damage(attacker: "Character", defender: "Character"):
	# TODO: Calculer dégâts
	dmg, crit = attacker.compute_damage(defender)
	print(f"{attacker.name} used {attacker.weapon.name}\n  {defender.name} took {dmg} dmg")
	return dmg


def run_battle(c1: "Character", c2: "Character"):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{c1.name} ({c1.hp}) starts a battle with {c2.name} ({c2.hp})")
	numberOfAttacks = 0
	while c1.hp > 0 and c2.hp > 0:
		if numberOfAttacks%2 == 0:
			dmg = deal_damage(c1, c2)
			c2.hp = c2.hp - dmg
			print(f"{c2.name} now has {c2.hp} health points\n")
		if numberOfAttacks%2 != 0:
			dmg = deal_damage(c1, c2)
			c1.hp = c1.hp - dmg
			print(f"{c1.name} now has {c1.hp} health points\n")
			
		

		numberOfAttacks += 1


	if c1.hp == 0: print(f"{c1.name} is sleeping with the fishes")
	if c2.hp == 0: print(f"{c2.name} is sleeping with the fishes")
	return numberOfAttacks
