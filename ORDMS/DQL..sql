-- create function AIRPORT(airport_name in varchar2(50), airport_type in varchar2(50),
--                         num_of_runways in number(3), country_name in varchar2(50), population in  number(10))
-- return AIRPORT
-- begin
--     set self.airport_name = airport_name
--     set self.airport_type = airport_type
--     set self.num_of_runways = num_of_runways
--     set
-- end;

insert into AIRPORT values (new AIRPORT_OBJTYP(1,'name1', 'type1', 3, new COUNTRY_OBJTYP('name1', 1000)));
commit;

