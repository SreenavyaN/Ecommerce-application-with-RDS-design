#creating a database
use SQLProject;
# Normalized database schema

# creating a relation 'Customer'
create table Customer(CustomerID INT NOT NULL, Country VARCHAR(150), Password VARCHAR(10),PRIMARY KEY(CustomerID));

#creating a relation 'Item'
create table Item(StockCode VARCHAR(7) NOT NULL, Description VARCHAR(150) NOT NULL, UnitPrice FLOAT, PRIMARY KEY(StockCode));

#creating a relation 'Invoice'
create table Invoice(InvoiceNo INT NOT NULL, InvoiceDate DATETIME, PRIMARY KEY(InvoiceNo));

#creating a relation 'Customer_Invoice'
#Creating a child table with Update and Delete Cascade from the main table.

CREATE TABLE `Customer_Invoice` (
 `InvoiceNo` int(11) DEFAULT NULL,
 `CustomerID` int(11) DEFAULT NULL,
 KEY `Customer_Invoice_ibfk_2` (`InvoiceNo`),
 KEY `Customer_Invoice_ibfk_1` (`CustomerID`),
 CONSTRAINT `Customer_Invoice_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `Customer` (`CustomerID`) ON DELETE CASCADE ON UPDATE CASCADE,
 CONSTRAINT `Customer_Invoice_ibfk_2` FOREIGN KEY (`InvoiceNo`) REFERENCES `Invoice` (`InvoiceNo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#creating a relation 'InvoiceDetails'
create table InvoiceDetails(InvoiceNo INT,StockCode VARCHAR(7), Quantity INT,FOREIGN KEY(InvoiceNo) REFERENCES Invoice(InvoiceNo),
FOREIGN KEY(StockCode) REFERENCES Item(StockCode));

#creating a relation 'Manager'
create table Manager(ManagerID INT NOT NULL, Password VARCHAR(20), PRIMARY KEY(ManagerID));

#Creating a Procedure for inserting the values into Customer relation
DELIMITER //
CREATE PROCEDURE CustomerData(IN Id int, IN Country VARCHAR(150),IN Password VARCHAR(10))
BEGIN
	INSERT INTO Customer values(Id, Country, Password);
END; //
DELIMITER ;

CALL SQLProject.CustomerData(11256,'India','pass1');
CALL SQLProject.CustomerData(11257,'America','pass2');
CALL SQLProject.CustomerData(11258,'Istanbul','pass3');
CALL SQLProject.CustomerData(11259,'France','pass4');
CALL SQLProject.CustomerData(11260,'Germany','pass5');
CALL SQLProject.CustomerData(11261,'United Kingdom','pass6');
CALL SQLProject.CustomerData(11262,'India','pass7');
CALL SQLProject.CustomerData(11263,'France','pass8');
CALL SQLProject.CustomerData(11264,'Istanbul','pass9');
CALL SQLProject.CustomerData(11265,'India','pass10');

#Creating a Procedure for inserting the values into Item relation
DELIMITER //
CREATE PROCEDURE ItemData(IN StockCode VARCHAR(7), IN Description VARCHAR(150),IN UnitPrice FLOAT)  
BEGIN
	INSERT INTO Item values(StockCode,Description,UnitPrice);
END; //
DELIMITER ;

CALL SQLProject.ItemData('30000','Green Armless Accent Chair','1.89');
CALL SQLProject.ItemData('30001','Galvin Cafeteria Table','1.90');
CALL SQLProject.ItemData('30002','Realspace Cressfield Bonded Leather Executive High-Back Chair','1.91');
CALL SQLProject.ItemData('30003','Marble Top Leilani Tulip Dining Table','1.92');
CALL SQLProject.ItemData('30004','Charcoal Gray and Ivory Dash Print Noemi Tub Chair','1.93');
CALL SQLProject.ItemData('30005','Gray Tweed Curved Back Jaden Chair','1.94');
CALL SQLProject.ItemData('30006','Yellow Woven Taryn Upholstered Chair','1.95');
CALL SQLProject.ItemData('30007','Sea Glass Terrazzo Domenico Outdoor Patio Dining Stool','1.96');
CALL SQLProject.ItemData('30008','Peacoat Blue Punched Metal Dimitri Outdoor Patio Accent Stool','1.97');
CALL SQLProject.ItemData('30009','Metal Faceted Octavia Outdoor Patio Stool','1.98');

#Creating a Procedure for inserting the values into Invoice relation
DELIMITER //
CREATE PROCEDURE InvoiceData(IN InvoiceNo INT, IN InvoiceDate DATETIME)
BEGIN
	INSERT INTO Invoice values(InvoiceNo,InvoiceDate);
END; //
DELIMITER ;

CALL SQLProject.InvoiceData(541001,'2012-01-10 08:34:00');
CALL SQLProject.InvoiceData(541002,'2012-01-10 08:35:00');
CALL SQLProject.InvoiceData(541003,'2012-02-10 08:36:00');
CALL SQLProject.InvoiceData(541004,'2012-02-10 08:37:00');
CALL SQLProject.InvoiceData(541005,'2012-03-10 09:34:00');
CALL SQLProject.InvoiceData(541006,'2012-03-10 08:35:00');
CALL SQLProject.InvoiceData(541007,'2012-04-10 08:39:00');
CALL SQLProject.InvoiceData(541008,'2012-04-10 08:45:00');
CALL SQLProject.InvoiceData(541009,'2012-09-10 08:55:00');
CALL SQLProject.InvoiceData(541010,'2012-01-10 08:34:00');

#Creating a Procedure for inserting the values into Customer_Invoice relation
DELIMITER //
CREATE PROCEDURE CustomerInvoiceData(IN InvoiceNo INT, IN Id INT)
BEGIN
	INSERT INTO Customer_Invoice values(InvoiceNo,Id);
END; //
DELIMITER ;

CALL SQLProject.CustomerInvoiceData(541001,11256);
CALL SQLProject.CustomerInvoiceData(541002,11257);
CALL SQLProject.CustomerInvoiceData(541003,11258);
CALL SQLProject.CustomerInvoiceData(541004,11259);
CALL SQLProject.CustomerInvoiceData(541005,11260);
CALL SQLProject.CustomerInvoiceData(541006,11261);
CALL SQLProject.CustomerInvoiceData(541007,11262);
CALL SQLProject.CustomerInvoiceData(541008,11263);
CALL SQLProject.CustomerInvoiceData(541009,11264);
CALL SQLProject.CustomerInvoiceData(541010,11265);

#Creating a Procedure for inserting the values into InvoiceDetails relation
DELIMITER //
CREATE PROCEDURE InvoiceDetailsData(IN InvoiceNo INT, IN StockCode VARCHAR(7), IN Quantity INT)
BEGIN
	INSERT INTO InvoiceDetails values(InvoiceNo,StockCode,Quantity);
END; //
DELIMITER ;

CALL SQLProject.InvoiceDetailsData(541010,'30000',3);
CALL SQLProject.InvoiceDetailsData(541010,'30001',4);
CALL SQLProject.InvoiceDetailsData(541010,'30002',5);
CALL SQLProject.InvoiceDetailsData(541010,'30003',1);
CALL SQLProject.InvoiceDetailsData(541009,'30004',3);
CALL SQLProject.InvoiceDetailsData(541009,'30005',3);
CALL SQLProject.InvoiceDetailsData(541009,'30006',8);
CALL SQLProject.InvoiceDetailsData(541009,'30007',3);
CALL SQLProject.InvoiceDetailsData(541008,'30008',3);
CALL SQLProject.InvoiceDetailsData(541008,'30009',1);

#Creating a Procedure for inserting the values into Manager relation
DELIMITER //
CREATE PROCEDURE ManagerData(IN ManagerId INT, IN Password VARCHAR(20))
BEGIN
	INSERT INTO Manager values(ManagerId, Password);
END; //
DELIMITER ;

CALL SQLProject.ManagerData(50000,'pass11');
CALL SQLProject.ManagerData(50001,'pass12');
CALL SQLProject.ManagerData(50002,'pass13');
CALL SQLProject.ManagerData(50003,'pass14');
CALL SQLProject.ManagerData(50004,'pass15');
CALL SQLProject.ManagerData(50005,'pass16');
CALL SQLProject.ManagerData(50006,'pass17');
CALL SQLProject.ManagerData(50007,'pass18');
CALL SQLProject.ManagerData(50008,'pass19');
CALL SQLProject.ManagerData(50009,'pass20');

#creating a relation 'newCustomers'
create table ConfirmationtoManager(CustomerID INT NOT NULL,Country VARCHAR(25) NOT NULL,PRIMARY KEY(CustomerID));

#Creating a trigger such that when a row is updated into Customer relation
#an update is made onto the newCustomer relation 
DELIMITER //
CREATE TRIGGER newCustomer AFTER INSERT ON Customer FOR EACH ROW
BEGIN
	INSERT INTO ConfirmationtoManager values(NEW.CustomerID,NEW.Country);
END; //
DELIMITER ;

#To create Views on Customer Table for Manager to view only CustomerID and Country but not the Password
CREATE VIEW CustomerView
AS SELECT CustomerID, Country
FROM Customer;





