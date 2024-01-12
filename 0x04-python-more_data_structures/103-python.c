#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Function to print info about Python list.
 * @p: PyObject list.
 */
void print_python_list(PyObject *p)
{
	int the_size, give, start;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	the_size = var->ob_size;
	give = list->allocated;

	printf("[*] About Python list\n");
	printf("[*] Size of Python List = %d\n", the_size);
	printf("[*] Allocated = %d\n", give);

	for (start = 0; start < the_size; start++)
	{
		type = list->ob_item[start]->ob_type->tp_name;
		printf("Component %d: %s\n", start, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[start]);
	}
}

/**
 * print_python_bytes - Function to print info about Python objects.
 * @p: PyObject object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char begin, sizer;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] Object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  Attempting: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		sizer = 10;
	else
		sizer = ((PyVarObject *)p)->ob_size + 1;

	printf("  initial %d bytes: ", sizer);
	for (begin = 0; begin < sizer; begin++)
	{
		printf("%02hhx", bytes->ob_sval[begin]);
		if (begin == (sizer - 1))
			printf("\n");
		else
			printf(" ");
	}
}
