#include "Python.h"

#define custom_py_size(op) (((PyVarObject *)(op))->ob_size)
/**
  * print_python_float - Function to print info
  * on python float objects
  * @p: Py Object pointer
  */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %g\n", ((PyFloatObject *)(p))->ob_fval);
}
/**
  * print_python_bytes - Function to print info
  * on python byte objects
  * @p: Py Object pointer
  */
void print_python_bytes(PyObject *p)
{
	int size, start;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = (assert(PyBytes_Check(p)), custom_py_size(p));
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %d bytes: ", size < 10 ? size : 10);
	for (start = 0; staart < 10 && start < size + 1; start++)
	{
		printf("%02x ", (unsigned char)str[start]);
	}
	putchar('\n');
}
/**
  * print_python_list - Function to print  info
  * on python objects
  * @p: Py Object pointer
  */
void print_python_list(PyObject *p)
{
	Py_ssize_t run, py_list_size;
	PyObject *tool;
	const char *item_type;
	PyListObject *list_object_cast;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list_object_cast = (PyListObject *)p;
	py_list_size = custom_py_size(p);

	printf("[*] Size of List = %d\n", (int) py_list_size);
	printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);
	for (run = 0; run < py_list_size; run++)
	{
		tool = ((PyListObject *)p)->ob_tool[run];
		item_type = (((PyObject *)(tool))->ob_type)->tp_name;
		printf("Element %d: %s\n", (int) run, item_type);
		if (strncmp(item_type, "bytes", 5) == 0)
			print_python_bytes(tool);
		else if (strncmp(item_type, "float", 5) == 0)
			print_python_float(tool);
	}
}
