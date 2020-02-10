from zombie import ZombieApp

if __name__ == "__main__":
	grid = int(input("Enter the Grid size (N):"))
	movements = raw_input("Enter zombie movement codes:")
	movements = movements.upper()
	zombieApp = ZombieApp(grid, movements)
	x = input("Enter position of zombie.\nX coordinate:")
	y = input("Y coordinate:")
	zombieApp.add_zombie(x, y)
	while True:
		menu =  "Enter 1 to add creature.\n"
		menu += "Enter 2 to continue and run the App.\n"
		menu += "Select one of above:"
		selection = input(menu)
		if selection == 1:
			x = input("X coordinate:")
			y = input("Y coordinate:")
			zombieApp.add_creature(x, y)
		elif selection == 2:
			break
		else:
			print("Unknown selection. Return to menu.")
	
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