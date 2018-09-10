#include "lists.h"

/**
 * check_cycle - checks to see if there is a cycle in a link list
 * @list: pointer to the link list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *quick = NULL;

	if (!list)
		return (0);
	slow = quick = list;
	do
	{
		slow = slow->next;
		quick = quick->next;
		if (quick)
			quick = quick->next;
	} while (quick && slow != quick);
	if (quick && slow == quick)
		return (1);
	return (0);
}
