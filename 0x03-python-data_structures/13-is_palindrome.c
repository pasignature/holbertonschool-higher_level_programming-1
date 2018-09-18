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
	if (!*head || !(*head)->next)
		return (1);
	bck = frnt->next;
	while (bck->next)
		bck = bck->next;
	while (frnt->n == bck->n)
	{
		end = bck;
		if (frnt == bck || frnt->next == bck || frnt->next->next == bck)
			return (1);
		else
		{
			frnt = frnt->next;
			bck = frnt->next;
			while (bck->next != end)
				bck = bck->next;
		}
	}
	return (0);
}
