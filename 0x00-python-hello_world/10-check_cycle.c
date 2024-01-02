#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: Pointer to the head of the linked list
 * Return: 0if there is no cycle 1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t  *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}

		slow = slow->next;
		fast = fast->next;
	}
	return (0);


}
