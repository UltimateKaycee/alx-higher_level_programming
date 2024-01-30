#include "Python.h"

/**
 * print_python_string - Function to prints info about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int leng_of;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	leng_of = ((PyASCIIObject *)(p))->leng_of;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", leng_of);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &leng_of));
}
