#include "menger.h"

/**
 * free_matrix - free the memory taken by the matrix
 *
 * @matrix: the matrix
 * @size: size of the matrix
 *
 * Return: Nothing
 */
void free_matrix(char **matrix, int size)
{
	int i;

	for (i = 0; i < size; i++)
	{
		free(matrix[i]);
	}
	free(matrix);
}

/**
 * print_matrix - Prints a matrix
 *
 * @matrix: the matrix to print
 * @size: size of the matrix
 *
 * Return: Nothing
 */
void print_matrix(char **matrix, int size)
{
	int i, j;

	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size; j++)
		{
			printf("%c", matrix[i][j]);
		}
		printf("\n");
	}
}

/**
 * menger_sponge - Put spaces in the matrix to get a 2D Menger Sponge
 *
 * @matrix: the matrix
 * @size: size of the matrix
 * @quotient: here to know where to put spaces
 *
 * Return: Nothing
 */
void menger_sponge(char **matrix, int size, int quotient)
{
	int i, j;

	if (quotient < 1)
		return;

	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size; j++)
		{
			if ((i / quotient) % 3 == 1 && (j / quotient) % 3 == 1)
				matrix[i][j] = ' ';
		}
	}
	menger_sponge(matrix, size, quotient / 3);
}

/**
 * create_matrix - Creates a matrix
 *
 * @size: size of the matrix
 *
 * Return: Nothing
 */
char **create_matrix(int size)
{
	int i, j;
	char **matrix = malloc(size * sizeof(char *));

	for (i = 0; i < size; i++)
	{
		matrix[i] = malloc(size * sizeof(char));
	}

	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size; j++)
		{
			matrix[i][j] = '#';
		}
	}
	return (matrix);
}

/**
 * menger - Draws a 2D Menger Sponge
 *
 * @level: the level of the Menger Sponge to draw
 *
 * Return: Nothing
 */
void menger(int level)
{
	int size = pow(3, level);
	int quotient = size / 3;
	char **matrix;

	if (level < 0)
		return;

	matrix = create_matrix(size);
	menger_sponge(matrix, size, quotient);
	print_matrix(matrix, size);
	free_matrix(matrix, size);
}
