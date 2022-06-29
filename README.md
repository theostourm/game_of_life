# game_of_life

This is an implementation of the game of life in Python.

before running the code, install matplotlib:
```
pip install matplotlib
```

to run the code:
```
python main.py
```

When you run the main function, the code asks some parameters. You can start with these parameters and mess up with them afterwards!

![Capture d’écran 2022-06-29 à 12 21 50](https://user-images.githubusercontent.com/26652900/176425033-9976c659-c434-44d8-8345-94fffd6ba2d7.png)

The project contains 2 test files, fell free to run the tests and play with them as well :)


--------------------------------------
<b>Logic about the implementation:</b>

1 - The "Cell" class represents a cell of the game. It is either dead or alive.

2 - The "Grid" class is used to represent the whole game. It has a length and a width, and a set of cells.

3 - The program initiates a grid with an approximate proportion of cells alive, randomly spread on the grid, the others are dead.

4 - For a generation, the program checks which cell has to change its status (to be killed or resurrected), according to the rules.

5 - The program kills or resurrects the given cells on the grid, so we have the next generation, and so on.

6 - A plot displays the generations when the program is launched.
