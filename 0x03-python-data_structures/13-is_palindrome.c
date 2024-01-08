#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: pointer to a pointer to the head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *arr;
	int i = 0, j;
	int size = 0;

	/*count number of elements in a linked list*/
	while (current != NULL)
	{
		size++;
		current = current->next;
	}

	/*Allocate memory for array*/
	arr = malloc(size * sizeof(int));
	if (arr == NULL)
		return (0);

	/*Reset currrent to head*/
	current = *head;

	/*Traverse linked list and store the head of list*/
	while (current != NULL)
	{
		arr[i++] = current->n;
		current = current->next;
	}

	/*compare the element in the array*/
	for (j = 0; j < i / 2; j++)
	{
		if (arr[j] != arr[i - j - 1])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}
