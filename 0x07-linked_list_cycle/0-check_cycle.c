#include "lists.h"

/**
 * check_cycle - cecks if a a singly linked list has a cycle in it.
 * @list: pointer to head of list
 * Return: 0 it there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}
