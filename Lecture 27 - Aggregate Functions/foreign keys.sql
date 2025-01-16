create table cities(id serial primary key, cityname varchar(50) not null, zipcode varchar(5) not null,)

insert into cities(cityname, zipcode) values
('Tbilisi', '01234'),
('Batumi', '10101'),
('Qutaisi', '51511'),
('Telavi', '91919')


create table accounttypes(id serial primary key, accounttypename varchar(50) not null)


insert into accounttypes(accounttypename) values('Visa'),('Master Card'), ('Amex'), ('ვადიანი ანაბარი')


create table customers(id serial primary key, idnumber varchar(11) not null, first_name varchar(30) not null,
last_name varchar(50), dateofbirth date, cityid integer, street varchar(70), housenumber varchar(5), income float)


insert into customers(idnumber, first_name, cityid, income) values
('123456789', 'John', 1, 1774.5),
('123456888', 'Anna', 2, 5554.5),
('123456777', 'Kate', 2, 4444.5),
('123456000', 'James', 3, 2224.5),
('123456111', 'Bob', 3, 3334.5)



create table accountnumbers(id serial primary key, customeridnumber varchar(11) not null, accountnumber varchar(50) not null,
accounttypeid integer not null, balance float default 0)


insert into accountnumbers(customeridnumber, accountnumber, accounttypeid) values
('123456789', 'GE00BG00000012345678', 1),
('123456789', 'GE00BG00000012345777', 2),
('123456000', 'GE00BG00000065421234', 1),
('123456888', 'GE00BG00000011222333', 1)



alter table customers add constraint customer_city_id_fk foreign key (cityid) references cities(id)

alter table accountnumbers add constraint account_type_id_fk foreign key (accounttypeid) references accounttypes(id)

alter table accountnumbers add constraint customer_id_number_fk foreign key (customeridnumber) references customers(idnumber)

alter table customers add constraint unique_id_number unique (idnumber)




------------------------------------------------------------------------------------------------------------------------------------------------

select count(*) from customers

select count(last_name) as last_names, count(first_name) as first_names from customers


select min(income), max(income), avg(income) from customers

select min(id), max(id) from customers


select count(distinct(cityid)) from customers
