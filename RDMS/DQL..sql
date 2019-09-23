-- Buying ticket online
-- Insert to ticket
insert into TICKET values (22,10,10,null);
commit;

-- Selling ticket by agents
-- Insert to ticket with agent
insert into TICKET values (22,10,10,10);
commit;

-- Issue boarding pass to passengers
-- Insert to boarding pass
insert into BOARDINGPASS values (10, 'FLIGHT_NUM4');
commit;

-- Showing the available seats of a flight
-- Select from seats without ISSOLD bit
SELECT *
from SEAT
where FLIGHT_NUM like 'FLIGHT_NUM10' and ISSOLD=0;

-- Display the flight list and departure time
-- Select from flight
select FLIGHT_NUM, DEPARTURE_TIME
from FLIGHT;

-- Display the flight list and arrival time
-- Select from FLIGHTDESTINATION
select FLIGHT_NUM, ARRIVAL_TIME
from FLIGHTDESTINATION;

-- List of on-board passengers of a flight of an airline in a date
-- Select from PASSENGER joining with boarding pass, flight, Aeroplane, Airline
select *
from PASSENGER p
    natural join TICKET
    natural join BOARDINGPASS
    natural join FLIGHT
    natural join AEROPLANE
    natural join AIRLINE a
where a.AIRLINE_NAME like 'NAME1'
;
