def var_dump(var, startspace : int=0):
	"""Dumps information about a variable

	This function displays structured information about a variable that includes its type and value. 
	Lists and dictionaries are explored recursively with values indented to show structure.

	Parameters
	----------
	var : any
		The variable to be dumped
	startspace : int, optional
		The number of spaces to indent with.
	"""
	
	vartype = type(var).__name__
	space = ' '*startspace
	
	# None type
	if var is None:
		print('%sNone' % space)
	
	# String, list and dict have a length that is useful to know
	elif vartype == 'str' or vartype == 'list' or vartype == 'dict':
		print('%s%s (length=%d): ' % (space, vartype, len(var)), end='')
		
		if vartype == 'str':
			print('\'%s\'' % var)
		
		# Lists contain other elements, so we need to call var_dump recursivly
		if vartype == 'list':
			if not len(var):
				print('[]')
			else:
				print('[')
				for item in var:
					var_dump(item, startspace=startspace+2)
				print('%s]' % space)
		
		# Dicts contain other elements, so we need to call var_dump recursivly
		if vartype == 'dict':
			if not len(var):
				print('{}')
			else:
				print('{')
				for key, value in var.items():
					print('%s\'%s\': ' % (' '*(startspace+2), key), end='')
					var_dump(value)
				print('%s}' % space)
	
	# Bool, int and float can just be outputed directly
	elif vartype == 'bool' or vartype == 'int' or vartype == 'float':
		print('%s%s: %s' % (space, vartype, var))
	
	# If it's not one of the types above, it's likely to be a class object.
	# These normally contain the __str__ method, but in case it doesn't we'll refuse to print
	else:
		print('%s%s: ' % (space, vartype), end='')
		if '__str__' in dir(var):
			print(var)
		else:
			print('(cannot display object)')
