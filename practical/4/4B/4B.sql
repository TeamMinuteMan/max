declare
a int;
b int;
c int;
i int;
begin
a:=0;
b:=1;
i:=3;
dbms_output.put_line(a);
dbms_output.put_line(b);
while i<=10 loop
c:=a+b;
dbms_output.put_line(c);
a:=b;
b:=c;
i:=i+1;
end loop;
end;
/