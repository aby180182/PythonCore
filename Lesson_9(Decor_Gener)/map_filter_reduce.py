from functools import reduce


people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}]
people_maped = list(map(lambda x: x.get('height'), people))
people_filtered = list(filter(None, people_maped))
people_reduced = reduce(lambda x, y: x + y, people_filtered)
print(people_reduced)

