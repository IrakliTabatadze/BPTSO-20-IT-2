
alter table test alter column first_name type varchar(50)

alter table test alter column first_name type integer -- Error

alter table test add column last_name varchar(30)

alter table test alter column first_name set not null

alter table test drop column last_name

alter table customers add constraint city_id_fk foreign key (cityid) references cities(id)

----------------------------------------------------------------------------------------------------------------------------------


select
	customers.id,
	customers.idnumber,
	customers.first_name,
	cities.cityname
from customers
	inner join cities on customers.cityid = cities.id



select
	customers.id,
	customers.idnumber,
	customers.first_name,
	cities.cityname
from customers
	left join cities on customers.cityid = cities.id


select
	customers.id,
	customers.idnumber,
	customers.first_name,
	cities.cityname
from customers
	right join cities on customers.cityid = cities.id


select
	customers.id,
	customers.idnumber,
	customers.first_name,
	cities.cityname
from customers
	full join cities on customers.cityid = cities.id




select
	customers.id,
	customers.idnumber,
	customers.first_name,
	cities.cityname
from customers
	cross join cities




select
	accounts.id,
	accounts.customeridnumber,
	customers.first_name,
	accounts.accountnumber,
	accounttypes.accounttypename,
	accounts.balance
from accounts
	left join accounttypes on accounts.accounttypeid = accounttypes.id
	right join customers on accounts.customeridnumber = customers.idnumber



select
	customers.id,
	customers.idnumber,
	customers.first_name,
	cities.cityname,
	cities.zipcode,
	accounts.accountnumber,
	accounttypes.accounttypename,
	accounts.balance
from customers
	left join cities on customers.cityid = cities.id
	left join accounts on customers.idnumber = accounts.customeridnumber
	left join accounttypes on accounts.accounttypeid = accounttypes.id


select
	customers.id,
	customers.idnumber,
	customers.first_name,
	cities.cityname,
	cities.zipcode,
	accounts.accountnumber,
	accounttypes.accounttypename,
	accounts.balance
from customers
	left join cities on customers.cityid = cities.id
	inner join accounts on customers.idnumber = accounts.customeridnumber
	right join accounttypes on accounts.accounttypeid = accounttypes.id
where idnumber = '123456789'

