# Write a function that prints the object types and returns 42

# provided declaration
def all_thing_is_obj(object: any) -> int:
	if isinstance(object, list):
		print("List :", type(object))
	elif isinstance(object, tuple):
		print("Tuple :", type(object))
	elif isinstance(object, set):
		print("Set :", type(object))
	elif isinstance(object, dict):
		print("Dict :", type(object))
	elif isinstance(object, str):
		print(f"{object}", "is in the kitchen :", type(object))
	else:
		print("Type not found")
	return (42)



