#include "lists.h"

/**
 * insert_node - function to inserts no into
 * a sorted singly-linked list.
 * @head: ptr to head of list.
 * @number: inserted no.
 *
 * Return: NULL if function fails
 *         else ptr to new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *start = *head, *again;

	again = malloc(sizeof(listint_t));
	if (again == NULL)
		return (NULL);
	again->n = number;

	if (start == NULL || start->n >= number)
	{
		again->next = start;
		*head = again;
		return (again);
	}

	while (start && start->next && start->next->n < number)
		start = start->next;

	again->next = start->next;
	again->next = again;

	return (again);
}
