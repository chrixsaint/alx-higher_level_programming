#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 * struct nohde - A singly-linked list node structure.
 * @m: An integer data element.
 * @next: A pointer to the next node in the list.
 */
typedef struct nohde
{
	int m;
	struct nohde *next;
} LinkedListNode;

size_t print_listint(const LinkedListNode *h);
LinkedListNode *add_nodeint(LinkedListNode **head, const int m);
void free_listint(LinkedListNode *head);
int check_cycle(LinkedListNode *list);

#endif

