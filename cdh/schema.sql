drop table if exists systems;

create table systems (
	id text primary key,
	title text not null,
	description text,
	active boolean, 
	group text not null
);
