""" Basic tests for ZombieApp program """
import unittest
from zombie import ZombieApp, Creature

class TestCreature(unittest.TestCase):
	def test_move_up(self):
		creature = Creature(0,0,4)
		creature.move("U")
		self.assertEqual(creature.x, 0)
		self.assertEqual(creature.y, 3)

	def test_move_down(self):
		creature = Creature(0,0,4)
		creature.move("D")
		self.assertEqual(creature.x, 0)
		self.assertEqual(creature.y, 1)
	
	def test_move_left(self):
		creature = Creature(0,0,4)
		creature.move("L")
		self.assertEqual(creature.x, 3)
		self.assertEqual(creature.y, 0)
	
	def test_move_right(self):
		creature = Creature(0,0,4)
		creature.move("R")
		self.assertEqual(creature.x, 1)
		self.assertEqual(creature.y, 0)

class TestZombieApp(unittest.TestCase):

	def test_add_zombie(self):
		zombieapp = ZombieApp(4, "D")
		zombieapp.add_zombie(0, 0)
		added_zombie = zombieapp.creatures[0]
		self.assertEqual(added_zombie.zombie, True)
		self.assertEqual(added_zombie.x, 0)
		self.assertEqual(added_zombie.y, 0)
		self.assertEqual(added_zombie.n, 4)
	
	def test_add_creature(self):
		zombieapp = ZombieApp(4, "D")
		zombieapp.add_creature(0, 0)
		added_creature = zombieapp.creatures[0]
		self.assertEqual(added_creature.zombie, False)
		self.assertEqual(added_creature.x, 0)
		self.assertEqual(added_creature.y, 0)
		self.assertEqual(added_creature.n, 4)
	
	def test_move_infect(self):
		zombieapp = ZombieApp(4, "R")
		zombieapp.add_zombie(0, 0)
		zombieapp.add_creature(1, 0)
		# creatures[0] is zombie
		zombieapp.move(zombieapp.creatures[0])
		# zombie position
		self.assertEqual(zombieapp.creatures[0].x, 1)
		self.assertEqual(zombieapp.creatures[0].y, 0)
		# zombie score
		self.assertEqual(zombieapp.creatures[0].score, 1)
		# poor creature is a zombie
		self.assertEqual(zombieapp.creatures[0].zombie, True)
	
	def test_list_infected(self):
		zombieapp = ZombieApp(4, "DDD")
		zombieapp.add_zombie(0, 0)
		zombieapp.add_creature(0, 1)
		zombieapp.add_creature(0, 2)
		zombieapp.add_creature(0, 3)
		# Check the move should return a list of zombies
		new_zombies = zombieapp.move(zombieapp.creatures[0])
		self.assertEqual(len(new_zombies), 3)
		# Check score
		self.assertEqual(zombieapp.creatures[0].score, 3)
		# Creatures should be all zombies
		for creature in zombieapp.creatures[1:3]:
			self.assertEqual(creature.zombie, True)
	
	def test_move_already_infected(self):
		zombieapp = ZombieApp(4, "RR")
		zombieapp.add_zombie(0, 0)
		zombieapp.add_creature(1, 0)
		zombieapp.add_creature(2, 0)

		zombieapp.move(zombieapp.creatures[0])
		# moving the new zombie should not list any zombie since
		# it was already infected
		new_zombies = zombieapp.move(zombieapp.creatures[1])
		self.assertEqual(new_zombies, [])
	
	def test_run_app(self):
		directions = "DLUURR"
		zombieapp = ZombieApp(4, directions)
		original_pos = []
		zombieapp.add_zombie(2, 1)
		zombieapp.add_creature(0, 1)
		zombieapp.add_creature(1, 2)
		zombieapp.add_creature(3, 1)
		# Get all the original position
		for creature in zombieapp.creatures:
			original_pos.append((creature.x, creature.y))
		# Run
		zombieapp.run()
		zombies = zombieapp.result()
		self.assertEqual(len(zombies), 4)
		# Check scores
		self.assertEqual(zombieapp.creatures[0].score, 1)
		self.assertEqual(zombieapp.creatures[1].score, 1)
		self.assertEqual(zombieapp.creatures[2].score, 1)

		# Check all creatures
		for index, creature in enumerate(zombieapp.creatures):
			# Creature should be zombie
			self.assertEqual(creature.zombie, True)
			# Check againts expected position
			x, y = original_pos[index]
			pos_x, pos_y = self.directions_to_coordinate(
										  directions
										  , x
										  , y
										  , creature.n)
			self.assertEqual(creature.x, pos_x)
			self.assertEqual(creature.y, pos_y)
			

	
	## Convenient function
	def directions_to_coordinate(self, directions, x, y, n):
		""" Translate the directions to update the current coordinates"""
		new_x = x
		new_y = y
		# R = x = +1
		# L = x = -1
		# D = y = +1
		# U = y = -1
		for each in directions:
			if each == 'R':
				new_x += 1
			elif each == 'L':
				new_x -= 1
			elif each == 'D':
				new_y += 1
			elif each == 'U':
				new_y -= 1
			
			# Check if outside the grid
			if new_x < 0:
				new_x = n - 1
			elif new_x == n:
				new_x = 0
			if new_y < 0:
				new_y = n - 1
			elif new_y == n:
				new_y = 0
				
		return new_x, new_y
		
		

if __name__ == '__main__':
    unittest.main()
		