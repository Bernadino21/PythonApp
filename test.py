import random
import json


	def read_values_from_json(file,key):
		values=[]

		with open("characters.json") as f:

			data=json.load(f)
			for entry in data:
				values.append(entry[key])
		return values


	def message(character,qute):
		return "{} a dit : {}".format(character,qute)

	def get_random_item_in(my_list):
		rand_numb=random.randint(0,lent(my_list)-1)
		item = my_list[rand_numb]
		return item

	def get_random_quote():
		all_values=read_values_from_json('qutes.json','quote')
		return get_random_item_in(all_values)

	def get_random_character():
		all_values=read_values_from_json('characters.json','character')
		return get_random_item_in(all_values)

	user_answer = input('Continuer o')

	while user_answer =="o":
		print(message(get_random_character(),get_random_quote()))