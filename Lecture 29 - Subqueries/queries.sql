select cityid, avg(income) from customers group by cityid

-- select first_name, last_name, avg(income) from customers group by first_name, last_name


select cityname, avg(income) from customers left join cities on customers.cityid = cities.id
group by cityname
having cityname in ('Batumi', 'Qutaisi')


select id from cities

select * from customers where cityid not in (select id from cities)

delete from customers where cityid in (select id from cities where cityname='Tbilisi' or cityname='Batumi')

update customers set cityid = null where cityid in (select id from cities where cityname='Tbilisi' or cityname='Batumi')



create or replace function set_create_date()
returns trigger as $$
	begin
		NEW.create_date = now();
		return NEW;
	end
$$
language plpgsql


create trigger set_create_date_trigger
before insert on customers
for each row
execute function set_create_date()


insert into customers(idnumber, first_name) values('13131313', 'Jack')

update customers set cityid = 4 where idnumber='13131313'



create or replace function set_update_date()
returns trigger as $$
	begin
		NEW.update_date = now();
		return NEW;
	end
$$
language plpgsql


create trigger set_update_date_trigger
before update on customers
for each row
execute function set_update_date()




create view aggregate_view as
select cityname, avg(income) from customers left join cities on customers.cityid = cities.id
group by cityname
having cityname in ('Batumi', 'Qutaisi')


select * from aggregate_view


