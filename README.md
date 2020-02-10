# ZombieApp
A zombie infection 2D app simulator. Consist of NxN grid on which zombies and creatures live. Both occupy a single square on the grid and are addressed using zero-indexed x-y coordinates. Top left corner is (x: 0, y: 0) with x represent horizontal coordinate, y represent vertical coordinate. The movements of a zombie are up, down, left and right (U,D,L,R).

If a zombie moves on the same location as a creature, the creature is transformed into another zombie and zombies score one point. The zombie continues moving and infecting creatures until has performed all its moves. Once it has completed its movement, the first newly created zombie moves using the same sequence as the original zombie. Once it has completed its move, the second newly created zombie moves, and so in order of infection with each zombie performing the same sequence of moves. Once no new zombies have been created and all the zombies have completed
moving the program ends.

Notes:
- The code is tested using Python 2.7.1
- If using Python 3, need to modify the raw_input() to input() in menu.py

Before using:
  - Extract files to a given directory. 
  - If there is no Python in your system, Install Python 2.7.

How to use:
  1. python fileinput.py input.txt - main program to run using input file
  2. python menu.py - main program to use menu
  3. python unit_test.py - unit tests
     
