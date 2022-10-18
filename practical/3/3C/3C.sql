declare
per float;
grade char(1);
begin
per:=&per;

if(per>=75.00) then
grade:='D';
elsif(per<75.00 and per>=60.00) then
grade:='F';
elsif(per<60.00 and per>45.00) then
grade:='S';
elsif(per<45.00 and per>35.00) then
grade:='P';
elsif(per<35.00) then
grade:='F';
end if;
case
when grade='D' then dbms_output.put_line('Distinction');
when grade='F' then dbms_output.put_line('First Class');
when grade='S' then dbms_output.put_line('Second Class');
when grade='P' then dbms_output.put_line('Pass');
when grade='K' then dbms_output.put_line('Fail');
else dbms_output.put_line('No such grade');
end case;
end;
/