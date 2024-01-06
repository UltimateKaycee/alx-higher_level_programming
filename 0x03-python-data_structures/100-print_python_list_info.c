#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - To print info abt Python lists.
 * @p: list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, start;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (start = 0; start < size; start++)
	{
		printf("Element %d: ", start);

		obj = PyList_GetItem(p, start);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
