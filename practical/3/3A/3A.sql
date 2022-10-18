declare 
a int;
begin
a:=&a;
if(mod(a,2)=0) then
dbms_output.put_line(a||'is Even.');
else
dbms_output.put_line(a||'is Odd.');
end if;
end;
/