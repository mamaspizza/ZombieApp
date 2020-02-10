class ZombieApp(object):
	def __init__(self, num, movements):
		""" Initialize the app of the values that will be used globally """
		self.creatures = []
		self.num = num
		self.movements = movements
	
	def add_zombie(self, x, y):
		""" Add zombie """
		c = Creature(x, y, self.num)
		c.zombie = True 
		self.creatures.append(c)
	
	def add_creature(self, x, y):
		""" Add creature """
		c = Creature(x, y, self.num)
		self.creatures.append(c)

	def move(self, zombie):
		""" Handles the movements of zombies """
		new_zombies = []
		directions = list(self.movements)
		for d in directions:
			x, y = zombie.move(d)
			# Check for creature that is this position
			
			non_zombies = []			
			for creature in self.creatures:
				if creature.x == x and creature.y == y:
					creature.zombie = True
					new_zombies.append(creature)
					zombie.score += 1
					continue
				non_zombies.append(creature)
			self.creatures = non_zombies
				
			#for creature in self.creatures:
			#	if creature.zombie:
			#		continue
			#	if creature.x == x and creature.y == y:
		#			creature.zombie = True
			#		new_zombies.append(creature)
			#		zombie.score += 1
		return new_zombies

	def run(self):
		""" Run the application """
		zombies = []
		# Check zombies within the creatures
		for creature in self.creatures:
			if not creature.zombie:
				continue
			zombies.append(creature)
			self.creatures.remove(creature)
			
        # Move zombies                        
		while len(zombies)> 0:
			new_zombies = []
			for zombie in zombies:				
				new_zombies.extend(self.move(zombie))
			zombies = new_zombies

	def result(self):
		""" Returns the list of zombies """
		zombies = []
		for creature in self.creatures:
			if not creature.zombie:
				continue
			zombies.append(creature)
		return zombies

	
class Creature(object):
	def __init__(self, x, y, n):
		""" Initialize zombie with current location and world coordinates.. """
		self.x = x
		self.y = y
		self.n = n
		self.zombie = False
		self.score = 0
		
	def move(self, direction):
		""" Move the position interpret with the world coordinates. """
		if direction == 'U':
			self.y -= 1
		elif direction == 'D':
			self.y += 1
		elif direction == 'L':
			self.x -= 1
		elif direction == 'R':
			self.x += 1
			
		# Check if outside the grid
		if self.x < 0:
			self.x = self.n - 1
		elif self.x == self.n:
			self.x = 0
		if self.y < 0:
			self.y = self.n - 1
		elif self.y == self.n:
			self.y = 0		
		return (self.x, self.y)


