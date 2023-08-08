#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle in it
 * @list: pointer to beginning of the node
 * Return: 1 if the list has a cycle, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

