from grid import Grid
import matplotlib.pyplot as plt


def main():
    # Input parameters for the user
    number_of_generations = int(input('number of generations to simulate? '))
    number_of_rows = int(input('number of rows? '))
    number_of_columns = int(input('number of columns? '))
    initial_life_probability = float(input('proportion of alive cells at the beginning (between 0 and 1)? '))

    # Create a grid
    grid = Grid(number_of_rows, number_of_columns, initial_life_probability)

    # Display the generations in a new window
    fig, ax = plt.subplots()
    img = ax.imshow(grid.show_grid(), interpolation='nearest')

    for i in range(number_of_generations):
        grid.update_grid()
        img.set_data(grid.show_grid())
        plt.pause(0.05)

    plt.show()
    plt.close()


if __name__ == "__main__":
    main()
