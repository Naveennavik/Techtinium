input_user=input("enter the statement:")
#your_string = "This is a string"
list_of_words = input_user.split()
next_word = int(list_of_words[list_of_words.index("hours") - 1]) 
next_word1= int(list_of_words[list_of_words.index("units") - 1])
hours = next_word
capacity = next_word1 
capacity_new_york=capacity
capacity_china=capacity
capacity_india=capacity
countries=["New york","China","India"]
print("output:")
for i in countries:
	if i == "New york":
		units_new_york={'10XLarge':320,'8XLarge':160,'4XLarge':80,'2XLarge':40,'XLarge':20,'Large':10}
		costs_new_york={'10XLarge':2820,'8XLarge':1400,'4XLarge':774,'2XLarge':450,'XLarge':230,'Large':120}
		new_york={}
		for i in units_new_york:
			if units_new_york[i] <= capacity_new_york:
				modulus=capacity_new_york // units_new_york[i]
				remain=capacity_new_york % units_new_york[i]
				capacity_new_york=remain
				key_new_york=i
				values_new_york=modulus
				new_york.update({key_new_york:values_new_york})
		total_new_york=0
		for key in costs_new_york:
			if key in new_york:
				total_new_york=total_new_york+(costs_new_york[key]*new_york[key])
		print("region :" "New York")
		print("total_cost:",total_new_york*hours)
		print("machines:",new_york)
