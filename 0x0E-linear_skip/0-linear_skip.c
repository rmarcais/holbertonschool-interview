#include "search.h"

/**
 * linear_skip - Function that searches for a value
 * in a sorted skip list of integers
 *
 * @list: Pointer to the head of the skip list to search in
 * @value: The value to search for
 * Return: A pointer on the first node where value is located
 */
skiplist_t *linear_skip(skiplist_t *list, int value)
{
	skiplist_t *current = list, *tmp = current;

	if (!list)
		return (NULL);

	while (current->express)
	{
		tmp = current;
		current = current->express;
		printf("Value checked at index [%ld] = [%d]\n",
		       current->index, current->n);
		if (current->n >= value)
			break;
	}

	if (current->n < value && !current->express)
	{
		tmp = current;
		while (current->next)
			current = current->next;
	}
	printf("Value found between indexes [%ld] and [%ld]\n",
	       tmp->index, current->index);

	while (tmp)
	{
		printf("Value checked at index [%ld] = [%d]\n",
		       tmp->index, tmp->n);
		if (tmp->n == value)
			return (tmp);
		tmp = tmp->next;
	}
	return (NULL);
}
