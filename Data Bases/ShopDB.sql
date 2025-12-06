CREATE TABLE Users (
    Id BIGINT PRIMARY KEY AUTO_INCREMENT,
    Full_Name VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Registration_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Products (
    Code VARCHAR(15) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Brand VARCHAR(50) NOT NULL,
    Admision_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ShoppingCart (
    Id BIGINT PRIMARY KEY AUTO_INCREMENT,
    User_Id BIGINT,
    Total_Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (User_Id) REFERENCES Users(Id)
);

CREATE TABLE ShoppingCartDetails (
    Id BIGINT PRIMARY KEY AUTO_INCREMENT,
    Cart_Id BIGINT,
    Product_Code VARCHAR(15),
    Quantity INT NOT NULL,
    Total_Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Cart_Id) REFERENCES ShoppingCart(Id),
    FOREIGN KEY (Product_Code) REFERENCES Products(Code)
);

CREATE TABLE PaymentMethods (
    Id BIGINT PRIMARY KEY AUTO_INCREMENT,
    Description VARCHAR(50) NOT NULL,
    Bank_Name VARCHAR(50) NOT NULL
);

CREATE TABLE Invoice (
    Id BIGINT PRIMARY KEY AUTO_INCREMENT,
    User_Id BIGINT,
    Payment_Method_Id BIGINT,
    Purchase_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Total_Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (User_Id) REFERENCES Users(Id),
    FOREIGN KEY (Payment_Method_Id) REFERENCES PaymentMethods(Id)
);

CREATE TABLE InvoiceDetails (
    Id BIGINT PRIMARY KEY AUTO_INCREMENT,
    Invoice_Id BIGINT,
    Product_Code VARCHAR(15),
    Quantity INT NOT NULL,
    Total_Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Invoice_Id) REFERENCES Invoice(Id),
    FOREIGN KEY (Product_Code) REFERENCES Products(Code)
);

CREATE TABLE Reviews (
    Id BIGINT PRIMARY KEY AUTO_INCREMENT,
    User_Id BIGINT,
    Product_Code VARCHAR(15),
    Rating INT CHECK (Rating >= 1 AND Rating <= 5),
    Comment VARCHAR(255),
    FOREIGN KEY (User_Id) REFERENCES Users(Id),
    FOREIGN KEY (Product_Code) REFERENCES Products(Code)
);

--------------------------------------------

ALTER TABLE Invoice
ADD COLUMN Telephone VARCHAR(20);

ALTER TABLE Invoice
ADD COLUMN Employee_Code VARCHAR(15);

--------------------------------------------

Select * from Products;
Select * from Products Where Price > 5000;
Select * from InvoiceDetails Where Product_Code = 'P001';
Select Product_Code, SUM(Total_Amount) from InvoiceDetails GROUP BY Product_Code;
Select * from Invoice Where User_Id = 2
Select * from Invoice ORDER BY Total_Amount DESC
Select * from Invoice Where Id = '7'