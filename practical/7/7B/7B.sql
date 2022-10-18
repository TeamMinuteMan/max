create table customers(id number,name varchar2(20),dept varchar2(20),salary number(10));
insert into customers values(1,'Pavan','IT',500000);
insert into customers values(2,'kaustubh','CS',600000);
insert into customers values(3,'Ritesh','CS',550000);
insert into customers values(4,'Sejal','IT',650000);

CREATE OR REPLACE FUNCTION totalCustomers
RETURN number IS
total  number(2):=0;
BEGIN
 SELECT count(*)into total
 FROM customers;
 RETURN total;
END;
/

DECLARE
 c number(2);
BEGIN
 c:=totalCustomers();
 dbms_output.put_line('Total no.of Customers:'||c);
END;
/