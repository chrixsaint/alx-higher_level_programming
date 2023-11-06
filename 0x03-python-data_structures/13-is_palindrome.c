#include <stdlib.h>
#include "lists.h"
/**
 * get_palindrme - checks if a singly linked list is a palindrome
 *
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if linked list is a palindrome, 0 otherwise
 */
int get_palindrme(listint_t **head)
{
	listint_t *current = *head;
	int aii = 0;
	int j = 0;

	int arr[1024];

	if (*head == NULL)
	{
		return (0);
	}
	while (current != NULL)
	{
		arr[aii++] = current->n;
		current = current->next;
	}

	for (j = 0; j < aii / 2; j++)
	{
		if (arr[j] != arr[aii - 1 - j])
			return (0);

	}
	return (1);

}
