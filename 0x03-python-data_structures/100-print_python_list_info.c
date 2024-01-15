#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about python list
 * @p: pointer to p
 * Return: zero on success
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	/*Obtain the size of the list*/
	size = PyList_Size(p);

	/*print the size and allocate memory of the list*/
	printf("[*] Size of the python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	/*iterate through the list and print information about each element*/
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

