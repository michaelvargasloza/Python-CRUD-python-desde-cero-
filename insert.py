from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData

#Función para insertar datos en la BD Mongo.
def insert():
	try:
		employeeid = input('Ingrese el ID del empleado: ')
		employeename = input('Nombre: ')
		employeeage = input('Edad: ')
		employeecountry = input('País: ')
		db.Employees.insert_one(
		{
			"id": employeeid,
			"name": employeename,
			"age": employeeage,
			"country": employeecountry

		})
		print("Usuario ingresado correctamente.")

	except ImportError:
		platform_specific_module = None
