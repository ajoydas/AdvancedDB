
-- create function AIRPORT(airport_name in varchar2(50), airport_type in varchar2(50),
--                         num_of_runways in number(3), country_name in varchar2(50), population in  number(10))
-- return AIRPORT
-- begin
--     set self.airport_name = airport_name
--     set self.airport_type = airport_type
--     set self.num_of_runways = num_of_runways
--     set
-- end;

insert into AIRPORT values (1,'name1', 'type1', 3, new COUNTRY_OBJTYP('name1', 1000));
commit;

insert into AIRLINE
values (1, 'sdsd','sdsd');
insert into AEROPLANE values (1,1,'1', 1);
insert into AIRPORT values (1,'asd','asf',1,COUNTRY_OBJTYP('name1', 1000));
commit;

insert into FLIGHT
values ('2343',1,TO_DATE('2003/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'),'2',1,
        FlightDestination_array(
            FlightDestination_objtyp(1,TO_DATE('2004/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss')),
            FlightDestination_objtyp(1,TO_DATE('2004/05/03 21:02:44', 'yyyy/mm/dd hh24:mi:ss'))
            ));

