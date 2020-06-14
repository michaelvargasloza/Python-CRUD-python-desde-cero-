import insert
import read
import update
import delete

class Programa:
	def __init__(self):
		self.dato = 1

	def menu(self):
		while self.dato:
			selection = input('\nSelecciona 1 para insertar, 2 para actualizar, 3 para leer, 4 para borrar.\n')

			if selection == '1':
				insert.insert()
			elif selection == '2':
				update.update()
			elif selection == '3':
				read.read()
			elif selection == '4':
				delete.delete()
			else:
				print ('\nSelección inválida.')


persona1 = Programa()
persona1.menu()