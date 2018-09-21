#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the singly linked list
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t **frnt = head;
	int mid = 0;

	if (!head)
		return (0);
	if (!*head || !(*head)->next)
		return (1);
	return (ip_helper(frnt, (*head)->next, &mid));
}

#include <stdio.h>
/**
 * ip_helper - recursive func that does the actual checking if is palindrome
 * @frnt: pointer to front of linked list
 * @bck: pointer to back of linked list
 * Return: 1 if match, 0 if not
 */
int ip_helper(listint_t **frnt, listint_t *bck, int *mid)
{
	if (bck->next)
	{
		if (!ip_helper(frnt, bck->next, mid))
			return (0);
		if (*mid)
			return (1);
	}
	if ((*frnt)->n == bck->n)
	{
		if (*frnt == bck || (*frnt)->next == bck)
			*mid = 1;
		else
			*frnt = (*frnt)->next;
		return (1);
	}
	return (0);
}
