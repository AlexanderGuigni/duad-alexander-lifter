--1.Obtenga todos los libros y sus autores
SELECT B.Name AS BookName, A.Name AS AuthorName FROM Books AS B
LEFT JOIN Authors AS A ON B.Author == A.ID 
--2.Obtenga todos los libros que no tienen autor
SELECT B.Name AS BookName, A.Name AS AuthorName FROM Books AS B
LEFT JOIN Authors AS A ON B.Author == A.ID
WHERE AuthorName IS NULL
--3.Obtenga todos los autores que no tienen libros
SELECT A.Name AS AuthorName FROM Authors AS A
LEFT JOIN Books AS B ON A.ID ==  B.Author
WHERE B.Name IS NULL
--4.Obtenga todos los libros que han sido rentados en algún momento
SELECT B.Name AS BookName FROM Books AS B
JOIN Rents AS R ON B.ID == R.BookID
--5.Obtenga todos los libros que nunca han sido rentados
SELECT B.Name AS BookName FROM Books AS B
LEFT JOIN Rents AS R ON B.ID == R.BookID
WHERE R.ID IS NULL
--6.Obtenga todos los clientes que nunca han rentado un libro
SELECT C.Name, C.Email FROM Customers AS C
LEFT JOIN Rents AS R ON C.ID == R.CustomerID
WHERE R.CustomerID IS NULL
--7.Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT B.Name AS BookName, R.State AS State FROM Books AS B
JOIN Rents AS R ON B.ID == R.BookID
WHERE  R.State == 'Overdue'