#include <stdio.h>
#include "sandpiles.h"

/**
 * print_grid - Print a 3x3 grid
 * @grid: The 3x3 grid to be printed
 *
 * This function prints the grid in a formatted manner.
 */
static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j != 0)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * stable - Check if a grid is stable
 * @grid: The 3x3 grid to be checked
 *
 * Return: 1 if stable, 0 if unstable.
 *
 * A grid is stable if none of its cells contain more than 3 grains.
 */
int stable(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid[i][j] > 3)
				return (0);  /* Unstable */
		}
	}
	return (1);  /* Stable */
}

/**
 * topple - Topple unstable cells in the grid
 * @grid: The 3x3 grid to be processed
 *
 * This function redistributes grains from cells that have more than 3 grains
 * to their neighboring cells.
 */
void topple(int grid[3][3])
{
	int temp[3][3] = {0};  /* Temporary grid for changes */
	int i, j;

	/* Process each cell */
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid[i][j] > 3)
			{
				grid[i][j] -= 4;  /* Remove 4 grains */

				/* Distribute grains to neighbors */
				if (i > 0)
					temp[i - 1][j]++;  /* Top */
				if (i < 2)
					temp[i + 1][j]++;  /* Bottom */
				if (j > 0)
					temp[i][j - 1]++;  /* Left */
				if (j < 2)
					temp[i][j + 1]++;  /* Right */
			}
		}
	}

	/* Apply changes from the temporary grid to the original grid */
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid[i][j] += temp[i][j];
		}
	}
}

/**
 * sandpiles_sum - Compute the sum of two sandpiles
 * @grid1: The first 3x3 grid (output grid)
 * @grid2: The second 3x3 grid
 *
 * This function computes the sum of two sandpiles and ensures that the
 * result is stable. The result is stored in grid1.
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j;

	/* Add grid2 to grid1 */
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] += grid2[i][j];
		}
	}

	/* Topple until the grid is stable */
	while (!stable(grid1))
	{
		printf("=\n");
		print_grid(grid1);  /* Print grid before toppling */
		topple(grid1);      /* Topple the unstable grid */
	}
}
