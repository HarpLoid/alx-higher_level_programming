#include "lists.h"

listint_t *reverse_list(listint_t **head);
/**
 * is_palindrome - checks if a linked list
 * is a palindrome
 * @head: A pointer to the head of the list
 *
 * Return: 0 if the list is not a palindrome
 * 1 if the list is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reversed, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reversed = reverse_list(&temp);
	mid = reversed;

	temp = *head;
	while (reversed)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	reverse_list(&mid);

	return (1);
}

/**
 * reverse_list - Reverse a list
 * @head: pointer to head of list
 * to reverse
 *
 * Return: pointer to the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head, *prev = NULL, *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
