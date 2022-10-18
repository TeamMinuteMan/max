DECLARE
n3 number(2);
BEGIN
n3:=adder(11,22);
dbms_output.put_line('Addition is:'||n3);
END;
/