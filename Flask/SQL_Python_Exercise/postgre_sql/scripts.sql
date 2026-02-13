--CREATE SCHEMA AND TABLES, POPULATE USER TABLE WITH DATA

CREATE SCHEMA lifter;

CREATE TABLE lifter.users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    birthdate DATE NOT NULL,
    is_enabled BOOLEAN DEFAULT true,
    is_in_arrears BOOLEAN DEFAULT false
);



INSERT INTO lifter.users (username, password, email, birthdate, is_enabled)
VALUES 
    ('john_smith', '$2a$10$hashedpassword1', 'john.smith@email.com', '1990-03-15', true),
    ('mary_jones', '$2a$10$hashedpassword2', 'mary.jones@email.com', '1985-07-22', true),
    ('david_brown', '$2a$10$hashedpassword3', 'david.brown@email.com', '1992-11-08', true),
    ('sarah_wilson', '$2a$10$hashedpassword4', 'sarah.wilson@email.com', '1988-01-30', true),
    ('michael_davis', '$2a$10$hashedpassword5', 'michael.davis@email.com', '1995-05-17', true),
    ('jennifer_miller', '$2a$10$hashedpassword6', 'jennifer.miller@email.com', '1991-09-25', true),
    ('robert_garcia', '$2a$10$hashedpassword7', 'robert.garcia@email.com', '1987-12-03', true),
    ('linda_martinez', '$2a$10$hashedpassword8', 'linda.martinez@email.com', '1993-04-19', true),
    ('william_rodriguez', '$2a$10$hashedpassword9', 'william.rodriguez@email.com', '1989-08-12', true),
    ('patricia_hernandez', '$2a$10$hashedpassword10', 'patricia.hernandez@email.com', '1994-02-28', true),
    ('james_lopez', '$2a$10$hashedpassword11', 'james.lopez@email.com', '1986-06-14', true),
    ('barbara_gonzalez', '$2a$10$hashedpassword12', 'barbara.gonzalez@email.com', '1990-10-07', true),
    ('richard_perez', '$2a$10$hashedpassword13', 'richard.perez@email.com', '1992-03-21', true),
    ('susan_sanchez', '$2a$10$hashedpassword14', 'susan.sanchez@email.com', '1988-07-16', true),
    ('charles_ramirez', '$2a$10$hashedpassword15', 'charles.ramirez@email.com', '1991-11-29', true),
    ('jessica_torres', '$2a$10$hashedpassword16', 'jessica.torres@email.com', '1993-01-05', true),
    ('thomas_flores', '$2a$10$hashedpassword17', 'thomas.flores@email.com', '1987-05-23', true),
    ('karen_rivera', '$2a$10$hashedpassword18', 'karen.rivera@email.com', '1995-09-11', true),
    ('daniel_gomez', '$2a$10$hashedpassword19', 'daniel.gomez@email.com', '1989-12-18', true),
    ('nancy_diaz', '$2a$10$hashedpassword20', 'nancy.diaz@email.com', '1994-04-02', true),
    ('matthew_cruz', '$2a$10$hashedpassword21', 'matthew.cruz@email.com', '1986-08-27', true),
    ('betty_reyes', '$2a$10$hashedpassword22', 'betty.reyes@email.com', '1992-02-14', true),
    ('anthony_morales', '$2a$10$hashedpassword23', 'anthony.morales@email.com', '1990-06-09', true),
    ('helen_jimenez', '$2a$10$hashedpassword24', 'helen.jimenez@email.com', '1988-10-31', true),
    ('mark_ruiz', '$2a$10$hashedpassword25', 'mark.ruiz@email.com', '1991-03-26', true),
    ('sandra_ortiz', '$2a$10$hashedpassword26', 'sandra.ortiz@email.com', '1993-07-13', true),
    ('paul_castillo', '$2a$10$hashedpassword27', 'paul.castillo@email.com', '1987-11-20', true),
    ('ashley_ramos', '$2a$10$hashedpassword28', 'ashley.ramos@email.com', '1995-01-08', true),
    ('steven_gutierrez', '$2a$10$hashedpassword29', 'steven.gutierrez@email.com', '1989-05-15', true),
    ('kimberly_vargas', '$2a$10$hashedpassword30', 'kimberly.vargas@email.com', '1994-09-22', true),
    ('andrew_mendoza', '$2a$10$hashedpassword31', 'andrew.mendoza@email.com', '1986-02-11', false),
    ('donna_castro', '$2a$10$hashedpassword32', 'donna.castro@email.com', '1992-06-28', false),
    ('joshua_chavez', '$2a$10$hashedpassword33', 'joshua.chavez@email.com', '1990-10-05', false),
    ('michelle_espinoza', '$2a$10$hashedpassword34', 'michelle.espinoza@email.com', '1988-01-19', false),
    ('kevin_silva', '$2a$10$hashedpassword35', 'kevin.silva@email.com', '1991-05-24', false),
    ('emily_medina', '$2a$10$hashedpassword36', 'emily.medina@email.com', '1993-09-07', false),
    ('brian_alvarado', '$2a$10$hashedpassword37', 'brian.alvarado@email.com', '1987-12-30', false),
    ('amanda_santos', '$2a$10$hashedpassword38', 'amanda.santos@email.com', '1995-04-16', false),
    ('george_aguilar', '$2a$10$hashedpassword39', 'george.aguilar@email.com', '1989-08-03', false),
    ('stephanie_guzman', '$2a$10$hashedpassword40', 'stephanie.guzman@email.com', '1994-11-27', false),
    ('edward_rojas', '$2a$10$hashedpassword41', 'edward.rojas@email.com', '1986-03-14', false),
    ('deborah_mendez', '$2a$10$hashedpassword42', 'deborah.mendez@email.com', '1992-07-21', false),
    ('ronald_delgado', '$2a$10$hashedpassword43', 'ronald.delgado@email.com', '1990-11-08', false),
    ('laura_moreno', '$2a$10$hashedpassword44', 'laura.moreno@email.com', '1988-02-25', false),
    ('jason_valencia', '$2a$10$hashedpassword45', 'jason.valencia@email.com', '1991-06-12', false),
    ('rebecca_herrera', '$2a$10$hashedpassword46', 'rebecca.herrera@email.com', '1993-10-29', false),
    ('ryan_campos', '$2a$10$hashedpassword47', 'ryan.campos@email.com', '1987-01-06', false),
    ('cynthia_vega', '$2a$10$hashedpassword48', 'cynthia.vega@email.com', '1995-05-23', false),
    ('jacob_guerrero', '$2a$10$hashedpassword49', 'jacob.guerrero@email.com', '1989-09-10', false),
    ('kathleen_soto', '$2a$10$hashedpassword50', 'kathleen.soto@email.com', '1994-12-17', false);

    CREATE TABLE lifter.cars(
    car_id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    is_available BOOLEAN DEFAULT true
    );

    CREATE TABLE lifter.rentals(
    rental_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES lifter.users(user_id),
    car_id INT REFERENCES lifter.cars(car_id),
    rental_date DATE DEFAULT CURRENT_DATE,
    is_returned BOOLEAN DEFAULT false
    );

