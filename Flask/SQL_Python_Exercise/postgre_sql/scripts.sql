--CREATE SCHEMA AND TABLES, POPULATE USER TABLE WITH DATA

CREATE SCHEMA lifter;

CREATE TABLE lifter.users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    birthdate DATE NOT NULL,
    is_enabled INTEGER DEFAULT 1,
    is_in_arrears INTEGER DEFAULT 0
);



INSERT INTO lifter.users (username, password, email, birthdate, is_enabled)
VALUES 
    ('john_smith', '$2a$10$hashedpassword1', 'john.smith@email.com', '1990-03-15', 1),
    ('mary_jones', '$2a$10$hashedpassword2', 'mary.jones@email.com', '1985-07-22', 1),
    ('david_brown', '$2a$10$hashedpassword3', 'david.brown@email.com', '1992-11-08', 1),
    ('sarah_wilson', '$2a$10$hashedpassword4', 'sarah.wilson@email.com', '1988-01-30', 1),
    ('michael_davis', '$2a$10$hashedpassword5', 'michael.davis@email.com', '1995-05-17', 1),
    ('jennifer_miller', '$2a$10$hashedpassword6', 'jennifer.miller@email.com', '1991-09-25', 1),
    ('robert_garcia', '$2a$10$hashedpassword7', 'robert.garcia@email.com', '1987-12-03', 1),
    ('linda_martinez', '$2a$10$hashedpassword8', 'linda.martinez@email.com', '1993-04-19', 1),
    ('william_rodriguez', '$2a$10$hashedpassword9', 'william.rodriguez@email.com', '1989-08-12', 1),
    ('patricia_hernandez', '$2a$10$hashedpassword10', 'patricia.hernandez@email.com', '1994-02-28', 1),
    ('james_lopez', '$2a$10$hashedpassword11', 'james.lopez@email.com', '1986-06-14', 1),
    ('barbara_gonzalez', '$2a$10$hashedpassword12', 'barbara.gonzalez@email.com', '1990-10-07', 1),
    ('richard_perez', '$2a$10$hashedpassword13', 'richard.perez@email.com', '1992-03-21', 1),
    ('susan_sanchez', '$2a$10$hashedpassword14', 'susan.sanchez@email.com', '1988-07-16', 1),
    ('charles_ramirez', '$2a$10$hashedpassword15', 'charles.ramirez@email.com', '1991-11-29', 1),
    ('jessica_torres', '$2a$10$hashedpassword16', 'jessica.torres@email.com', '1993-01-05', 1),
    ('thomas_flores', '$2a$10$hashedpassword17', 'thomas.flores@email.com', '1987-05-23', 1),
    ('karen_rivera', '$2a$10$hashedpassword18', 'karen.rivera@email.com', '1995-09-11', 1),
    ('daniel_gomez', '$2a$10$hashedpassword19', 'daniel.gomez@email.com', '1989-12-18', 1),
    ('nancy_diaz', '$2a$10$hashedpassword20', 'nancy.diaz@email.com', '1994-04-02', 1),
    ('matthew_cruz', '$2a$10$hashedpassword21', 'matthew.cruz@email.com', '1986-08-27', 1),
    ('betty_reyes', '$2a$10$hashedpassword22', 'betty.reyes@email.com', '1992-02-14', 1),
    ('anthony_morales', '$2a$10$hashedpassword23', 'anthony.morales@email.com', '1990-06-09', 1),
    ('helen_jimenez', '$2a$10$hashedpassword24', 'helen.jimenez@email.com', '1988-10-31', 1),
    ('mark_ruiz', '$2a$10$hashedpassword25', 'mark.ruiz@email.com', '1991-03-26', 1),
    ('sandra_ortiz', '$2a$10$hashedpassword26', 'sandra.ortiz@email.com', '1993-07-13', 1),
    ('paul_castillo', '$2a$10$hashedpassword27', 'paul.castillo@email.com', '1987-11-20', 1),
    ('ashley_ramos', '$2a$10$hashedpassword28', 'ashley.ramos@email.com', '1995-01-08', 1),
    ('steven_gutierrez', '$2a$10$hashedpassword29', 'steven.gutierrez@email.com', '1989-05-15', 1),
    ('kimberly_vargas', '$2a$10$hashedpassword30', 'kimberly.vargas@email.com', '1994-09-22', 1),
    ('andrew_mendoza', '$2a$10$hashedpassword31', 'andrew.mendoza@email.com', '1986-02-11', 0),
    ('donna_castro', '$2a$10$hashedpassword32', 'donna.castro@email.com', '1992-06-28', 0),
    ('joshua_chavez', '$2a$10$hashedpassword33', 'joshua.chavez@email.com', '1990-10-05', 0),
    ('michelle_espinoza', '$2a$10$hashedpassword34', 'michelle.espinoza@email.com', '1988-01-19', 0),
    ('kevin_silva', '$2a$10$hashedpassword35', 'kevin.silva@email.com', '1991-05-24', 0),
    ('emily_medina', '$2a$10$hashedpassword36', 'emily.medina@email.com', '1993-09-07', 0),
    ('brian_alvarado', '$2a$10$hashedpassword37', 'brian.alvarado@email.com', '1987-12-30', 0),
    ('amanda_santos', '$2a$10$hashedpassword38', 'amanda.santos@email.com', '1995-04-16', 0),
    ('george_aguilar', '$2a$10$hashedpassword39', 'george.aguilar@email.com', '1989-08-03', 0),
    ('stephanie_guzman', '$2a$10$hashedpassword40', 'stephanie.guzman@email.com', '1994-11-27', 0),
    ('edward_rojas', '$2a$10$hashedpassword41', 'edward.rojas@email.com', '1986-03-14', 0),
    ('deborah_mendez', '$2a$10$hashedpassword42', 'deborah.mendez@email.com', '1992-07-21', 0),
    ('ronald_delgado', '$2a$10$hashedpassword43', 'ronald.delgado@email.com', '1990-11-08', 0),
    ('laura_moreno', '$2a$10$hashedpassword44', 'laura.moreno@email.com', '1988-02-25', 0),
    ('jason_valencia', '$2a$10$hashedpassword45', 'jason.valencia@email.com', '1991-06-12', 0),
    ('rebecca_herrera', '$2a$10$hashedpassword46', 'rebecca.herrera@email.com', '1993-10-29', 0),
    ('ryan_campos', '$2a$10$hashedpassword47', 'ryan.campos@email.com', '1987-01-06', 0),
    ('cynthia_vega', '$2a$10$hashedpassword48', 'cynthia.vega@email.com', '1995-05-23', 0),
    ('jacob_guerrero', '$2a$10$hashedpassword49', 'jacob.guerrero@email.com', '1989-09-10', 0),
    ('kathleen_soto', '$2a$10$hashedpassword50', 'kathleen.soto@email.com', '1994-12-17', 0);

    CREATE TABLE lifter.cars(
    car_id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    is_available INTEGER DEFAULT 1
    );

    CREATE TABLE lifter.rentals(
    rental_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES lifter.users(user_id),
    car_id INT REFERENCES lifter.cars(car_id),
    rental_date DATE DEFAULT CURRENT_DATE,
    is_returned INTEGER DEFAULT 0
    );

