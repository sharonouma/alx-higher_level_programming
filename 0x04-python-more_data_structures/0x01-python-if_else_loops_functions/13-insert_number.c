#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the head of the list
 * @number: The number to insert
 *
 * Return: Address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current_node = *head;
	listint_t *previous_node = NULL;

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!current_node || number < current_node->n)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}

	while (current_node && number > current_node->n)
	{
		previous_node = current_node;
		current_node = current_node->next;
	}

	new_node->next = current_node;
	previous_node->next = new_node;

	return (new_node);
}