--INSERT NEW USER AND CAR, UPDATE USER AND CAR STATUS, RECORD A RENTAL, MARK A CAR AS RETURNED, QUERY AVAILABLE AND UNAVAILABLE CARS

INSERT INTO lifter.users (username, password, email, birthdate, is_enabled)
VALUES 
    ('john_smith', '$2a$10$hashedpassword1', 'john.smith@email.com', '1990-03-15', true);

INSERT INTO lifter.cars (brand, model, year, is_available)
VALUES
    ('Toyota', 'Camry', 2020, true);
UPDATE lifter.users
SET is_enabled = false
WHERE user_id = 1;

UPDATE lifter.users
SET is_in_arrears = false
WHERE user_id = 1;

UPDATE lifter.cars
SET is_available = false
WHERE car_id = 1;

INSERT INTO lifter.rentals (user_id, car_id, rental_date, is_returned)
VALUES
    (1, 1, '2024-06-01', false);


-------
UPDATE lifter.rentals
SET is_returned = true
WHERE rental_id = 1;

UPDATE lifter.cars
SET is_available = true
WHERE car_id = (SELECT car_id FROM lifter.rentals WHERE rental_id = 1);
--------

UPDATE lifter.cars
SET is_available = false
WHERE car_id = 1;

SELECT * FROM lifter.cars
WHERE is_available = true;
SELECT * FROM lifter.cars
WHERE is_available = false;

SELECT * FROM lifter.users;

SELECT * FROM lifter.cars;

SELECT * FROM lifter.rentals;

---------------
DROP TABLE lifter.rentals;
DROP TABLE lifter.cars;
DROP TABLE lifter.users;

