# -*- coding: utf-8 -*-
# http://blog.jobbole.com/77240/
# todo： http://www.bjhee.com/greenlet.html

typedef struct _greenlet {
	PyObject_HEAD
	char* stack_start;
	char* stack_stop;
	char* stack_copy;
	intptr_t stack_saved;
	struct _greenlet* stack_prev;
	struct _greenlet* parent;
	PyObject* run_info;
	struct _frame* top_frame;
	int recursion_depth;
	PyObject* weakreflist;
	PyObject* exc_type;
	PyObject* exc_value;
	PyObject* exc_traceback;
	PyObject* dict;
} PyGreenlet;
