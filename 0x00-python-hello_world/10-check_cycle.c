#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Function to checks if a singly-linked
 * list has a cycle.
 * @list: list.
 *
 * Return: 0 If no cycle
 *         1 If a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *brand, *gard;

	if (list == NULL || list->next == NULL)
		return (0);

	brand = list->next;
	gard = list->next->next;

	while (brand && gard && gard->next)
	{
		if (brand == gard)
			return (1);

		brand = brand->next;
		gard = gard->next->next;
	}

	return (0);
}
