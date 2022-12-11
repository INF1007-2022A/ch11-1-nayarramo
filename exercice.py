from game import *


def main():
	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmor", 250, 100, 120, 60)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)

	print(f"\n\nTest attack\n")
	deal_damage(c1, c2)
	print(f"\n------------\n")

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")


if __name__ == "__main__":
	main()

