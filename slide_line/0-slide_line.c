#include "slide_line.h"

/**
 * slide_left - Slides and merges an array to the left.
 * @line: The array of integers.
 * @size: The size of the array.
 */
void slide_left(int *line, size_t size)
{
	size_t i, j;

	/* Step 1: Remove zeros by shifting elements to the left */
	for (i = 0, j = 0; i < size; i++)
	{
		if (line[i] != 0)
		{
			if (j != i)
			{
				line[j] = line[i];
				line[i] = 0;
			}
			j++;
		}
	}

	/* Step 2: Merge adjacent equal numbers */
	for (i = 0; i < size - 1; i++)
	{
		if (line[i] == line[i + 1] && line[i] != 0)
		{
			line[i] *= 2;
			line[i + 1] = 0;
		}
	}

	/* Step 3: Remove zeros again */
	for (i = 0, j = 0; i < size; i++)
	{
		if (line[i] != 0)
		{
			if (j != i)
			{
				line[j] = line[i];
				line[i] = 0;
			}
			j++;
		}
	}
}

/**
 * slide_right - Slides and merges an array to the right.
 * @line: The array of integers.
 * @size: The size of the array.
 */
void slide_right(int *line, size_t size)
{
	size_t i, j;

	/* Step 1: Remove zeros by shifting elements to the right */
	for (i = size - 1, j = size - 1; (int)i >= 0; i--)
	{
		if (line[i] != 0)
		{
			if (j != i)
			{
				line[j] = line[i];
				line[i] = 0;
			}
			j--;
		}
	}

	/* Step 2: Merge adjacent equal numbers */
	for (i = size - 1; i > 0; i--)
	{
		if (line[i] == line[i - 1] && line[i] != 0)
		{
			line[i] *= 2;
			line[i - 1] = 0;
		}
	}

	/* Step 3: Remove zeros again */
	for (i = size - 1, j = size - 1; (int)i >= 0; i--)
	{
		if (line[i] != 0)
		{
			if (j != i)
			{
				line[j] = line[i];
				line[i] = 0;
			}
			j--;
		}
	}
}

/**
 * slide_line - Slides and merges an array to the left or right.
 * @line: The array of integers.
 * @size: The size of the array.
 * @direction: The direction to slide, either SLIDE_LEFT or SLIDE_RIGHT.
 *
 * Return: 1 on success, 0 on failure.
 */
int slide_line(int *line, size_t size, int direction)
{
	if (direction == SLIDE_LEFT)
	{
		slide_left(line, size);
	}
	else if (direction == SLIDE_RIGHT)
	{
		slide_right(line, size);
	}
	else
	{
		return (0);
	}

	return (1);
}