-- =====================================================
-- Multi-row INSERT for lifter.cars table
-- 50 car entries with varied availability
-- =====================================================

INSERT INTO lifter.cars (brand, model, year, is_available)
VALUES 
    -- Toyota (10 cars)
    ('Toyota', 'Camry', 2022, true),
    ('Toyota', 'Corolla', 2023, true),
    ('Toyota', 'RAV4', 2024, true),
    ('Toyota', 'Highlander', 2021, false),
    ('Toyota', 'Tacoma', 2023, true),
    ('Toyota', 'Prius', 2024, true),
    ('Toyota', '4Runner', 2022, false),
    ('Toyota', 'Sienna', 2023, true),
    ('Toyota', 'Avalon', 2021, true),
    ('Toyota', 'Tundra', 2024, false),
    
    -- Honda (10 cars)
    ('Honda', 'Civic', 2023, true),
    ('Honda', 'Accord', 2024, true),
    ('Honda', 'CR-V', 2022, false),
    ('Honda', 'Pilot', 2023, true),
    ('Honda', 'Odyssey', 2024, true),
    ('Honda', 'HR-V', 2022, true),
    ('Honda', 'Ridgeline', 2023, false),
    ('Honda', 'Passport', 2024, true),
    ('Honda', 'Insight', 2021, true),
    ('Honda', 'Fit', 2022, false),
    
    -- Ford (10 cars)
    ('Ford', 'F-150', 2024, true),
    ('Ford', 'Mustang', 2023, true),
    ('Ford', 'Explorer', 2022, false),
    ('Ford', 'Escape', 2024, true),
    ('Ford', 'Edge', 2023, true),
    ('Ford', 'Bronco', 2024, false),
    ('Ford', 'Ranger', 2022, true),
    ('Ford', 'Expedition', 2023, true),
    ('Ford', 'Maverick', 2024, false),
    ('Ford', 'EcoSport', 2021, true),
    
    -- Chevrolet (10 cars)
    ('Chevrolet', 'Silverado', 2024, true),
    ('Chevrolet', 'Equinox', 2023, false),
    ('Chevrolet', 'Traverse', 2022, true),
    ('Chevrolet', 'Tahoe', 2024, true),
    ('Chevrolet', 'Malibu', 2023, false),
    ('Chevrolet', 'Colorado', 2024, true),
    ('Chevrolet', 'Blazer', 2022, true),
    ('Chevrolet', 'Suburban', 2023, false),
    ('Chevrolet', 'Camaro', 2024, true),
    ('Chevrolet', 'Trax', 2022, true),
    
    -- Nissan (5 cars)
    ('Nissan', 'Altima', 2023, true),
    ('Nissan', 'Sentra', 2024, false),
    ('Nissan', 'Rogue', 2022, true),
    ('Nissan', 'Pathfinder', 2023, true),
    ('Nissan', 'Frontier', 2024, false),
    
    -- Hyundai (5 cars)
    ('Hyundai', 'Elantra', 2023, true),
    ('Hyundai', 'Tucson', 2024, true),
    ('Hyundai', 'Santa Fe', 2022, false),
    ('Hyundai', 'Sonata', 2023, true),
    ('Hyundai', 'Palisade', 2024, true);

-- =====================================================
-- Multi-row INSERT for lifter.rentals table
-- 20 rental entries with varied dates and return status
-- =====================================================

INSERT INTO lifter.rentals (user_id, car_id, rental_date, is_returned)
VALUES 
    -- Rentals activos (is_returned = false) - 8 registros
    (1, 4, '2026-01-15', false),
    (2, 7, '2026-01-20', false),
    (3, 13, '2026-01-25', false),
    (5, 23, '2026-02-01', false),
    (8, 26, '2026-02-02', false),
    (12, 29, '2026-02-03', false),
    (15, 35, '2026-02-04', false),
    (18, 48, '2026-02-04', false),
    
    -- Rentals devueltos (is_returned = true) - 12 registros
    (1, 1, '2025-12-01', true),
    (2, 2, '2025-12-05', true),
    (3, 5, '2025-12-10', true),
    (4, 8, '2025-12-15', true),
    (6, 11, '2025-12-20', true),
    (7, 15, '2025-12-22', true),
    (9, 18, '2025-12-28', true),
    (10, 21, '2026-01-02', true),
    (11, 25, '2026-01-05', true),
    (13, 30, '2026-01-08', true),
    (16, 33, '2026-01-12', true),
    (20, 40, '2026-01-18', true);