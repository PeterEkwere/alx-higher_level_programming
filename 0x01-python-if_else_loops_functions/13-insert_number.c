#include "lists.h"
/**
 * insert_node - is a function that adds a node to a list
 * @head: is a pointer to the first node
 * @number: is a data to be inserted
 * Return: a pointer to the node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *previous;
	listint_t *node = malloc(sizeof(listint_t));

	if (!node)
	{
		return (NULL);
	}
	node->n = number;
	node->next = NULL;
	current = *head;
	previous = NULL;
	if (*head == NULL)
	{
		*head = node;
	}
	else
	{
		while (current != NULL)
		{
			if (current->n > number)
			{
				node->next = previous->next;
				previous->next = node;
				break;
			}
			previous = current;
			current = current->next;
		}
	}
	return (node);

}
