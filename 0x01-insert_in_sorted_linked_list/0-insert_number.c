#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * listint_t *insert_node - inserts a number
 * into a sorted singly list
 * @head: points to the head of the list
 * @number: number to insert
 * Return: the adress of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	if (head == NULL || *head == NULL)
		return (NULL);

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	while (tmp->next && tmp->next->n < number)
		tmp = tmp->next;
	if (tmp != *head)
	{
		new->next = tmp->next;
		tmp->next = new;
	}
	else
	{
		new->next = tmp;
		*head = new;
	}
	return (new);
}
