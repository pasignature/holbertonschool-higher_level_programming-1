#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the singly linked list
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *walk = *head;
	int i = 0, count = 0, mid = 0;
	ssize_t sum1 = 0, sum2 = 0;

	if (!head)
		return (0);
	if (!*head || !(*head)->next)
		return (1);
	for (; walk; count++, walk = walk->next)
		sum1 += walk->n;
	mid = count / 2;
	for (walk = *head, i = 0; i < mid; walk = walk->next, i++)
		sum2 += walk->n;
	if (count % 2)
		sum1 -= walk->n;
	if (sum1 / 2 == sum2)
		return (1);
	return (0);
}
