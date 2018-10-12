
CREATE TABLE ptype (
  id int not null auto_increment primary key,
  description varchar(255)
);


CREATE TABLE pstatus (
  id int not null auto_increment primary key,
  description varchar(255)
);


CREATE TABLE person(
   pid int(11) not null auto_increment,
   type int,
   fame varchar(70),
   mname varchar(70),
   lname varchar(70),
   r_street varchar(255),
   r_city varchar(100),
   r_state varchar(100),
   status int,

   PRIMARY KEY (pid),

   FOREIGN KEY fk_person_ptype(type)
   REFERENCES ptype(id),

   FOREIGN KEY fk_person_pstatus(status)
   REFERENCES pstatus(id)
);


CREATE TABLE offender (
  opid int not null primary key,
  born date,
  died date,
  FOREIGN KEY fk_offender_person(opid)
  REFERENCES person(pid)
);


CREATE TABLE otypes (
  id int not null auto_increment primary key,
  description varchar(255)
);


CREATE TABLE offence_event (
  oid int not null auto_increment primary key,
  type int,
  victimpid int(11),
  motive varchar(255),
  date date,
  time time,
  witnesspid int(11),
  l_street varchar(255),
  l_city varchar(100),
  l_state varchar(100),

  FOREIGN KEY fk_offence_type(type)
  REFERENCES otypes(id),

  FOREIGN KEY fk_offence_victim(victimpid)
  REFERENCES person(pid),

  FOREIGN KEY fk_offence_witness(witnesspid)
  REFERENCES person(pid)
);


CREATE TABLE offender_offence (
  id  int not null auto_increment primary key,
  oid int,
  opid int,

  UNIQUE KEY (oid,opid),

  FOREIGN KEY fk_oo_offence(oid)
  REFERENCES offence_event(oid),

  FOREIGN KEY fk_oo_offender(opid)
  REFERENCES offender(opid)
);


CREATE TABLE prison (
  prid int not null auto_increment primary key,
  staffcount int,
  inchargeid int,
  a_street varchar(255),
  a_city varchar(100),
  a_state varchar(100),
  capacity int,

  FOREIGN KEY fk_prison_person(inchargeid)
  REFERENCES person(pid)
);


CREATE TABLE inmate (
  id int not null auto_increment primary key,
  opid int(11),
  ioid int,
  prid int,
  cellno int,
  startdate date,
  enddate date,
  misdemenour int,

  UNIQUE KEY (opid,prid,ioid,startdate),

  FOREIGN KEY fk_inmate_prison(prid)
  REFERENCES prison(prid),

  FOREIGN KEY fk_inmate_person(opid)
  REFERENCES offender(opid),

  FOREIGN KEY fk_inmate_offence(ioid)
  REFERENCES offence_event(oid)
);


CREATE TABLE family_member (
  id int not null auto_increment primary key,
  fmpid int(11),
  opid int(11),
  UNIQUE KEY(fmpid, opid),

  FOREIGN KEY fk_family_family(fmpid)
  REFERENCES person(pid),


  FOREIGN KEY fk_family_offender(opid)
  REFERENCES offender(opid)
);


CREATE TABLE biometrics (
  opid int(11) not null primary key,
  bloodgroup varchar(5),
  sex char(1),
  height int(3),
  hair varchar(20),
  weight int(3),
  eye varchar(20),
  skin varchar(20),
  img varchar(255),

  FOREIGN KEY fk_biometrics_offender(opid)
  REFERENCES offender(opid)

);


CREATE TABLE aka (
  id int not null auto_increment primary key ,
  opid int(11),
  name varchar(255),
  UNIQUE KEY(opid, name),

  FOREIGN KEY fk_aka_offender(opid)
  REFERENCES offender(opid)

);


CREATE TABLE trial (
  tid int not null auto_increment primary key,
  startdate date,
  enddate date,
  verdict varchar(255) not null DEFAULT 'NA',
  opid int(11),

  FOREIGN KEY fk_trial_offender(opid)
  REFERENCES offender(opid)

);
