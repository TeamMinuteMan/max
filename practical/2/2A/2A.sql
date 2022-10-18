create sequence s1
start with 10
increment by 1
minvalue 10
maxvalue 100
cache 10;

create table student(
sid number(3),
sname varchar2(20));

desc user_sequences;

insert into student values(s1.nextval,'&name');

insert into student values(s1.nextval,'&name');

insert into student values(s1.nextval,'&name');


select * from student;