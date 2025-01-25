from models import session, Customer, City, Account, AccountTypes
from datetime import datetime

customers = session.query(Customer).all()

print(customers)

for customer in customers:
    print(customer.idnumber)



customers = session.query(Customer.idnumber, Customer.first_name).all()
print(customers)

for customer in customers:
    print(customer)


customer = session.query(Customer).filter(Customer.id == 1).first()

print(customer.first_name)
print(customer.last_name)


customers = session.query(Customer).filter(Customer.create_date < datetime(2025, 1, 23, 12, 25)).all()

print(datetime(2025, 1, 23, 12, 25, 15))

for customer in customers:
    print(customer.id, customer.create_date)


join_customers = session.query(Customer, City, Account).join(City, Customer.cityid == City.id).join(Account, Customer.idnumber == Account.customeridnumber).all()

print(join_customers)

for customer, city, account in join_customers:
    print(customer.idnumber, city.cityname, account.accountnumber)



city1 = City('Tbilisi', '12345')
city2 = City('Tbilisi', '12345')

cities = [city1, city2]

session.add(city)
session.add_all(cities)
session.commit()



update_customer = session.query(Customer).filter(Customer.id == 1).first()

print(update_customer.cityid)

update_customer.cityid = 1

session.commit()



delete_city = session.query(City).filter(City.id == 6).first()

session.delete(delete_city)
session.commit()
