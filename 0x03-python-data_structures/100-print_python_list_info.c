#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the Python struct
 *
 */
void print_python_list_info(PyObject *p)
{
  unsigned int index;

  printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
  printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

  for (index = 0; index < PyList_Size(p); index++)
    printf("Element %d: %s\n", index, Py_TYPE(PyList_GetItem(p, index))->tp_name);
}
