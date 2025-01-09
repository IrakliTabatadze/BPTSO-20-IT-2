create table customer(
	id serial primary key,
	first_name varchar(25),
	last_name varchar(25),
	dateofbirth date,
	create_date timestamp,
	salary float
)


insert into customer(first_name, last_name, dateofbirth, create_date, salary) values(
	'John', 'Doe', '1990-05-25', '2025-01-09', 1000
),
('Anna', 'Smith', '1992-05-25', '2025-01-09', 2000),
('Kate', 'Doe', '1995-05-25', '2025-01-09', 3000),
('Jake', 'Dawson', '1997-05-25', '2025-01-09', 4000),
('John', 'Doe', '2000-05-25', '2025-01-09', 5000)

insert into customer(first_name, last_name, dateofbirth, create_date, salary) values(
	'John', 'Doe', NULL, '2025-01-09', NULL
),
('Anna', 'Smith', '1992-05-25', NULL, 2000),
('Kate', NULL, '1995-05-25', '2025-01-09', 3000),
('Jake', 'Dawson', '1997-05-25', '2025-01-09', 4000),
('John', 'Doe', '2000-05-25', '2025-01-09', NULL)



-- ყველა ჩანაწერის წაკითხვა
select * from customer

-- ყველა ჩანაწერის წაკითხვა რომლის სახელიც არის John
select * from customer where first_name = 'John'

-- ყველა ჩანაწერის წაკითხვა რომლის სახელიც არის John(ყურადღება არ ექცევა რეგისტრებს)
select * from customer where first_name ilike 'john'

-- ყველა ჩანაწერის წაკითხვა რომლის სახელიც იწყება J სიმბოლოზე (ყურადღება ექცევა რეგისტრებს)
select * from customer where first_name like 'J%'

-- ყველა ჩანაწერის წაკითხვა რომლის სახელიც იწყება J სიმბოლოზე (ყურადღება არ ექცევა რეგისტრებს)
select * from customer where first_name ilike 'j%'

-- ყველა ჩანაწერის წაკითხვა რომლის გვარიც სრულდება on სიმბოლოებზე (ყურადღება არ ექცევა რეგისტრებს)
select * from customer where last_name ilike '%on'

-- ყველა ჩანაწერის წაკითხვა რომლის გვარშიც მოხსენიებულია სიმბოლო i (ყურადღება არ ექცევა რეგისტრებს)
select * from customer where last_name ilike '%i%'

-- ყველა ჩანაწერის წაკითხვა რომლის სახელიც არის John ან დაბადების თარიღი არის 1995 წლის 1 იანვარი
select * from customer where first_name = 'John' or dateofbirth > '1995-01-01'

-- ყველა ჩანაწერის წაკითხვა რომელშიც შევსებული არ არის გვარის მნიშვნელობა
select * from customer where last_name is NULL

-- ყველა ჩანაწერის წაკითხვა რომელშიც შევსებული არის გვარის მნიშვნელობა
select * from customer where last_name is not NULL

-- ფილტრაცია თარიღების მიხედვით
select * from customer where dateofbirth = '1990-05-25'
select * from customer where dateofbirth < '2000-01-01' and dateofbirth > '1995-01-01'
select * from customer where dateofbirth < '2000-01-01' or dateofbirth > '1995-01-01'
select * from customer where dateofbirth between '1995-01-01' and '2000-01-01'
select * from customer where id between 3 and 7

-- სორტირება და მაქსიმალური რაოდენობის წაკითხვა
select * from customer order by dateofbirth asc limit 2
select * from customer where dateofbirth is not NULL order by dateofbirth desc limit 2

-- ჩანაწერების განახლება
update customer set create_date = '2025-01-01'
update customer set create_date = '2024-10-10' where first_name = 'John'

-- ჩანაწერების წაშლა
delete from customer where first_name = 'John'
delete from customer

-- ცხრილის გასუფთავება
truncate customer


drop table customer



