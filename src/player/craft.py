
def craft(recipe_list, recipe, inventory, amount=1, debug=False):
	craftable = True
	tmp_storage = inventory.storage[:]

	for x in range(amount):
		for x in recipe_list[recipe]["recipe"]:
			if x in tmp_storage:
				tmp_storage.remove(x)
			else:
				print("Cannot craft this item.")
				return
	
	if debug:
		print("Confirmed Craftable")

	for x in range(amount):
		for x in recipe_list[recipe]["recipe"]:
			if x in inventory.storage:
				inventory.storage.remove(x)
			else:
				print("Cannot craft this item. Some of your stuff burned.")
				return

	print("Crafted " + str(amount) + " "+recipe)	
	inventory.add(recipe, recipe_list[recipe]["type"])