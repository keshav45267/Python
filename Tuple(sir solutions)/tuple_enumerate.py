# to return every other element from the tuple

def skip_elements(elements):
	new_tuple = tuple()
	for i,e in enumerate(elements):
		if i%2 == 0:
			new_tuple = new_tuple + (e,)
	return new_tuple


print(skip_elements(("a", "b", "c", "d", "e", "f", "g")))
print(skip_elements(('Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach')))
