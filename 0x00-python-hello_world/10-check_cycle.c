#include "lists.h"

/**
 * check_cycle - checks whether a linked list has a cycle.
 * @list: Is a pointer to a linked list structure
 * Return: 0 as false if theres on cycle and 1 as true if there is a cycle.
 */

int check_cycle(listint_t *list)
{
listint_t *first = list;
listint_t *second = list;

if (list == NULL)
{
return (0);
}
second = second->next;
 
while (first != NULL && second != NULL && second->next != NULL)
{
if ( first == second)
{
return 1;
}
first = first->next;
second = second->next->next;
}
return 0;
}