--INSERT NEW USER AND CAR, UPDATE USER AND CAR STATUS, RECORD A RENTAL, MARK A CAR AS RETURNED, QUERY AVAILABLE AND UNAVAILABLE CARS

INSERT INTO lifter.users (username, password, email, birthdate, is_enabled)
VALUES 
    ('john_smith', '$2a$10$hashedpassword1', 'john.smith@email.com', '1990-03-15', 1);

INSERT INTO lifter.cars (brand, model, year, is_available)
VALUES
    ('Toyota', 'Camry', 2020, 1);
UPDATE lifter.users
SET is_enabled = 0
WHERE user_id = 1;

UPDATE lifter.users
SET is_in_arrears = 0
WHERE user_id = 1;

UPDATE lifter.cars
SET is_available = 0
WHERE car_id = 1;

INSERT INTO lifter.rentals (user_id, car_id, rental_date, is_returned)
VALUES
    (1, 1, '2024-06-01', 0);


-------
UPDATE lifter.rentals
SET is_returned = 1
WHERE rental_id = 1;

UPDATE lifter.cars
SET is_available = 1
WHERE car_id = (SELECT car_id FROM lifter.rentals WHERE rental_id = 1);
--------

UPDATE lifter.cars
SET is_available = 0
WHERE car_id = 1;

SELECT * FROM lifter.cars
WHERE is_available = 1;
SELECT * FROM lifter.cars
WHERE is_available = 0;

SELECT * FROM lifter.users;

SELECT * FROM lifter.cars;

SELECT * FROM lifter.rentals;

---------------
DROP TABLE lifter.rentals;
DROP TABLE lifter.cars;
DROP TABLE lifter.users;


query = 'INSERT INTO lifter.rentals (user_id, car_id, rental_date, is_returned) VALUES (%s, %s, %s, %s)',
args = (1, 3, '2026-01-30', 0)