#include "python.h"
#include <stdio.h>

/**
 * print_python_list - ...
 * @p: ..
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, typeName);
	}
}
/**
 * print_python_bytes - ...
 * @p: ...
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_GET_SIZE(p);
	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);

	if (size > 10)
	{
		size = 10;
	}

	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %zd bytes:", size);
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		printf(" %02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}
/**
 * print_python_float - ...
 * @p: ...
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}
