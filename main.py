# Me gusta la administración financiera, entonces quisiera hacer un programa que me ayude a registrar mis gastos del
# dia en un archivo .csv de la fecha del mes, podría aprovechar los decoradores para hacer la accion de escritura y edición del archivo y poder reutilizar esta pieza de codigo en otros proyectos. O incluso dentro del mismo codigo. Al final incluyo una funcion que también
# me entrega un balance

# Encapsular en una clase y hacer un first commit de este codigo a mi github de cemar ortiz (:
# TO_DO: on the first entry of the month, query the balance of the previous month if available
# if not available, skip and register the movement as first entry

from datetime import date
import pandas as pd
import os


# save_csv_with_date(*args, **kwargs) decorator 
def save_csv_with_date(func):
	today = date.today()
	path = 	str(today.month) + '_' + str(today.year) + '.csv'
	header = 'Movement, Concept, Partition, Date'
	
	if not os.path.exists(path):
		with open(path, 'w') as f:
			f.write(header + '\n')
			f.close()
			
	def wrapper(*args, **kwargs):
		with open(path, 'a') as f:
			f.write(func() + ',' + str(today) + '\n')
			f.close()
			
	return wrapper

# movement_register(amount) function
@save_csv_with_date
def movement_register():
	movement = int(input('Movement: '))
	concept = input('Concept: ')
	partition = input('Partition: ')
	
	return f'{movement}, {concept}, {partition}'
	
def get_balance():
	today = date.today()
	path = 	str(today.month) + '_' + str(today.year) + '.csv'
	df = pd.read_csv(path)
	balance = df['Movement'].sum()
	print('Your current balance is: ' + str(balance))
	
if __name__ == '__main__':
	movement_register()
	get_balance()
