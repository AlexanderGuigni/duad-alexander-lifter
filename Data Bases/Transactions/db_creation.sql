CREATE SCHEMA IF NOT EXISTS transactions;

CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Invoices (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL,
    is_returned BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE InvoiceDetails (
    id SERIAL PRIMARY KEY,
    invoice_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES Invoices(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

INSERT INTO Products (name, price, stock) VALUES
('Product A', 10.00, 100),
('Product B', 20.00, 100),
('Product C', 30.00, 100),
('Product D', 40.00, 100),
('Product E', 50.00, 100),
('Product F', 60.00, 100),
('Product G', 70.00, 100),
('Product H', 80.00, 100),
('Product I', 90.00, 100),
('Product J', 100.00, 100);

INSERT INTO Users (name, email) VALUES
('User 1', 'user1@example.com'),
('User 2', 'user2@example.com'),
('User 3', 'user3@example.com'),
('User 4', 'user4@example.com'),
('User 5', 'user5@example.com');