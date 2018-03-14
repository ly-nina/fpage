drop table if exists gps;
drop table if exists wait;

create table gps
(id integer primary key autoincrement,
name string not null,
time datetime default (datetime('now', 'localtime'))  
latlng string not null,
);


create table wait
(id integer primary key autoincrement,
time datetime default (datetime('now', 'localtime')),
location string not null);



