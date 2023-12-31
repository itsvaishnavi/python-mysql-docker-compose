import pymysql

class DBClass:
	def __init__(self):
		self.connection = pymysql.connect(user='root',password='password',host='test-mysql-db',database='db')
		print("Connection to database successful....")
		self.cursor = self.connection.cursor()


	def create_table_if_not_exists(self):
		query = "create table if not exists test_table(id int, s_name text);"

		try:
			self.cursor.execute(query)

		except Exception as e:
			print(e)

		else:
			print("Table created successfully....")


	def insert_data(self, data:tuple):
		query = "insert into test_table(id, s_name) values (%s, '%s')" %data
		print(query)

		try:
			self.cursor.execute(query)
			self.connection.commit()
		
		except Exception as e:
			print(e)

		else:
			print("Data inserted successfully...")


	def update_record(self):
		pass