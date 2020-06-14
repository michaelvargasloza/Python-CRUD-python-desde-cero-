from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData

def delete():
	try:
		criteria = input("\nIngrese el ID del empleado para eliminar: ")
		db.Employees.delete_many({"id": criteria})
		print('\nBorrado exitoso.\n')
	except ImportError:
		platform_specific_module = None