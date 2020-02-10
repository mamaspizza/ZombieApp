from zombie import ZombieApp
import sys
import os

if __name__ == "__main__":
	argv = sys.argv
	if len(argv) < 2:
		raise Exception("Command Arguments should include input file.")
	filepath = argv[1]
	if not os.path.exists(filepath):
		raise Exception("Input file does not exist.")
	
	with open(filepath, 'r') as f:
		lines = f.readlines()
	# Process the inputs	
	grid = int(lines[0])
	zombie_pos = lines[1].rstrip()
	creatures_pos = lines[2].rstrip().split(':')
	movements = lines[3].rstrip()
	
	zombieApp = ZombieApp(grid, movements)
	pos = zombie_pos.split(',')
	x = int(pos[0])
	y = int(pos[1])
	zombieApp.add_zombie(x, y)
	
	for raw_pos in creatures_pos:
		pos = raw_pos.split(',')
		x = int(pos[0])
		y = int(pos[1])
		zombieApp.add_creature(x, y)
	
	zombieApp.run()	
	zombies = zombieApp.result()
	# Print result
	final_positions = []
	total_score = 0
	for zombie in zombies:
		total_score += zombie.score
		final_positions.append((zombie.x, zombie.y))

	print("zombies score: " + str(total_score))
	print("zombies final positions: " + str(final_positions))
		
	