CREATE table Airline
(
    airline_id   number(10) primary key,
    airline_name varchar2(20),
    airline_type varchar2(20)
);

CREATE table Aeroplane
(
    aeroplane_id          number(10) primary key,
    airline_id number(10),
    model       varchar2(20),
    capacity    number(10),
    CONSTRAINT Aeroplane_FK FOREIGN KEY (airline_id) REFERENCES Airline (airline_id)
);

CREATE table Country
(
    country_id         number(3) primary key,
    country_name       varchar2(20),
    population number(10)
);

CREATE table Airport
(
    airport_id          number(10) primary key,
    airport_name       varchar2(50),
    airport_type       varchar2(20),
    num_of_runways    number(3),
    country_id number(3),
    CONSTRAINT Airport_FK FOREIGN KEY (country_id) REFERENCES Country (country_id)
);

CREATE table Flight
(
    flight_num varchar2(20) primary key,
    aeroplane_id number(10),
    departure_time DATE,
    gate_num varchar2(10),
    airport_id_source number(10),
    CONSTRAINT Flight_FK FOREIGN KEY (airport_id_source) REFERENCES Airport (airport_id)
);

CREATE table Passenger
(
    passenger_id number(10) primary key,
    passport_num number(15),
    date_of_expiry DATE,
    country_id number(3),
    CONSTRAINT Passenger_FK FOREIGN KEY (country_id) REFERENCES Country (country_id)
);

CREATE table Seat
(
    seat_id number(10) primary key,
    seat_no varchar2(10),
    seat_type varchar2(20),
    price number(10),
    isSold number(1),
    flight_num varchar2(20),
    CONSTRAINT Seat_FK FOREIGN KEY (flight_num) REFERENCES Flight (flight_num)
);

CREATE table Agent
(
    agent_id          number(10) primary key,
    license_num       number(10),
    membership_num    number(10),
    country_id number(3),
    CONSTRAINT Agent_FK FOREIGN KEY (country_id) REFERENCES Country (country_id)
);

CREATE table Ticket
(
    ticket_id number(10) primary key,
    seat_id number(10),
    passenger_id number(10),
    agent_id          number(10) null,
    CONSTRAINT Ticket_Seat_FK FOREIGN KEY (seat_id) REFERENCES Seat (seat_id),
    CONSTRAINT Ticket_Passenger_FK FOREIGN KEY (passenger_id) REFERENCES Passenger (passenger_id),
    CONSTRAINT Ticket_Agent_FK FOREIGN KEY (agent_id) REFERENCES Agent (agent_id)
);

CREATE table BoardingPass
(
    ticket_id number(10),
    flight_num varchar2(20),
    CONSTRAINT BoardingPass_Ticket_FK FOREIGN KEY (ticket_id) REFERENCES Ticket (ticket_id),
    CONSTRAINT BoardingPass_Flight_FK FOREIGN KEY (flight_num) REFERENCES Flight (flight_num),
    CONSTRAINT BoardingPass_PK PRIMARY KEY (ticket_id, flight_num)
 );

CREATE table PNR
(
    pnr_id number(10) primary key,
    pnr_name varchar2(50),
    contact_info varchar2(50),
    passenger_id number(10),
    CONSTRAINT PNR_FK FOREIGN KEY (passenger_id) REFERENCES Passenger (passenger_id)
);


/* Relations */
CREATE table FlightDestination
(
    flight_num varchar2(20),
    airport_id_dest number(10),
    arrival_time DATE,
    CONSTRAINT FlightDestination_Airport_FK FOREIGN KEY (airport_id_dest) REFERENCES Airport (airport_id),
    CONSTRAINT FlightDestination_Flight_FK FOREIGN KEY (flight_num) REFERENCES Flight (flight_num)
);

CREATE table PNRSSR
(
    pnr_id number(10),
    service varchar2(20),
    CONSTRAINT PNRSSR_FK FOREIGN KEY (pnr_id) REFERENCES PNR (pnr_id)
);

CREATE table Distance
(
    airport_id_source number(10),
    airport_id_dest number(10),
    distant number(10),
    CONSTRAINT Distance_Source_FK FOREIGN KEY (airport_id_source) REFERENCES Airport (airport_id),
    CONSTRAINT Distance_Dest_FK FOREIGN KEY (airport_id_dest) REFERENCES Airport (airport_id)
);