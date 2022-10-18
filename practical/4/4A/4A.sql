declare
num int;
fact int;
i int;
begin
num:=&num;
fact:=1;
for i in 1..num loop
fact:=fact*i;
end loop;
dbms_output.put_line(fact);
end;
/