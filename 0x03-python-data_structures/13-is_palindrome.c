#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * reverse - reverse a linked list
 * @head: start of list
 *
 * Return: reversed list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *ptr, *qtr;

	if (head == NULL)
		return (NULL);
	ptr = head;
	qtr = ptr->next;

	if (qtr == NULL)
		return (ptr);
	qtr = reverse(qtr);
	ptr->next->next = ptr;
	ptr->next = NULL;

	return (qtr);
}
/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: start of linked list
 *
 * Return: 0 | 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *qtr, *first, *second;

	ptr = *head;
	qtr = *head;
	if (head == NULL || *head == NULL || ptr->next == NULL)
		return (1);
	while (1)
	{
		ptr = ptr->next->next;
		if (ptr == NULL)
		{
			second = qtr->next;
			break;
		}
		if (ptr->next == NULL)
		{
			second = qtr->next->next;
			break;
		}
		qtr = qtr->next;
	}
	qtr->next = NULL;
	second = reverse(second);
	first = *head;
	while (first->next != NULL && second->next != NULL)
	{
		if (first->n == second->n)
		{
			first = first->next;
			second = second->next;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
