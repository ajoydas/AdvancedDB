CREATE type Airline_objtyp as object
(
    airline_id   number(10),
    airline_name         varchar2(20),
    airline_type varchar2(20)
);
create table Airline of Airline_objtyp (
    PRIMARY KEY (airline_id)
);

CREATE type Aeroplane_objtyp as object
(
    aeroplane_id    number(10),
    airline_id number(10),
    model       varchar2(20),
    capacity    number(10)
);

create table Aeroplane of Aeroplane_objtyp (
    PRIMARY KEY (aeroplane_id),
    FOREIGN KEY (airline_id) REFERENCES Airline(airline_id)
);

CREATE type Country_objtyp as object
(
    country_name       varchar2(20),
    population number(10)
);

CREATE type Airport_objtyp as object
(
    airport_id          number(10),
    airport_name       varchar2(50),
    airport_type       varchar2(20),
    num_of_runways    number(3),
    country Country_objtyp
);

create table Airport of Airport_objtyp (
    PRIMARY KEY (airport_id)
);

CREATE type FlightDestination_objtyp as object
(
    airport_id_dest number(10),
    arrival_time DATE
);

CREATE TYPE FlightDestination_array AS VARRAY(10) OF FlightDestination_objtyp;


CREATE type Flight_objtyp as object
(
    flight_num varchar2(20),
    aeroplane_id number(10),
    departure_time DATE,
    gate_num varchar2(10),
    airport_id_source number(10),
    dests FlightDestination_array
);

create table Flight of Flight_objtyp (
    PRIMARY KEY (flight_num),
    FOREIGN KEY (aeroplane_id) REFERENCES Aeroplane (aeroplane_id),
    FOREIGN KEY (airport_id_source) REFERENCES Airport (airport_id)
);

CREATE type Passenger_objtyp as object
(
    passport_num number(15),
    date_of_expiry DATE,
    country Country_objtyp
);

CREATE type Seat_objtyp as object
(
    seat_id number(10),
    seat_no varchar2(10),
    seat_type varchar2(20),
    price number(10),
    isSold number(1),
    flight_num varchar2(20)
);

create table Seat of Seat_objtyp (
    primary key (seat_id),
    FOREIGN KEY (flight_num) REFERENCES Flight (flight_num)
);

CREATE type PNR_objtyp as object
(
    pnr_id number(10),
    pnr_name varchar2(50),
    contact_info varchar2(50),
    passenger Passenger_objtyp
);

create table PNR of PNR_objtyp
(
    primary key (pnr_id)
);

CREATE type Agent_objtyp as object
(
    license_num       number(10),
    membership_num    number(10),
    country Country_objtyp
);

CREATE type Ticket_objtyp as object
(
    ticket_id number(10),
    seat_id number(10),
    pnr_id number(10),
    agent Agent_objtyp
);

create table Ticket of Ticket_objtyp (
    primary key (ticket_id),
    FOREIGN KEY (seat_id) REFERENCES Seat (seat_id),
    FOREIGN KEY (pnr_id) REFERENCES PNR (pnr_id)
);

CREATE type BoardingPass_objtyp as object
(
    ticket_id number(10),
    flight_num varchar2(20)
);

create table BoardingPass of BoardingPass_objtyp (
    primary key (ticket_id, flight_num),
    FOREIGN KEY (ticket_id) REFERENCES Ticket (ticket_id),
    FOREIGN KEY (flight_num) REFERENCES Flight (flight_num)
);


/* Relations */
-- CREATE type FlightDestination_objtyp as object
-- (
--     flight_num varchar2(20),
--     airport_id_dest number(10),
--     arrival_time DATE
-- );

-- create table FlightDestination of FlightDestination_objtyp (
--     FOREIGN KEY (airport_id_dest) REFERENCES Airport (airport_id),
--     FOREIGN KEY (flight_num) REFERENCES Flight (flight_num)
-- );

CREATE type PNRSSR_objtyp as object
(
    pnr_id number(10),
    service varchar2(20)
);

create table PNRSSR of PNRSSR_objtyp (
    FOREIGN KEY (pnr_id) REFERENCES PNR (pnr_id)
);

CREATE type Distance_objtyp as object
(
    airport_id_source number(10),
    airport_id_dest number(10),
    distant number(10)
);

create table Distance of Distance_objtyp (
    FOREIGN KEY (airport_id_source) REFERENCES Airport (airport_id),
    FOREIGN KEY (airport_id_dest) REFERENCES Airport (airport_id)
);