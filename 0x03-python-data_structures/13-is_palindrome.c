#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the singly linked list
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t **frnt = head;

	if (!head)
		return (0);
	if (!*head || !(*head)->next)
		return (1);
	return (ip_helper(frnt, (*head)->next));
}

#include <stdio.h>
/**
 * ip_helper - recursive function that does the actual checking if is palindrome
 * @frnt: pointer to front of linked list
 * @bck: pointer to back of linked list
 * Return: 1 if match, 0 if not
 */
int ip_helper(listint_t **frnt, listint_t *bck)
{
	if (bck->next)
	{
		if (!ip_helper(frnt, bck->next))
			return (0);
	}
	else
	{
		if ((*frnt)->n != bck->n)
			return (0);
		if (*frnt == bck || (*frnt)->next == bck)
			return (1);
		*frnt = (*frnt)->next;
	}
	return (1);
}
