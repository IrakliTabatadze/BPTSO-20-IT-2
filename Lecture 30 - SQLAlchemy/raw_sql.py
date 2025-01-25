import psycopg2

host = 'localhost' # 127.0.0.1
port = '5432'
user = 'postgres'
password = '123123'
database = 'BPTSO-20-IT-2'

connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)

print('Connection established')

cursor = connection.cursor()

# select_query = '''
#     select * from customers;
# '''

select_query = 'select * from customers where id = 1'

cursor.execute(select_query)

# data = cursor.fetchall()
data = cursor.fetchone()

print(data)



delete_query = 'delete from cities where id = 1'

cursor.execute(delete_query)

connection.commit()


cursor.close()
connection.close()

# ORM - Object Related Mapping