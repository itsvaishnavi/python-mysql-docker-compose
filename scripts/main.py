from dbclass import DBClass

def main():
	dBClass = DBClass()

	dBClass.create_table_if_not_exists()

	dBClass.insert_data((1, "Vaishnavi"))

	dBClass.insert_data((2, "Bhakti"))

	dBClass.insert_data((3, "Vipra"))

if __name__ == "__main__":
	main()