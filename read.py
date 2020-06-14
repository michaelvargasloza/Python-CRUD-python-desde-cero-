from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData

def read():
	try:
		empcol = db.Employees.find()
		print('\nListado de datos de la BD Empleados:\n')
		for emp in empcol:
			print(emp)

	except ImportError:
		platform_specific_module = None