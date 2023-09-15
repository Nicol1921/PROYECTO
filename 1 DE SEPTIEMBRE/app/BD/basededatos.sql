create database santyfashion;
-- drop database santyfashion;
use santyfashion;

CREATE TABLE Referencia (
  idReferencia INT NOT NULL PRIMARY KEY,
  nombre VARCHAR(60) NOT NULL,
  descripcion VARCHAR(60) NOT NULL,
  referencia VARCHAR(60) NOT NULL,
  imagen LONGBLOB NOT NULL
);

CREATE TABLE Prenda (
  idPrenda INT NOT NULL PRIMARY KEY,
  idVenta INT NOT NULL,
  idReferencia INT NOT NULL,
  talla VARCHAR(60) NOT NULL,
  fecha DATE NOT NULL,
  estado VARCHAR(60) NOT NULL,
  color VARCHAR(60) NOT NULL,
  precio int NOT NULL
);

CREATE TABLE Venta (
  idVenta int not null primary key auto_increment,
  idPrenda INT NOT NULL,
  idPreVenta int not null,
  fecha date not null,
  codigo VARCHAR(60) NOT NULL,
  estado VARCHAR(60) NOT NULl
);

CREATE TABLE PreVenta (
idPreVenta int not null primary key auto_increment,
idPrenda int not null,
fecha date not null,
fechaEnvio date not null,
estado VARCHAR(60) NOT NULL
);

CREATE TABLE Administrador (
idAdmin  int not null primary key auto_increment,
nombre varchar(60) not null,
apellido varchar(60) not null,
usuario varchar(60) not null,
contrasena varchar(60) not null,
compContrasena varchar(60)not null 
);

SELECT * FROM Venta;


ALTER TABLE Prenda
ADD FOREIGN KEY (idReferencia) REFERENCES Referencia(idReferencia);

ALTER TABLE Prenda
ADD FOREIGN KEY (idVenta) REFERENCES Venta(idVenta);

ALTER TABLE Venta
ADD FOREIGN KEY (idPrenda) REFERENCES Prenda(idPrenda);

ALTER TABLE Venta
ADD FOREIGN KEY (idPreVenta) REFERENCES PreVenta(idPreVenta);

ALTER TABLE PreVenta
ADD FOREIGN KEY (idPrenda) REFERENCES Prenda(idPrenda);


