#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert a node
 * in a sorted singly linked list
 * @head: head of list
 * @number: number to insert
 *
 * Return: address of new node
 * or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *prev;

	current = *head;
	prev = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else
	{
		while (current->next)
		{
			if (current->n >= new->n)
			{
				new->next = current;
				if(prev)
					prev->next = new;
				else
					*head = new;
				return (new);
			}

			prev = current;
			current = current->next;
		}
		current->next = new;
	}

	return (new);
}
