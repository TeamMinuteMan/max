declare
num int:=1;
begin
loop
if num>10 then
exit;
end if;
dbms_output.put_line(num);
num:=num+1;
end loop;
end;
/