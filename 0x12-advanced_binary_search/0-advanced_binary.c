#include "search_algos.h"

/**
 * print_array - Prints an array of integers.
 * @array: The array
 * @low: The beginning of the array
 * @high: The end of the array
 * Return: Nothing
 */
void print_array(int *array, int low, int high)
{
	int i;

	printf("Searching in array: ");
	for (i = low; i <= high; i++)
	{
		printf("%d", array[i]);
		if (i != high)
			printf(", ");
	}
	printf("\n");
}

/**
 * binary_search - Searches for a value in a sorted array of integers.
 * @array: The array
 * @low: The beginning of the array
 * @high: The end of the array
 * @value: Value to search for
 * Return: The index where value is located
 */
int binary_search(int *array, int low, int high, int value)
{
	int mid;

	if (low > high)
		return (-1);

	print_array(array, low, high);

	mid = low + (high - low) / 2;

	if (array[mid] == value && (mid == 0 || array[mid - 1] < value))
		return (mid);
	else if (array[mid] < value)
		return (binary_search(array, mid + 1, high, value));
	else if (array[mid] >= value)
		return (binary_search(array, low, mid, value));
	return (-1);
}

/**
 * advanced_binary - Searches for a value in a sorted array of integers.
 * @array: The array
 * @size: Size of the array
 * @value: Value to search for
 * Return: The index where value is located
 */
int advanced_binary(int *array, size_t size, int value)
{
	if (!array || size == 0)
		return (-1);

	return (binary_search(array, 0, size - 1, value));
}
