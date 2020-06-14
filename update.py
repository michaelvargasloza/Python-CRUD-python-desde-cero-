from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData

def update():
	try:
		criteria = input('\nIngrese el ID para actualizar: ')
		name = input('\nIngrese el nombre para actualizar: ')
		age = input('\nIngrese la edad para actualizar: ')
		country = input('\nIngrese el país para actualizar: ')

		db.Employees.update_one(
		{"id": criteria},
		{
			"$set": {
				"name": name,
				"age": age,
				"country": country
			}
		}
		)
		print("\nDatos actualizados correctamente.\n")

	except ImportError:
		platform_specific_module = None