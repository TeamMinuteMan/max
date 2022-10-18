declare
a int;
begin
a:= 10;
<<jump>>
while a<20 loop
dbms_output.put_line('value of a: ' || a);
a:=a+1;
if(a=15) then
a:=a+1;
goto jump;
end if;
end loop;
end;
/