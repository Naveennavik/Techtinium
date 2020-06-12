input_user=input("enter the statement:")
list_of_words = input_user.split()
hours = int(list_of_words[list_of_words.index("hours") - 1]) 
capacity= int(list_of_words[list_of_words.index("units") - 1])
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
	if i == "India":
		units_india = {'10XLarge':320,'8XLarge':160,'4XLarge':80,'2XLarge':40,'Large':10} 
		costs_india = {'10XLarge':2970,'8XLarge':1300,'4XLarge':890,'2XLarge':413,'Large':140}
		india = {}
		for i in units_india:            
			if units_india[i] <= capacity_india:
				modulus=capacity_india // units_india[i]
				remain = capacity_india % units_india[i]
				capacity_india = remain
				key_india = i
				values_india = modulus
				india.update({key_india:values_india})
		total_india = 0
		for key in costs_india:
			if key in india:
				total_india=total_india+(costs_india[key]*india[key])
		print("'region':'India'")
		print("'total_cost':",total_india*hours)
		print("machines:",india)

	if i == 'China':
		units_china = {'8XLarge':160,'4XLarge':80,'XLarge':20,'Large':10} 
		costs_china = {'8XLarge':1180,'4XLarge':670,'XLarge':200,'Large':110}
		china = {}
		for i in units_china:
			if units_china[i] <= capacity_china:
				modulus=capacity_china // units_china[i]
				remain = capacity_china % units_china[i]
				capacity_china = remain
				key_china = i
				values_china = modulus
				china.update({key_china:values_china})
		total_china = 0
		for key in costs_china:
			if key in china:
				total_china=total_china+(costs_china[key]*china[key])
		print("'region':'China'")
		print("'total_cost':",total_china*hours)
		print("machines:",china)