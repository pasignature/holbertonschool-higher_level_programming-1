#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the singly linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *frnt = *head, *bck = *head, *end = NULL;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	while (bck->next)
		bck = bck->next;
	while (frnt->n == bck->n)
	{
		end = bck;
		if (frnt == bck || frnt->next == bck || frnt->next->next == bck)
		{
			return (1);
		}
		else
		{
			frnt = frnt->next;
			bck = frnt;
			while (bck->next != end)
				bck = bck->next;
		}
	}
	return (0);
}
