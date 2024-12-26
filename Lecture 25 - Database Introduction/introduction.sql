-- მონაცემთა ბაზის შექმნა
create database test4

-- მონაცემთა ბაზის წაშლა
drop database test4


-- ცხრილის შექმნა
create table customer2(
	id integer not null,
	first_name varchar(20),
	description text,
	price float
)


-- ცხრილში ინფორმაციის ჩაწერა(ყველა სვეტი თანმიმდევრულად)
insert into customer values(20, 'John', 'New Description', 10.5)


-- ცხრილში ინფორმაციის ჩაწერა(მხოლოდ არჩეული სვეტები)
insert into customer(first_name, description) values('Anna', 'New Description 2'), ('Anna', 'New Description 2'),
('Anna', 'New Description 2'), ('Anna', 'New Description 2')

-- ცხრილიდან ინფორმაციის წაკითხვა(ყველა სვეტი)
select * from customer

-- ცხრილიდან ინფორმაციის წაკითხვა(მხოლოდ არჩეული სვეტები)
select description, first_name from customer
