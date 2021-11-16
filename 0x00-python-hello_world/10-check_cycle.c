#include "lists.h"

/**
 * check_cycle - checks whether a linked list has a cycle.
 * @list: Is a pointer to a linked list structure
 * Return: 0 as false if theres on cycle and 1 as true if there is a cycle.
 */

int check_cycle(listint_t *list)
{
  if (list = NULL)
    return 0;
  
  listint_t *first = list->next;
  listint_t *second = list;

  while (first != NULL && first->next != NULL && second != NULL)
    {
      if ( first == second)
	{
	  return 1;
	}
  first = first->next->next;
  second = second->next;
    }
  return 0;
}
