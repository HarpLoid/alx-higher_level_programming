#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/*
 * check_cycle - checks if a list
 * has a cycle
 * @list: head pointer of list
 *
 * Return: 1 if list has a cycle
 * or 0 if list doesn't have a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
