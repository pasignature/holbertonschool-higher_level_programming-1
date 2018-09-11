#include "lists.h"

/**
 * insert_node - inserts a node into a sorted link list
 * @head: ptr to the head of a link list
 * @number: number stored in the new node
 * Return: returns the pointer to the new link ist
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new)
	{
		new->n = number;
		new->next = *head;
		if (!new->next || new->n <= (*head)->n)
			*head = new;
		else
			while (new->next && new->n > new->next->n)
			{
				prev = new->next;
				new->next = prev->next;
				if (!new->next)
					break;
			}
		if (prev)
			prev->next = new;
	}
	return (new);
}
