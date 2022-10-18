declare
a int;
begin
a:=&a;
if(a=15) then
dbms_output.put_line('Guess is correct');
else
NULL;
end if;
end;
/